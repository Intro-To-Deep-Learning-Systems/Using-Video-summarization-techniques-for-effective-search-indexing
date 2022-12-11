from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
if __name__ == "__main__":
    vd = Video()
    no_of_frames_to_returned = 12

    # initialize diskwriter to save data at desired location
    diskwriter = KeyFrameDiskWriter(location="selectedframes")

    # Video file path
    video_file_path = os.path.join("..","..", "uploaded", "files", "image1670653463040.mp4")

    print(f"Input video file path = {video_file_path}")

    # extract keyframes and process data with diskwriter
    vd.extract_video_keyframes(
        no_of_frames=no_of_frames_to_returned, file_path=video_file_path,
        writer=diskwriter
    )