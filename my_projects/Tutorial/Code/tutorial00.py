from manimlib.imports import *
from manim_sandbox.utils.imports import *


# 注意:DarkScene为我自定义背景色的场景,
# 若想要使用,请将以下代码取消注释
# class DarkScene(Scene):
# 	CONFIG = {"camera_config":{"background_color":"#1f252A"}}


class MoveToTargetExample(DarkScene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.scale(3).shift(RIGHT * 7 + UP * 2)  # 操作A的target

        self.add(A)
        self.wait()
        self.play(MoveToTarget(A))
        self.wait()


class MoveToTargetExample2(DarkScene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.become(Square(side_length=2, color=BLUE).shift(
            RIGHT * 2))  # 操作A的target

        self.add(A)
        self.wait()
        self.play(MoveToTarget(A))
        self.wait()


class RotateScene1(DarkScene):
    def construct(self):
        axes = Axes().set_opacity(0.4)
        sq1 = Square(side_length=1, color=BLUE).shift(UP * 2.5)
        sq2 = Square(side_length=1, color=RED).shift(UP * 2.5)
        self.add(axes, sq1, sq2)
        self.wait(0.5)
        self.play(
            Rotating(sq1, about_point=ORIGIN, radians=TAU / 3),
            sq2.rotate, {"about_point": ORIGIN, "angle": TAU / 3},
            run_time=3
        )
        self.wait(0.5)


class UpdateSample(DarkScene):
    def construct(self):
        dot = Dot()
        text = TextMobject("This is some text.").next_to(dot, RIGHT)

        # text.add_updater(lambda a:a.next_to(dot, RIGHT))

        def anim(obj):
            obj.next_to(dot, RIGHT)

        text.add_updater(anim)
        self.add(dot, text)
        self.play(dot.shift, UP * 3)
        self.play(dot.shift, DOWN * 3)
        self.wait()
