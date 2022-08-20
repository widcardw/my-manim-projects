from manimlib import *


class ShowCreationExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[ShowCreation(mob) for mob in mobjects]
        )

        self.wait()


class UncreateExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)

        self.wait(0.3)

        self.play(
            *[Uncreate(mob) for mob in mobjects]
        )

        self.wait()


class DrawBorderThenFillExample(Scene):
    def construct(self):
        vmobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        vmobjects.scale(1.5)
        vmobjects.arrange(RIGHT, buff=2)

        self.play(
            *[DrawBorderThenFill(mob) for mob in vmobjects]
        )

        self.wait()


class WriteExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[Write(mob) for mob in mobjects]
        )

        self.wait()


class ShowIncreasingSubsetsExample(Scene):
    def construct(self):
        text = Text("ShowIncreasingSubsets")
        text.set_width(11)
        self.wait()
        self.play(ShowIncreasingSubsets(text, run_time=4))
        self.wait()


class ShowSubmobjectsOneByOneExample(Scene):
    def construct(self):
        text = Text("ShowSubmobjectsOneByOne")
        text.set_width(11)
        self.wait()
        self.play(ShowSubmobjectsOneByOne(text, run_time=4))
        self.wait()
