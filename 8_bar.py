from manimlib import *
from scipy import stats


class seq(Scene):
    def construct(self):
        # арифметическая последовательность
        seq_eq = Tex("S_n = \\frac{a_1+a_n}{2}\\cdot n")
        a_n1 = Tex("a_{n+1} = a_n+d")
        a = Tex("a_n = a_1+ d\\cdot (n-1)")
        # геометрическая последовательность
        seq_eq = Tex("S_n = \\frac{b_1\\cdot (q^n-1)}{q-1}")
        b_n1 = Tex("b_{n+1} = b_n\\cdot q")
        b = Tex("b_n = b_1\\cdot q^{n+1}")


        S = [25, 32, 24 ,32, 16, 18, 19]
        avr = np.mean(S)
        med = np.median(S)
        minim = np.min(S)
        maxim = np.max(S)
        raz = maxim-minim
        mod = stats.mode(S)
        print(avr)
        print(med)
        print(minim)
        print(maxim)
        print(raz)
        print(mod[0])
        for i in range(len(S)):
            st = Tex(str(S[i]))
            st.move_to(i*RIGHT)
            self.play(Write(st))


class ShowBarChart(Scene):

    CONFIG ={

    "height":5,

    "width":12,

    "n_ticks":4,

    "tick_width":0.2,

    "label_y_axis":True,

    "y_axis_label_height":0.25,

    "max_value":50,

    "bar_colors":["#704595","#3386a6","#96e4e4","#76df51","#fff033","#febf32","#ff3334"],

    "bar_fill_opacity":0.8,

    "bar_stroke_width":4,

    "bar_names":["Oxygen","Silicon","Iron","Calcium","Aluminum","Magnesium","Other"],

    "bar_label_scale_val":0.5,

    }

    

    def construct(self):

       composition=[41,19.5,11.5,10,8,6,4]

       chart=BarChart(values=composition,**self.CONFIG).scale(0.8)

       text_top=Text("Composition of Lunar Soil").scale(0.9).next_to(

        chart,UP,buff=0.1)

       text_left=Text("Relative Concentration").rotate(

       angle=TAU/4,axis=OUT).scale(0.6).next_to(chart,LEFT,buff=0.5)

       

       self.play(Write(chart),Write(text_top),Write(text_left),run_time=10)    

       self.wait(3)




