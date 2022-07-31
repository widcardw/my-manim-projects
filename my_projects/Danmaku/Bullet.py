from manimlib.imports import *


class Bullet(Triangle):
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 0,
        "length": DEFAULT_ARROW_TIP_LENGTH,
        "start_angle": PI,
        "aspect": 1.5,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        digest_config(self, kwargs)
        self.set_height(self.length, stretch=True)
        self.set_width(self.length * self.aspect, stretch=True)
        self.points[5:7] += np.array([self.length, 0, 0])
        self.scale(0.5)

    def get_angle(self):
        return angle_of_vector(self.get_vector())

    def get_vector(self):
        return self.point_from_proportion(0.5) - self.get_start()