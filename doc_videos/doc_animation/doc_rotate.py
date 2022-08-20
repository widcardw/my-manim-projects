from manimlib import *


class RotatingExample(Scene):
    def construct(self):
        square=Square().scale(2)
        self.add(square)

        self.play(
            Rotating(
                square,
                angle=PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotating(
                square,
                angle=PI,
                run_time=2,
                axis=RIGHT
            )
        )
        self.wait(0.3)


class RotateExample(Scene):
    def construct(self):
        square=Square().scale(2)
        self.add(square)

        self.play(
            Rotate(
                square,
                PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotate(
                square,
                PI,
                run_time=2,
                axis=RIGHT
            )
        )
        self.wait(0.3)