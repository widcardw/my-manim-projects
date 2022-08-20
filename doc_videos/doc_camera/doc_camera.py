from manimlib import *


class ReorientCameraExample(Scene):
    def setup(self):
        # 初始化场景
        axes = ThreeDAxes()
        self.add(axes)
        sphere = Sphere().move_to(axes.coords_to_point(3, 2, 2))
        self.add(sphere)

    def construct(self) -> None:
        # 获取相机帧的引用
        camera = self.camera.frame
        self.wait()
        # 使用四元数旋转（欧拉旋转经常会检测到万向节锁死）
        self.play(camera.animate.set_orientation(Rotation([0.8, 0.2, 0.1, 0.9])))
        self.wait()


class MoveCameraExample(Scene):
    def setup(self):
        # 初始化坐标系
        self.plane = NumberPlane()
        self.plane.add_coordinate_labels()
        self.add(self.plane)

    def t_func(self, t):
        # 螺线参数方程
        a, b = 3, 3
        return np.array([
            a * np.cos(t) / t,
            b * np.sin(t) / t,
            0
        ])

    def construct(self):
        # 获取相机帧的引用
        frame = self.camera.frame
        # 创建螺线
        curve = ParametricCurve(self.t_func, t_range=[0.1, 100, 0.05], color=YELLOW)
        self.add(curve)
        self.play(
            curve.animate.set_stroke(width=0.3),       # 设置螺线粗细
            frame.animate.set_width(2).rotate(PI / 2), # 旋转缩放相机帧
            run_time=3
        )
        self.wait(0.5)