from manimlib.imports import *
from manim_sandbox.imports import *


class Scene_(Scene):
    CONFIG = {"camera_config": {"background_color": "#ffffff"}}


class Scene1(Scene_):

    def construct(self):
        hL = Line(color=BLUE).scale(7).shift(UP*3)
        dot0= Dot(color=ORANGE).shift(UP*2)
        self.add(hL, dot0)
        vg=VGroup()
        doti = Dot(color=ORANGE).move_to(hL.get_start())
        l_1 = Line(color=BLACK, stroke_width=1.5).put_start_and_end_on(dot0.get_center(), doti.get_center())
        l_2 = l_1.copy().rotate(PI/2).scale(10).set_color(PURPLE).set_stroke(width=6)
        doti.save_state()
        self.add(doti, l_1, l_2, vg)

        def anim(obj, alpha):
            doti.restore()
            doti.shift(RIGHT*hL.get_length()*alpha)
            l_1.put_start_and_end_on(dot0.get_center(), doti.get_center())
            l_2.become(l_1.copy().rotate(PI / 2).scale(100).set_color(PURPLE).set_stroke(width=6))
            vg.add(l_2.copy().set_stroke(width=2,color=PURPLE_E))

        self.play(UpdateFromAlphaFunc(doti, anim), run_time=8, rate_func=linear)
        self.wait()


class Scene2(Scene_):

    def construct(self):
        dot_a = Dot(np.array([-3,-3,0]), color=PURPLE_A)
        dot_b = Dot(np.array([0,3,0]), color=PURPLE_A)
        dot_c = Dot(np.array([3,-3,0]), color=PURPLE_A)
        l_1 = Line(color=BLUE).put_start_and_end_on(dot_a.get_center(), dot_b.get_center())
        l_2 = Line(color=BLUE).put_start_and_end_on(dot_b.get_center(), dot_c.get_center())
        l_3 = l_1.copy()
        lineG = VGroup()
        self.add(dot_a, dot_b, dot_c, l_1, l_2, l_3, lineG)

        def anim(obj, alpha):
            dot_a.move_to(l_1.point_from_proportion(alpha))
            dot_b.move_to(l_2.point_from_proportion(alpha))
            l_3.put_start_and_end_on(dot_a.get_center(), dot_b.get_center())
            # if int(alpha*100) % 5 == 0:  #加if之后会间歇的加入中间的包络线
            #     lineG.add(l_3.copy().set_stroke(width=2, color=BLUE_A))
            lineG.add(l_3.copy().set_stroke(width=2, color=BLUE_A)) #这行的话最后是用线填充这个区域

        self.play(UpdateFromAlphaFunc(l_3, anim), run_time=8, rate_func=linear)
        self.wait()


#注意:下面这个场景如果渲染的话等待时长会超出想象!
#我做梦都没想到100秒的动画居然渲染了一个多小时
#可以尝试把时间和set_value改小,然后再尝试
#视频效果见->https://www.acfun.cn/v/ac15122185
class Envelop(Scene):

    def construct(self):
        num=360
        lines=VGroup()
        t=ValueTracker(0.)
        dec_num=DecimalNumber(0,number_decimal_places=2).to_corner(DR, buff=0.5)
        text=TexMobject("n=").next_to(dec_num,LEFT,buff=0.18)
        
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
        dec_num.add_updater(lambda a:a.set_value(t.get_value()))
        self.add(lines, dec_num,text)
        lines.add_updater(func)
        self.add(lines,dec_num)
        self.play(t.set_value, 7, run_time=100, rate_func=linear)
