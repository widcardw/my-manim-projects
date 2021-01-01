from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene1(NewGraphScene):

    def construct(self):
        # graph_origin=np.array([-4, -2.5, 0])
        self.y_max = 5
        self.y_min = -1
        self.y_axis_height = 6
        self.x_min = -1
        self.x_max = 9
        self.x_axis_width = 10
        self.setup_axes(animate=True)

        def func(z, ita):
            f = 2
            for i in range(int(ita)-1, 1, -1):
                f = 2+(z-1)/f
            return 1+(z-1)/f

        sqrt_graph = ParametricFunction(lambda t: [t-4, np.sqrt(t)-2.5, 0], t_min=0, t_max=9, color=WHITE,
                                        stroke_width=18, stroke_opacity=0.3).set_plot_depth(-1)
        graph = ParametricFunction(
            lambda t: [t-4, func(t, 2)-2.5, 0], t_min=0, t_max=9, color=BLUE)
        self.play(ShowCreation(graph), ShowCreation(sqrt_graph))
        formula_01 = TexMobject(r"y=1+{x-1\over 2}").to_corner(UR)
        self.play(Write(formula_01))
        self.wait()
        formula = [
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over 2}}}}}}}}}}}}",
            r"y=1+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\displaystyle{x-1\over {2+\ddots}}}}}}}}}}}}}",
        ]
        formula_group = VGroup(*[
            TexMobject(tex).to_corner(UR) for tex in formula
        ])
        graph_group = VGroup(*[
            ParametricFunction(
                lambda t: [t - 4, func(t, i) - 2.5, 0], t_min=0, t_max=9, color=BLUE)
            for i in range(3, 11)
        ]
        )
        for i in range(5):
            self.play(Transform(graph, graph_group[i]),
                      Transform(formula_01, formula_group[i]))
            self.wait()
        self.play(RT(graph, graph_group[-1]),
                  RT(formula_01, formula_group[-1]))
        self.wait()
        sq_y = TexMobject(r"\sqrt{x}").move_to(
            formula_group[-1][0][0].get_center()+LEFT*0.2+UP*0.1)
        self.play(RT(formula_group[-1][0][0], sq_y))
        self.wait()
