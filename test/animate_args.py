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
