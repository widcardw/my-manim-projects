# from 群友 嘤
from manimlib import *

class Grid(VMobject):
    def __init__(self, w: int = 5, h: int = 5, ws: float = 1, hs: float = 1, **kwargs):
        super().__init__(**kwargs)
        # 竖线
        for i in range(w + 1):
            self.add(Line(i * RIGHT * ws, UP * h * hs +
                     i * RIGHT * ws).insert_n_curves(12))
        # 横线
        for j in range(h + 1):
            self.add(Line(j * UP * hs, RIGHT * w * ws +
                     j * UP * hs).insert_n_curves(12))
        self.center()


class SpreadGrid(Scene):
    def construct(self) -> None:
        grid = Grid(12, 12, 0.5, 0.5)
        slices = 12
        # 竖线颜色
        opacity_h = np.zeros((slices, slices))
        opacity_w = np.zeros((slices, slices))
        opacity_h[(slices * 1)//4:(slices * 3)//4,
                  (slices * 1)//4:(slices * 3)//4] = 1
        opacity_w[(slices * 1)//4:(slices * 3)//4,
                  (slices * 1)//4:(slices * 3)//4] = 1
        # color_grid = [[WHITE for i in range(slices)] for j in range(2 * slices)]
        # grid.set_stroke(opacity=np.concatenate((opacity_h.flatten(), opacity_w.flatten())))
        self.add(grid)

        def opacity_anim(mob: VMobject, alpha):
            opacity_h[int(slices*(0.5-alpha/2)):int(slices*(0.5+alpha/2)),
                      int(slices*(0.5-alpha/2)):int(slices*(0.5+alpha/2))] = 1
            opacity_w[int(slices*(0.5-alpha/2)):int(slices*(0.5+alpha/2)),
                      int(slices*(0.5-alpha/2)):int(slices*(0.5+alpha/2))] = 1
            mob.set_stroke(opacity=np.concatenate(
                (opacity_h.flatten(), opacity_w.flatten())))

        self.play(UpdateFromAlphaFunc(grid, opacity_anim), run_time=2)


class test_3(Scene):
    def construct(self):
        def new_shader(i):
            return f"""
            float width = 6.0;
            vec2 lower = fract(point.xy * 2);
            float t = {i};
            float alpha = - length(point.xy / width) + t;
            if (alpha < 0) 
                discard;
            //if (alpha < 0.01) return vec4(1,1,0,t);
            if (max(abs(lower.x - 0.5), abs(lower.y - 0.5)) < 0.45) 
                discard;
            if (alpha < 0.1) 
                color = mix(vec4(0,0,0,0), vec4(1,1,0,1), smoothstep(0.0, 0.1, alpha));
            else 
                color = mix(vec4(1,1,0,1), vec4(1,1,1,1), smoothstep(0.1, 0.2, alpha));
            return color;
            """

        def update_shader(mob, i):
            mob.init_shader_data()
            mob.set_color_by_code(new_shader(i * 1.3))

        m = Surface(resolution=(2, 2)).scale(6.05).center()
        self.add(m)
        self.play(UpdateFromAlphaFunc(m, update_shader, run_time=3))
        sd = m.shader_wrapper.vert_data
        print(sd, sd.shape)

