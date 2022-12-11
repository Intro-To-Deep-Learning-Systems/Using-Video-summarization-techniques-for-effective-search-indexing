from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
def extract_keyframes(video_file_path):
    vd = Video()
    no_of_frames_to_returned = 10

    # initialize diskwriter to save data at desired location
    diskwriter = KeyFrameDiskWriter(location="./nodeserver/uploaded/keyframes")

    print(f"Input video file path = {video_file_path}")

    # extract keyframes and process data with diskwriter
    vd.extract_video_keyframes(
        no_of_frames=no_of_frames_to_returned, file_path=video_file_path,
        writer=diskwriter
    )

    file_name = video_file_path.split("/")[-1]
    file_name = file_name.split(".")[0]
    file_names = []
    for i in range(no_of_frames_to_returned):
        file_names.append("./nodeserver/uploaded/keyframes/"+file_name+"_"+str(i)+".jpeg")

    return file_names

if __name__ == '__main__':
    video_file_path = os.path.join("/Users/suryakiran/Downloads/using-video-summarization-techniques-for-effective-search-indexing/nodeserver/uploaded/files/image1670653463040.mp4")
    a = extract_keyframes(video_file_path)
    print(a)

