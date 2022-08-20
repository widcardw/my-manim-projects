from manimlib import *


class TransformExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3)
        C = Text("C-Text").scale(3)

        self.add(A)
        self.wait()
        self.play(Transform(A, B))
        self.wait()
        self.play(Transform(A, C))  # notice here
        self.wait()


class ReplacementTransformExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3)
        C = Text("C-Text").scale(3)

        self.add(A)
        self.wait()
        self.play(ReplacementTransform(A, B))
        self.wait()
        self.play(ReplacementTransform(B, C))  # notice here
        self.wait()


class TransformFromCopyExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3).shift(UP*2)

        self.add(A)
        self.wait()
        self.play(TransformFromCopy(A, B))
        self.wait()


class ClockwiseTransformExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3).shift(UP*2)

        self.add(A)
        self.wait()
        self.play(ClockwiseTransform(A, B))
        self.wait()


class CounterclockwiseTransformExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3).shift(UP*2)

        self.add(A)
        self.wait()
        self.play(CounterclockwiseTransform(A, B))
        self.wait()


class MoveToTargetExample(Scene):
    def construct(self):
        A = Text("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.scale(3).shift(RIGHT*7+UP*2)  # 操作A的target

        self.add(A)
        self.wait()
        self.play(MoveToTarget(A))
        self.wait()


class SelfPlayExample(Scene):
    def construct(self):
        A = Text("Text-A").to_edge(LEFT)

        self.add(A)
        self.wait()
        # self.play(
        #     A.scale, 3,
        #     A.shift, RIGHT*7+UP*2,
        # )
        self.play(
            A.animate.scale(3).shift(RIGHT*7+UP*2)
        )
        self.wait()


class ApplyMethodExample(Scene):
    def construct(self):
        A = Text("Text-A").to_edge(LEFT)

        self.add(A)
        self.wait()
        self.play(
            ApplyMethod(A.scale, 3),  # 这个不会执行
            ApplyMethod(A.shift, RIGHT*7+UP*2),
        )
        self.wait()


class ApplyPointwiseFunctionExample(Scene):
    def construct(self):
        def trans(p: np.ndarray) -> np.ndarray:
            return np.array([
                p[0] + np.sin(p[1]),
                p[1] + np.sin(p[0]),
                p[2]
            ])
        plane = NumberPlane()
        self.add(plane)
        self.wait()
        plane.prepare_for_nonlinear_transform()
        self.play(ApplyPointwiseFunction(trans, plane))
        self.wait()


# class ApplyPointwiseFunctionToCenterExample(Scene):
#     # 暂时不能用
#     def construct(self):
#         def trans(p: np.ndarray) -> np.ndarray:
#             return np.array([
#                 p[0] + np.sin(p[1]),
#                 p[1] + np.sin(p[0]),
#                 p[2]
#             ])
#         plane = NumberPlane()
#         self.add(plane)
#         self.wait()
#         plane.prepare_for_nonlinear_transform()
#         self.play(ApplyPointwiseFunctionToCenter(trans, plane))
#         self.wait()


class ShrinkToCenterExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Square(),
            RegularPolygon(fill_opacity=1, color=GREEN),
            Text("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[ShrinkToCenter(mob) for mob in mobjects]
        )

        self.wait()


class RestoreExample(Scene):
    def construct(self):
        A = Text("Text-A").to_edge(LEFT)
        A.save_state()  # 记录下现在状态，restore会回到此时
        A.scale(3).shift(RIGHT*7+UP*2)

        self.add(A)
        self.wait()
        self.play(Restore(A))
        self.wait()


class ApplyFunctionExample(Scene):
    def construct(self):
        A = Text("Text-A").to_edge(LEFT)

        def function(mob):
            return mob.scale(3).shift(RIGHT*7+UP*2)
            # 需要return一个mobject

        self.add(A)
        self.wait()
        self.play(ApplyFunction(function, A))
        self.wait()


class ApplyMatrixExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(2)
        mat = np.array([
            [1, 3, 1],
            [0.5, 1, 1],
            [1, 1, 1]
        ])

        self.add(A)
        self.wait()
        self.play(ApplyMatrix(mat, A))
        self.wait()


class ApplyComplexFunctionExample(Scene):
    def construct(self):
        A = NumberPlane()
        A.prepare_for_nonlinear_transform()

        def complex_func(z: complex) -> complex:
            return z**3

        self.add(A)
        self.wait()
        self.play(ApplyComplexFunction(complex_func, A), run_time=3)
        self.wait()


class CyclicReplaceExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3)
        VGroup(A, B).arrange(RIGHT)

        self.add(A, B)
        self.wait()
        self.play(CyclicReplace(A, B))  # 或Swap(A, B)
        self.wait()
