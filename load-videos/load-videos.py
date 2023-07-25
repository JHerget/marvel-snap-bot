import json
import cv2

with open("config.json", "r") as file:
    config = json.loads(file.read())
    url = config["video_url"]

