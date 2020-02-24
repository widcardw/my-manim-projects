from manimlib.imports import *

class ellipse(Scene):
    def get_ellipse(self, a, b, **kwargs):
        return ParametricFunction(lambda t: a*np.cos(t)*RIGHT+b*np.sin(t)*UP, t_min=-PI, t_max=PI)

    def get_ellipse_tg_line(self, a, b, x0, y0, **kwargs):
        return ParametricFunction(lambda t: (y0+b**2*x0*t)*UP+(x0-a**2*y0*t)*RIGHT, t_min=-10, t_max=10)

    CONFIG = {"const_a": 3.0, "const_b": 2.0, "theta": PI/6}

    def construct(self):
        var = ValueTracker(self.theta)
        graph = self.get_ellipse(self.const_a, self.const_b)\
            .set_color("#0077FF")
        dot_ = Dot().add_updater(lambda a: a.move_to(
            self.const_a*np.cos(var.get_value())*RIGHT+self.const_b*np.sin(var.get_value())*UP))
        tg = self.get_ellipse_tg_line(self.const_a, self.const_b,
                                      self.const_a*np.cos(var.get_value()),
                                      self.const_b*np.sin(var.get_value())).set_color("#FFFF00")
        tg.add_updater(lambda m: m.become(
            self.get_ellipse_tg_line(self.const_a, self.const_b,
                                     self.const_a * np.cos(var.get_value()),
                                     self.const_b*np.sin(var.get_value())).set_color("#FFFF00")))
        self.add(graph)
        self.add(tg)
        self.add(dot_)
        self.play(var.increment_value, 2*PI/3)
        self.play(var.increment_value, -PI/2)
        self.wait(0.8)

