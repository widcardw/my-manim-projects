from manimlib import *
from ManimGL_MathJax.manimgl_mathjax import *


def get_dim(direction: np.ndarray) -> int:
    dim = np.where(np.abs(direction) == 1)[0][0]
    return dim


class Reveal(Animation):
    CONFIG = {
        "lag_ratio": 1
    }

    def __init__(self, mobject: VMobject, direction=UP, **kwargs):
        self.mobject = mobject
        self.direction = direction
        self.dim = get_dim(direction)
        self.background_rect = BackgroundRectangle(mobject)
        self.mobject.shift(- direction *
                           self.mobject.length_over_dim(self.dim))
        Animation.__init__(self, mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.shift(
            self.direction * self.background_rect.length_over_dim(self.dim) * alpha)
        target = Intersection(self.background_rect,
                              self.mobject).match_style(self.mobject)
        if isinstance(self.starting_mobject, SVGMobject):
            target.set_fill(
                color=self.starting_mobject.get_fill_color(), opacity=1)
        self.mobject.become(target)


class TestReveal(Scene):
    def construct(self):
        cir = JTex("\\pi r^2", color=WHITE)
        self.play(Reveal(cir, RIGHT), run_time=2)
        self.add(cir)
