from manimlib import *


class HomotopyExample(Scene):
      def construct(self):
          def homotopy_fun(x, y, z, t):
              return [x * t, y * t, z]

          mob = Square()
          self.add(mob)
          self.play(Homotopy(homotopy_fun, mob))
          self.wait()


class ComplexHomotopyExample(Scene):
    def construct(self):
        def complex_func(z: complex, t: float) -> complex:
            return interpolate(z, z**3, t)

        mobjects = VGroup(
            Text("Text"),
            Square(side_length=1),
        ).arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.play(
            *[ComplexHomotopy(
                complex_func,
                mob
            ) for mob in mobjects]
        )
        self.wait(0.3)


class PhaseFlowExample(Scene):
    def construct(self):
        def func(t):
            return t*0.5*RIGHT

        mobjects=VGroup(
            Text("Text").scale(3),
            Square(),
        ).arrange(RIGHT,buff=2)

        self.play(
            *[PhaseFlow(
                func, mob,
                run_time = 2,
            )for mob in mobjects]
        )

        self.wait()


class MoveAlongPathExample(Scene):
    def construct(self):
        line=Line(ORIGIN,RIGHT*FRAME_WIDTH,buff=1)
        line.move_to(ORIGIN)
        dot=Dot(color=YELLOW)
        dot.move_to(line.get_start())

        self.add(line,dot)
        self.play(
            MoveAlongPath(dot,line)
        )
        self.wait(0.3)