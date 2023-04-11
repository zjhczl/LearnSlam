class Camera:
    # 相机内参
    fx = ''
    fy = ''
    cx = ''
    cy = ''
    depth_scale = ''
    # 坐标转换

    def world2camera(p_w, Tcw):
        pass

    def camera2world(p_c, Tcw):
        pass

    def camera2pixel(p_c):
        pass

    def pixel2camera(p_p, depth):
        pass

    def pixel2world(p_p, Tcw, depth):
        pass

    def world2pixel(p_w, Tcw):
        pass
