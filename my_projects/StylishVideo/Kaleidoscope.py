from manimlib.imports import *


# class bezier(Scene):
#     def construct(self):
#         color_list = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
#         pos = [UL*1.5, UL*1.5+DL*1.2, UR*1.2, DR*1.5]
#         curve = VGroup(*[BezierCurve(pos).rotate(i*TAU/66).set_color(
#             color_list) for i in range(66)])
#         curve2 = VGroup(*[BezierCurve(pos).rotate(PI,
#                                                   axis=pos[-1]-pos[0])
#                           .rotate(i*TAU/66).set_color(color_list) for i in range(66)])
#         curve3 = VGroup(curve, curve2).move_to(
#             ORIGIN).set_stroke(width=1, opacity=1)
#         curve4 = curve3.copy().set_stroke(width=10, opacity=0.3)
#         curve5 = VGroup(curve3, curve4).scale(2)
#         self.add(curve5)


class test(Scene):
    def Cup(self, x, dt):
        x.t -= dt
        if x.t < 0:
            self.remove(x)
        x.set_width(2*(x.edr-rush_into(x.t/x.allt)*(x.edr-x.opr)))
        x.set_stroke(width=rush_into(x.t/x.allt)*x.st)

    def Ripples(self, pos=ORIGIN, stroke_width=20, start_radius=1, end_radius=2, time=1, color="#aef"):
        C = Circle(radius=start_radius, stroke_width=stroke_width, color=color)
        C.move_to(pos)
        C.opr = start_radius
        C.edr = end_radius
        C.st = stroke_width
        C.t = time
        C.allt = time
        self.add(C)
        C.add_updater(self.Cup)

    def construct(self):
        self.wait(1)
        for i in range(10):
            self.Ripples(pos=random.randint(-4, 4)*LEFT+random.randint(-4, 4)*UP,
                         end_radius=random.randint(2, 5), time=random.randint(5, 10)/10)
            self.wait(random.randint(3, 7)/10)
        self.wait(5)
