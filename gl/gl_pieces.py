from manimlib import *


class GlPieces(VGroup):
    def __init__(self, vmob: VMobject, piece_num=5, **kwargs):
        super().__init__(**kwargs)
        # TODO
        # To be simplified
        height = vmob.get_height()
        bottom = vmob.get_bottom()[1]
        # vmob.rotate(dir_angle)

        for i in range(piece_num):
            cp = vmob.copy()
            a1 = bottom + i / piece_num * height
            a2 = bottom + (i + 1) / piece_num * height
            print(a1, a2)
            cp.set_color_by_code(f'''
                color.a=step({a1}, (point.y))-step({a2}, (point.y));
            ''')
            self.add(cp)


class TestGlPiece(Scene):
    def construct(self):
        cir = Square(fill_opacity=1).scale(3)
        glp = GlPieces(cir, 6)
        self.play(FadeIn(glp, LEFT), lag_ratio=0.5)
        self.wait()
