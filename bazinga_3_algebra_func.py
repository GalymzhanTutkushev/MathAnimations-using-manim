from manimlib import *


class slide1(Scene):
   
    def construct(self):
        x = 3
        y = x+3
        t = Tex("f(x) = x+3")
        t.to_edge(UP)
        box  = RoundedRectangle(width= 4,height = 3)
        box.set_fill(TEAL_E,0.6)
        self.play(ShowCreation(box))
        in1 = Tex(str(x)).next_to(box,LEFT,buff = 2)
        out1 = Tex(str(y)).next_to(box,RIGHT,buff = 1)
        in_arr = Arrow(4*LEFT,3*LEFT)
        out_arr = Arrow(2*RIGHT,3*RIGHT)
        self.play(Write(in1))
        self.play(Write(in_arr))
        self.play(in_arr.animate.shift(RIGHT),in1.animate.shift(RIGHT))
        self.play(Write(out_arr))
        self.play(Write(out1))

        self.play(Write(t))
        self.wait(pause_time)

class slide5(Scene):
    def construct(self):

        axes = Axes((-5, 6), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: x**2 +2,
            color=BLUE,
        )
        

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        # sin_label = axes.get_graph_label(sin_graph, "$$\\y=x^2+2$$")
       

        f = Tex("y = x^2+2")
        f.to_edge(UP)
        self.play(Write(f))

        parabola = axes.get_graph(lambda x: x**2+2)
        parabola.set_stroke(BLUE)


        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)



class slide9(Scene):
    def construct(self):

        axes = Axes((-5, 6), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: x,
            color=BLUE,
        )
        

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        # sin_label = axes.get_graph_label(sin_graph, "$$\\y=x^2+2$$")
       

        f = Tex("y = a\\cdot x")
        f.to_edge(UP)
        self.play(Write(f))

        parabola = axes.get_graph(lambda x: x)
        parabola.set_stroke(BLUE)


        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)




class slide9(Scene):
    def construct(self):

        axes = Axes((-5, 6), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: x,
            color=BLUE,
        )
        

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        # sin_label = axes.get_graph_label(sin_graph, "$$\\y=x^2+2$$")
       

        f = Tex("y = b")
        f.to_edge(UP)
        self.play(Write(f))
        b = 4
        parabola = axes.get_graph(lambda x: b)
        parabola.set_stroke(BLUE)


        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)



class slide11(Scene):
    def construct(self):

        axes = Axes((-5, 6), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

       
        sin_graph = axes.get_graph(
            lambda x: x,
            color=BLUE,
        )
    
        f = Tex("y = ax+b")
        f0 = Tex("ax+b=0")
        f.to_edge(UP)
        self.play(Write(f))
        b = 4
        parabola = axes.get_graph(lambda x: b)
        parabola.set_stroke(BLUE)


        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)

class slide12(Scene):
    def construct(self):

        axes = Axes((-5, 6), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

       
        sin_graph = axes.get_graph(
            lambda x: x,
            color=BLUE,
        )
    
        f = Tex("y = kx +b")
        abc = Tex("Ax+Bx=C")
        k = Tex("k = \\frac{-A}{B}")
        b =Tex("b = \\frac{C}{B}")
        f.to_edge(UP)
        self.play(Write(f))
        b = 4
        parabola = axes.get_graph(lambda x: b)
        parabola.set_stroke(BLUE)


        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
