from manimlib import DEGREES, DOWN, ImageMobject, Scene, Group, RIGHT, TexText
import numpy as np


# class BengBuScene(Scene):
# 	def construct(self) -> None:
# 		sweat = ImageMobject("assets/sweat.png").set_width(0.5)
# 		smile = ImageMobject("assets/smile.png").set_width(0.5)
# 		g = Group(sweat, smile).arrange(RIGHT, buff=1.4)
# 		g2 = Group(*[g.copy().move_to(np.array([i * 0.3, -i * 0.4, 0])).rotate(i * 20 * DEGREES) for i in range(-20, 21)])
# 		self.add(g2)
# 		for item in g2:
# 			item.add_updater(lambda i, dt: i.rotate(dt * 50 * DEGREES))
# 		self.wait(10)


class TestTex(Scene):
	def construct(self) -> None:
		a = TexText("在 $abc$ 中")
		self.add(a)
