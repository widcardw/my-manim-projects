from manimlib.imports import *
from my_projects.Danmaku.Bullet import *


class TestBullet(Scene):
    def construct(self):
        vqueue1 = VGroup()
        vqueue2 = VGroup()
        self.an = 0

        def update_bullet1(obj, dt):
            obj.add(Bullet().scale(0.7).rotate(self.time * 10 + self.an * 10))
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7:
                    obj.remove(k)
            self.an += 1 * DEGREES

        # def update_bullet2(obj, dt):
        #     obj.add(Bullet().scale(0.7).rotate(PI + self.time * 10 + self.an * 10))
        #     for k in obj:
        #         k.shift(dt * 2 * np.array([
        #             np.cos(k.get_angle()),
        #             np.sin(k.get_angle()),
        #             0
        #         ]))
        #         if abs(get_norm(k.get_center() - ORIGIN)) > 7:
        #             obj.remove(k)
        #     self.an += 1 * DEGREES

        vqueue1.add_updater(update_bullet1)
        # vqueue2.add_updater(update_bullet2)
        self.add(vqueue1)
        self.wait(15)
