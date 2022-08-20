from manimlib import *


class MatrixReflect(Scene):
    def construct(self):
        m1 = Matrix([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 'A', 'B', 'C']
        ])

        m1.get_brackets().set_color(BLUE)
        m1.scale(0.8).to_edge(LEFT, buff=1.5)

        m2 = Matrix([
            [3, 4, 5, 0, 9],
            [5, 1, 4, 2, 8],
            [1, 1, 4, 5, 1],
            [1, 9, 1, 9, 8],
            [10, '\\text{嗯}', '\\text{哼}', '\\text{哼}', '\\text{啊}']
        ])
        m2.scale(0.7).to_edge(RIGHT, buff=1.5)
        m2.get_brackets().set_color(GOLD)
        m2m = m2.get_mob_matrix()
        for it in m2m[3:]:
            for jt in it:
                jt.set_color(RED)

        m2m[0][-1].set_color(RED)
        m2m[1][-1].set_color(RED)
        m2m[2][-1].set_color(RED)

        arrow1 = Arrow(m1.get_right(), m2.get_left(), color=GREY)
        cross = Tex('\\times', color=RED).next_to(arrow1, UP)

        VGroup(m1, m2, arrow1, cross).shift(UP*2)

        self.add(m1, m2, arrow1, cross)

        m3 = Matrix([
            [1, 2, 3, 4, 4],
            [5, 6, 7, 8, 8],
            [9, 'A', 'B', 'C', 'C'],
            ['D', 'E', 'F', 0, 0],
            ['D', '\\text{摸}', '\\text{乐}', '\\text{摆}', '\\text{寄}']
        ])

        m3.get_brackets().set_color(BLUE)
        m3m = m3.get_mob_matrix()
        for it in m3m[3:]:
            for jt in it:
                jt.set_color(GREEN)
        m3m[0][-1].set_color(GREEN)
        m3m[1][-1].set_color(GREEN)
        m3m[2][-1].set_color(GREEN)
        m3.scale(0.7).to_edge(LEFT, buff=1.5).shift(DOWN * 2)
        self.add(m3)

        m4 = Matrix([
            [3, 4, 5, 0, 9],
            [5, 1, 4, 2, 8],
            [1, 1, 4, 5, 1],
            [1, 9, 1, 9, 8],
            [10, '\\text{嗯}', '\\text{哼}', '\\text{哼}', '\\text{啊}']
        ])
        m4.scale(0.7).to_edge(RIGHT, buff=1.5).shift(DOWN*2)
        m4.get_brackets().set_color(GOLD)
        m4m = m4.get_mob_matrix()

        for it in m4m[3:]:
            for jt in it:
                jt.set_color(YELLOW)

        m4m[0][-1].set_color(YELLOW)
        m4m[1][-1].set_color(YELLOW)
        m4m[2][-1].set_color(YELLOW)
        self.add(m4)
        arrow2 = Arrow(m3.get_right(), m4.get_left(), color=GREY)
        checkmark = Tex('\\checkmark', color=GREEN).next_to(arrow2, UP)
        self.add(arrow2, checkmark)

        for i in [m1, m2, m3, m4, checkmark, cross]:
            i.set_backstroke(color=BLACK, width=5)


class ShiftRotateExample(Scene):
    def construct(self):
        square = VGroup(Square(), Dot()).shift(LEFT*5)
        square.save_state()
        numline = NumberLine(x_range=[-5, 5, 1])

        def anim(m: Mobject, alpha: float):
            m.restore()
            m.shift(10 * alpha * RIGHT)
            m.rotate(PI * 3 * alpha)

        self.add(numline, square)
        self.play(UpdateFromAlphaFunc(square, anim), run_time=4)


class MyRotateExample(Scene):
    def construct(self):
        square = Square()
        square.save_state()

        def my_rotate(m: Mobject, alpha: float):
            m.restore()
            m.rotate(PI * 3 * alpha)

        self.add(square)
        self.play(UpdateFromAlphaFunc(square, my_rotate), run_time=4)


class MoveAlongPathExample(Scene):
    def construct(self):
        graph = FunctionGraph(lambda x: np.sin(PI * x), x_range=[-5, 5, 0.1])
        self.add(graph)

        dot = Dot().move_to(graph.get_start())
        self.add(dot)

        def update_dot(dot: Mobject, alpha: float):
            dot.move_to(graph.pfp(alpha))

        self.play(UpdateFromAlphaFunc(dot, update_dot), run_time=4)

        # 然而，Grant 早就已经封装好一个动画类了，叫 MoveAlongPath ，有兴趣的读者可以尝试一下

