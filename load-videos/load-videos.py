from youtube import YoutubeVideo
from crop import Crop
from simpletk import Window
from PIL import Image, ImageTk
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

width, height = (300, 300)
root = Window(width=width, height=height+50, title="Marvel Snap")
canvas = root.add_canvas(width=width, height=height, row=1, col=1, row_span=50, col_span=50)
next_button = root.add_button(width=10, height=1, text="Next Image", row=51, col=25)

cropped_frame = Crop(frame=frame, layout=config["hoogland_layout"]).get_all()[0]
image = ImageTk.PhotoImage(image=Image.fromarray(cropped_frame))
canvas.create_image(width//2, height//2, image=image)

root.mainloop()

# url = YoutubeVideo(url).getbest()["url"]
# video = cv2.VideoCapture(url)
# fps = video.get(cv2.CAP_PROP_FPS)
# start_frame = int((60*start_min + start_sec)*fps)
#
# video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
# success, frame = video.read()
# print(success)
#
# cropped_frame = Crop(frame=frame, layout=config["hoogland_layout"])
# cropped_frame.display_locations()
# cropped_frame.display_opponent_cards()
# cropped_frame.display_player_cards()