from manimlib import *

class TestRestore(Scene):
    def construct(self) -> None:
        a = Circle()
        a.save_state()
        self.add(a)
        self.play(Transform(a, Square()))
        self.wait()
        self.play(a.animate.restore())
