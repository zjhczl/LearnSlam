import yaml


class Config:
    def __init__(self, confPath) -> None:
        self.setParameterFile(confPath)

    def setParameterFile(self, confPath):
        with open(confPath, 'r', encoding='utf8') as file:  # utf8可识别中文
            self.conf = yaml.safe_load(file)

    def get(self, name):
        return self.conf[name]


if __name__ == '__main__':
    confPath = '/home/zj/cx/LearnSlam/python/myslam/config.yaml'
    conf = Config(confPath)
    print(conf.get("camera.fx"))
