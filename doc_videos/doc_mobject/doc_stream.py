from manimlib import *


def get_vector_field_and_stream_lines(func, coordinate_system,
                                      magnitude_range=(0.5, 4),
                                      vector_opacity=0.75,
                                      vector_thickness=0.03,
                                      color_by_magnitude=False,
                                      line_color=GREY_A,
                                      line_width=3,
                                      line_opacity=0.75,
                                      sample_freq=5,
                                      n_samples_per_line=10,
                                      arc_len=3,
                                      time_width=0.3,
                                      ):
    vector_field = VectorField(
        func, coordinate_system,
        magnitude_range=magnitude_range,
        vector_config={
            "fill_opacity": vector_opacity,
            "thickness": vector_thickness,
        }
    )

    stream_lines = StreamLines(
        func, coordinate_system,
        step_multiple=1.0 / sample_freq,
        n_samples_per_line=n_samples_per_line,
        arc_len=arc_len,
        magnitude_range=magnitude_range,
        color_by_magnitude=color_by_magnitude,
        stroke_color=line_color,
        stroke_width=line_width,
        stroke_opacity=line_opacity,
    )
    animated_lines = AnimatedStreamLines(
        stream_lines,
        line_anim_config={
            "time_width": time_width,
        },
    )

    return vector_field, animated_lines


class FuncFlow(Scene):
    CONFIG = {
        "field_config": {
            "color_by_magnitude": True,
            "magnitude_range": (0.5, 9),
            "arc_len": 3,
        },
        "plane_config": {
            "x_range": [-8, 8],
            "y_range": [-4, 4],
            "height": 8,
            "width": 16,
        },
        "label_height": 3,
        "run_time": 5,
        "slow_factor": 0.25,
    }

    def construct(self):
        mr = np.array(self.field_config["magnitude_range"])

        self.field_config["magnitude_range"] = self.slow_factor * mr

        plane = NumberPlane(**self.plane_config)
        plane.add_coordinate_labels()

        vector_field, animated_lines = get_vector_field_and_stream_lines(
            self.func, plane,
            **self.field_config,
        )

        func_label = Tex("\\begin{cases} \
            x = x + y \\\\ \
            y = x - y \
            \\end{cases}")
        func_label.to_corner(UR)
        func_label.set_stroke(BLACK, 5, background=True)

        self.add(plane)
        self.add(vector_field)
        self.add(animated_lines)
        self.add(func_label)
        self.wait(self.run_time)

    def func(self, x, y):
        return self.slow_factor * np.array([x + y, x - y])
