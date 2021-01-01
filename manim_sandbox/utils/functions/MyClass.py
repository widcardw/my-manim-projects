from manimlib.imports import *
from manim_sandbox.utils.functions.MathTools import *
import math

# 数学工具


def arg_angle(start, end):
    start_x, start_y, end_x, end_y = start[0], start[1], end[0], end[1]
    mode = 1
    if start_x < end_x and start_y < end_y:
        mode = 1
    elif start_x > end_x and start_y < end_y:
        mode = 2
    elif start_x > end_x and start_y > end_y:
        mode = 3
    elif start_x < end_x and start_y > end_y:
        mode = 4
    if start_y == end_y and start_x > end_x:
        mode = 5
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    theta = math.atan(delta_y / delta_x)
    if mode == 1:
        pass
    elif mode == 2:
        theta += PI
    elif mode == 3:
        theta += PI
    elif mode == 4:
        theta += 2 * PI
    elif mode == 5:
        theta = PI
    return theta


def get_len(start, end):
    start_x, start_y, end_x, end_y = start[0], start[1], end[0], end[1]
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    return np.sqrt(delta_x ** 2 + delta_y ** 2)

# VGroup对象


def MyAngle(A, O, B, radius, color, line_width=0.05):
    start_angle = arg_angle(O, B)
    triangle = MyTriangle(O, B, A)
    a, b, c = triangle.a, triangle.b, triangle.c
    angle = math.acos((b * b + c * c - a * a) / (2 * b * c))
    return VGroup(
        AnnularSector(
            start_angle,
            angle,
            arc_center=O,
            inner_radius=radius - line_width,
            outer_radius=radius,
            color=color
        ),
        Sector(
            start_angle,
            angle,
            arc_center=O,
            outer_radius=radius - line_width,
            color=color,
            fill_opacity=0.5
        )
    )


def MyArrow(start, end, color):
    ARC = PI / 180
    AB = 1 / 3
    BQ = CQ = AB * np.sin(17 * ARC)
    PQ = BQ / np.tan(50 * ARC)
    AQ = AB * np.cos(17 * ARC)
    AP = AQ - PQ
    #设A点坐标为(0, 0)
    A, B, P, C = np.array([0., 0., 0.]), np.array(
        [-AQ, BQ, 0.]), np.array([-AP, 0., 0.]), np.array([-AQ, -CQ, 0.])

    # 平移箭头
    arrow_len = get_len(start, end)
    A[0] += arrow_len
    B[0] += arrow_len
    P[0] += arrow_len
    C[0] += arrow_len

    # 旋转箭头
    theta = arg_angle(start, end)
    rotate_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 0]
    ])
    A = np.inner(rotate_matrix, A.T).T + start
    B = np.inner(rotate_matrix, B.T).T + start
    P = np.inner(rotate_matrix, P.T).T + start
    C = np.inner(rotate_matrix, C.T).T + start

    return VGroup(
        Line(start, end + (P - A), color=color),
        Polygon(A, B, P, C, color=color, fill_opacity=1).set_stroke(
            width=DEFAULT_STROKE_WIDTH/4),
    )


class Lab(Scene):
    def dot_map(self):
        dots = VGroup()
        nums = VGroup()
        for x in range(-7, 8):
            for y in range(-4, 5):
                dots.add(Dot().scale(0.5).move_to(
                    RIGHT * x + UP * y).set_opacity(1 / 4))
                if y == 0:
                    nums.add(TextMobject(str(x)).scale(0.5).move_to(
                        RIGHT * x + UP * y + DOWN * 1 / 4).set_opacity(1 / 4))
                if x == 0 and y != 0:
                    nums.add(TextMobject(str(y)).scale(0.5).move_to(
                        RIGHT * x + UP * y + LEFT * 1 / 4).set_opacity(1 / 4))
        self.add(dots, nums)

    def construct(self):
        self.dot_map()
        A, O, B = np.array([2, 3, 0]), ORIGIN, np.array([2, -3, 0])
        angle = MyAngle(A, O, B, 0.5, YELLOW)
        dots = [Dot(A), Dot(O), Dot(B)]
        self.add(angle, *dots)
        self.wait(2)
