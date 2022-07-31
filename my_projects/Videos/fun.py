from manimlib.imports import *
from manim_sandbox.utils.imports import *


class test(NewGraphScene):
    def construct(self):
        self.setup_axes()
        self.add_parametric_graph(
            lambda t: [t-np.sin(t)-PI, 1-np.cos(t)-1, 0], t_min=0, t_max=TAU)


class CompareRotate(Scene):

    def construct(self):

        cir4 = Circle(radius=3, stroke_opacity=0.2, color=WHITE).shift(LEFT*2)
        dot4 = Dot(color=RED).shift(RIGHT*1)
        dot5 = Dot(color=BLUE).shift(RIGHT*1)
        dot6 = Dot(color=GREEN).shift(RIGHT * 1)
        dot7 = Dot(color=YELLOW).shift(RIGHT * 1)
        text4 = Text("RED:   Rotate smooth",
                     font="Consolas for Powerline FixedD", color=RED).scale(0.4)
        text5 = Text("BLUE:  Rotating linear",
                     font="Consolas for Powerline FixedD", color=BLUE).scale(0.4)
        text6 = Text("GREEN: Rotating smooth",
                     font="Consolas for Powerline FixedD", color=GREEN).scale(0.4)
        text7 = Text("YELLOW:Rotating sine",
                     font="Consolas for Powerline FixedD", color=YELLOW).scale(0.4)
        vgroup_text = VGroup(
            text4, text5, text6, text7
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(RIGHT*4.2)
        self.add(cir4, dot4, dot5, dot6, dot7, vgroup_text)
        for i in range(2):
            self.play(
                Rotate(dot4, TAU, about_point=LEFT*2),
                Rotating(dot5, radians=TAU, about_point=LEFT*2),
                Rotating(dot6, radians=TAU, rate_func=smooth,
                         about_point=LEFT*2),
                MRotate(dot7, radians=TAU, about_point=LEFT*2),
                run_time=4
            )
            self.wait(1)


class TestFont(Scene):
    def construct(self):
        text = TextMobject("字体测试Abc").shift(UP)
        text2 = TexMobject(
            r"\sum_{n=1}^{\infty}{1\over n^2}={\pi^2 \over 6}").next_to(text, DOWN)
        #text3 = TextMobject("公式").scale(2).next_to(text2, DOWN)
        self.play(Write(text))
        self.play(Write(text2))
        self.wait()


class BGPic(Scene):
    def construct(self):
        rect = Rectangle(width=50, height=FRAME_HEIGHT/2, fill_opacity=1)
        rect.set_color([RED, ORANGE, YELLOW, TEAL, BLUE, "#0000ff"])
        rect.set_sheen_direction(DOWN)
        self.add(rect)


class BoolVGroup(VMobject):
    def __init__(self, *vmobject,**kwargs):
        if not all([isinstance(m, VMobject) for m in vmobject]):
            raise Exception("All submobjects must be of type VMobject")
        super().__init__(**kwargs)
        for index, obj in enumerate(vmobject):
            if index % 2:
                self.append_points(obj.get_all_points()[::-1])
            else:
                self.append_points(obj.get_all_points())


class TextBool(Scene):
    def construct(self):
        cir = Circle().scale(5)
        text = TextMobject("Hello").scale(5)
        bg = BoolVGroup(cir, text)
        bg.set_stroke(width=0)
        bg.set_fill(opacity=0.3)
        self.add(bg)
