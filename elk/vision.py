import numpy as np
import cv2
import random
from matplotlib import pyplot as plt

def my_median_blur(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if (i + z - indexer < 0) | (i + z - indexer > len(data) - 1):
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if (j + z - indexer < 0) | (j + indexer > len(data[0]) - 1):
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])
            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []

    return data_final


def median_blur(img, filter_size):
    result = cv2.medianBlur(img, filter_size)

    return result


def add_salt_pepper_noise(img, prob):
    rows, cols, ch = img.shape

    noise_salt = random.randint(0, prob)
    for i in range(noise_salt):
        y = random.randint(0, rows - 1)
        x = random.randint(0, cols - 1)
        img[y][x] = 255

    noise_pepper = random.randint(0, prob)
    for i in range(noise_pepper):
        y = random.randint(0, rows - 1)
        x = random.randint(0, cols - 1)
        img[y][x] = 0

    result = img
    return result

# original
image = cv2.imread('./elk/jump.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('Original', image)

# Add Salt pepper noise
noisy_img = add_salt_pepper_noise(image, 1000)
cv2.imshow('noisy_img', noisy_img)

# Apply Median Filter
Median_blur_img = median_blur(noisy_img, 15)
cv2.imshow('Median Blur', Median_blur_img)

# Median Blur by numpy
# filtered_img = my_median_blur(noisy_img, 5)
filtered_img = my_median_blur(noisy_img, filter_size=3)
cv2.imshow('filtered_img', filtered_img)


cv2.waitKey(0)
cv2.destroyAllWindows()