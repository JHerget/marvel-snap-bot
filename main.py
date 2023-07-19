from os import path, mkdir, listdir
from urllib.parse import quote
import requests as client
import json

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

# Check the image directory and download every card that doesn't exist (and the variants).
print("Downloading card images...")
for index in range(len(cards_json)):  # Using range so we know which index we're on even if we skip a card.
    card_name = cards_json[index]['defId']
    card_images_dir = f"{images_dir}/cards"
    card_dir = f"{card_images_dir}/{card_name}"

    if not path.isdir(card_images_dir):
        mkdir(card_images_dir)

    # If a directory for a card does not exist, attempt to fetch the base card and save it.
    if not path.isdir(card_dir):
        # Fetch the card.
        card_img = client.get(f"{card_img_url}/{card_name}.webp")
        if card_img.ok:
            # Create the directory for it.
            mkdir(card_dir)
            # Save the image.
            with open(f"{card_dir}/{card_name}.jpg", "wb") as file:
                file.write(card_img.content)

        # e.g. (204/301 200) Downloading card Valkyrie.webp...
        print(f"({index + 1}/{len(cards_json)} {card_img.status_code}) Downloading card {card_name}...")

    # Start fetching the variants of the card.
    variant_number = 1

    success = True
    while success:
        # Default to false in case we don't attempt fetching the image.
        success = False

        # The card name plus an incremented value e.g. Valkyrie_01.webp. Keep incrementing the value until nothing
        # gets returned, in which case we assume there are no more variants.
        variant_name = f"{card_name}_{variant_number:02d}"

        # If we downloaded the base card (e.g Valkyrie.webp) and we haven't already downloaded the variant.
        if path.isdir(card_dir) and f"{variant_name}.jpg" not in listdir(card_dir):
            # Fetch the variant.
            variant_img = client.get(f"{card_img_url}/{variant_name}.webp")
            if variant_img.ok:
                # Save the variant in the base card's folder.
                with open(f"{card_dir}/{variant_name}.jpg", "wb") as file:
                    file.write(variant_img.content)

            success = variant_img.ok

            # e.g. (204/301 200) Downloading card Valkyrie_01.webp...
            print(f"({index + 1}/{len(cards_json)} {variant_img.status_code}) Downloading variant {variant_name}...")

        variant_number += 1

# Check the image directory and download every location that doesn't exist
print("Downloading location images...")
for index in range(len(locations_json)):  # Using range so we know which index we're on even if we skip a location.
    location_name = locations_json[index]["defId"]
    location_file_name = quote(f"{locations_json[index]['name']}")  # Serializes the name for a web URL.
    location_images_dir = f"{images_dir}/locations"
    location_dir = f"{location_images_dir}/{location_name}"

    # If a base directory for the locations doesn't exist, create it.
    if not path.isdir(location_images_dir):
        mkdir(location_images_dir)

    # If a directory for the specific location doesn't exist, try fetch it and create the directory.
    if not path.isdir(location_dir):
        # Fetch location image and save it.
        location_img = client.get(f"{location_img_url}/{location_file_name}.webp")
        if location_img.ok:
            # Create the directory for it.
            mkdir(location_dir)
            # Save the image.
            with open(f"{location_dir}/{location_file_name}.jpg", "wb") as file:
                file.write(location_img.content)

        # e.g. (47/136 200) Downloading location Sinister%20London.webp...
        print(f"({index + 1}/{len(locations_json)} {location_img.status_code}) Downloading location {location_name}...")

print("Complete!")
