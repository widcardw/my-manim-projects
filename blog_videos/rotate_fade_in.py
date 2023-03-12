from manimlib import ITALIC, PI, TAU, UP, Animation, Mobject, Scene, Text, integer_interpolate, np


class RotateFadeIn(Animation):

    def __init__(
        self,
        mobject: Mobject,
        angle: float = PI,
        axis: np.ndarray = UP,
        **kwargs
    ):
        self._angle = angle
        self._axis = axis
        super().__init__(mobject, **kwargs)

    def begin(self) -> None:
        self._cached_angle = 0
        super().begin()
        # self.mobject.rotate(-self._angle, self._axis)
        self.starting_mobject.rotate(-self._angle, self._axis)

    def interpolate_mobject(self, alpha: float) -> None:
        # index, subalpha = integer_interpolate(0, 2, alpha)
        # self.mobject.become(self.starting_mobject)
        # self.mobject.rotate(alpha * self._angle, axis=self._axis)
        # if index == 0:
        #     self.mobject.set_opacity(subalpha)
        # else:
        #     self.mobject.set_opacity(1)
        self.mobject.become(self.starting_mobject)
        self.mobject.rotate(alpha * self._angle, self._axis)
        self.mobject.set_opacity(alpha)


class RotateFadeInExample(Scene):
    def construct(self) -> None:
        r = Text("Rotate", font="Jetbrains Mono", slant=ITALIC).scale(3)
        self.play(RotateFadeIn(r, angle=TAU/3, run_time=3))