# 计算输入 alpha 对应点处切线的倾斜角


def angle_of_tan(graph: ParametricCurve, alpha: float, dx=0.01) -> float:
    vect = graph.pfp(alpha + dx) - graph.pfp(alpha - dx)
    return angle_of_vector(vect)


class MoveAlongPathExample2(Scene):
    def construct(self):
        graph = FunctionGraph(lambda x: x * np.cos(PI * x) / 2,
                              x_range=[-5, 5, 0.1])
        arrow = ArrowTip().scale(0.8)
        # 保存 arrow 的旋转角度
        arrow.save_state()
        self.add(graph, arrow)

        def update_arrow(m: Mobject, alpha: float):
            # 恢复旋转角
            m.restore()
            # 旋转
            m.rotate(angle_of_tan(graph, alpha))
            # 移动
            m.move_to(graph.pfp(alpha))

        self.play(UpdateFromAlphaFunc(arrow, update_arrow), run_time=6)


class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-1, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )

        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

        h_line = axes.get_h_line(dot.get_left())
        v_line = axes.get_v_line(dot.get_bottom())

        def redraw_h_line(m: Mobject):
            m.become(axes.get_h_line(dot.get_left()))

        def redraw_v_line(m: Mobject):
            m.become(axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(
            dot.animate.move_to(axes.c2p(3, -2)),
            UpdateFromFunc(h_line, redraw_h_line),
            UpdateFromFunc(v_line, redraw_v_line)
        )
        self.wait()
        self.play(
            dot.animate.move_to(axes.c2p(1, 1)),
            UpdateFromFunc(h_line, redraw_h_line),
            UpdateFromFunc(v_line, redraw_v_line)
        )
        self.wait()

        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75).to_corner(UL),
            UpdateFromFunc(h_line, redraw_h_line),
            UpdateFromFunc(v_line, redraw_v_line),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))


class RollingCircleExample(Scene):
    def construct(self):
        c1 = Circle(radius=2)
        c2 = VGroup(
            Circle(radius=1),   # 圆
            Dot(),              # 圆心
            Vector(DOWN * 0.8),  # 箭头
        )
        c2.shift(UP * 3).set_color(GOLD)
        c2.save_state()

        path = TracedPath(lambda: c2[0].pfp(0.75),
                          stroke_width=6,
                          stroke_color=YELLOW)
        self.add(c1, c2, path)

        def update_c2(m: Mobject, alpha: float):
            m.restore()
            m.rotate(-3 * TAU * alpha)
            m.move_to(3 * np.array([
                np.sin(TAU * alpha),
                np.cos(TAU * alpha),
                0
            ]))

        self.play(
            UpdateFromAlphaFunc(c2, update_c2),
            run_time=6
        )


class BezierExample(Scene):
    def construct(self):
        points = np.array([
            [-4, -3, 0],
            [0, 3, 0],
            [6, -2, 0]
        ])

        dots = VGroup(*[Dot(p) for p in points])
        lines = VGroup(
            Line(points[0], points[1]),
            Line(points[1], points[2]),
        ).set_stroke(width=2)

        self.add(dots, lines)

        moving_dot1 = Dot(points[0], color=GOLD)
        moving_dot2 = Dot(points[1], color=GOLD)

        moving_line = Line(points[0], points[1], color=GOLD)

        moving_line.add_updater(
            lambda l: l.put_start_and_end_on(
                moving_dot1.get_center(), 
                moving_dot2.get_center()
            )
        )

        moving_dot3 = Dot(color=RED)

        path = TracedPath(moving_dot3.get_center, stroke_width=6, stroke_color=RED)

        self.add(moving_dot1, moving_dot2, moving_dot3, moving_line, path)

        self.play(
            UpdateFromAlphaFunc(moving_dot1, lambda d, a: d.move_to(lines[0].pfp(a))),
            UpdateFromAlphaFunc(moving_dot2, lambda d, a: d.move_to(lines[1].pfp(a))),
            UpdateFromAlphaFunc(moving_dot3, lambda d, a: d.move_to(moving_line.pfp(a))),
            run_time=4
        )







