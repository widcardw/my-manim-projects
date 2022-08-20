from manimlib import *


class BroadcastExample(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        anim_kwargs = {
            'big_radius': 5,
            'n_circles': 8,
            'lag_ratio': 0.1,
            'color': YELLOW
        }
        self.play(Broadcast(dot, **anim_kwargs))
        self.wait()