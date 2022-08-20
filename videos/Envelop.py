from manimlib import *
# broken

class Test(Scene):

    def construct(self):
        num=360
        lines=VGroup()
        t=ValueTracker(0.)
        dec_num=DecimalNumber(0,number_decimal_places=2).to_corner(DR, buff=0.5)
        text=Tex("n=").next_to(dec_num,LEFT,buff=0.18)

        def func(lines, dt):
            lines_=VGroup()
            for i in range(num):
                distance=get_norm(np.array([np.cos(i*TAU/num),np.sin(i*TAU/num),0])\
                              -np.array([np.cos(t.get_value()*i*TAU/num),np.sin(t.get_value()*i*TAU/num),0]))
                if distance > 0:
                    line_i=Line(3.5*np.array([np.cos(i*TAU/num),np.sin(i*TAU/num),0]),
                            3.5*np.array([np.cos(t.get_value()*i*TAU/num),np.sin(t.get_value()*i*TAU/num),0]),
                            stroke_width=1)
                    lines_.add(line_i)
            lines_.set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
            lines.become(lines_)
        lines.set_color_by_gradient([RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE])
        dec_num.add_updater(lambda a: a.set_value(t.get_value()))
        self.add(lines, dec_num,text)
        lines.add_updater(func)
        self.add(lines,dec_num)
        self.play(t.animate.set_value(7), run_time=7, rate_func=linear)
