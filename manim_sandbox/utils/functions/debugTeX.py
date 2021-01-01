# from @鹤翔万里
# 将Text(str(i))替换为Integer,避免生成过多的Text svg


from manimlib.imports import *
from manim_sandbox.utils.imports import *
import itertools


def debugTeX(self, texm, scale_factor=0.3):
    for i, j in enumerate(texm):
        tex_id = Integer(i, background_stroke_width=2) \
            .scale(scale_factor).set_color(PURPLE_A)
        tex_id.move_to(j)
        self.add(tex_id)


def debugAllPoints(self, obj, scale_factor=0.5):
    for i, points in enumerate(obj.get_all_points()):
        point_id = Integer(i, background_stroke_width=2) \
            .scale(scale_factor).set_color(PURPLE_A)
        point_id.move_to(points)
        self.add(point_id)


def debugPoints(self, obj, scale_factor=0.5):
    for i, points in enumerate(obj.get_points()):
        point_id = Integer(i, background_stroke_width=2) \
            .scale(scale_factor).set_color(PURPLE_A)
        point_id.move_to(points)
        self.add(point_id)


class AllPointsIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        # digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        for index, points in enumerate(obj.get_all_points()):
            point_id = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            point_id.move_to(points)
            self.add(point_id)


class PointIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        # digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        for index, points in enumerate(obj.get_points()):
            point_id = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            point_id.move_to(points)
            self.add(point_id)


class TexIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        for index, single_tex in enumerate(obj):
            tex_index = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            tex_index.move_to(single_tex.get_center())
            self.add(tex_index)
