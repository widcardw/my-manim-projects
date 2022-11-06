from manimlib import *

class Bullet(ArrowTip):
    def __init__(self, vector: npt.NDArray[np.float64] = RIGHT, **kwargs):
        super().__init__(**kwargs)
        self.data["points"][4] += LEFT*0.5
        self.scale(0.3)
        self.rotate(angle_of_vector(vector) + PI)
        self.vector = vector

    def get_angle(self):
        return angle_of_vector(self.vector)

    def get_vector(self):
        return self.vector

    def set_vector(self, vector: np.ndarray):
        previous_angle = self.get_angle()
        self.vector = vector
        self.rotate(angle_of_vector(vector) - previous_angle + PI)
        return self

    def set_angle(self, angle: float):
        previous_vector = self.get_vector()
        self.rotate(angle - self.get_angle())
        self.vector = rotate_vector(previous_vector, angle)
        return self


color_list = [RED, GOLD, YELLOW, GREEN, TEAL, BLUE, PURPLE]
v = 3


class TestDanmaku(Scene):
    def construct(self):
        vg1 = VGroup()
        vg2 = VGroup()
        # vg3 = VGroup()

        def update_one_trace(start_angle: float):
            def update(mob, dt):
                mob.add(Bullet(rotate_vector(RIGHT, start_angle + self.time ** 2)))
                mob.set_color_by_gradient(*color_list)
                for o in mob:
                    o.shift(v * dt * o.vector)
                    if o.is_off_screen():
                        mob.remove(o)
            return update

        vg1.add_updater(update_one_trace(0))
        vg2.add_updater(update_one_trace(PI))
        # vg3.add_updater(update_one_trace(2 * TAU / 3))
        self.add(vg1, vg2)
        self.wait(5)


omega = 0.25
side_length = 10


class SquareDanmaku(Scene):
    def construct(self):
        vg = VGroup()
        self.count = 0

        def update_danmaku(mob: VGroup, dt: float):
            if self.count % 15 == 0:
                vectors = np.array([
                    rotate_vector(v * RIGHT, self.time * omega),
                    rotate_vector(v * UP, self.time * omega),
                    rotate_vector(v * LEFT, self.time * omega),
                    rotate_vector(v * DOWN, self.time * omega),
                ])
                mob.add(*[
                    Bullet(interpolate(
                        vectors[j % 4], vectors[(j + 1) % 4], k / side_length))
                    for k in range(side_length)
                    for j in range(4)
                ])
            for o in mob:
                o.shift(dt * o.vector)
                if o.is_off_screen():
                    mob.remove(o)
            mob.set_color_by_gradient(*color_list)
            self.count += 1

        vg.add_updater(update_danmaku)
        self.add(vg)
