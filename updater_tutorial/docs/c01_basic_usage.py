from manimlib import *


class BasicExample(Scene):
    def construct(self):
        dot = Dot(LEFT*2)
        text = Text("This is a dot").next_to(dot, RIGHT)
        text.add_updater(lambda m: m.next_to(dot, RIGHT))
        self.add(dot, text)
        self.play(Rotate(dot, PI * 2, about_point=ORIGIN), run_time=4.44)


class InterpolateExampleScene(Scene):
    def construct(self):
        square = Square(side_length=4, color=YELLOW) \
            .shift(LEFT*4).insert_n_curves(4)
        circle = Circle(radius=2).shift(RIGHT*4)

        interpolates = VGroup()

        for alpha in np.linspace(0.1, 1, 9):
            v = VMobject(color=GREY)
            v.set_points(interpolate(square.get_points(),
                         circle.get_points(), alpha))
            interpolates.add(v)

        self.add(interpolates)
        self.add(square, circle)

        square_points = VGroup(*[
            Integer(i, color=GOLD)
            .set_backstroke()
            .scale(0.5).move_to(p)
            for (i, p) in enumerate(square.get_points())
        ])

        circle_points = VGroup(*[
            Integer(i, color=GOLD)
            .set_backstroke()
            .scale(0.5).move_to(p)
            for (i, p) in enumerate(circle.get_points())
        ])

        self.add(square_points, circle_points)


'''
1. 绘制一条线段 $AB$，并绘制它的垂直平分线，使得当线段 $AB$ 移动、旋转的时候，中垂线始终能够垂直平分这条线段。
'''


class PerpendicularBisectorExample(Scene):
    def construct(self):
        line = Line(LEFT*2, RIGHT*2)
        bisector = line.copy().rotate(PI / 2).scale(5)
        bisector.set_color(RED)
        self.add(line, bisector)

        bisector.add_updater(lambda m: m
                             .set_angle(line.get_angle() + PI / 2)
                             .move_to(line.get_center())
                             )

        self.play(line.animate.put_start_and_end_on(
            np.array([0, 1, 0]), np.array([4, 2, 0])))
        self.play(Rotate(line, PI / 2))


'''
2. 绘制一段圆弧，使用两个 `ValueTracker` 分别控制它的弧度和半径。
'''

class ArcExample(Scene):
    def construct(self):
        arc = Arc(angle=PI / 2, radius=2)
        arc.set_color(YELLOW)
        self.add(arc)

        radius = ValueTracker(2)
        angle = ValueTracker(PI / 2)
        arc.add_updater(lambda m: m.become(
            Arc(angle=angle.get_value(), radius=radius.get_value())
        ))
        self.add(radius, angle)

        self.play(radius.animate.set_value(3))
        self.play(angle.animate.set_value(PI))

'''
3. 绘制一条数轴，在上面添加一个点，使用 `ValueTracker` 类来控制点的位置，同时使用 `DecimalNumber` 来显示点所代表的数值。
'''

class NumberLineScene(Scene):
    def construct(self):
        # 创建数轴
        number_line = NumberLine(x_range=[-5, 5, 1], width=10)
        number_line.add_numbers()
        self.add(number_line)

        v = ValueTracker(0)
        # 点
        dot = Dot(number_line.n2p(v.get_value()), color=YELLOW)
        # 显示数值
        label = DecimalNumber(v.get_value(), num_decimal_places=2)
        self.add(dot, label)

        dot.add_updater(lambda m: m.move_to(number_line.n2p(v.get_value())))
        label.add_updater(lambda m: m.set_value(v.get_value()).next_to(dot, UP))

        self.play(v.animate.set_value(5), run_time=2)
        self.play(v.animate.set_value(-4), run_time=3)
        

'''
在坐标系上绘制一条函数 $y=\sin(x+\varphi)$，使用你觉得方便的方法，使得改变 $\varphi$ 值的时候，图像也能动态改变。
'''


class SineGraphScene(Scene):
    def construct(self):
        axes = Axes(x_range=[-10, 10, 1], y_range=[-2, 2, 0.25])
        self.add(axes)

        graph = axes.get_graph(
            lambda x: np.sin(x), x_range=[-9, 9, 0.1]
        )
        self.add(graph)

        phi = ValueTracker(0)
        graph.add_updater(lambda g: g.set_points(axes.get_graph(
            lambda x: np.sin(x + phi.get_value()), x_range=[-9, 9, 0.1]
        ).get_points()))

        graph.add_updater(lambda g: g.become(
            axes.get_graph(
                lambda x: np.sin(x + phi.get_value()), 
                x_range=[-9, 9, 0.1]
            )
        ))

        self.add(phi, graph)
        self.play(phi.animate.set_value(4), run_time=3)