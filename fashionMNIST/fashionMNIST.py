import torchvision
import matplotlib.pyplot as plt
import numpy as np
import random

train_images, train_labels = zip( *torchvision.datasets.FashionMNIST(".", train=True, download=True))
train_images = np.asarray([np.array(img) for img in train_images], dtype=np.float32)
train_labels = np.asarray(train_labels, dtype=np.int64)


test_images, test_labels = zip(*torchvision.datasets.FashionMNIST(".", train=False, download=True))
test_images = np.asarray([np.array(img) for img in test_images], dtype=np.float32)
test_labels = np.asarray(test_labels, dtype=np.int64)

#Normalizing
test_images /=255
train_images /= 255

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]
num_classes = len(class_names)

num_images = 16
random_indices = random.sample(range(len(train_images)), num_images)
images = train_images[random_indices]
labels = train_labels[random_indices]

# Plot the images in a 5x5 grid
fig, axes = plt.subplots(4, 4, figsize=(8, 8))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(images[i], cmap= "winter_r")
    ax.set_title(class_names[labels[i]])
    ax.axis("off")

plt.show()