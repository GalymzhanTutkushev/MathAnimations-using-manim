from manimlib import *

class slide2(Scene):

    def construct(self):
        s = Tex("Ax+By=C")
        s1 = Tex("y=-\frac{A}{B}\cdot x+\frac{C}{B}")
        s2 = Tex("x=-\frac{B}{A}\cdot y+\frac{C}{A}")

class slide4(Scene):

    def construct(self):
         
        # s2 = Tex("\\left\{\\begin{array}{ll} y = f_1(x)\\;,\\y = f_2(x)\\;,\\end{array}\\right.")
        

        axes = Axes((-6, 6), (-3, 6))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * x**2,
            color=BLUE,
        )
       
        relu_graph = axes.get_graph(
            lambda x: 2 * x,
            color=YELLOW,
        )
        
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ShowCreation( relu_graph),
            # FadeTransform(sin_label, relu_label),
        )
        self.wait()
       
        parabola = axes.get_graph(lambda x: 2 * x**2)
        parabola.set_stroke(BLUE)
        

       
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(1, sin_graph))
        self.play(FadeIn(dot, scale=0.5))
        dot0 = Dot(color=RED)
        dot0.move_to(axes.i2gp(0, sin_graph))
        self.play(FadeIn(dot0, scale=0.5))
        
        self.wait()




class slide5(Scene):

    def construct(self):
         
        # s2 = Tex("\\left\{\\begin{array}{ll} y = f_1(x)\\;,\\y = f_2(x)\\;,\\end{array}\\right.")
        

        axes = Axes((-6, 6), (-3, 6))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * x**2+1.5,
            color=BLUE,
        )
       
        relu_graph = axes.get_graph(
            lambda x: 2 * x,
            color=YELLOW,
        )
        
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ShowCreation( relu_graph),
            # FadeTransform(sin_label, relu_label),
        )
        self.wait()
       
        parabola = axes.get_graph(lambda x: 2 * x**2)
        parabola.set_stroke(BLUE)
        

       
        # dot = Dot(color=RED)
        # dot.move_to(axes.i2gp(1, sin_graph))
        # self.play(FadeIn(dot, scale=0.5))
        # dot0 = Dot(color=RED)
        # dot0.move_to(axes.i2gp(0, sin_graph))
        # self.play(FadeIn(dot0, scale=0.5))
        
        self.wait(pause_time)



class slide6(Scene):

    def construct(self):
         
        # s2 = Tex("\\left\{\\begin{array}{ll} y = f_1(x)\\;,\\y = f_2(x)\\;,\\end{array}\\right.")
        

        axes = Axes((-6, 6), (-3, 6))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: x+1,
            color=BLUE,
        )
       
        relu_graph = axes.get_graph(
            lambda x: 2 * x,
            color=YELLOW,
        )
        parabola = axes.get_graph(lambda x: 2*x+1)
        parabola.set_stroke(BLUE)
        
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ShowCreation( relu_graph),
            # FadeTransform(sin_label, relu_label),
        )
        self.wait()
       
        
        

       
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(1, sin_graph))
        self.play(FadeIn(dot, scale=0.5))
        # dot0 = Dot(color=RED)
        # dot0.move_to(axes.i2gp(0, sin_graph))
        # self.play(FadeIn(dot0, scale=0.5))
        
        self.wait(pause_time)
        self.play(
            Transform(sin_graph,parabola),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(pause_time)


            
class slide9(Scene):

    def construct(self):

        s = Tex("\\left\\{\\begin{array}{ll} y=-\\frac{A}{B}\\cdot x+\\frac{C}{B}\\;,\\Dx+Ey=F\\;.\\end{array}\\right.")
        s.to_edge(UP)
        self.play(Write(s))