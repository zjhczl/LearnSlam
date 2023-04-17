# orb特征检测和fnn匹配

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# ORB特征检测


def ORB(img):
    img = img
    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(img, None)
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    return kp, des

# # draw only keypoints location,not size and orientation
# img2 = cv.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
# plt.imshow(img2), plt.show()


# FLANN匹配
path1 = '/home/zj/cx/LearnSlam/python/1.png'
path2 = '/home/zj/cx/LearnSlam/python/2.png'
img1 = cv.imread(path1, cv.IMREAD_GRAYSCALE)
img2 = cv.imread(path2, cv.IMREAD_GRAYSCALE)
kp1, des1 = ORB(img1)
kp2, des2 = ORB(img2)


FLANN_INDEX_LSH = 6
index_params = dict(algorithm=FLANN_INDEX_LSH,
                    table_number=6,  # 12
                    key_size=12,     # 20
                    multi_probe_level=1)  # 2

# FLANN_INDEX_KDTREE = 1
# index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]
# print([[0, 0] for i in range(10)])
# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches[:100]):
    if m.distance < 0.5*n.distance:
        matchesMask[i] = [1, 0]
        matche1 = matches[i][0]
        matche2 = matches[i][1]
        print("-----------------")
        print(matche1.queryIdx)  # 测试图像的特征点描述符的下标（第几个特征点描述符），同时也是描述符对应特征点的下标。
        # 每个特征点本身也具有以下属性：.pt:关键点坐标，.angle：表示关键点方向，.response表示响应强度，.size:标书该点的直径大小。
        print(kp1[matche1.queryIdx].pt)

        print(matche1.trainIdx)  # 样本图像的特征点描述符下标,同时也是描述符对应特征点的下标。
        print(kp2[matche1.trainIdx].pt)
        print(matche1.distance)  # 代表这怡翠匹配的特征点描述符的欧式距离，数值越小也就说明俩个特征点越相近。
        print("~~~~~~~~~")
        print(matche2.queryIdx)
        print(matche2.trainIdx)
        print(matche2.distance)
        print("-----------------")
        print("")
draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=cv.DrawMatchesFlags_DEFAULT)


img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2,
                         matches, None, **draw_params)
plt.imshow(img3,), plt.show()
