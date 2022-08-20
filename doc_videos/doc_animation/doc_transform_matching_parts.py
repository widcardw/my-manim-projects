from manimlib import *


class TransformMatchingShapesExample(Scene):
    def construct(self):
        a = Text("the morse code").scale(2)
        b = Text("here some dots").scale(2)
        self.add(a)
        self.wait()
        self.play(TransformMatchingShapes(a, b, path_arc=PI/2))
        self.wait()
        self.play(TransformMatchingShapes(b, a, path_arc=PI/2))
        self.wait()


class TransformMatchingTexExample(Scene):
    def construct(self):
        a = Tex("A", "^2", "=", "B^2+C^2")
        b = Tex("A", "=", "\\sqrt{", "B^2+C^2", "}")
        self.add(a)
        self.wait()
        self.play(TransformMatchingTex(a, b, key_map={"^2": "\\sqrt{"}))
        self.wait()

class TransformMatchingStringsExample(Scene):
    def construct(self):
        kw = {
            "isolate": [
                "\\int_{0}^{\\infty} \\mathrm{e}^{- t}",
                "\\mathrm{d} t",
                "c_{0}",
                "c_{1} t",
                "c_{2} t^{2}",
                "c_{n} t^{n}"
            ],
            "tex_to_color_map": {
                "\\mathrm{e}": MAROON_A,
                "c_{0}": BLUE,
                "c_{1}": BLUE,
                "c_{2}": BLUE,
                "c_{n}": BLUE
            }
        }
        explicit_formula = MTex(
            "\\int_{0}^{\\infty} \\mathrm{e}^{- t}"
            " \\left( c_{0} + c_{1} t + c_{2} t^{2} + \\cdots + c_{n} t^{n} \\right) \\mathrm{d} t",
            **kw
        )
        expanded_formula = MTex(
            "\\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{0} \\mathrm{d} t"
            " + \\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{1} t \\mathrm{d} t"
            " + \\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{2} t^{2} \\mathrm{d} t"
            " + \\cdots"
            " + \\int_{0}^{\\infty} \\mathrm{e}^{- t} c_{n} t^{n} \\mathrm{d} t",
            **kw
        ).scale(0.8)
        self.add(explicit_formula)
        self.wait()
        self.play(TransformMatchingStrings(explicit_formula, expanded_formula), run_time=2)
        self.wait()