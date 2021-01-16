from manimlib.imports import *
from manim_sandbox.utils.imports import *


class OneDim(DarkScene):
    def construct(self):
        dot_lst = [
            np.array([-2.5, 0, 0]),
            np.array([2.5, 0, 0])
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        path = obj.curve_path
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class TwoDim(DarkScene):
    def construct(self):
        dot_lst = [
            np.array([-4, -2.5, 0]),
            np.array([0, 2.5, 0]),
            np.array([4, -2.5, 0]),
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        path = obj.curve_path
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class ThreeDim(DarkScene):
    def construct(self):
        dot_lst = [
            np.array([-4, -2.5, 0]),
            np.array([-1.5, 2.5, 0]),
            np.array([1.5, -2.5, 0]),
            np.array([4, 2.5, 0])
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        path = obj.curve_path
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=7)
        self.wait()


class FourDim(DarkScene):
    def construct(self):
        dot_lst = [
            np.array([-4, -3, 0]),
            np.array([-1.5, 2.5, 0]),
            np.array([1, -3, 0]),
            np.array([5, -1, 0]),
            np.array([2, 2.5, 0])
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        path = obj.curve_path
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class FiveDim(DarkScene):
    def construct(self):
        dot_lst = [
            np.array([0, -1, 0]),
            np.array([-5, -2.5, 0]),
            np.array([-2, 3.2, 0]),
            np.array([1, -2, 0]),
            np.array([5, -3.5, 0]),
            np.array([2, 1, 0])
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        path = obj.curve_path
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class SixDim(DarkScene):
    def construct(self):
        dot_lst = [
            np.array([-5.9, 2.35, 0]),
            np.array([-1.58, 2.29, 0]),
            np.array([-5.62, -1.83, 0]),
            np.array([2.04, 2.33, 0]),
            np.array([4.64, -2.21, 0]),
            np.array([0.64, -0.51, 0]),
            np.array([4.66, 1.17, 0])
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        obj[1].add_updater(line_anim)
        path = obj.curve_path
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class Six(DarkScene):
    def construct(self):
        dot_lst = [4 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]) for i in range(7)]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        path = obj.curve_path
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class Four(DarkScene):
    def construct(self):
        dot_lst = [4.2 * np.array([np.cos(i * TAU / 4 - PI / 4), np.sin(i * TAU / 4 - PI / 4), 0])
                   for i in range(21)]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        obj[1].add_updater(line_anim)
        path = obj.curve_path

        # pts = AllPointsIndex(path)

        self.add(obj)
        self.wait()
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),
                  ShowCreation(path),
                  run_time=6.5)
        self.wait()


class EndText(DarkScene):
    def construct(self):
        text = TextMobject("Bezier Curve").scale(3)
        self.play(Write(text), run_time=2)
        self.wait(4)


class EndText1(DarkScene):
    def construct(self):
        text = TextMobject("Bezier Curve").scale(3)
        self.play(WriteRandom(text[0]), run_time=2)
        self.wait(4)


class EndText2(DarkScene):
    def construct(self):
        text = TextMobject("Bezier Curve").scale(3)
        self.play(ReversedWrite(text[0]), run_time=2)
        self.wait(4)
