import cv2
import numpy as np
import torch
import sys
from helpers import init_helper, vsumm_helper, bbox_helper, video_helper
from helpers import model_zoo

from ..imagecaption.image_captioning import img_caption
from keyframe import extract_keyframes
from extract_keywords import extract_keywords

CPU = torch.device('cpu')
D = torch.device
def main():
    SOURCE = str(sys.argv[1])
    name = SOURCE.split("/")[-1]
    print('Loading DSNet model ...')
    model = model_zoo.get_model()
    model = model.eval().to("cuda")
    state_dict = torch.load('./nodeserver/pythonscripts/DSNet/model/summe.yml.4.pt',
                            map_location=lambda storage, loc: storage)
    model.load_state_dict(state_dict)

    # load video
    print('Preprocessing source video ...')
    video_proc = video_helper.VideoPreprocessor(15)
    n_frames, seq, cps, nfps, picks = video_proc.run(SOURCE)
    seq_len = len(seq)

    print('Predicting summary ...')
    with torch.no_grad():
        seq_torch = torch.from_numpy(seq).unsqueeze(0).to("cuda")

        pred_cls, pred_bboxes = model.predict(seq_torch)

        pred_bboxes = np.clip(pred_bboxes, 0, seq_len).round().astype(np.int32)

        pred_cls, pred_bboxes = bbox_helper.nms(pred_cls, pred_bboxes, 0.5)
        pred_summ = vsumm_helper.bbox2summary(
            seq_len, pred_cls, pred_bboxes, cps, n_frames, nfps, picks)

    print('Writing summary video ...')

    # load original video
    cap = cv2.VideoCapture(SOURCE)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # create summary video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('./outputs/'+name, fourcc, fps, (width, height))

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if pred_summ[frame_idx]:
            out.write(frame)

        frame_idx += 1

    out.release()
    cap.release()
    #new code
    text_caption = []
    img_list = extract_keyframes('./nodeserver/pythonscripts/DSNet/outputs/'+name)
    for img in img_list:
        text_caption.append(img_caption(img))

    keywords = extract_keywords(text_caption)
    with open('/nodeserver/pythonscripts/DSNet/outputs/captions_'+name+'.txt', 'w') as f:
        # for line in keywords:
        f.write(f"{keywords}\n")
    print("done")




if __name__ == '__main__':
    main()
