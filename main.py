from os import path, mkdir
import json
import requests as client

with open("config.json", "r") as file:
    config = json.loads(file.read())

    images_dir = config["images_dir"]

    if not path.isdir(images_dir):
        mkdir(images_dir)

# Get most up-to-date card and location data.
try:
    cards_json = client.get(config["card_json_url"]).json()
    locations_json = client.get(config["location_json_url"]).json()
except:
    raise Exception("Couldn't fetch the latest card or location information!")

# Check the image directory and download every card that doesn't exist.
counter = 1
for card in cards_json:
    card_name = card["defId"]

    # Fetch card image and save it.
    card_img = client.get(f"{config['card_img_url']}/{card_name}.webp")
    with open(f"{images_dir}/{card_name}.webp", "wb") as file:
        file.write(card_img.content)

    print(f"({counter}/{len(cards_json)} {card_img.status_code}) Downloading card {card_name}...")

    counter += 1