class Derivative(Scene):
    CONFIG = {
        "x_start": 3,
        "x_end": 7,
        "axes_config": {
            "center_point": [-4.5,-2.5,0],
            "x_axis_config": {
                "x_min": -1,
                "x_max": 10,
                "include_numbers": True
            },
            "y_axis_config": {
                "label_direction": LEFT,
                "x_min": -1,
                "x_max": 6,
                "include_numbers": True
            },
        },
        "func": lambda x: 0.1 * (x - 2) * (x - 8) * (x - 5) + 3,
        "func_config": {
            "color": RED,
            "x_min": 0.8,
            "x_max": 9,
        },
        "dot_radius": 0.1,
        "line_config": {}
    }
    def construct(self):
        axes = self.get_axes()
        func = self.get_graph(self.func,**self.func_config)
        dot_start = self.get_dot_from_x_coord(self.x_start)
        dot_end   = self.get_dot_from_x_coord(self.x_end)
        line = VMobject()
        line.add_updater(self.get_line_updater(dot_start,dot_end))
        # self.add(axes,func,dot_start,dot_end,line)
        self.play(
            Write(axes),
            ShowCreation(func),
            *list(map(GrowFromCenter,[dot_start,dot_end]))
        )
        self.play(ShowCreation(line))
        self.wait()
        self.move_dot(dot_end, self.x_end, self.x_start + 0.0001, run_time=8)
        line.clear_updaters()
        self.remove(dot_end)
        line.add_updater(self.get_derivative_updater(dot_start))
        self.add(line)
        self.wait()
        self.move_dot(
            dot_start,
            self.x_start, 8,
            run_time=18,
            rate_func=there_and_back
        )
        self.wait(3)

    def get_axes(self):
        self.axes = Axes(**self.axes_config)
        # FIX Y LABELS
        y_labels = self.axes.get_y_axis().numbers
        for label in y_labels:
            label.rotate(-PI/2)
        return self.axes

    def get_graph(self,func,**kwargs):
        return self.axes.get_graph(
                                    func,
                                    **kwargs
                                )

    def get_f(self,x_coord):
        return self.axes.c2p(x_coord, self.func(x_coord))

    def get_dot_from_x_coord(self,x_coord,**kwargs):
        return Dot(
            self.get_f(x_coord),
            radius=self.dot_radius,
            **kwargs
        )

    def get_dot_updater(self, start, end):
        def updater(mob,alpha):
            x = interpolate(start, end, alpha)
            coord = self.get_f(x)
            mob.move_to(coord)
        return updater

    def get_line_across_points(self,d1,d2,buff):
        reference_line = Line(d1.get_center(),d2.get_center())
        vector = reference_line.get_unit_vector()
        return Line(
            d1.get_center() - vector * buff,
            d2.get_center() + vector * buff,
            **self.line_config
        )

    def get_line_updater(self,d1,d2,buff=3,**kwargs):
        def updater(mob):
            mob.become(
                self.get_line_across_points(d1,d2,buff)
            )
        return updater

    def move_dot(self,dot,start,end,*args,**kwargs):
        self.play(
            UpdateFromAlphaFunc(
                dot, self.get_dot_updater(start,end),
                *args,
                **kwargs
            )
        )

    def get_derivative_updater(self, dot, length=6):
        def updater(mob):
            derivative = Line(
                dot.get_center(),
                self.get_dot_from_x_coord(
                    self.axes.p2c(dot.get_center())[0] + 0.0001
                ).get_center(),
                **self.line_config
            )
            derivative.set_length(length)
            derivative.move_to(dot)
            mob.become(derivative)
        return updater

        
class diff(Scene):
    def construct(self):
        axes = Axes(

            x_range=(-5, 6),

            y_range=(-4, 4),

            height=6,
            width=10,

            axis_config={
                # "stroke_color": GREY_A,
                "stroke_width": 2,
            },

            y_axis_config={
                "include_tip": True,
            }
        )

        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

       

        g_graph = axes.get_graph(
            lambda x: 2*np.exp(-x**2/3),
            color=BLUE,
        )
        
        v = axes.get_v_line_to_graph(1,g_graph)
        h = axes.get_h_line_to_graph(1,g_graph)
        r = axes.get_tangent_line(1,g_graph,length=3)
        r2 = axes.get_tangent_line(2,g_graph,length=3)
        r3 = axes.get_tangent_line(3,g_graph,length=3)
        
       
        self.play(
            ShowCreation(h),
            ShowCreation(v),
            ShowCreation(r),
            ShowCreation(g_graph),
        )
        self.wait()
        self.play(ReplacementTransform(r,r2))
        self.wait()
        self.play(ReplacementTransform(r2,r3))
        self.wait(pause_time)
        

