from manimlib import *


class AutoValue(ValueTracker):
    def __init__(self, value=0., **kwargs):
        super().__init__(value=value, **kwargs)

    def keep_update(self, obj: ValueTracker, func):
        self.add_updater(
            lambda a: a.set_value(func(obj.get_value()))
        )


class FuncMobject(Mobject):

    def __init__(self, func=lambda a: a, **kwargs):
        super().__init__(**kwargs)
        self.data["func"] = func

    def get_func(self):
        return self.data["func"]

    def set_func(self, func=lambda a: a):
        self.data["func"] = func
        return self


class AxesWithRect(Axes):

    def input_to_function_point(self, x, func: FuncMobject):
        return self.c2p(x, func.get_func()(x))

    def i2fp(self, x, func: FuncMobject):
        return self.input_to_function_point(x, func)

    def get_discrete_rectangles(self,
                                func,
                                x_range=None,
                                dx=None,
                                input_sample_type="center",
                                stroke_width=0.2,
                                stroke_color=BLACK,
                                fill_opacity=1.,
                                colors=(BLUE, GREEN),
                                show_signed_area=True):
        if x_range is None:
            x_range = self.x_range[:2]
        if dx is None:
            dx = self.x_range[2]
        if len(x_range) < 3:
            x_range = [*x_range, dx]

        rects = []
        xs = np.arange(*x_range)
        for x0, x1 in zip(xs, xs[1:]):
            if input_sample_type == "left":
                sample = x0
            elif input_sample_type == "right":
                sample = x1
            elif input_sample_type == "center":
                sample = 0.5 * x0 + 0.5 * x1
            else:
                raise Exception("Invalid input sample type")
            height = get_norm(
                self.i2fp(sample, func) - self.c2p(sample, 0)
            )
            rect = Rectangle(
                width=(self.c2p(x1, 0) - self.c2p(x0, 0))[0], height=height)
            rect.move_to(self.c2p(x0, 0), DL)
            rects.append(rect)
        result = VGroup(*rects)
        result.set_submobject_colors_by_gradient(*colors)
        result.set_style(
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            fill_opacity=fill_opacity,
        )
        return result


