from manimlib import *


class ThreeDSceneExample(InteractiveScene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP))
        self.play(square.animate.shift(DOWN))
        self.embed()
