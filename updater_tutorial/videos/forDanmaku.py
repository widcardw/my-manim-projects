from manimlib import *


class Bullet(Triangle):
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 0,
        "length": DEFAULT_ARROW_TIP_LENGTH,
        "start_angle": PI,
        "aspect": 1.5,
        "angle": 0,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        digest_config(self, kwargs)
        self.set_height(self.length, stretch=True)
        self.set_width(self.length * self.aspect, stretch=True)
        self.data["points"][4] += np.array([self.length, 0, 0])
        self.scale(0.35)

    def get_angle(self):
        return self.angle

    def get_vector(self):
        return self.point_from_proportion(0.5) - self.get_start()

    def rotate(self, angle, axis=OUT, **kwargs):
        super().rotate(angle, axis, **kwargs)
        self.angle = angle
        return self


class TestDanmaku(Scene):
    def construct(self):
        trace1 = VGroup()
        trace2 = VGroup()
        trace3 = VGroup()
        color_map = [PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED]

        def update_one_trace(start_angle):
            def update(obj, dt):
                obj.add(Bullet().rotate(self.time ** 2 * PI + start_angle))
                obj.set_color_by_gradient(*color_map)
                for k in obj:
                    k.shift(np.array([
                        np.cos(k.get_angle()),
                        np.sin(k.get_angle()),
                        0
                    ]) * 4 * dt)
                    if abs(get_norm(k.get_center())) > 7:
                        obj.remove(k)

            return update

        trace1.add_updater(update_one_trace(0))
        trace2.add_updater(update_one_trace(TAU / 3))
        trace3.add_updater(update_one_trace(TAU / 3 * 2))
        self.add(trace1, trace2, trace3)
        self.wait(10)
