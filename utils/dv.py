from manimlib import *


class Bar(VGroup):
    def __init__(self, label: str, data: float, axes: Axes, **kwargs):
        super().__init(**kwargs)
        rect_width = axes.x_axis.n2p(data)[0] - axes.x_axis.n2p(0)[0]
        rect_height = axes.y_axis.x_step * axes.label_config["height_ratio"]
        text_label = Text(label, font=axes.label_config["font"])
        text_label.set_height(rect_height)
        rect_bar = Rectangle(width=rect_width, height=rect_height, **kwargs)
        self.add(rect_bar, text_label)
        self.bar = dict()
        self.bar["label"] = label
        self.bar["data"] = data
        self.bar["axes"] = axes

    def position_bar(self, pos: Sequence[float]):
        self[0].move_to(pos, aligned_edge=LEFT)
        self[1].next_to(self[0], RIGHT)
        return self

    def position_by_order(self, order: int):
        self.position_bar(self.bar["axes"].c2p(
            0, self.bar["axes"].y_axis.x_max - order - 0.5))
        return self

    def reset_data(self, data: float):
        self.bar["data"] = data
        rect_width = self.bar["axes"].x_axis.n2p(
            data)[0] - self.bar["axes"].x_axis.n2p(0)[0]
        self[0].set_width(rect_width, stretch=True)
        return self


class BarAxes(Axes):
    CONFIG = {
        "label_config": {
            "font": "Huiwen-mincho",
            "color": WHITE,
            "height_ratio": 0.7
        },
        "rect_config": {
            "stroke_width": 0,
            "fill_opacity": 1,
        }
    }

    def get_one_bar(self, label: str, data: float, order: int, **kwargs) -> Bar:
        bar = Bar(label, data, self, **kwargs)
        bar.position_by_order(order)
        return bar

    def get_bars(self, labels: Sequence[str], data: Sequence[float], color_map: Sequence[ManimColor] = None) -> VGroup:
        bars = VGroup()
        order = 0
        sorted_data = sorted(zip(labels, data),
                             key=lambda x: x[1], reverse=True)
        for label, d in zip(labels, data):
            order = sorted_data.index((label, d))
            bar = self.get_one_bar(label, d, order, color=color_map[order],
                                   stroke_width=self.rect_config["stroke_width"],
                                   fill_opacity=self.rect_config["fill_opacity"])
            if order >= self.y_axis.x_max:
                bar.set_fill(opacity=0)
            bars.add(bar)
        return bars