class DiscreteBinomialDistributionScene(Scene):
    def update_n_anim(self, n, axes, coordinate_labels, rects, fm, label_n):
        axes = AxesWithRect(
            x_range=[0, n * 1.05, n // 10],
            y_range=[0, 0.35, 0.1],
            y_axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 1
                }
            }
        )
        coordinate_labels.generate_target()
        coordinate_labels.target = axes.add_coordinate_labels()
        self.play(
            MoveToTarget(coordinate_labels),
            rects.animate.become(
                axes.get_discrete_rectangles(
                    fm, x_range=[0, n + 1, 1], fill_opacity=0.8)
            ),
            label_n[1].animate.set_value(n)
        )

    def update_n_anim_2(self, n, axes, coordinate_labels, rects, fm, label_n):
        coordinate_labels.target = axes.add_coordinate_labels()
        return (
            MoveToTarget(coordinate_labels),
            rects.animate.become(
                axes.get_discrete_rectangles(
                    fm,
                    x_range=[0, 1 + 1 / n, 1 / n], fill_opacity=0.8, stroke_width=0
                )
            ),
            label_n[1].animate.set_value(n)
        )

    def construct(self):
        n = 20
        p = ValueTracker(0.6)
        label_p = VGroup(
            Tex("p="),
            DecimalNumber(p.get_value(), number_decimal_places=2)
        ).arrange(RIGHT, buff=0.1).to_corner(UR)
        label_p[1].shift(UP * 0.05)
        label_n = VGroup(
            Tex("n="),
            Integer(n)
        ).arrange(RIGHT, buff=0.1)
        label_n[1].shift(UP * 0.03)
        label_n.next_to(
            label_p[0][0][1], DOWN, submobject_to_align=label_n[0][0][1]).shift(DOWN * 0.5)
        label_p[1].add_updater(lambda a: a.set_value(p.get_value()))

        def binomial_distribution(m):
            return choose(n, int(m)) * (1 - p.get_value()) ** (n - int(m)) * p.get_value() ** int(m)

        fm = FuncMobject(binomial_distribution)
        fm.add_updater(lambda a: a.set_func(binomial_distribution))

        axes = AxesWithRect(
            x_range=[0, n * 1.05, n // 10],
            y_range=[0, 0.35, 0.1],
            y_axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 1
                }
            }
        )
        x_label = Tex("m").next_to(axes[0], RIGHT)
        y_label = Tex("p").next_to(axes[1], RIGHT, aligned_edge=UP)
        coordinate_labels = axes.add_coordinate_labels()
        self.add(p, fm, axes, coordinate_labels,
                 label_p[0], label_p[1], label_n, x_label, y_label)
        rects = axes.get_discrete_rectangles(
            FuncMobject(lambda a: 1e-10),
            x_range=[0, n + 1, 1],
            fill_opacity=0.8
        )
        self.add(rects)
        self.play(rects.animate.become(
            axes.get_discrete_rectangles(
                fm, x_range=[0, n + 1, 1], fill_opacity=0.8)
        ), lag_ratio=0.2, run_time=1.5)
        self.wait()
        rects.add_updater(lambda a: a.become(
            axes.get_discrete_rectangles(
                fm, x_range=[0, n + 1, 1], fill_opacity=0.8)
        ))
        self.add(rects)
        self.play(p.animate.set_value(0.2), run_time=1.5)
        self.wait()
        self.play(p.animate.set_value(0.6), run_time=1.5)
        self.wait()

        # start to increase sample size
        rects.clear_updaters()
        # for _ in self.mobjects:
        #     _.clear_updaters()

        n = 40
        self.update_n_anim(n, axes, coordinate_labels, rects, fm, label_n)
        self.wait()
        n = 100
        self.update_n_anim(n, axes, coordinate_labels, rects, fm, label_n)
        self.wait()

        Ex = AutoValue(p.get_value())
        Ex.keep_update(p, lambda a: a)
        Dx = AutoValue(p.get_value() * (1 - p.get_value()) / n)
        Dx.keep_update(p, lambda a: a * (1 - a) / n)
        Vx = AutoValue(math.sqrt(Dx.get_value()))
        Vx.keep_update(Dx, lambda a: math.sqrt(a))
        self.add(Ex, Dx, Vx)

        def binomial_distribution_fixed(t):
            m = int(n * t)
            return choose(n, m) * (1 - p.get_value()) ** (n - m) * p.get_value() ** m * n

        def normal_distribution(t):
            return 1 / math.sqrt(2 * PI) / Vx.get_value() * np.exp(-(t - Ex.get_value()) ** 2 / 2 / Dx.get_value())

        # prepare to transform into m / n format
        axes = AxesWithRect(
            x_range=[0, 1.05, 0.1],
            y_range=[0, 31.5, 3],
            x_axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 1
                }
            },
            y_axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 0
                }
            }
        )
        self.play(*self.update_n_anim_2(n, axes, coordinate_labels,
                                        rects, FuncMobject(binomial_distribution_fixed), label_n))
        self.play(
            x_label.animate.become(Tex("{m\\over n}").next_to(axes[0], RIGHT)),
            y_label.animate.become(Tex("np").next_to(
                axes[1], RIGHT, aligned_edge=UP))
        )
        self.add(axes)
        graph = axes.get_graph(normal_distribution, x_range=[0, 1, 1 / n])
        self.play(ShowCreation(graph))
        self.wait()
        n = 400
        self.play(graph.animate.become(axes.get_graph(
            normal_distribution, x_range=[0, 1, 1 / n])))
        self.play(
            *self.update_n_anim_2(n, axes, coordinate_labels, rects,
                                  FuncMobject(binomial_distribution_fixed), label_n),
            graph.animate.become(axes.get_graph(
                normal_distribution, x_range=[0, 1, 1 / n]))
        )
        self.wait()
        n = 800
        self.play(graph.animate.become(axes.get_graph(
            normal_distribution, x_range=[0, 1, 1 / n])))
        self.play(
            *self.update_n_anim_2(n, axes, coordinate_labels, rects,
                                  FuncMobject(binomial_distribution_fixed), label_n),
            graph.animate.become(axes.get_graph(
                normal_distribution, x_range=[0, 1, 1 / n]))
        )

        for _ in self.mobjects:
            _.clear_updaters()

        self.wait()


class FormulaScene(Scene):
    def construct(self):
        binomial_distribution = Tex(
            r"X\sim B\left(n, p\right)"
        )
        bd_formula = Tex(
            r"P(X=m)={n\choose m}(1-p)^{n-m}p^m"
        ).shift(DOWN / 2)
        normal_distribution = Tex(
            r"X\sim N\left(\mu,\sigma^2\right)",
        ).shift(UP / 2).to_edge(RIGHT)
        nd_formula = Tex(
            r"p(x)={1\over \sqrt{2\pi}\sigma}e^{-\displaystyle{(x-\mu)^2\over 2\sigma^2}}",
            isolate=[r"\sigma^2", r"\mu"]
        ).next_to(normal_distribution, DOWN).to_edge(RIGHT)
        self.play(Write(binomial_distribution))
        self.play(
            binomial_distribution.animate.shift(UP / 2),
            FadeIn(bd_formula, UP)
        )
        self.wait()
        self.play(
            binomial_distribution.animate.to_edge(LEFT),
            bd_formula.animate.to_edge(LEFT).shift(DOWN / 2),
            FadeIn(normal_distribution, RIGHT),
            FadeIn(nd_formula, RIGHT)
        )
        # self.play(Write(normal_distribution))
        # self.play(FadeIn(nd_formula, UP))
        self.wait()


