class Frame:
    id = ''
    time_stamp = ''
    Tcw = ''  # 世界坐标系到相机坐标系
    color = ''
    depth = ''
    camera = ''

    def __init__(self, id, time_stamp, Tcw, color, depth, camera) -> None:
        self.id = id
        self.time_stamp = time_stamp
        self.Tcw = Tcw
        self.color = color
        self.depth = depth
        self.camera = camera

    def createFrame():
        pass

    def findDepth():
        pass
    # 获得相机中心

    def getCamCenter():
        pass

    def isInFrame():
        pass
