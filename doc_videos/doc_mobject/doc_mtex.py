from manimlib import *

class MTexSpecifySubstrings(Scene): 
    def construct(self):
        tex = MTex("\\sqrt{{s}}").shift(UP)
        tex.select_part("s").set_fill(TEAL)
        self.add(tex)
        poly = MTex(
            "p(x) = a_0 x^0 + a_1 x^1 + \\cdots + a_{n-1} x^{n-1} + a_n x^n",
            tex_to_color_map={re.compile(r"a_(.+?) x\^\1"): ORANGE}
        )
        self.add(poly)
