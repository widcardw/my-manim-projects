from manimlib import *


class PhoneCallScene(Scene):
    def init_script(self, script: list):
        self.script = script
        # self.text_vgroup = VGroup(Dot())
        # for sc in script:
        #     tx = Text(sc, font=self.font).scale(2 + np.random.random())
        #
        #     self.text_vgroup.add(tx)

    def init_font(self, font, weight="MEDIUM"):
        self.font = font
        self.weight = weight
        self.angle = 0
        self.cur_rotate = 0
        self.rotate_prob = 0.5

    def construct(self):
        frame = self.camera.frame
        self.text_vgroup = VGroup(Dot(UP))
        for sc in self.script:
            rand = np.random.random(5)
            tx = Text(
                sc, font=self.font, weight=self.weight
            ).set_width((2 + rand[0]) * 3)
            if sc.__len__() > 10:
                tx.set_width(10 + rand[1])
            if rand[4] > self.rotate_prob:
                if self.angle == 0:
                    self.angle = PI / 2
                    self.cur_rotate = PI / 2
                elif abs(self.angle - PI / 2) <= 0.1:
                    self.angle = 0
                    # tx.rotate(-PI / 2)
                    self.cur_rotate = -PI / 2
            else:
                self.cur_rotate = 0
            tx.rotate(self.angle)
            tx.next_to(
                self.text_vgroup[-1],
                np.dot(DOWN, rotation_about_z(-self.angle)),
                aligned_edge=np.dot(
                    ORIGIN if rand[2] > 0.8 and rand[4] < self.rotate_prob else LEFT,
                    rotation_about_z(-self.angle)
                ),
                # buff=0
            )
            tx.set_color(Color(hsl=(rand[3], 0.4, 0.5)))
            tx.add_background_rectangle(opacity=0.75)
            # print("angle=", self.angle)
            # print("cur=", self.cur_rotate)
            self.play(
                GrowFromPoint(tx, tx.get_top()),
                frame.animate
                    .rotate(self.cur_rotate)
                    .set_width(max(tx.get_width(), tx.get_height()) * 1.5)
                    .move_to(tx.get_center())
            )
            self.text_vgroup.add(tx)
            self.wait()


class Scene1(PhoneCallScene):
    def construct(self):
        text = []
        with open("my_videos/videos/script.txt", encoding="utf-8") as fin:
            for line in fin:
                text.append(line)
        # print(text)
        self.init_font("serif")
        self.init_script(text)
        super().construct()
