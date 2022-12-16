from flask import Flask
from flask import request
import os
import cv2
import numpy as np
import torch
import sys
from helpers import init_helper, vsumm_helper, bbox_helper, video_helper
from helpers import model_zoo
from DSNet.keyframe import extract_keyframes
CPU = torch.device('cpu')
GPU= torch.device('cuda')
D = torch.device
from imagecaption.image_captioning import img_caption
from ExpansionNet.captionpipeline import getCaptions
from extract_keywords import extract_keywords

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/dynamicsummary", methods=['POST'])
def dynamicsummary():
    SOURCE=request.get_json()["params"]
    print(request.get_json()["params"], file=sys.stderr)
    name = SOURCE.split("\\")[-1]
    print('Loading DSNet model ...')
    model = model_zoo.get_model()
    model = model.eval().to("cuda")
    state_dict = torch.load('nodeserver/pythonscripts/DSNet/model/summe.yml.4.pt',
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
    out = cv2.VideoWriter(os.path.abspath('./nodeserver/pythonscripts/DSNet/outputs/summaryof'+name), fourcc, fps, (width, height))

    print("NAME--"+name, file=sys.stderr)

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
    img_list = extract_keyframes(os.path.abspath('./nodeserver/pythonscripts/DSNet/outputs/summaryof'+name))
    '''
    #TEST MODE
    img_list=[os.path.abspath('./nodeserver/pythonscripts/test/5155093236_01067e4f6e_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/2633528304_369cf89ce1_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/9874637964_ce338575f0_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/1176519574_b4d569ecbe_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/5093961450_d8c840d0d2_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/9372536208_b97bc7eeff_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/9419081044_7cebf902ec_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/9743494618_f0faea1cdc_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/8700354838_884967117d_z.jpg'),
                os.path.abspath('./nodeserver/pythonscripts/test/9362545580_34d972390d_z.jpg')]

    '''
    # img_list=[os.path.abspath('./nodeserver/pythonscripts/test2/5485180146_5de595f352_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/8214231212_7d3ed4ec5f_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/5126051354_4265ae0dc2_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/5357285163_a24a1218a2_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/4826364673_e1d2fe0d7a_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/7359571760_37321faa50_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/8484957526_9a1a9a8598_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/4603398792_6bb6898455_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/7158482064_92f2821812_z.jpg'),
    #             os.path.abspath('./nodeserver/pythonscripts/test2/5225530351_c7b8987e0a_z.jpg')]
    MODE="EXPANSIONNET" #EXPANSIONNET or CLIPCLAP

    if(MODE=="EXPANSIONNET"):
        text_caption=getCaptions(img_list)

    else:
        for img in img_list:
            text_caption.append(img_caption(img))
            print(text_caption,file=sys.stderr)

            # text_caption = []
            # img_list = extract_keyframes('./nodeserver/pythonscripts/DSNet/outputs/'+name)
            # for img in img_list:
            #     text_caption.append(img_caption(img))

    keywords = extract_keywords(text_caption)

    link = name +","+str(keywords)
    with open(os.path.abspath('./nodeserver/pythonscripts/DSNet/outputs/captions.txt'), 'a') as f:
        f.write(f"{link}\n")
    print("done")


    # print("done")
    return request.get_json()["params"]