from pixel import Pixel


class Dot(Pixel):
    size = 12
    type = 4

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
