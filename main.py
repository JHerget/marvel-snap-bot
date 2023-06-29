from os import path, mkdir, listdir
from urllib.parse import quote
import requests as client
import json
import os

with open("config.json", "r") as file:
    config = json.loads(file.read())

    card_json_url = config["card_json_url"]
    location_json_url = config["location_json_url"]
    card_img_url = config["card_img_url"]
    location_img_url = config["location_img_url"]
    images_dir = config["images_dir"]

    if not path.isdir(images_dir):
        mkdir(images_dir)

# Get most up-to-date card and location data.
try:
    cards_json = client.get(card_json_url).json()
    locations_json = client.get(location_json_url).json()
except:
    raise Exception("Couldn't fetch the latest card or location information!")

# Check the image directory and download every card that doesn't exist.
print("Downloading card images...")
for index in range(len(cards_json)):  # Using range so we know which index we're on even if we skip a card.
    card_name = f"{cards_json[index]['defId']}.webp"

    if card_name in os.listdir(images_dir):
        continue

    # Fetch card image and save it.
    card_img = client.get(f"{card_img_url}/{card_name}")
    if card_img.ok:
        with open(f"{images_dir}/{card_name}", "wb") as file:
            file.write(card_img.content)

    # e.g. (204/301 200) Downloading card Valkyrie.webp...
    print(f"({index + 1}/{len(cards_json)} {card_img.status_code}) Downloading card {card_name}...")

# Check the image directory and download every location that doesn't exist
print("Downloading location images...")
for index in range(len(locations_json)):  # Using range so we know which index we're on even if we skip a location.
    location_name = quote(f"{locations_json[index]['name']}.webp")

    if location_name in listdir(images_dir):
        continue

    # Fetch location image and save it.
    location_img = client.get(f"{location_img_url}/{location_name}")
    if location_img.ok:
        with open(f"{images_dir}/{location_name}", "wb") as file:
            file.write(location_img.content)

    # e.g. (47/136 200) Downloading location Sinister%20London.webp...
    print(f"({index + 1}/{len(locations_json)} {location_img.status_code}) Downloading location {location_name}...")

print("Complete!")
