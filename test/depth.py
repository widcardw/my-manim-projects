from manimlib import *

class TestDepthTest(Scene):
    def construct(self) -> None:
        square = Square(fill_opacity=0.5, fill_color=BLUE_E)
        square.apply_depth_test()
        line = Line(OUT, IN)
        line.apply_depth_test()
        self.add(line, square )