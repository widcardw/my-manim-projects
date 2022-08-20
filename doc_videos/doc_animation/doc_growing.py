from manimlib import *

class GrowFromPointExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
        mobjects.arrange(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromPoint(mob,mob.get_center()+direction*3) for mob in mobjects]
            )

        self.wait()


class GrowFromCenterExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        self.play(
            *[GrowFromCenter(mob) for mob in mobjects]
        )

        self.wait()


class GrowFromEdgeExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
        mobjects.arrange(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromEdge(mob,direction) for mob in mobjects]
            )

        self.wait()


class GrowArrowExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Arrow(LEFT,RIGHT),
                Vector(RIGHT*2).set_color(YELLOW)
            )
        mobjects.scale(3)
        mobjects.arrange(DOWN,buff=2)

        self.play(
            *[GrowArrow(mob)for mob in mobjects]
        )

        self.wait()

class SpinInFromNothingExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1, color=GREEN),
                Text("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        self.play(
            *[SpinInFromNothing(mob) for mob in mobjects]
        )

        self.wait()