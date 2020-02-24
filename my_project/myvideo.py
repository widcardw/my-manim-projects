from manimlib.imports import *

class HelloWorld(Scene):
	def construct(self):
		helloworld = TextMobject("Hello World!").scale(3)
		line = Line(np.array([-4.5,-1,0]),np.array([4.5,-1,0]),color=BLUE)
		formula = TexMobject("\\frac{\\mathrm{d}}{\\mathrm{d} x}f(x)=\\lim_{h\\rightarrow 0}\\frac{f(x+h)-f(x)}{h}").scale(1.3)
		manim = TextMobject("Powered by Manim").scale(1.5)
	 
		self.play(Write(helloworld))
		self.play(ShowCreation(line))
		self.play(FadeOut(line))
		self.play(Transform(helloworld, formula))
		self.wait(1)
		self.play(FadeOutAndShiftDown(helloworld))
		self.play(Write(manim))
		self.wait(2)
		
		
class Lifanghe(Scene):
	def construct(self):
		text1 = TexMobject("1^3+2^3+3^3+4^3+...+n^3=?").scale(1.2)
		grid = NumberPlane()
		
		self.play(Write(text1))
		self.wait(1)
		self.play(ApplyMethod(text1.scale, 0.6))
		self.play(ApplyMethod(text1.to_corner, DR))
		self.play(ShowCreation(grid, run_time=3, lag_ratio=0.1))
		
		
class sincos1(Scene):
	def construct(self):
		text1=TexMobject("sin\\alpha+sin\\beta=2sin\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}").move_to(UP * 2.4)
		text2=TexMobject("sin\\alpha-sin\\beta=2cos\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}").move_to(UP * 0.8)
		text3=TexMobject("cos\\alpha+cos\\beta=2cos\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}").move_to(DOWN * 0.8)
		text4=TexMobject("cos\\alpha-cos\\beta=-2sin\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}").move_to(DOWN * 2.4)
		group1=VGroup(text1,text2,text3,text4)
		why=TextMobject("But why?",color=YELLOW).move_to(RIGHT * 4)
		why.scale(2.5)
		
		self.play(Write(text1),
			Write(text2),
			Write(text3),
			Write(text4),
		)
		self.wait(2)
		self.play(ApplyMethod(group1.shift, LEFT * 2.5))
		self.play(ShowCreation(why))
		self.wait(2)


class sincos2(Scene):
	def construct(self):
		text1=TexMobject("sin\\alpha+sin\\beta").move_to(UP*3.3)
		text2=TexMobject("\\alpha=","\\frac{\\alpha+\\beta}{2}+\\frac{\\alpha-\\beta}{2}").move_to(UP*2.3+LEFT*3)
		
		text3=TexMobject("\\beta=","\\frac{\\alpha+\\beta}{2}-\\frac{\\alpha-\\beta}{2}").move_to(UP*2.3+RIGHT*3)
		
		text4=TexMobject("sin\\alpha+sin\\beta","=","sin(\\frac{\\alpha+\\beta}{2}+\\frac{\\alpha-\\beta}{2})","+","sin(\\frac{\\alpha+\\beta}{2}-\\frac{\\alpha-\\beta}{2})").move_to(UP*1.1)
		text5=TexMobject("=","sin\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}","+","cos\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}")
		text5[0].set_color(WHITE)
		text5[1].set_color(BLUE)
		text5[2].set_color(WHITE)
		text5[3].set_color(RED)
		text6=TexMobject("+","sin\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}","-","cos\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}").move_to(DOWN*1.1)
		text6[0].set_color(WHITE)
		text6[1].set_color(BLUE)
		text6[2].set_color(WHITE)
		text6[3].set_color(RED)
		text7=TexMobject("=","2sin\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}").move_to(DOWN*2.2+LEFT*2.2)
		text7[0].set_color(WHITE)
		text7[1].set_color(YELLOW)
		
		self.play(Write(text1))
		self.wait(0.5)
		self.play(Write(text2))
		self.wait(2)
		self.play(Write(text3))
		self.wait(3)
		self.play(
			Write(text4[0]),
			Write(text4[1]),
			Write(text4[3]),
			ReplacementTransform(text2[1].copy(),text4[2]),
			ReplacementTransform(text3[1].copy(),text4[4]),
			)
		self.wait(3)
		self.play(ReplacementTransform(text4[2].copy(),text5))
		self.wait(1)
		self.play(ReplacementTransform(text4[4].copy(),text6))
		self.wait(3)
		self.play(
			Write(text7[0]),
			ReplacementTransform(text5[1].copy(),text7[1]),
			ReplacementTransform(text6[1].copy(),text7[1]),
			)
		self.wait(4)


