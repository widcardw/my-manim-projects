from manimlib.imports import *
from manim_sandbox.utils.imports import *


class _2020To2021(Scene):
    def construct(self):
        color_list = [RED, GOLD, GREEN, BLUE]
        text = TextMobject("2020").scale(12).set_color_by_gradient(color_list)
        ind = AllPointsIndex(text, scale_factor=0.4, color=WHITE)
        ind.add_updater(lambda a: a.become(
            AllPointsIndex(text, scale_factor=0.4, color=WHITE)
        ))
        self.add(text, ind)
        self.wait(2)
        self.play(text.become,
                  TextMobject("2021").scale(12).set_color_by_gradient(color_list))
        self.wait(2)

        current = {"time": 2020,
                   "diligence": 998244353,
                   "caption": Text("2020")
                   }
        dt = 1

        def future(day):
            day.time += dt
            day.diligence += dt * 100
            day.caption.become(
                Text("2021")
            )

        self.play(UpdateFromFunc(current, future))

#         code_str = """past=Text("2020")
# def anim(obj, alpha):
#     obj.become(Text("2021"))
# self.play(UpdateFromAlphaFunc(past, anim))"""
#         code = CodeLine(code_str)
#         self.add(code)
