from manimlib import *


class AnimationGroupExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.wait()
        anims = AnimationGroup(
            *[GrowFromCenter(mob) for mob in mobjects]
        )
        self.play(anims)
        self.wait()


class SuccessionExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.wait()
        anims = Succession(
            *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
        )
        self.play(anims)
        self.wait()


class LaggedStartExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.wait()
        anims = LaggedStart(
            *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
        )
        self.play(anims)
        self.wait()


class LaggedStartMapExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.wait()
        anims = LaggedStartMap(
            FadeOut, mobjects
        )
        self.play(anims)
        self.wait()
