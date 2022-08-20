from manimlib import *


class TwoMillionLogo(Scene):
    def construct(self):
        n = ValueTracker(2)
        text = VGroup(
            Tex("n="),
            DecimalNumber(2.0)
        ).arrange(RIGHT).to_corner(DR)
        text[1].add_updater(
            lambda a: a.set_value(n.get_value())
        )
        logo = VMobject().add_updater(
            lambda a: a.become(
                ParametricCurve(
                    lambda t: np.array([
                        np.sign(np.cos(t)) * np.power(abs(np.cos(t)), 2 / n.get_value()),
                        np.sign(np.sin(t)) * np.power(abs(np.sin(t)), 2 / n.get_value()),
                        0
                    ]),
                    t_range=[0, TAU, 0.02]
                ).scale(2)
            )
        )
        self.add(logo, text)
        self.wait()
        self.play(n.animate.set_value(10), run_time=8, rate_func=linear)
        logo.clear_updaters()
        self.wait()


class Chopstick(Scene):
    def construct(self):
        stick = ParametricSurface(
            lambda u, v: np.array([
                np.sign(np.cos(u)) * np.power(abs(np.cos(u)), 2 / np.log(v)) / np.clip(8 - np.log(v), 4, 6),
                np.sign(np.sin(u)) * np.power(abs(np.sin(u)), 2 / np.log(v)) / np.clip(8 - np.log(v), 4, 6),
                v / 4 - 5
            ]),
            u_range=(0, TAU),
            v_range=(np.exp(2), 40)
        )
        self.add(ThreeDAxes(), stick)
