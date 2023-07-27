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

video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
success, frame = video.read()
print(success)

height, width, channels = frame.shape
row_start = int(float(config["hoogland_layout"]["locations"]["row_start"])*height)
row_end = int(float(config["hoogland_layout"]["locations"]["row_end"])*height)
col_start = int(float(config["hoogland_layout"]["locations"]["col_start"])*width)
col_end = int(float(config["hoogland_layout"]["locations"]["col_end"])*width)
locations = frame[row_start:row_end, col_start:col_end]

cv2.imshow("frame", locations)
cv2.waitKey(5000)

# image = cv2.imread("test.png")
# height, width, channels = image.shape
#
# row_start = int(float(config["hoogland_layout"]["locations"]["row_start"])*height)
# row_end = int(float(config["hoogland_layout"]["locations"]["row_end"])*height)
# col_start = int(float(config["hoogland_layout"]["locations"]["col_start"])*width)
# col_end = int(float(config["hoogland_layout"]["locations"]["col_end"])*width)
# locations = image[row_start:row_end, col_start:col_end]
#
# cv2.imshow("testimage", locations)
# cv2.waitKey(10000)
# print(image.shape)