class FormulaScene2(Scene):
    def construct(self):
        binomial_distri = Tex(
            r"X\sim B\left(n, p\right)",
            isolate=['n', 'p']
        ).shift(UP * 0.6)
        arrow = Line(tip_config={'tip_style': 1}).add_tip().scale(0)
        n_to_inf = Tex(r'n\to\infty').next_to(binomial_distri, RIGHT)
        normal_distri = Tex(
            r"X\sim N\left(\mu,\sigma^2\right)",
            isolate=[r'\mu', r'\sigma^2']
        ).next_to(binomial_distri, DOWN)
        self.play(Write(binomial_distri), Write(normal_distri))
        self.play(FadeIn(n_to_inf, RIGHT))
        self.wait()
        self.play(LaggedStart(
            binomial_distri.animate.move_to(LEFT * 3),
            normal_distri.animate.move_to(RIGHT * 3),
            arrow.animate.set_width(2),
            n_to_inf.animate.scale(0.6).next_to(arrow, UP),
            lag_ratio=0.1
        ))
        self.wait()
        normal_distri2 = Tex(
            r"X\overset{\cdot}{\sim} N\left(np,\sigma^2\right)",
            isolate=[r'np', r'\sigma^2']
        ).move_to(RIGHT * 3)
        self.play(
            ReplacementTransform(normal_distri, normal_distri2),
            TransformFromCopy(VGroup(binomial_distri[1], binomial_distri[3]), normal_distri2[1], path_arc=PI),
        )
        self.add(normal_distri2)
        self.wait()
        normal_distri3 = Tex(
            r"X\overset{\cdot}{\sim} N\left(", "np", ",", r"np(1-p)", r"\right)",
        ).move_to(RIGHT * 3.7)
        self.play(
            TransformMatchingTex(normal_distri2, normal_distri3),
            TransformFromCopy(VGroup(binomial_distri[1], binomial_distri[3]), normal_distri3[3], path_arc=PI),
        )
        self.add(normal_distri3)
        self.wait()
        formula = Tex(
            r"p(x)\approx{1\over \sqrt{2\pi}\sigma}e^{-\displaystyle{(x-\mu)^2\over 2\sigma^2}}",
            isolate=[r"\mu", r"\sigma^2"]
        ).shift(DOWN)
        self.play(
            VGroup(binomial_distri, arrow, n_to_inf, normal_distri3).animate.center().shift(UP * 0.6),
            FadeIn(formula, UP)
        )
        self.wait()
        self.play(
            normal_distri3[1].animate.set_color(YELLOW).scale(1.3),
            formula[1].animate.set_color(YELLOW).scale(1.3),
            run_time=1.5, rate_func=there_and_back_with_pause
        )
        self.wait()
        self.play(
            normal_distri3[3].animate.set_color(TEAL).scale(1.3),
            formula[3].animate.set_color(TEAL).scale(1.3),
            run_time=1.5, rate_func=there_and_back_with_pause
        )
        self.wait()


class NormalDistributionScene(Scene):
    def construct(self):
        n = 20
        p = ValueTracker(0.6)
        Ex = AutoValue(n * p.get_value())
        Ex.keep_update(p, lambda a: a * n)
        Dx = AutoValue(n * p.get_value() * (1 - p.get_value()))
        Dx.keep_update(p, lambda a: n * a * (1 - a))
        Vx = AutoValue(math.sqrt(Dx.get_value()))
        Vx.keep_update(Dx, lambda a: math.sqrt(a))

        def normal_distribution(t):
            return 1 / math.sqrt(2 * PI) / Vx.get_value() * np.exp(-(t - Ex.get_value()) ** 2 / 2 / Dx.get_value())

        def binomial_distribution(m):
            return choose(n, int(m)) * (1 - p.get_value()) ** (n - int(m)) * p.get_value() ** int(m)

        self.add(p, Ex, Dx, Vx)
        axes = Axes(
            x_range=[0, n * 1.05, n // 10],
            y_range=[0, 0.35, 0.1],
            y_axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 1
                }
            }
        )
        axes.add_coordinate_labels()
        self.add(axes)
        graph = axes.get_graph(
            normal_distribution,
            x_range=[0, n, n / 100]
        )
        graph.add_updater(lambda a: a.become(
            axes.get_graph(
                normal_distribution,
                x_range=[0, n, n / 100]
            )
        ))
        self.play(ShowCreation(graph))
        self.wait()
        self.play(p.animate.set_value(0.4))
        self.wait()
        rects = axes.get_riemann_rectangles(
            axes.get_graph(lambda t: 0.0001, x_range=[0, n, 1]), x_range=[0, n + 1, 1], fill_opacity=0.8
        )
        self.add(rects)
        self.play(rects.animate.become(
            axes.get_riemann_rectangles(
                graph, x_range=[0, n + 1, 1], fill_opacity=0.8
            )
        ), lag_ratio=0.2, run_time=1.5)
        self.wait()

        rects.add_updater(lambda a: a.become(
            axes.get_riemann_rectangles(
                graph, x_range=[0, n + 1, 1], fill_opacity=0.8
            )
        ))
        self.play(p.animate.set_value(0.6))

        for i in self.mobjects:
            i.clear_updaters()
        self.wait()
