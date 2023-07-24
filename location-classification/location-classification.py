from tensorflow.keras.utils import image_dataset_from_directory as image_dataset
from tensorflow.keras import layers, optimizers, losses
from os import listdir
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import json

with open("config.json", "r") as file:
    config = json.loads(file.read())

    base_dir = config["dataset_dir"]
    locations_dir = f"{base_dir}/locations"

# Grab a random image from the directory and show it. Can be useful for getting familiar with the data.
def display_random_image(directory):
    """
    :param directory: base path of the dataset containing the class directories
    :return: random image from the dataset
    """
    random_class = random.sample(listdir(directory), 1).pop()
    random_image_name = random.sample(listdir(f"{directory}/{random_class}"), 1).pop()
    random_image = mpimg.imread(f"{directory}/{random_class}/{random_image_name}")
    print(random_image_name)

    plt.imshow(random_image)
    plt.axis(False)

    return random_image


# Create a graph of a model's metrics so it's easier to tell how well the model is fitting to the data.
def graph_model_metrics(history):
    plt.plot(history.history["accuracy"], label="accuracy")
    plt.plot(history.history["val_accuracy"], label="val_accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.ylim([0, 1])
    plt.legend()


# Simply display the model's ending metrics in a way that's easy for the user to understand.
def evaluate_model(model, dataset):
    loss, accuracy = model.evaluate(dataset, verbose=0)
    print(f"Loss: {round(loss, 4)}")
    print(f"Accuracy: {round(accuracy * 100, 2)}%")


# Divide each image's RGB values by 255 to put it between 0 and 1 so it's easier for the model to train.
def normalize_image(image, label):
    return image/255., label


# Load the images from the dataset.
location_dataset = image_dataset(locations_dir, image_size=(256, 256))
# Normalize the images.
location_dataset.map(normalize_image)

# Split the dataset into training and validation sets.
DATASET_SIZE = len(location_dataset)
LOCATION_TRAIN = int(0.8 * DATASET_SIZE)

location_train = location_dataset.take(LOCATION_TRAIN)
location_val = location_dataset.skip(LOCATION_TRAIN)

# Set the seed so the model trains the same each time (which will make it easier to test parameters)
tf.random.set_seed(42)

# TinyVGG architecture.
model_1 = tf.keras.Sequential(layers=[
    layers.Conv2D(filters=10, kernel_size=3, activation="relu", input_shape=(256, 256, 3)),
    layers.Conv2D(filters=10, kernel_size=3, activation="relu"),
    layers.MaxPool2D(),
    layers.Conv2D(filters=10, kernel_size=3, activation="relu"),
    layers.Conv2D(filters=10, kernel_size=3, activation="relu"),
    layers.MaxPool2D(),
    layers.Flatten(),
    layers.Dense(127, activation="softmax")
])

model_1.compile(
    optimizer=optimizers.Adam(),
    loss=losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

history_1 = model_1.fit(
    x=location_train,
    epochs=50,
    validation_data=location_val
)

evaluate_model(model_1, location_val)
graph_model_metrics(history_1)
model_1.save("model_1")
