from manimlib.imports import *
from manim_sandbox.utils.imports import *


class ShiftRotate(Scene):

    def construct(self):
        grid = ScreenGrid()
        self.add(grid)
        sq_1 = Square(side_length=1, color=TEAL).shift(LEFT*5)
        sq_1.save_state()

        def func(mob, alpha):
            sq_1.restore()
            sq_1.shift(RIGHT*10*alpha)
            sq_1.rotate(PI*3*alpha)

        self.play(UpdateFromAlphaFunc(sq_1, func), run_time=5, rate_func=sine)
        self.wait()


class RandomWaterMark(Scene):
    def construct(self):
        grid = ScreenGrid().set_opacity(0.4)
        self.add(grid)
        text = Text("bilibili独播", font="思源黑体 CN Bold").scale(0.5)

        def move_to_random_place(mob, dt):
            text.move_to(np.array([
                (random.randint(-7, 7))*dt*60,
                (random.randint(-4, 4))*dt*40,
                0
            ]))

        text.add_updater(move_to_random_place)
        self.add(text)
        self.wait(5)
