from manimlib.imports import *
from manim_sandbox.utils.imports import *


class GreenScene(Scene):
    CONFIG = {"camera_config": {"background_color": "#00ff00"}}


class Sample1(Scene):
    def construct(self):
        tex1 = TexMobject(r"\sqrt x ", stroke_width=2)
        tex2 = TexMobject(r"{(xyz)^2\over 2}", stroke_width=2)
        tex3 = TexMobject(r"S={1\over 2}Ah", stroke_width=2)
        tex4 = TexMobject(r"u^x", stroke_width=2)
        tex5 = TexMobject(
            r"e=\lim_{n\to \infty}\left(1+{1\over n}\right)^n", stroke_width=2)
        tex6 = TexMobject(r"x-y", stroke_width=2)
        tex7 = TexMobject(r"\sqrt{x+y\over x-y}", stroke_width=2)
        tex8 = TexMobject(r"|Z|=\sqrt{a^2+b^2}", stroke_width=2)
        tex9 = TexMobject(r"\sqrt{{1\over 12}+{1\over 48}}", stroke_width=2)
        tex10 = TexMobject(r"y^2={{\sqrt y}\over{x+2}}", stroke_width=2)
        tex11 = Matrix([["x", "x^2+1", "1"], ["y", "y^2+1", "1"],
                        ["z", "z^2+1", "1"]], stroke_width=2)
        self.add(tex11)
