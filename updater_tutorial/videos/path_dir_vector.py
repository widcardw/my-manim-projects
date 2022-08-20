from manimlib import *


class PathVector(VGroup):
    CONFIG = {
        'd_alpha': 1e-6,
        'tip_size': 0.3,
        'vector_num': 8
    }

    def __init__(self, vmobject: VMobject, offset=0, reversed=1, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        d_alpha = self.d_alpha
        for i in range(self.vector_num):
            # a1 = clip(i / self.vector_num - d_alpha + offset, 0, 1)
            # a2 = clip(i / self.vector_num + d_alpha + offset, 0, 1)
            a1 = (i / self.vector_num - d_alpha + offset * reversed) % 1
            a2 = (i / self.vector_num + d_alpha + offset * reversed) % 1
            angle = angle_of_vector(vmobject.pfp(a2) - vmobject.pfp(a1))
            reversed_angle = 0 if reversed == 1 else PI
            tip = ArrowTip().scale(self.tip_size).rotate(angle + reversed_angle).move_to(vmobject.pfp(a1))
            self.add(tip)
