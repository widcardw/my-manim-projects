from manimlib import IN, ORIGIN, OUT, PI, PURPLE, RED, UP, LaggedStartMap, Scene, Square, Text, VGroup, RIGHT, Mobject, integer_interpolate, interpolate, interpolate_color, linear, np

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


color_list = [PURPLE, RED, RED, PURPLE]


class Aniplex(Scene):
    def construct(self) -> None:
        ani = VGroup(*[
            Text(i, font="Arial", slant="italic", bold="BOLD").scale(3)
            for i in 'ANIPLEX'
        ]).arrange(RIGHT, buff=0.5)
        square = Square(side_length=1.5).move_to(ani[0])
        square.save_state()

        squs = VGroup()

        def square_anim(mob: Mobject, alpha: float):
            mob.restore()
            mob.move_to(interpolate(
                ani[0].get_center(), ani[-1].get_center(), alpha))
            index1, subalpha1 = integer_interpolate(0, 2, alpha)
            if index1 == 0:
                mob.scale(1 + subalpha1 / 2)
            else:
                mob.scale(1.5 - subalpha1 / 2)
            index2, subalpha2 = integer_interpolate(0, 6, alpha)
            mob.rotate(np.sin(PI * (index2 + subalpha2)), axis=UP)
            mob.set_color(
                interpolate_color(
                    interpolate_color(PURPLE, RED, alpha),
                    interpolate_color(RED, PURPLE, alpha),
                    alpha
                )
            )

        def update_group(mob: Mobject, alpha: float):
            index, subalpha = integer_interpolate(0, 6, alpha)
            if len(mob) <= index or abs(alpha - 1) < 1e-8:
                mob.add(square.copy().clear_updaters())
            mob.set_color_by_gradient(*color_list)

        self.wait()
        self.add(squs)
        self.play(
            LaggedStartMap(RotateFadeIn, ani, lag_ratio=0.1),
            UpdateFromAlphaFunc(square, square_anim),
            UpdateFromAlphaFunc(squs, update_group),
            run_time=2, rate_func=linear)
        self.remove(square)
        self.play(*[
            squs[i].animate.rotate(
                i * PI / (len(ani) - 1) - (0 if i * PI / (len(ani) - 1) < PI / 2 else PI), axis=UP)
            for i in range(len(ani))
        ], run_time=0.5)
        self.wait()
