from manimlib import *


class FadeOutExample(Scene):
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
            *[FadeOut(mob) for mob in mobjects]
        )

        self.wait()


class FadeInExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[FadeIn(mob) for mob in mobjects]
        )

        self.wait()


class FadeInFromExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        directions = [UP, LEFT, DOWN, RIGHT]

        for direction in directions:
            self.play(
                *[FadeIn(mob, shift=direction) for mob in mobjects]
            )

        self.wait()


class FadeOutAndShiftExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        directions = [UP, LEFT, DOWN, RIGHT]

        self.add(mobjects)
        self.wait(0.3)

        for direction in directions:
            self.play(
                *[FadeOut(mob, shift=direction) for mob in mobjects]
            )

        self.wait()


class FadeInFromLargeExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        scale_factors = [0.3, 0.8, 1, 1.3, 1.8]

        for scale_factor in scale_factors:
            t_scale_factor = Text(
                f"scale_factor = {scale_factor}", font="monospace")
            t_scale_factor.to_edge(UP)

            self.add(t_scale_factor)

            self.play(
                *[FadeIn(mob, scale=scale_factor) for mob in mobjects]
            )

            self.remove(t_scale_factor)

        self.wait(0.3)


class FadeInFromPointExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.wait()
        self.play(
            *[FadeInFromPoint(mob, UP*3) for mob in mobjects]
        )
        self.wait()


class FadeOutToPointExample(Scene):
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
        self.play(
            *[FadeOutToPoint(mob, DOWN*3) for mob in mobjects]
        )
        self.wait()


class FadeTransformExample(Scene):
    def construct(self):
        m_a = Rectangle(width=6, height=2, color=BLUE, fill_opacity=1)
        m_b = Text("Rectangle").scale(3)
        self.add(m_a)
        self.wait()
        self.play(FadeTransform(m_a, m_b))
        self.wait()


class FadeTransformPiecesExample(Scene):
    def construct(self):
        m_a = VGroup(*[
            Circle(radius=0.4)
            .move_to((np.random.random(3)-0.5) * 3)
            for i in range(6)
        ])
        m_b = Text("Circle").scale(3)
        self.add(m_a)
        self.wait()
        self.play(FadeTransformPieces(m_a, m_b))
        self.wait()
