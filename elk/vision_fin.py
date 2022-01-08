import numpy as np
import cv2
import random
from matplotlib import pyplot as plt

'''
Problem #1 Image Transformations
'''
# 구성한 행렬을 OpenCV Library의 cv2.warpAffine 함수를 이용하여 임의의 이미지에 적용

# 1-1
def translate(image, x, y):
    rows, cols, ch = image.shape

    translation_matrix = np.array([[1,0,x],[0,1,y]],np.float32)
    # 이미지를 x축으로 x, y축으로 y 이동시키는 행렬
    transformed_image = cv2.warpAffine(image,translation_matrix,(cols,rows))
    #warpAffine 함수를 통한 이동변환

    return transformed_image


def rotate(image, angle):
    rows, cols, ch = image.shape

    rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    # 이미지의 (cols/2, row/2) 중심 위치에서 angle만큼 회전
    transformed_image = cv2.warpAffine(image,rotation_matrix,(cols,rows))
    # warpAffine 함수를 통한 회전 변환
    return transformed_image


def similarity(image, x, y, angle, scale):
    rows, cols, ch = image.shape

    rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),angle,scale)
    # 이미지의 (cols/2, row/2) 중심 위치에서 angle만큼 회전, scale 만큼 비율 조절
    transformed_image_temp = cv2.warpAffine(image,rotation_matrix,(cols,rows))
    translation_matrix = np.array([[1,0,x],[0,1,y]], np.float32)
    # 이미지를 x축으로 x, y축으로 y 만큼 이동
    transformed_image = cv2.warpAffine(transformed_image_temp,translation_matrix,(cols,rows))
    # warpAffine 함수를 통한 회전 변환
    return transformed_image

#Translation
img = cv2.imread('jump.JPG',cv2.IMREAD_COLOR)       #컬러 이미지 파일 불러오기
img_translation = translate(img, 100, 50)       # x: 100  y: 50 평행이동
img_rotation = rotate(img, 45)      #45deg 만큼 회전
img_similarity = similarity(img, 100, 50, 45, 0.5)
    #45deg 회전, 0.5배 축소, x+100, y+50 만큼 평행 이동

# 각 변환을 적용한 이미지를 출력
cv2.imshow('Original',img)
cv2.imshow('Translation', img_translation)
cv2.imshow('Rotation', img_rotation)
cv2.imshow('Similarity', img_similarity)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 2-1
# OpenCV Library를 이용하여 Gaussian Filter를 임의의 이미지에 적용

def Gaussian_blur(image):   # 평균이 아닌 중앙값으로 해당 픽셀을 대체, 점 모양의 잡음을 제거하는데 효과적

    result = cv2.GaussianBlur(image, (7,7), 0)  # 크기 7 by 7, 분산 0 인 가우시안 필터 적용

    return result


# 2-2
# Sobel, Laplacian Filter를 임의의 이미지에 적용

def Sobel(image):   #수평 또는 수직 에지를 추출하는데 유용

    result = cv2.Sobel(image, -1, 1, 0)
    # cvSobel(in, out, xorder, yorder, aperture_size);
    return result


def Laplacian(image):   #급격하게 변하는 Edge추출에 적합

    result = cv2.Laplacian(image, -1)
    # cvLaplace(in, out, aperture_size);

    return result


# 2-3

def add_salt_pepper_noise(image, prob):
    rows, cols, ch = image.shape

    # 0 ~ prob-1 사이의 salt 노이즈 개수를 랜덤하게 입력
    noise_salt = random.randint(0, prob)
    for i in range (noise_salt):
        y = random.randint(0, rows -1)
        x = random.randint(0, cols -1)
        image[y][x] = 255

    # 0 ~ prob-1 사이의 pepper 노이즈 개수를 랜덤하게 입력
    noise_pepper = random.randint(0, prob)
    for i in range (noise_pepper):
        y = random.randint(0, rows -1)
        x = random.randint(0, cols -1)
        image[y][x] = 0

    result = image
    return result


# 2-4
def median_blur(image, filter_size):
    result = cv2.medianBlur(image, filter_size)

    return result

#Filtering
img = cv2.imread('jump.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original',img)

#2-1
img_Gaussian = Gaussian_blur(img)
cv2.imshow('Gaussian_blur', img_Gaussian)

#2-2
img_sobel = Sobel(img)
cv2.imshow('Sobel', img_sobel)

img_Laplacian = Laplacian(img)
cv2.imshow('Laplacian', img_Laplacian)

#2-3
img_salt_pepper = add_salt_pepper_noise(img, 5000)
cv2.imshow('Salt and Pepper Noise', img_salt_pepper)

img_Gaussian_noise = Gaussian_blur(img_salt_pepper)
cv2.imshow('Gaussian blur with Noise', img_Gaussian_noise)

img_sobel_noise = Sobel(img_salt_pepper)
cv2.imshow('Sobel with Noise', img_sobel_noise)

img_Laplacian_noise = Laplacian(img_salt_pepper)
cv2.imshow('Laplacian with Noise', img_Laplacian_noise)

#2-4
img_median_noise = median_blur(img_salt_pepper,5)
cv2.imshow('Median Filter with Noise', img_median_noise)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Image Pyramids
# 3-1
img = cv2.imread('jump.jpg', cv2.IMREAD_COLOR)
rows, cols, ch = img.shape

# To down-sample an image, you should set the size smaller than the image
down_result_01 = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
down_result_02 = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
down_result_03 = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

img1 = cv2.imread('jump.jpg', cv2.IMREAD_COLOR)
rows, cols, ch = img.shape

# To up-sample an image, you should set the size lager than the image

# 최근방 이웃 보간법
up_result_01 = cv2.resize(img, dsize=(0,0), fx=2, fy=2, interpolation=cv2.INTER_AREA)
# 3차 보간법
up_result_02 = cv2.resize(img, dsize=(0,0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# 양선형 보간법
up_result_03 = cv2.resize(img, dsize=(0,0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original',img)
cv2.imshow('Original1', img1)
cv2.imshow('down_result_01', down_result_01)
cv2.imshow('down_result_02', down_result_02)
cv2.imshow('down_result_03', down_result_03)
cv2.imshow('up_result_01', up_result_01)
cv2.imshow('up_result_02', up_result_02)
cv2.imshow('up_result_03', up_result_03)


# 3-2
img2 = cv2.imread('jump.jpg', cv2.IMREAD_COLOR)
rows, cols, ch = img.shape

Gaussian_01 = cv2.pyrDown(img2)
Gaussian_02 = cv2.pyrDown(Gaussian_01)  # You should use Gaussian_01 as the input

cv2.imshow('Original',img2)
cv2.imshow('Gaussian_01', Gaussian_01)
cv2.imshow('Gaussian_02', Gaussian_02)

cv2.imshow('Original.jpg',img2)
cv2.imshow('pyrDown_01', Gaussian_01)
cv2.imshow('pyrDown_02', Gaussian_02)

cv2.waitKey(0)
cv2.destroyAllWindows()

