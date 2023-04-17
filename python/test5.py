# 相机的标定
import numpy as np
import cv2 as cv
import glob

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*13, 3), np.float32)
print(objp)
objp[:, :2] = np.mgrid[0:13, 0:6].T.reshape(-1, 2)
print(objp)
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
images = glob.glob('/home/zj/cx/LearnSlam/python/img/*.jpeg')

for fname in images:
    img = cv.imread(fname)
    cv.namedWindow("zj", 0)
    cv.resizeWindow("zj", 600, 600)  # 设置窗口大小

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    print("findChessboardCorners...")
    ret, corners = cv.findChessboardCorners(gray, (13, 6), None)  # （内点的行列）

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(
            gray, corners, (11, 11), (-1, -1), criteria)  # 使角点的精度达到亚像素级别。

        imgpoints.append(corners2)
        print(objp.shape)
        print(corners2.shape)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (13, 6), corners2, ret)
        cv.imshow('zj', img)
        cv.waitKey(500)
# 返回ret、相机矩阵、畸变系数、旋转和平移向量等。
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None)
print('ret:')
print(ret)
print('mtx(相机矩阵):')
print(mtx)
print("dist(畸变系数)")
print(dist)
print('rvecs(旋转):')
print(rvecs)
print('tvecs(平移向量):')
print(tvecs)


img = cv.imread('/home/zj/cx/LearnSlam/python/img/8.jpeg')
h, w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# # undistort
# dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# # crop the image
# # x, y, w, h = roi
# # dst = dst[y:y+h, x:x+w]
# cv.imshow("zj", dst)
# cv.waitKey(0)

# undistort
mapx, mapy = cv.initUndistortRectifyMap(
    mtx, dist, None, newcameramtx, (w, h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
cv.imshow('zj', dst)
cv.waitKey(0)

mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(
        objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print("total error: {}".format(mean_error/len(objpoints)))


def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    print(corner)
    print(tuple(imgpts[0].ravel()))
    img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(
        imgpts[0].ravel())[0]), int(tuple(
            imgpts[0].ravel())[1])), (255, 0, 0), 5)
    img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(
        imgpts[1].ravel())[0]), int(tuple(
            imgpts[1].ravel())[1])), (0, 255, 0), 5)
    img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(
        imgpts[2].ravel())[0]), int(tuple(
            imgpts[2].ravel())[1])), (0, 0, 255), 5)
    return img


criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)


for fname in glob.glob('/home/zj/cx/LearnSlam/python/img/*.jpeg'):
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (13, 6), None)
    if ret == True:
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        # Find the rotation and translation vectors.
        ret, rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)
        # project 3D points to image plane
        imgpts, jac = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)

        img = draw(img, corners2, imgpts)
        cv.imshow('zj', img)
        k = cv.waitKey(0) & 0xFF
        if k == ord('s'):
            cv.imwrite(fname[:6]+'.png', img)


cv.destroyAllWindows()