class sincos3(Scene):
	def construct(self):
		text1=TexMobject("sin\\alpha-sin\\beta").move_to(UP*2.4+LEFT*3)
		text2=TexMobject(
			"=sin(",
			"\\frac{\\alpha+\\beta}{2}+\\frac{\\alpha-\\beta}{2}",
			")-sin(",
			"\\frac{\\alpha+\\beta}{2}-\\frac{\\alpha-\\beta}{2}",
			")"
			).move_to(UP*1.2)
		text2[0].set_color(WHITE)
		text2[1].set_color(BLUE)
		text2[2].set_color(WHITE)
		text2[3].set_color(RED)
		text2[4].set_color(WHITE)
		text3=TexMobject(
			"=",
			"sin\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}",
			"+",
			"cos\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(LEFT*0.3)
		text3[0].set_color(WHITE)
		text3[1].set_color(BLUE)
		text3[2].set_color(WHITE)
		text3[3].set_color(RED)
		text4=TexMobject(
			"-",
			"sin\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}",
			"+",
			"cos\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(DOWN*1.2)
		text4[0].set_color(WHITE)
		text4[1].set_color(BLUE)
		text4[2].set_color(WHITE)
		text4[3].set_color(RED)
		text5=TexMobject(
			"=",
			"2cos\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(DOWN*2.4+LEFT*2.5)
		text5[0].set_color(WHITE)
		text5[1].set_color(YELLOW)
		
		self.play(Write(text1))
		self.wait()
		self.play(Write(text2))
		self.wait(2)
		self.play(ReplacementTransform(text2[1].copy(),text3))
		self.wait()
		self.play(ReplacementTransform(text2[3].copy(),text4))
		self.wait(2)
		self.play(
		Write(
			text5[0]),
			ReplacementTransform(text3[3].copy(),text5[1]),
			ReplacementTransform(text4[3].copy(),text5[1])
			)
		self.wait(4)


class sincos4(Scene):
	def construct(self):
		text1=TexMobject("cos\\alpha+cos\\beta").move_to(UP*2.4+LEFT*3)
		text2=TexMobject(
			"=cos(",
			"\\frac{\\alpha+\\beta}{2}+\\frac{\\alpha-\\beta}{2}",
			")+cos(",
			"\\frac{\\alpha+\\beta}{2}-\\frac{\\alpha-\\beta}{2}",
			")"
			).move_to(UP*1.2)
		text2[0].set_color(WHITE)
		text2[1].set_color(BLUE)
		text2[2].set_color(WHITE)
		text2[3].set_color(RED)
		text2[4].set_color(WHITE)
		text3=TexMobject(
			"=",
			"cos\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}",
			"-",
			"sin\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(LEFT*0.3)
		text3[0].set_color(WHITE)
		text3[1].set_color(BLUE)
		text3[2].set_color(WHITE)
		text3[3].set_color(RED)
		text4=TexMobject(
			"+",
			"cos\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}",
			"+",
			"sin\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(DOWN*1.2)
		text4[0].set_color(WHITE)
		text4[1].set_color(BLUE)
		text4[2].set_color(WHITE)
		text4[3].set_color(RED)
		text5=TexMobject(
			"=",
			"2cos\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}"
			).move_to(DOWN*2.4+LEFT*2.5)
		text5[0].set_color(WHITE)
		text5[1].set_color(YELLOW)
		
		self.play(Write(text1))
		self.wait()
		self.play(Write(text2))
		self.wait(2)
		self.play(ReplacementTransform(text2[1].copy(),text3))
		self.wait()
		self.play(ReplacementTransform(text2[3].copy(),text4))
		self.wait(2)
		self.play(
		Write(
			text5[0]),
			ReplacementTransform(text3[1].copy(),text5[1]),
			ReplacementTransform(text4[1].copy(),text5[1])
			)
		self.wait(4)
		
		
class sincos5(Scene):
	def construct(self):
		text1=TexMobject("cos\\alpha-cos\\beta").move_to(UP*2.4+LEFT*3)
		text2=TexMobject(
			"=cos(",
			"\\frac{\\alpha+\\beta}{2}+\\frac{\\alpha-\\beta}{2}",
			")-cos(",
			"\\frac{\\alpha+\\beta}{2}-\\frac{\\alpha-\\beta}{2}",
			")"
			).move_to(UP*1.2)
		text2[0].set_color(WHITE)
		text2[1].set_color(BLUE)
		text2[2].set_color(WHITE)
		text2[3].set_color(RED)
		text2[4].set_color(WHITE)
		text3=TexMobject(
			"=",
			"cos\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}",
			"-",
			"sin\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(LEFT*0.3)
		text3[0].set_color(WHITE)
		text3[1].set_color(BLUE)
		text3[2].set_color(WHITE)
		text3[3].set_color(RED)
		text4=TexMobject(
			"-",
			"cos\\frac{\\alpha+\\beta}{2}cos\\frac{\\alpha-\\beta}{2}",
			"-",
			"sin\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(DOWN*1.2)
		text4[0].set_color(WHITE)
		text4[1].set_color(BLUE)
		text4[2].set_color(WHITE)
		text4[3].set_color(RED)
		text5=TexMobject(
			"=",
			"-2sin\\frac{\\alpha+\\beta}{2}sin\\frac{\\alpha-\\beta}{2}"
			).move_to(DOWN*2.4+LEFT*2.5)
		text5[0].set_color(WHITE)
		text5[1].set_color(YELLOW)
		
		self.play(Write(text1))
		self.wait()
		self.play(Write(text2))
		self.wait(2)
		self.play(ReplacementTransform(text2[1].copy(),text3))
		self.wait()
		self.play(ReplacementTransform(text2[3].copy(),text4))
		self.wait(2)
		self.play(
		Write(
			text5[0]),
			ReplacementTransform(text3[3].copy(),text5[1]),
			ReplacementTransform(text4[3].copy(),text5[1])
			)
		self.wait(4)
		
		
class chinesetest(Scene):
	def construct(self):
		text=TextMobject("积化和差公式推导").scale(2)
		
		self.play(Write(text))
		self.wait(2)
		self.play(FadeOutAndShiftDown(text))
		self.wait(0.5)
		
		
class licence(Scene):
	def construct(self):
		text1=TextMobject("Powered by Manim and FFmpeg")
		
		
		self.play(Write(text1))
		
		self.wait(3)
		
		
class ji1(Scene):
	def construct(self):
		text1=TexMobject(
			"sin(\\alpha+\\beta)",
			"=",
			"sin\\alpha",
			"cos\\beta",
			"+",
			"cos\\alpha",
			"sin\\beta",
			"(1)"
			).to_edge(UP)
		text1[0].set_color(WHITE)
		text1[1].set_color(WHITE)
		text1[2].set_color(BLUE)
		text1[3].set_color(BLUE)
		text1[4].set_color(WHITE)
		text1[5].set_color(RED)
		text1[6].set_color(RED)
		text1[7].set_color(YELLOW)

		text2=TexMobject(
			"sin(\\alpha-\\beta)",
			"=",
			"sin\\alpha",
			"cos\\beta",
			"-",
			"cos\\alpha",
			"sin\\beta",
			"(2)"
			).next_to(text1,DOWN)
		text2[0].set_color(WHITE)
		text2[1].set_color(WHITE)
		text2[2].set_color(BLUE)
		text2[3].set_color(BLUE)
		text2[4].set_color(WHITE)
		text2[5].set_color(RED)
		text2[6].set_color(RED)
		text2[7].set_color(YELLOW)

		text5=TextMobject(
			"(1)+(2)",
			"可得"
			).next_to(text2,DOWN)
		text5.set_color(ORANGE)

		text6=TexMobject(
			"sin(\\alpha+\\beta)+sin(\\alpha-\\beta)",
			"=",
			"2",
			"sin\\alpha",
			"cos\\beta"
			).next_to(text5,DOWN)
		text6[0].set_color(WHITE)
		text6[1].set_color(WHITE)
		text6[2].set_color(YELLOW)
		text6[3].set_color(BLUE)
		text6[4].set_color(BLUE)
		rectangle1=Rectangle(color=ORANGE,height=1.5,width=2.3).move_to(LEFT*0.2+UP*2.8)
		rectangle2=Rectangle(color=ORANGE,height=1.5,width=2.7).move_to(RIGHT*2.4+UP*2.8)
		text7=TextMobject("稍微化一下",color=ORANGE).next_to(text6,DOWN)
		
		text9=TexMobject(
			"sin\\alpha",
			"cos\\beta",
			"=",
			"\\frac{1}{2}",
			"[sin(\\alpha+\\beta)+sin(\\alpha-\\beta)]"
			).next_to(text6,DOWN)
		text9[0].set_color(BLUE)
		text9[1].set_color(BLUE)
		text9[2].set_color(WHITE)
		text9[3].set_color(YELLOW)
		text9[4].set_color(YELLOW)
		group1=VGroup(text5,text6,text9)

		self.play(Write(text1))
		self.play(Write(text2))
		self.wait(1)
		self.play(
			ShowCreation(rectangle1),
			ShowCreation(rectangle2)
			)
		self.play(Write(text5))
		self.play(
			FadeOut(rectangle1),
			FadeOut(rectangle2),
			)
		self.play(
			ReplacementTransform(text1[0].copy(),text6[0]),
			ReplacementTransform(text2[0].copy(),text6[0]),
			Write(text6[1])
			)
		self.play(
			ReplacementTransform(text1[2].copy(),text6[2]),
			ReplacementTransform(text1[3].copy(),text6[2]),
			ReplacementTransform(text2[2].copy(),text6[3]),
			ReplacementTransform(text2[3].copy(),text6[4]),
			)
		self.wait(0.5)
		self.play(Write(text7))
		self.play(FadeOut(text7))
		self.play(
			ReplacementTransform(text6[3].copy(),text9[0]),
			ReplacementTransform(text6[4].copy(),text9[1]),
			ReplacementTransform(text6[0].copy(),text9[4]),
			ReplacementTransform(text6[2].copy(),text9[3]),
			Write(text9[2])
			)
		self.wait()
		self.play(ApplyMethod(group1.to_edge,DOWN))
		self.wait(2)

		text10=TextMobject("同理,","(1)-(2)","可得").next_to(text2,DOWN)
		text10.set_color(ORANGE)

		text11=TexMobject(
			"sin(\\alpha+\\beta)-sin(\\alpha-\\beta)",
			"=",
			"2",
			"cos\\alpha",
			"sin\\beta"
			).next_to(text10,DOWN)
		text11[0].set_color(WHITE)
		text11[1].set_color(WHITE)
		text11[2].set_color(YELLOW)
		text11[3].set_color(RED)
		text11[4].set_color(RED)

		text8=TextMobject("也稍微化一下",color=ORANGE).next_to(text11,DOWN)

		text12=TexMobject(
			"cos\\alpha",
			"sin\\beta",
			"=",
			"\\frac{1}{2}",
			"[sin(\\alpha+\\beta)-sin(\\alpha-\\beta)]"
			).next_to(text11,DOWN)
		text12[0].set_color(RED)
		text12[1].set_color(RED)
		text12[2].set_color(WHITE)
		text12[3].set_color(YELLOW)
		text12[4].set_color(YELLOW)

		self.play(
			ShowCreation(rectangle1),
			ShowCreation(rectangle2),
			Write(text10)
			)
		self.play(
			FadeOut(rectangle1),
			FadeOut(rectangle2)
			)
		self.play(
			ReplacementTransform(text1[0].copy(),text11[0]),
			ReplacementTransform(text2[0].copy(),text11[0]),
			Write(text11[1])
			)
		self.play(
			ReplacementTransform(text1[5].copy(),text11[2]),
			ReplacementTransform(text1[6].copy(),text11[2]),
			ReplacementTransform(text2[5].copy(),text11[3]),
			ReplacementTransform(text2[6].copy(),text11[4])
			)
		self.play(Write(text8))
		self.play(FadeOut(text8))
		self.wait(0.5)
		self.play(
			ReplacementTransform(text11[3].copy(),text12[0]),
			ReplacementTransform(text11[4].copy(),text12[1]),
			ReplacementTransform(text11[0].copy(),text12[3]),
			ReplacementTransform(text11[2].copy(),text12[4]),
			Write(text12[2])
			)
		self.play(
			FadeOut(text1),
			FadeOut(text2),
			FadeOut(text5),
			FadeOut(text6),
			FadeOut(text10),
			FadeOut(text11)
			)
		self.play(
			ApplyMethod(text9.move_to,UP*0.8),
			ApplyMethod(text12.move_to,DOWN*0.8)
			)
		self.wait(2)
		self.play(
			FadeOut(text9),
			FadeOut(text12)
			)
		self.wait()

class ji2(Scene):
	def construct(self):
		text1=TexMobject(
			"cos(\\alpha+\\beta)",
			"=",
			"cos\\alpha",
			"cos\\beta",
			"-",
			"sin\\alpha",
			"sin\\beta",
			"(3)"
			).to_edge(UP)
		text1[0].set_color(WHITE)
		text1[1].set_color(WHITE)
		text1[2].set_color(BLUE)
		text1[3].set_color(BLUE)
		text1[4].set_color(WHITE)
		text1[5].set_color(RED)
		text1[6].set_color(RED)
		text1[7].set_color(YELLOW)

		text2=TexMobject(
			"cos(\\alpha-\\beta)",
			"=",
			"cos\\alpha",
			"cos\\beta",
			"+",
			"sin\\alpha",
			"sin\\beta",
			"(4)"
			).next_to(text1,DOWN)
		text2[0].set_color(WHITE)
		text2[1].set_color(WHITE)
		text2[2].set_color(BLUE)
		text2[3].set_color(BLUE)
		text2[4].set_color(WHITE)
		text2[5].set_color(RED)
		text2[6].set_color(RED)
		text2[7].set_color(YELLOW)

		text5=TextMobject(
			"(3)+(4)",
			"可得"
			).next_to(text2,DOWN)
		text5.set_color(ORANGE)

		text6=TexMobject(
			"cos(\\alpha+\\beta)+cos(\\alpha-\\beta)",
			"=",
			"2",
			"cos\\alpha",
			"cos\\beta"
			).next_to(text5,DOWN)
		text6[0].set_color(WHITE)
		text6[1].set_color(WHITE)
		text6[2].set_color(YELLOW)
		text6[3].set_color(BLUE)
		text6[4].set_color(BLUE)
		rectangle1=Rectangle(color=ORANGE,height=1.5,width=2.3).move_to(LEFT*0.2+UP*2.8)
		rectangle2=Rectangle(color=ORANGE,height=1.5,width=2.7).move_to(RIGHT*2.4+UP*2.8)
		text7=TextMobject("稍微化一下",color=ORANGE).next_to(text6,DOWN)
		
		text9=TexMobject(
			"cos\\alpha",
			"cos\\beta",
			"=",
			"\\frac{1}{2}",
			"[cos(\\alpha+\\beta)+cos(\\alpha-\\beta)]"
			).next_to(text6,DOWN)
		text9[0].set_color(BLUE)
		text9[1].set_color(BLUE)
		text9[2].set_color(WHITE)
		text9[3].set_color(YELLOW)
		text9[4].set_color(YELLOW)
		group1=VGroup(text5,text6,text9)

		self.play(Write(text1))
		self.play(Write(text2))
		self.wait(1)
		self.play(
			ShowCreation(rectangle1),
			ShowCreation(rectangle2)
			)
		self.play(Write(text5))
		self.play(
			FadeOut(rectangle1),
			FadeOut(rectangle2),
			)
		self.play(
			ReplacementTransform(text1[0].copy(),text6[0]),
			ReplacementTransform(text2[0].copy(),text6[0]),
			Write(text6[1])
			)
		self.play(
			ReplacementTransform(text1[2].copy(),text6[2]),
			ReplacementTransform(text1[3].copy(),text6[2]),
			ReplacementTransform(text2[2].copy(),text6[3]),
			ReplacementTransform(text2[3].copy(),text6[4]),
			)
		self.wait(0.5)
		self.play(Write(text7))
		self.play(FadeOut(text7))
		self.play(
			ReplacementTransform(text6[3].copy(),text9[0]),
			ReplacementTransform(text6[4].copy(),text9[1]),
			ReplacementTransform(text6[0].copy(),text9[4]),
			ReplacementTransform(text6[2].copy(),text9[3]),
			Write(text9[2])
			)
		self.wait()
		self.play(ApplyMethod(group1.to_edge,DOWN))
		self.wait(2)

		text10=TextMobject("同理,","(3)-(4)","可得").next_to(text2,DOWN)
		text10.set_color(ORANGE)

		text11=TexMobject(
			"cos(\\alpha+\\beta)-cos(\\alpha-\\beta)",
			"=",
			"-2",
			"sin\\alpha",
			"sin\\beta"
			).next_to(text10,DOWN)
		text11[0].set_color(WHITE)
		text11[1].set_color(WHITE)
		text11[2].set_color(YELLOW)
		text11[3].set_color(RED)
		text11[4].set_color(RED)

		text8=TextMobject("也稍微化一下",color=ORANGE).next_to(text11,DOWN)

		text12=TexMobject(
			"sin\\alpha",
			"sin\\beta",
			"=",
			"-\\frac{1}{2}",
			"[cos(\\alpha+\\beta)-cos(\\alpha-\\beta)]"
			).next_to(text11,DOWN)
		text12[0].set_color(RED)
		text12[1].set_color(RED)
		text12[2].set_color(WHITE)
		text12[3].set_color(YELLOW)
		text12[4].set_color(YELLOW)

		self.play(
			ShowCreation(rectangle1),
			ShowCreation(rectangle2),
			Write(text10)
			)
		self.play(
			FadeOut(rectangle1),
			FadeOut(rectangle2)
			)
		self.play(
			ReplacementTransform(text1[0].copy(),text11[0]),
			ReplacementTransform(text2[0].copy(),text11[0]),
			Write(text11[1])
			)
		self.play(
			ReplacementTransform(text1[5].copy(),text11[2]),
			ReplacementTransform(text1[6].copy(),text11[2]),
			ReplacementTransform(text2[5].copy(),text11[3]),
			ReplacementTransform(text2[6].copy(),text11[4])
			)
		self.play(Write(text8))
		self.play(FadeOut(text8))
		self.wait(0.5)
		self.play(
			ReplacementTransform(text11[3].copy(),text12[0]),
			ReplacementTransform(text11[4].copy(),text12[1]),
			ReplacementTransform(text11[0].copy(),text12[3]),
			ReplacementTransform(text11[2].copy(),text12[4]),
			Write(text12[2])
			)
		self.play(
			FadeOut(text1),
			FadeOut(text2),
			FadeOut(text5),
			FadeOut(text6),
			FadeOut(text10),
			FadeOut(text11)
			)
		self.play(
			ApplyMethod(text9.move_to,UP*0.8),
			ApplyMethod(text12.move_to,DOWN*0.8)
			)
		self.wait(1)

		text13=TexMobject(
			"sin\\alpha",
			"cos\\beta",
			"=",
			"\\frac{1}{2}",
			"[sin(\\alpha+\\beta)+sin(\\alpha-\\beta)]"
			).to_edge(UP,buff=1.2)
		text13[0].set_color(BLUE)
		text13[1].set_color(BLUE)
		text13[2].set_color(WHITE)
		text13[3].set_color(YELLOW)
		text13[4].set_color(YELLOW)

		text14=TexMobject(
			"cos\\alpha",
			"sin\\beta",
			"=",
			"\\frac{1}{2}",
			"[sin(\\alpha+\\beta)-sin(\\alpha-\\beta)]"
			).next_to(text13,DOWN)
		text14[0].set_color(RED)
		text14[1].set_color(RED)
		text14[2].set_color(WHITE)
		text14[3].set_color(YELLOW)
		text14[4].set_color(YELLOW)

		group2=VGroup(text13,text14)
		group3=VGroup(text9,text12)

		self.play(
			FadeInFrom(group2,UP),
			ApplyMethod(group3.move_to,DOWN*1.4)
			)
		self.wait()
		text15=TextMobject("这就是积化和差公式的推导").to_edge(DOWN)
		self.play(Write(text15))
		self.wait(2.5)
		group4=VGroup(text9,text12,text13,text14,text15)
		self.play(FadeOut(group4))
		self.wait()


class grid(Scene):
	def construct(self):
		grid=NumberPlane()
		self.play(ShowCreation(grid, run_time=3, lag_ratio=0.1))
		self.wait()


class fonttest(Scene):
	def construct(self):
		text1=Text("字体测试", font="等线")

		self.play(Write(text1))
		self.wait(2)


class lifanghe1(Scene):
	def construct(self):
		sum1=TexMobject(
			"1^3",   #0
			"+",     #1
			"2^3",   #2
			"+",     #3
			"3^3",   #4
			"+",     #5
			"4^3",   #6
			"+\\cdots +n^3=?")
		self.play(Write(sum1))
		self.wait(0.8)
		self.play(sum1.scale,0.8,sum1.to_edge,DOWN+RIGHT)
		net_plate=VGroup()
		for l in range(6):
			line_y_l_u = Line(np.array([-10, l + 0.5, 0]), np.array([10, l + 0.5, 0]), color=BLUE, stroke_width=0.2)
			line_y_l_d = Line(np.array([-10, -l-0.5, 0]), np.array([10, -l-0.5, 0]), color=BLUE, stroke_width=0.2)
			net_plate.add(line_y_l_u,line_y_l_d)
		for k in range(10):
			line_x_k_l=Line(np.array([k+0.5,-8,0]),np.array([k+0.5,8,0]),color=BLUE,stroke_width=0.2)
			line_x_k_r = Line(np.array([-k-0.5, -8, 0]), np.array([-k-0.5, 8, 0]), color=BLUE, stroke_width=0.2)
			net_plate.add(line_x_k_l, line_x_k_r)
		for j in range(6):
			line_y_j_u=Line(np.array([-10,j+1,0]),np.array([10,j+1,0]),color=BLUE,stroke_width=0.6)
			line_y_j_d = Line(np.array([-10, -j, 0]), np.array([10, -j, 0]), color=BLUE, stroke_width=0.6)
			net_plate.add(line_y_j_u,line_y_j_d)
		for i in range(10):
			line_x_i_l=Line(np.array([i+1,-8,0]),np.array([i+1,8,0]),color=BLUE,stroke_width=0.6)
			line_x_i_r=Line(np.array([-i,-8,0]),np.array([-i,8,0]),color=BLUE,stroke_width=0.6)
			net_plate.add(line_x_i_l,line_x_i_r)
		line_xx=Line(np.array([-10,-3,0]),np.array([12,-3,0]),color=WHITE,stroke_width=1)
		line_yy=Line(np.array([-6,-8,0]),np.array([-6,9,0]),color=WHITE,stroke_width=1)
		net_plate.add(line_xx,line_yy)
		self.play(ShowCreation(net_plate),run_time=3,lag_ratio=0.02)
		textreminder1=TextMobject("每一个小方格的边长都为1",color=YELLOW).scale(0.8).move_to(DOWN*3.3+LEFT*3)
		self.play(Write(textreminder1))
		self.wait(1)
		mul1x3=TexMobject("1^3",color=YELLOW).move_to(DOWN*2.6+RIGHT*1.1).scale(0.8)
		mul1x2x1=TexMobject("1^2 \\times 1",color=YELLOW).move_to(DOWN*2.6+RIGHT*1.1).scale(0.8)
		square1=Square(side_length=0.5,color=RED,fill_color=RED,fill_opacity=0.3).move_to(DOWN*2.6+RIGHT*0.8)
		mulx1=TexMobject("\\times 1",color=YELLOW).next_to(square1,RIGHT,buff=0.05).scale(0.8)
		gra1x3=VGroup(square1,mulx1)
		#self.play(WiggleOutThenIn(sum1[0]))
		self.play(ReplacementTransform(sum1[0].copy(),mul1x3))
		self.wait(0.8)
		self.play(ReplacementTransform(mul1x3,mul1x2x1))
		self.wait(0.8)
		self.play(ReplacementTransform(mul1x2x1,gra1x3))
		self.wait(1)
		self.play(
			FadeOut(mulx1),
			ApplyMethod(square1.move_to,DOWN*2.75+LEFT*5.75)
		)
		self.wait(2)
		mul2x3=TexMobject("2^3",color=YELLOW).move_to(DOWN*2.4+RIGHT*1.8).scale(0.8)
		mul2x2x2=TexMobject("2^2","\\times 2",color=YELLOW).move_to(DOWN*2.4+RIGHT*1.8).scale(0.8)
		square2=Square(side_length=1,color=RED,fill_color=RED,fill_opacity=0.3).move_to(DOWN*2.4+RIGHT*1.8)
		square2_1=Square(side_length=1,color=RED,fill_color=RED,fill_opacity=0.3)
		#mulx2=TexMobject("\\times 2",color=YELLOW).next_to(square2,RIGHT,buff=0.05).scale(0.8)
		self.play(ReplacementTransform(sum1[2].copy(),mul2x3))
		self.wait(0.8)
		self.play(ReplacementTransform(mul2x3,mul2x2x2))
		self.wait(0.8)
		self.play(
			ReplacementTransform(mul2x2x2[0],square2),
			ApplyMethod(mul2x2x2[1].shift,RIGHT*0.8)
			)
		self.wait(0.8)
		self.play(ReplacementTransform(mul2x2x2[1],square2_1.next_to(square2,buff=0)))
		self.wait(0.8)
		self.play(ApplyMethod(square2.move_to,DOWN*2+LEFT*5.5),run_time=0.6,lag_ratio=0.1)
		self.play(ApplyMethod(square2_1.move_to,DOWN*2+LEFT*4.5),run_time=0.6,lag_ratio=0.1)
		self.wait(1)
		mul3x3=TexMobject("3^3",color=YELLOW).move_to(DOWN*2.4+RIGHT*2.8).scale(0.8)
		mul3x2x3=TexMobject("3^2","\\times 3",color=YELLOW).move_to(DOWN*2.4+RIGHT*2.8).scale(0.8)
		square3_1=Square(side_length=1.5,color=RED,fill_color=RED,fill_opacity=0.3).move_to(DOWN*2.1+RIGHT*2)
		square3_2=Square(side_length=1.5,color=RED,fill_color=RED,fill_opacity=0.3).next_to(square3_1,RIGHT,buff=0)
		square3_3=Square(side_length=1.5,color=RED,fill_color=RED,fill_opacity=0.3).next_to(square3_2,RIGHT,buff=0)
		gra3=VGroup(square3_2,square3_3)
		self.play(ReplacementTransform(sum1[4].copy(),mul3x3))
		self.wait(0.8)
		self.play(ReplacementTransform(mul3x3,mul3x2x3))
		self.wait(0.8)
		self.play(ReplacementTransform(mul3x2x3[0],square3_1))
		self.wait(0.8)
		self.play(ReplacementTransform(mul3x2x3[1],gra3))
		self.wait(0.8)
		self.play(ApplyMethod(square3_1.move_to,DOWN*0.75+LEFT*5.25),run_time=0.3,lag_ratio=0.1)
		self.play(ApplyMethod(square3_2.move_to,DOWN*0.75+LEFT*3.75),run_time=0.3,lag_ratio=0.1)
		self.play(ApplyMethod(square3_3.move_to,DOWN*0.75+LEFT*2.25),run_time=0.3,lag_ratio=0.1)
		self.wait(1)
		mul4x3=TexMobject("4^3",color=YELLOW).move_to(DOWN*2.4+RIGHT*3.3).scale(0.8)
		mul4x2x4=TexMobject("4^2","\\times 4",color=YELLOW).move_to(DOWN*2.4+RIGHT*3.3).scale(0.8)
		square4_1=Square(side_length=2,color=RED,fill_color=RED,fill_opacity=0.3).move_to(DOWN*1.9+RIGHT*2.2)
		square4_2=Square(side_length=2,color=RED,fill_color=RED,fill_opacity=0.3).next_to(square4_1,buff=0)
		square4_3=Square(side_length=2,color=RED,fill_color=RED,fill_opacity=0.3).next_to(square4_2,buff=0)
		square4_4=Square(side_length=2,color=RED,fill_color=RED,fill_opacity=0.3).next_to(square4_3,buff=0)
		gra4=VGroup(square4_2,square4_3,square4_4)
		gra4_1=VGroup(gra4,square4_1)
		self.play(ReplacementTransform(sum1[6].copy(),mul4x3))
		self.wait(0.8)
		self.play(ReplacementTransform(mul4x3,mul4x2x4))
		self.wait(0.8)
		self.play(ReplacementTransform(mul4x2x4[0],square4_1))
		self.wait(0.8)
		self.play(ReplacementTransform(mul4x2x4[1],gra4))
		self.play(ApplyMethod(gra4_1.move_to,UP*2.5))
		self.wait(0.8)
		self.play(ApplyMethod(gra4_1.move_to,UP*1+LEFT*2))
		self.wait(1)
		line=Line(np.array([-6,-3,0]),np.array([18,9,0]),color=PINK)
		self.play(ShowCreation(line))
		tria1_1=Polygon(np.array([-6,-3,0]),np.array([-5.5,-3,0]),np.array([-5.5,-2.75,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria1_2=Polygon(np.array([-5,-2.5,0]),np.array([-5.5,-2.5,0]),np.array([-5.5,-2.75,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria2_1=Polygon(np.array([-5,-2.5,0]),np.array([-4,-2.5,0]),np.array([-4,-2,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria2_2=Polygon(np.array([-4,-2,0]),np.array([-4,-1.5,0]),np.array([-3,-1.5,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria3_1=Polygon(np.array([-3,-1.5,0]),np.array([-1.5,-0.75,0]),np.array([-1.5,-1.5,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria3_2=Polygon(np.array([-1.5,-0.75,0]),np.array([-1.5,0,0]),np.array([0,0,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria4_1=Polygon(np.array([0,0,0]),np.array([2,0,0]),np.array([2,1,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		tria4_2=Polygon(np.array([2,1,0]),np.array([2,2,0]),np.array([4,2,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		triangle=VGroup(tria1_1,tria1_2,tria2_1,tria2_2,tria3_1,tria3_2,tria4_1,tria4_2)
		self.play(ShowCreation(triangle))
		textreminder2=TextMobject("我们可以发现这些标出的三角形面积分别对应相等",color=YELLOW).move_to(DOWN*2.5+RIGHT*1.3).scale(0.8)
		self.play(Write(textreminder2))
		self.play(Uncreate(triangle))
		bigtriangle=Polygon(np.array([-6,-3,0]),np.array([-6,2,0]),np.array([4,2,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		textreminder3=TextMobject("因此所有红色正方形面积之和等于黄色大三角形面积之和",color=YELLOW).move_to(DOWN*2.5+RIGHT*1.3).scale(0.8)
		self.play(
			ReplacementTransform(textreminder2,textreminder3),
			ShowCreation(bigtriangle)
		)
		self.wait(1)
		brace1=Brace(bigtriangle,LEFT)
		text1=TexMobject("\\sum_{i=0}^{4}{i}").next_to(brace1,LEFT,buff=-0.2).scale(0.6)
		self.play(ShowCreation(brace1),Write(text1))
		brace2=Brace(bigtriangle,UP)
		text2=TexMobject("4 \\times 5").next_to(brace2,UP,buff=0)
		self.play(ShowCreation(brace2),Write(text2))
		self.wait(1)
		text3=TexMobject("\\sum_{i=0}^{4}{i^3}=\\frac{(1+2+3+4)\\times4\\times5}{2}=100",color=YELLOW).move_to(DOWN*1.2+RIGHT*2.5).scale(0.8)
		self.play(Write(text3))
		self.wait(1)

class lifanghe2(Scene):
	def construct(self):
		text1=TextMobject("什么?没有找到明显的规律?")
		self.play(Write(text1))
		self.wait(1)
		self.play(FadeOutAndShiftDown(text1))
		net_plate=VGroup()
		for l in range(6):
			line_y_l_u = Line(np.array([-10, l + 0.5, 0]), np.array([10, l + 0.5, 0]), color=BLUE, stroke_width=0.2)
			line_y_l_d = Line(np.array([-10, -l-0.5, 0]), np.array([10, -l-0.5, 0]), color=BLUE, stroke_width=0.2)
			net_plate.add(line_y_l_u,line_y_l_d)
		for k in range(10):
			line_x_k_l=Line(np.array([k+0.5,-8,0]),np.array([k+0.5,8,0]),color=BLUE,stroke_width=0.2)
			line_x_k_r = Line(np.array([-k-0.5, -8, 0]), np.array([-k-0.5, 8, 0]), color=BLUE, stroke_width=0.2)
			net_plate.add(line_x_k_l, line_x_k_r)
		for j in range(6):
			line_y_j_u=Line(np.array([-10,j+1,0]),np.array([10,j+1,0]),color=BLUE,stroke_width=0.6)
			line_y_j_d = Line(np.array([-10, -j, 0]), np.array([10, -j, 0]), color=BLUE, stroke_width=0.6)
			net_plate.add(line_y_j_u,line_y_j_d)
		for i in range(10):
			line_x_i_l=Line(np.array([i+1,-8,0]),np.array([i+1,8,0]),color=BLUE,stroke_width=0.6)
			line_x_i_r=Line(np.array([-i,-8,0]),np.array([-i,8,0]),color=BLUE,stroke_width=0.6)
			net_plate.add(line_x_i_l,line_x_i_r)
		line_xx=Line(np.array([-10,-3,0]),np.array([12,-3,0]),color=WHITE,stroke_width=1)
		line_yy=Line(np.array([-6,-8,0]),np.array([-6,9,0]),color=WHITE,stroke_width=1)
		net_plate.add(line_xx,line_yy)
		text2=TextMobject("我们不妨把视野放到n阶").move_to(DOWN*3.5+RIGHT*4)
		self.play(ShowCreation(net_plate),Write(text2),run_time=3,lag_ratio=0.02)
		line=Line(np.array([-6,-3,0]),np.array([14,7,0]),color=PINK)
		self.play(ShowCreation(line))
		text3=TextMobject("根据上一段视频").move_to(DOWN*3.5+RIGHT*4)
		self.play(ReplacementTransform(text2,text3))
		self.wait(0.5)
		text4=TextMobject("我们发现所有正方形面积之和等于这样一个三角形的面积").move_to(DOWN*3.5).scale(0.7)
		bigtriangle=Polygon(np.array([-6,-3,0]),np.array([-6,2,0]),np.array([4,2,0]),color=YELLOW,fill_color=YELLOW,fill_opacity=0.3)
		self.play(ReplacementTransform(text3,text4),ShowCreation(bigtriangle))
		self.wait(0.6)
		brace1=Brace(bigtriangle,LEFT)
		tex1=TexMobject("\\sum_{i=1}^{n}{i}").scale(0.6).next_to(brace1,LEFT,buff=0)
		brace2=Brace(bigtriangle,UP)
		tex2=TexMobject("n(n+1)").next_to(brace2,UP)
		self.play(ShowCreation(brace1),Write(tex1))
		self.play(ShowCreation(brace2),Write(tex2))
		self.wait(0.8)
		text5=TextMobject("同时我们发现,这个三角形的两直角边长度可以轻松计算出来").move_to(DOWN*3.5).scale(0.7)
		self.play(ReplacementTransform(text4,text5))
		self.wait(1.3)
		text6=TextMobject("因此,我们由三角形面积公式,可以得到以上式子").move_to(DOWN*3.5).scale(0.7)
		self.play(ReplacementTransform(text5,text6))
		self.wait(0.8)
		self.play(FadeOut(text6))
		tex3=TexMobject("\\sum_{i=1}^{n}{i^3}=","\\frac{1}{2}{(1+2+3+...+n) \\times n(n+1)}").move_to(DOWN*2.2+RIGHT*2)
		self.play(Write(tex3))
		self.wait(0.8)
		tex4=TexMobject("\\frac{1}{4}{[n(n+1)]^2}").next_to(tex3[0])
		self.play(ReplacementTransform(tex3[1],tex4))
		self.wait(1.5)
		tex5=TexMobject("\\sum_{i=1}^{n}{i^3}=\\frac{1}{4}{[n(n+1)]^2}").move_to(DOWN*0.6)
		text7=TextMobject("这就是立方和公式的一种推导方式").move_to(UP*0.6)
		self.play(FadeOut(net_plate),FadeOut(bigtriangle),FadeOut(brace1),FadeOut(brace2),FadeOut(tex1),FadeOut(tex2),FadeOut(line),FadeOutAndShift(tex3[0],UP),FadeOutAndShift(tex4,UP),FadeInFromDown(tex5))
		self.play(Write(text7))
		self.wait(2)
		self.play(FadeOut(tex5),FadeOut(text7))
		self.wait(0.7)

class dec(Scene):
	CONFIG={"theta":PI/3,"line_size":1.5,"radius":0.7,"increment_theta":PI/3}
	def construct(self):
		theta1=ValueTracker(self.theta)
		line1=Line(ORIGIN,RIGHT*self.line_size,color=YELLOW)
		line2=Line(ORIGIN,RIGHT*self.line_size,color=YELLOW)
		line2.rotate(theta1.get_value(),about_point=ORIGIN)
		line2.add_updater(lambda m:m.set_angle(theta1.get_value()))
		arc1=Arc(radius=self.radius,start_angle=line1.get_angle(),angle=line2.get_angle(),color=RED)
		decimal1=DecimalNumber(60, number_decimal_place=3,unit="^{\\circ}")
		decimal1.add_updater(lambda b:b.next_to(arc1,UP))
		decimal1.add_updater(lambda b:b.set_value(theta1.get_value()/PI*180))
		self.play(*[ShowCreation(obj) for obj in [line1,line2,arc1,decimal1]])
		arc1.add_updater(lambda m:m.become(Arc(
			radius=self.radius,color=RED,start_angle=line1.get_angle(),angle=line2.get_angle())))
		cos_val=DecimalNumber(0,number_decimal_place=3,include_sign=True).to_edge(RIGHT,buff=0.8)
		sin_val=DecimalNumber(0,number_decimal_place=3,include_sign=True).next_to(cos_val,DOWN)
		cos_val.add_updater(lambda a:a.set_value(np.cos(theta1.get_value())))
		sin_val.add_updater(lambda a:a.set_value(np.sin(theta1.get_value())))
		self.play(Write(cos_val),Write(sin_val))
		self.add(arc1,decimal1,cos_val,sin_val)
		self.wait(0.4)
		self.play(theta1.increment_value,self.increment_theta)
		for i in range(1,5):
			self.wait(0.6)
			self.play(theta1.increment_value, self.increment_theta)
		self.wait()