from youtube import YoutubeVideo
import json
import cv2

with open("config.json", "r") as file:
    config = json.loads(file.read())

    url = config["video_url"]
    start_min, start_sec = config["start_time"].split(":")
    start_min = int(start_min)
    start_sec = int(start_sec)

url = YoutubeVideo(url).getbest()["url"]
video = cv2.VideoCapture(url)
fps = video.get(cv2.CAP_PROP_FPS)
start_frame = int((60*start_min + start_sec)*fps)

# video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
success, frame = video.read()

print(success)

print(cv2.CAP_PROP_FRAME_COUNT)
print(cv2.CAP_PROP_POS_FRAMES)