class integral(Scene):
    def construct(self):
        axes = Axes(

            x_range=(-5, 6),

            y_range=(-1, 10),

            height=6,
            width=10,

            axis_config={
                # "stroke_color": GREY_A,
                "stroke_width": 2,
            },

            y_axis_config={
                "include_tip": True,
            }
        )

        axes.add_coordinate_labels(
            font_size=14,
            # num_decimal_places=1,
        )
        self.add(axes)

       

        g_graph = axes.get_graph(
            lambda x: 5*np.exp(-x**2/3),
            color=BLUE,
        )
        g_graph1 = axes.get_graph(
            lambda x: 3*np.sin(x),
            color=BLUE,
        )
        g_graph1 = axes.get_graph(
            lambda x: 3*(x),
            color=BLUE,
        )
        g_graph1 = axes.get_graph(
            lambda x: 0.3*x**2,
            color=BLUE,
        )
        r = axes.get_riemann_rectangles(g_graph,[0,3],1)
        r2 =  axes.get_riemann_rectangles(g_graph,[0,3],0.5)
        r3 =  axes.get_riemann_rectangles(g_graph,[0,3],0.1)
        # r4 = VMobject()
        # r4 = axes.get_area_under_graph(g_graph,[0,3])
        self.play(
           
            ShowCreation(r),
            ShowCreation(g_graph),
        )
        self.wait()
        self.play(ReplacementTransform(r,r2))
        self.wait()
        self.play(ReplacementTransform(r2,r3))
        self.wait()
      
        self.wait(pause_time)
        

        
class taylor(Scene):
    def construct(self):
        t = Tex("e^x ="," 1"," + x"," + \\frac{x^2}{2!}"," +\\frac{x^3}{3!}"," +\\frac{x^4}{4!}"," +\\frac{x^5}{5!}"," +\\frac{x^6}{6!}"," +\\frac{x^7}{7!}",)
        t.to_edge(DOWN)
       
        exps=[lambda x: 1, lambda x:1+ x, lambda x:1+x+x**2/2, lambda x:1+x+x**2/2+x**3/6,
        lambda x:1+x+x**2/2+x**3/6+x**4/24,lambda x:1+x+x**2/2+x**3/6+x**4/24+x**5/120,
        lambda x:1+x+x**2/2+x**3/6+x**4/24+x**5/120+x**6/720,
        lambda x:1+x+x**2/2+x**3/6+x**4/24+x**5/120+x**6/720+x**7/(720*7)]
        axes = Axes(

            x_range=(-5, 6),

            y_range=(-1, 8),

            height=6,
            width=10,

            axis_config={
                # "stroke_color": GREY_A,
                "stroke_width": 2,
            },

            y_axis_config={
                "include_tip": True,
            }
        )

        axes.add_coordinate_labels(
            font_size=14,
            # num_decimal_places=1,
        )
        axes.shift(UP)
        self.add(axes)

       

        g_graph = axes.get_graph(
            lambda x: np.exp(x),
            color=GREEN,
        )
        
        self.play(
           
            ShowCreation(g_graph),
        )
        # graph = list(map(axes.get_graph(),exps))
        self.play(Write(t[0]))
        for i in range(len(exps)):
            graph1 = axes.get_graph(
            exps[i],
            color=RED)
        
            self.wait()
            self.play(Write(t[i+1]))
            self.play(ShowCreationThenFadeOut(graph1))
            # self.remove(graph1)
           
        
        self.wait(pause_time)
        

class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-1, 10),
            # y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
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
        self.play(dot.animate.move_to(axes.c2p(5, 0.1)))
        self.wait()
        
        # Similarly, you can call axes.point_to_coords, or axes.p2c
        # print(axes.p2c(dot.get_center()))

        # We can draw lines from the axes to better mark the coordinates
        # of a given point.
        # Here, the always_redraw command means that on each new frame
        # the lines will be redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        g_graph = axes.get_graph(
            lambda x: np.exp(-x**2),
            color=BLUE,
        )
        r = axes.get_riemann_rectangles(g_graph,[0,3],0.1)
        s = axes.get_tangent_line(1,g_graph,)
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
            ShowCreation(r),
            ShowCreation(g_graph),
        )
        self.play(
            
            ShowCreation(s),
           
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()
        
        # If we tie the dot to a particular set of coordinates, notice
        # that as we move the axes around it respects the coordinate
        # system defined by them.
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75),
            axes.animate.to_corner(UL),
            
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # тригонометрические функции
        sin_graph = axes.get_graph(
            lambda x: math.sin(x),
            color=BLUE,
        )
        
        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.wait(2)