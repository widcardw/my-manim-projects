from manimlib import *
from manimgl_mathjax import *
from my_videos.utils.reveal import get_dim, Reveal


class Unmask(Animation):
    CONFIG = {
        "lag_ratio": 1,
    }

    def __init__(self, mobject, direction, **kwargs):
        self.direction = direction
        self.mobject = mobject
        self.dim = get_dim(direction)
        self.background_rect = BackgroundRectangle(mobject)
        self.background_rect.shift(- direction *
                                   self.background_rect.length_over_dim(self.dim))
        self.bg_pos = self.background_rect.get_center()
        Animation.__init__(self, mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.background_rect.move_to(interpolate(
            self.bg_pos, self.starting_mobject.get_center(), alpha))
        target = Intersection(self.background_rect,
                              self.starting_mobject).match_style(self.mobject)
        if isinstance(self.starting_mobject, SVGMobject):
            target.set_fill(
                color=self.starting_mobject.get_fill_color(), opacity=1)
        self.mobject.become(target)


class TestUnmask(Scene):
    def construct(self):
        text = TexText("Hello, world!").scale(3).shift(UP)
        tex = JTex(
            "f(x;\\mu,\\sigma)=\\frac{1}{\\sqrt{2\\pi\\sigma^2}}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}").scale(1.5).shift(DOWN)
        self.play(Unmask(text, UP))
        self.play(Reveal(tex, RIGHT))
        self.wait()
