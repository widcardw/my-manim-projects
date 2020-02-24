from manimlib.imports import *


class Func(Scene):

    def construct(self):

        graph = ParametricFunction(
            lambda t: UP*(np.exp(t)/t-5)+t*RIGHT, t_min=0.01, t_max=10).set_color("#FFFF00")
        self.play(ShowCreation(graph))
        self.wait()
