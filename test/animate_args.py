from manimlib import *


class TestAnimateArgs(Scene):
    def construct(self) -> None:
        a = Circle().to_edge(LEFT)
        anim_builder = (
            a
            .animate(run_time=3, time_span=(1, 2), rate_func=double_smooth, path_arc=PI/2)
            .scale(3)
            .to_edge(RIGHT)
        )
        b = Square()
        self.add(b)
        self.play(anim_builder, b.animate.scale(3).set_anim_args(run_time=4))

class TestColorExample(Scene):
    def construct(self) -> None:
        s = Square(side_length=5, stroke_width=0, fill_color=[
            RED, ORANGE, YELLOW,
            YELLOW, GREEN, TEAL,
            TEAL, BLUE, PURPLE,
            PURPLE, MAROON, RED
        ], fill_opacity=1)
        self.add(s)
