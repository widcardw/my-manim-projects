from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene02(DarkScene):
    def construct(self):
        space1 = DashedVMobject(Square(side_length=1.5), color=GREY).shift(LEFT * 3).scale(1.05).rotate(PI / 4)
        space2 = DashedVMobject(Square(side_length=1.5), color=GREY).shift(RIGHT * 3).scale(1.05).rotate(PI / 4)
        squ1 = Square(side_length=1.5, fill_opacity=1, stroke_width=0, color=BLUE).shift(LEFT * 3).rotate(PI / 4)
        squ1.set_sheen(0.5, UP)
        self.play(ShowCreation(space1), ShowCreation(space2))
        self.play(FadeInFromPoint(squ1, squ1.get_center()))
        self.wait()
        self.play(squ1.shift, RIGHT * 6, run_time=1.5, rate_func=linear)
        self.wait()
        cir = Circle(radius=1, fill_opacity=1, stroke_width=0).shift(RIGHT * 3).scale(2).rotate(PI/16)
        cir.set_sheen(0.5, UL)
        pol = RegularPolygon(8, color=ORANGE, fill_opacity=1).shift(LEFT * 3).scale(2).shift(UP).rotate(PI/16)
        pol.set_sheen(0.5, UL)
        self.play(
            ReplacementTransform(squ1, cir),
            Transform(space2, DashedVMobject(Circle(radius=1, color=GREY).shift(RIGHT * 3).scale(2.05).rotate(PI/16))),
            Transform(space1, DashedVMobject(RegularPolygon(8, color=GREY)).shift(LEFT * 3).scale(2.05).rotate(PI/16)),
        )
        self.wait()
        code = VGroup(
            CodeLine("def interpolate(start, end, alpha):"),
            CodeLine("return (1 - alpha) * start + alpha * end")
        )
        text_alpha = TexMobject("\\alpha=")
        dec = DecimalNumber(0.).next_to(text_alpha)
        al = VGroup(text_alpha, dec)
        code[1].next_to(code[0][4], DOWN, aligned_edge=LEFT, buff=0.2)
        code.move_to(DOWN * 2.2)
        self.play(space1.shift, UP, space2.shift, UP, cir.shift, UP,
                  FadeInFrom(code))
        line_group = VGroup(*[
            Line(cir.point_from_proportion(i/8),
                 pol.get_vertices()[i], color=YELLOW_A)
            for i in range(8)
        ])
        al.next_to(cir, DOWN)
        self.play(Write(al))
        self.play(Transform(cir, pol),
                  UpdateFromAlphaFunc(dec, lambda a, alpha: a.set_value(alpha)),
                  UpdateFromFunc(al, lambda a:a.next_to(cir, DOWN)),
                  ShowCreation(line_group, lag_ratio=0),
                  run_time=2, rate_func=sine)
        self.wait()
