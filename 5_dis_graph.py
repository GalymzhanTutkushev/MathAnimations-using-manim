from manimlib import *

class trigon(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # тригонометрические функции
        sin_graph = axes.get_graph(
            lambda x: math.sin(x),
            color=BLUE,
        )
        cos_graph = axes.get_graph(
            lambda x: math.cos(x),
            color=BLUE,
        )
        tg_graph = axes.get_graph(
            lambda x:  math.tan(x),
            color=BLUE,
        )
        ctg_graph = axes.get_graph(
            lambda x: 1 /math.tan(x),
            color=BLUE,
        )

        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        cos_label = axes.get_graph_label(sin_graph, "\\cos(x)")
        tg_label = axes.get_graph_label(tg_graph, "tg(x)")
        ctg_label = axes.get_graph_label(ctg_graph, "ctg(x)")
        
        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(sin_graph),FadeOut(sin_label))

        self.play(
            ShowCreation(cos_graph),
            FadeIn(cos_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(cos_graph),FadeOut(cos_label))

        self.play(
            ShowCreation(tg_graph),
            FadeIn(tg_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(tg_graph),FadeOut(tg_label))

        self.play(
            ShowCreation(ctg_graph),
            FadeIn(ctg_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(ctg_graph),FadeOut(ctg_label))
       
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            
            ShowCreation(parabola)
        )
        self.wait()
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
        self.wait(pause_time)



class exponenta(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        
        exp_graph = axes.get_graph(
            lambda x: math.exp(x),
            color=BLUE,
        )
        
        
        exp_label = axes.get_graph_label(exp_graph, "\\exp(x)")
        
        self.play(
            ShowCreation(exp_graph),
            FadeIn(exp_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(exp_graph),FadeOut(exp_label))
        self.wait(pause_time)
        


class logarifm(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        
        log_graph = axes.get_graph(
            lambda x: np.log(x),
            color=BLUE,
        )
        
        log_label = axes.get_graph_label(log_graph, "\\ln(x)")
        
        self.play(
            ShowCreation(log_graph),
            FadeIn(log_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(log_graph),FadeOut(log_label))
        self.wait(pause_time)





class polynom(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

         
        polynom_graph = axes.get_graph(
            lambda x:  x**3+x**2+x+1,
            color=BLUE,
        )

        polynom_label = axes.get_graph_label(polynom_graph, "\\x^3+x^2+x+1")

        self.play(
            ShowCreation(polynom_graph),
            FadeIn(polynom_label, RIGHT),
        )
        self.wait(2)
        self.play(FadeOut(polynom_graph),FadeOut(polynom_label))

        self.wait(pause_time)
