from manimlib import *


class FocusOnExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            Tex("x")
        ).scale(2)
        mobjects.arrange(RIGHT, buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors = [GREY, RED, BLUE]

        self.add(mobjects)

        for obj, color in zip(mobject_or_coord, colors):
            self.play(FocusOn(obj, color=color))

        self.wait(0.3)


class IndicateExample(Scene):
    def construct(self):
        #              0     1    2
        formula = Tex("f(", "x", ")")
        dot = Dot()

        VGroup(formula, dot)\
            .scale(3)\
            .arrange(DOWN, buff=3)

        self.add(formula, dot)

        for mob in [formula[1], dot]:
            self.play(Indicate(mob))

        self.wait(0.3)


class FlashExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            Tex("x")
        ).scale(2)
        mobjects.arrange(RIGHT, buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors = [GREY, RED, BLUE]

        self.add(mobjects)

        for obj, color in zip(mobject_or_coord, colors):
            self.play(Flash(obj, color=color, flash_radius=0.5))

        self.wait(0.3)


class CircleIndicateExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            Tex("x")
        ).scale(2)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.wait(0.2)

        for obj in mobjects:
            self.play(CircleIndicate(obj))


class ShowPassingFlashExample(Scene):
    # for ShowPassingFlashAround
    def construct(self):
        mobjects = VGroup(
            Dot(),
            Tex("x")
        ).scale(2)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.wait(0.2)

        for obj in mobjects:
            self.play(ShowPassingFlash(obj))


class ShowCreationThenDestructionExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[ShowCreationThenDestruction(mob) for mob in mobjects]
        )

        self.wait()


class ShowCreationThenFadeOutExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[ShowCreationThenFadeOut(mob) for mob in mobjects]
        )

        self.wait()


# abstract class
# class AnimationOnSurroundingRectangleExample(Scene):
#     def construct(self):
#         mobjects = VGroup(
#             Circle(),
#             Circle(fill_opacity=1),
#             Text("Text").scale(2)
#         )
#         mobjects.scale(1.5)
#         mobjects.arrange(RIGHT, buff=2)
#         self.add(mobjects)

#         self.play(
#             *[AnimationOnSurroundingRectangle(mob) for mob in mobjects]
#         )

#         self.wait()


class ShowPassingFlashAroundExample(Scene):
    # 目前有显示不全的 bug
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[ShowPassingFlashAround(mob) for mob in mobjects]
        )

        self.wait()


class ShowCreationThenDestructionAroundExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[ShowCreationThenDestructionAround(mob) for mob in mobjects]
        )

        self.wait()


class ShowCreationThenFadeAroundExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[ShowCreationThenFadeAround(mob) for mob in mobjects]
        )

        self.wait()


class ApplyWaveExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[ApplyWave(mob) for mob in mobjects]
        )

        self.wait()


class WiggleOutThenInExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[WiggleOutThenIn(mob) for mob in mobjects]
        )

        self.wait()


class TurnInsideOutExample(Scene):
    # 对文字使用会造成非常大的问题
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[TurnInsideOut(mob) for mob in mobjects]
        )

        self.wait()


class FlashyFadeInExample(Scene):
    # 效果不是很明显
    def construct(self):
        mobjects = VGroup(
            Circle(fill_opacity=0.5, stroke_width=[0, 6, 0, 6, 0, 6]),
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.play(
            *[FlashyFadeIn(mob) for mob in mobjects]
        )

        self.wait()
