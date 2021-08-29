from manimlib import *
import numpy as np

class slide2(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            # The axes will be stretched so as to match the specified
            # height and width
            height=7,
            width=7,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": BLACK,
                "stroke_width": 2,
            },
            
            y_axis_config={
                "include_tip": True,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=0,
        )
        self.play(ShowCreation(axes),run_time=5)
        self.wait(3)




class slide3(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            height=7,
            width=10,
           
            axis_config={
                "stroke_color": BLACK,
                "stroke_width": 2,
            },

        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=0,
        )
        self.add(axes)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 1)))
        self.wait()
        
        # Similarly, you can call axes.point_to_coords, or axes.p2c
        # print(axes.p2c(dot.get_center()))

        # We can draw lines from the axes to better mark the coordinates
        # of a given point.
        # Here, the always_redraw command means that on each new frame
        # the lines will be redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # If we tie the dot to a particular set of coordinates, notice
        # that as we move the axes around it respects the coordinate
        # system defined by them.
        f_always(dot.move_to, lambda: axes.c2p(1, 1))

        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))
        self.wait(3)
        # Other coordinate systems you can play around with include
        # ThreeDAxes, NumberPlane, and ComplexPlane.

