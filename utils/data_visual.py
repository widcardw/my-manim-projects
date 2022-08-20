from manimlib import *


class Bar(VGroup):
    def __init__(self, data_tuple: tuple[str, float], axes: Axes, **kwargs):
        super().__init__(**kwargs)
        label_width = axes.x_axis.n2p(data_tuple[1])[0] - axes.x_axis.n2p(0)[0]
        label_height = axes.y_axis.x_step * axes.label_config["height_ratio"]
        text_label = Text(data_tuple[0], font=axes.label_config["font"])
        text_label.set_height(label_height)
        rect_bar = Rectangle(width=label_width, height=label_height, **kwargs)
        self.add(rect_bar, text_label)
        self.bar_key = data_tuple[0]
        self.bar_data = data_tuple[1]
        self.bar_axes = axes

    def position_bar(self, pos: Sequence[float]):
        self[0].move_to(pos, aligned_edge=LEFT)
        self[1].next_to(self[0], RIGHT)
        return self

    def position_by_order(self, order: int):
        self.position_bar(self.bar_axes.c2p(
            0, self.bar_axes.y_axis.x_max - order - 0.5))
        return self

    def reset_data(self, data: float):
        self.bar_data = data
        label_width = self.bar_axes.x_axis.n2p(
            data)[0] - self.bar_axes.x_axis.n2p(0)[0]
        self[0].set_width(label_width, stretch=True)
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

    def get_one_bar(self, data_tuple: tuple[str, float], order: int, **kwargs) -> Bar:
        bar = Bar(data_tuple, self, **kwargs)
        bar.position_bar(self.c2p(0, self.y_axis.x_max - order - 0.5))
        return bar

    def get_bars_within_range(self, data: dict[str, float], color_map: dict[str, ManimColor] = None) -> VGroup:
        # buffer_range = min(int(self.y_axis.x_max * 1.5), len(data))
        # step_sequence = sorted(data.items(), key=lambda x: x[1], reverse=True)[
        #     :buffer_range]
        bars = VGroup()
        order = 0
        sdata = sorted(data.items(), key=lambda x: x[1], reverse=True)
        for it in data.items():
            color = None
            if color_map is None:
                color = random_color()
            else:
                color = color_map[it[0]]
            order = sdata.index(it)
            bar = self.get_one_bar(it, order, color=color,
                                   stroke_width=self.rect_config["stroke_width"], 
                                   fill_opacity=self.rect_config["fill_opacity"])
            if order >= self.y_axis.x_max:
                bar.set_fill(opacity=0)
            bars.add(bar)
            order += 1
        return bars

    def update_data(self, bars: Iterable[Bar], data: dict[str, float]):
        sdata = sorted(data.items(), key=lambda x: x[1], reverse=True)
        new_bars = bars.copy()
        for bar in new_bars:
            bar.reset_data(data[bar.bar_key])
            order = sdata.index((bar.bar_key, bar.bar_data))
            bar.position_by_order(order)
            bar.set_opacity(1)
            if order >= self.y_axis.x_max:
                bar.set_fill(opacity=0)
        return new_bars


class TestBarAxes(Scene):
    def construct(self) -> None:
        data = {
            "a": 2, "b": 3, "f": 1, "g": 5, "o": 6, "p": 9, "q": 7
        }
        color_map = {
            "a": RED_A, "b": RED_B, "f": RED_C, "g": RED_D, "o": RED_E, "p": GOLD_B, "q": GOLD_C
        }
        axes = BarAxes(x_range=[-1, 10, 1], y_range=[-1, 5, 1])
        bars = axes.get_bars_within_range(data, color_map)
        self.add(axes, bars)
        data = {
            "a": 5, "b": 4, "f": 6, "g": 8, "o": 5, "p": 4, "q": 6
        }
        self.wait()
        new_bars = axes.update_data(bars, data)
        self.play(*[Transform(b, n) for (b, n) in zip(bars, new_bars)])
        self.wait()
