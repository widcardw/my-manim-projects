from manimlib import IN, ORIGIN, OUT, PI, PURPLE, RED, UP, Integer, LaggedStartMap, Scene, Square, Text, VGroup, RIGHT, Mobject, integer_interpolate, interpolate, interpolate_color, linear, np

from manimlib.animation.animation import Animation

from manimlib.animation.update import UpdateFromAlphaFunc


class RotateFadeIn(Animation):
    def interpolate_mobject(self, alpha: float) -> None:
        index, subalpha = integer_interpolate(0, 2, alpha)
        self.mobject.become(self.starting_mobject)
        self.mobject.rotate(alpha * PI * 4, axis=UP)
        if index == 0:
            self.mobject.set_opacity(subalpha)
        else:
            self.mobject.set_opacity(1)


color_list = [PURPLE, RED, PURPLE]


class CSquare(Square):
    def __init__(self, side_length: float = 2, **kwargs):
        super().__init__(side_length, **kwargs)
        self.angle = 0

    def rotate(self, angle: float, axis: np.ndarray = ..., about_point: np.ndarray | None = None, **kwargs):
        self.angle += angle
        return super().rotate(angle, axis, about_point, **kwargs)

    def save_state(self, use_deepcopy: bool = False):
        self.__saved_angle = self.angle
        return super().save_state(use_deepcopy)

    def restore(self):
        self.angle = self.__saved_angle
        return super().restore()


class Aniplex(Scene):
    def construct(self) -> None:
        ani = VGroup(*[
            Text(i, font="Arial", slant="italic", bold="BOLD").scale(3)
            for i in 'ANIPLEX'
        ]).arrange(RIGHT, buff=0.5)

        squs = VGroup(*[
            CSquare(side_length=1.5, color=PURPLE).move_to(ani[0])
            for _ in range(7)
        ])
        for s in squs:
            s.save_state()

        squs.set_stroke(opacity=0)

        def gene_updater(index: int):
            def updater(mob: Mobject, a: float):
                cur, al = integer_interpolate(0, 6, a)
                if cur < index - 1:
                    return
                alpha = (cur - index + al) / 6
                mob.restore()
                if cur == index - 1:
                    mob.set_stroke(opacity=al)
                mob.move_to(interpolate(
                    ani[0].get_center(), ani[-1].get_center(), alpha))
                index1, subalpha1 = integer_interpolate(0, 2, alpha)
                if index1 == 0:
                    mob.scale(1 + subalpha1 / 2)
                else:
                    mob.scale(1.5 - subalpha1 / 2)
                index2, subalpha2 = integer_interpolate(0, 4, alpha)
                mob.rotate(-mob.angle, axis=UP)
                mob.rotate(np.sin(PI * (index2 + subalpha2)) + PI / 2, axis=UP)
                mob.set_color(
                    interpolate_color(
                        interpolate_color(PURPLE, RED, alpha),
                        interpolate_color(RED, PURPLE, alpha),
                        alpha
                    )
                )
            return updater

        self.wait()
        self.add(squs)
        self.play(
            LaggedStartMap(RotateFadeIn, ani, lag_ratio=0.1),
            *[
                UpdateFromAlphaFunc(squs[i], gene_updater(i))
                for i in range(len(squs))
            ],
            # UpdateFromAlphaFunc(square, square_anim),
            # UpdateFromAlphaFunc(squs, update_group),
            run_time=2, rate_func=linear)
        print(list(map(lambda a: a.angle, squs)))
        # self.remove(square)
        self.play(*[
            squs[i].animate.rotate(-squs[i].angle - i * PI / (len(squs) - 1) + (0 if i * PI / (len(squs) - 1) < PI / 2 else PI), axis=UP)
            for i in range(len(squs))
        ], run_time=0.5)
        self.wait()
