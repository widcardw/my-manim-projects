from manimlib import *
from my_videos.utils.pixel_mobject import *


class MultiCameraScene(Scene):
    def construct(self):
        text = Circle(radius=2, fill_opacity=0.5).to_edge(LEFT)
        self.add(text)
        surface = ParametricSurface(lambda u, v: np.array(
            [8*u, 6*v, 0])).center().to_edge(RIGHT)
        self.add(surface)
        self.wait(0.1)
        cm = PixelMobject(self.camera.get_pixel_array())
        self.add(cm)
        self.wait(0.1)

