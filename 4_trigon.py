from manimlib import *

class vectors(Scene):
    def construct(self):
        v1 = Arrow()
        self.wait(pause_time)


class circle_eq(Scene):
    def construct(self):
        test = Tex("x^2+y^2=R^2")
        test.to_edge(UP)
        
        R=2
        c1 = Circle(radius = R)
        r = Line(ORIGIN,R*LEFT)
        r_label = Tex("R").next_to(r,UP)
        self.play(Write(c1))
        self.play(Write(r),Write(r_label))
        self.play(Write(test))

class ellipse_eq(Scene):
    def construct(self):
        test = Tex("\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1")
        test.to_edge(UP)
        w=8
        h=4
        a = Line(ORIGIN,w/2*RIGHT)
        b = Line(ORIGIN,h/2*UP) 
        a_label = Tex("a").next_to(a,UP)   
        b_label = Tex("b").next_to(a,LEFT)   
        e = Ellipse(width = w,height = h)
        self.play(Write(e))
        self.play(ShowCreation(a),ShowCreation(b))
        self.play(ShowCreation(a_label),ShowCreation(b_label))
        self.play(Write(test))

class Ellipse(ParametricFunction):
    def __init__(self, a, e, **kwargs):
        digest_config(self,kwargs)
        b = np.sqrt( - ( (e ** 2) - 1 ) * ( a ** 2 ) ) 
        super().__init__(
            lambda t: np.array([
                a * np.sin(t),
                b * np.cos(t),
                0
            ]),
            t_min = 0,
            t_max = 2 * PI,
            **kwargs,
        )

def there_and_back_linear(t):
    new_t = 2 * t if t < 0.5 else 2 * (1 - t)
    return linear(new_t)

class EllipseScene(Scene):
    CONFIG = {
        "semi_major_axis": 2,        # a
        "eccentricity": 0,           # e
        "focus_config": {
            "radius": 0.1,
            "color": RED
        },
        "line_config": {
            "color": TEAL
        },
        "number_line_config": {
            "unit_size": 9, 
            "x_min": 0,
            "x_max": 1,
            "include_numbers": True,
            "numbers_to_show": np.arange(0,1.1, 0.1),
            "decimal_number_config": {
                "num_decimal_places": 1
            },
            "tick_frequency": 0.1
        },
        "dot_config": {
            "radius": 0.1,
            "color": YELLOW,
        }
    }

    def construct(self):
        # Ellipse
        a, e = self.semi_major_axis, self.eccentricity
        ellipse = Ellipse(a, e)
        # Focus
        dots = VGroup(*[
            Dot(**self.focus_config) for _ in range(2)
        ])
        # 
        dot = Dot(**self.dot_config)
        # directrix
        lines = VGroup(*[
            DashedLine(
                DOWN * FRAME_Y_RADIUS,
                UP * FRAME_Y_RADIUS,
                **self.line_config
            ) for _ in range(2)
        ])
        # number_line
        number_line = NumberLine(**self.number_line_config)
        number_line.set_x(0)
        number_line.to_edge(DOWN)
        # eccentricity
        eccentricity = TexMobject("\\varepsilon")
        eccentricity.next_to(number_line.n2p(1), RIGHT,buff=0.5)
        # add all mobs to a group
        group = VGroup(ellipse, lines, dots, dot)
        dot.move_to(number_line.n2p(0))
        number_plane = NumberPlane().fade(0.5)
        self.number_line = number_line
        self.play(
            FadeIn(number_plane),
            *list(map(GrowFromCenter, [ellipse, *dots])),
            # This is the same as:
            # GrowFromCenter(ellipse),
            # GrowFromCenter(dots[0]),
            # GrowFromCenter(dots[1])
            *list(map(Write, [number_line, eccentricity])),
            GrowFromCenter(dot)
        )
        self.add(group)
        self.play(
            UpdateFromAlphaFunc(
                group, self.get_ellipse_group(group, a, e, 1),
                run_time=20,
                rate_func=there_and_back_linear
            )
        )
        self.wait()

    def get_ellipse_group(self, mob, a, e_start, e_end):
        def updater_func(mob,alpha):
            ellipse, lines, dots, dot = mob
            e_target = interpolate(e_start, e_end, alpha)
            c_target = e_target * a
            dots[0].set_x(c_target)
            dots[1].set_x(-c_target)
            f_target = a / (e_target + 0.000001)
            lines[0].set_x(f_target)
            lines[1].set_x(-f_target)
            dot.move_to(self.number_line.n2p(e_target))
            ellipse.become(
                Ellipse(
                    a, e_target
                )
            )
        return updater_func

class focus_ellipse(Scene):
    def construct(self):
        w=4
        h=2
        e = Ellipse(width = w*2,height = h*2)
        
        f1 = np.sqrt(w**2-h**2)
        print(f1)
        focus1 = SmallDot([f1,0,0]).set_color(RED)
        focus2 = SmallDot([-f1,0,0]).set_color(RED)
        self.play(ShowCreation(e))
        self.play(ShowCreation(focus1),ShowCreation(focus2))

        X = [x/10 for x in range(-w*10,-21,4)]
     
        y = [np.abs(h*np.sqrt(1-x**2/w**2)) for x in X]
        dots = []
        
        for i,j in zip(X,y):
            dots.append([i,j,0])
        
        Dots = VGroup(*[SmallDot(d) for d in dots])
        self.play(ShowCreation(Dots))
        dots1 = []
        
        for i,j in zip(X,y):
            dots1.append([i,-j,0])
        
        Dots1 = VGroup(*[SmallDot(d) for d in dots1])
        self.play(ShowCreation(Dots1))

        Lines1 =VGroup(*[Line([-f1,0,0],d) for d in dots])
        LinesUP1 =VGroup(*[Line(d,[f1,0,0]) for d in dots])
        Lines2 =VGroup(*[Line([-f1,0,0],d) for d in dots1])
        LinesUP2 =VGroup(*[Line(d,[f1,0,0]) for d in dots1])
        self.play(ShowCreation(Lines1),ShowCreation(Lines2))
        self.play(ShowCreation(LinesUP1),ShowCreation(LinesUP2))

        self.wait(pause_time)
       

class parabola_eq(Scene):
    def construct(self):
            def construct(self):
        axes = Axes((-5, 6), (-5, 6))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        a= 1
        b = 0 
        c = -2
        sin_graph = axes.get_graph(
            lambda x:a*x**2+b*x+c),
            color=BLUE,
        )
        
        sin_label = axes.get_graph_label(sin_graph, "ax^2+bx+c")
        
        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)

class focus_parabola(Scene):
    def construct(self):
        a = 1/2
        b = 0
        c = -2
        p = FunctionGraph(lambda x: a*x**2+b*x+c)
        x0 = -b/(2*a)
        y0 = c-(b**2-1)/(4*a)
        X = [x/10 for x in range(-20,21,4)]
     
        y = [a*x**2+b*x+c for x in X]
        dots = []
        
        for i,j in zip(X,y):
            dots.append([i,j,0])
        
        Dots = VGroup(*[SmallDot(d) for d in dots])
        Lines =VGroup(*[Line([x0,y0,0],d) for d in dots])
        LinesUP =VGroup(*[Line(d,d+10*UP) for d in dots])
        
        print(y)
        print(y0)
        focus = SmallDot([x0,y0,0])
        focus.set_color(RED)
        self.play(ShowCreation(p))
        self.play(ShowCreation(focus))
        self.play(ShowCreation(Dots))
        
        for i in range(len(Lines)):
            self.play(MoveAlongPath(focus.copy(),Lines[i]))
            self.play(MoveAlongPath(focus.copy(),LinesUP[i]))
        

        self.play(Write(Lines))
        self.play(Write(LinesUP))
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
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
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
        self.play(
            axes.animate.scale(0.75),
            axes.animate.to_corner(UL),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

class ParabolaCreation(Scene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "x_axis_width": 12,
        "y_axis_height": 7,
        "graph_origin": 3.5 * DOWN,
        "y_min": 0,
        "y_max": 7,
    }
    def construct(self):
        self.setup_axes()
        self.x_axis.remove(self.x_axis[1])
        self.y_axis.remove(self.y_axis[1])
        self.play(Write(self.axes))

        h = 0; k = 1; p = 1
        parabola_function = lambda x: ((x-h)**2)/(4*p) + k

        parabola_right = self.get_graph(
                parabola_function,
                x_min = 0,
                x_max = 5,
                color = BLUE
            ).set_stroke(None,3)
        

        parabola_left = self.get_graph(
                parabola_function,
                x_min = 0,
                x_max = -5,
                color = BLUE
            ).set_stroke(None,3)
        anim_kwargs = {"run_time":5,"rate_func":linear}
        self.move_dot_path(parabola_right,anim_kwargs)
        self.move_dot_path(parabola_left,anim_kwargs)

    def move_dot_path(self,parabola,anim_kwargs):
        h = 0; k = 1; p = 1
        parabola_copy = parabola.copy()
        focus = Dot(self.coords_to_point(0,2))
        dot_guide = Dot(self.coords_to_point(h,p))
        dot_d = Dot(self.coords_to_point(0,0))
        circle = Circle(radius=1).move_to(self.coords_to_point(h,p))
        line_f_d = DashedLine(focus.get_center(),dot_guide.get_center())
        line_d_d = DashedLine(dot_guide.get_center(),dot_d.get_center())


        group = VGroup(circle,line_f_d,line_d_d,dot_d)

        def update_group(group):
            c,f_d,d_d,d = group
            d.move_to(self.coords_to_point(dot_guide.get_center()[0],0))
            radius = get_norm(focus.get_center() - dot_guide.get_center())
            new_c = Circle(radius = radius)
            new_c.move_to(dot_guide)
            c.become(new_c)
            f_d.become(DashedLine(focus.get_center(),dot_guide.get_center()))
            d_d.become(DashedLine(dot_guide.get_center(),dot_d.get_center()))

        group.add_updater(update_group)

        self.play(*[
            GrowFromCenter(mob) for mob in [circle,line_f_d,line_d_d,dot_guide,dot_d,focus]
            ])
        self.add(
            group,
            focus,
            dot_guide,
            )
        self.wait()
        self.play(
            ShowCreation(parabola),
            MoveAlongPath(dot_guide,parabola_copy),
            **anim_kwargs
            )
        group.clear_updaters()
        self.wait(1.2)
        self.play(FadeOut(VGroup(group,dot_guide,focus)))

class hyperbola_eq(Scene):
    def construct(self):
        axes = Axes((-5, 6), (-5, 6))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        sin_graph = axes.get_graph(
            lambda x:1/x),
            color=BLUE,
        )
        
        sin_label = axes.get_graph_label(sin_graph, "\\frac{1}{x}")
        
        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)

class PointWithTrace(Scene):
    def construct(self):
         # Формулы тригонометрии
        sin_eq = Tex("\sin(\\alpha) = \\frac{a}{c}")
        cos_eq = Tex("\cos(\\alpha) = \\frac{b}{c}")
        tan_eq = Tex("\tg(\\alpha) = \\frac{a}{b}")
        ctn_eq = Tex("ctg(\\alpha) = \\frac{b}{a}")
        main_tr = Tex("\sin^2\\theta + \cos^2\\theta = 1")
        
        sin_eq.to_edge(UP) 
        cos_eq.to_edge(UP) 

        self.play(Write(sin_eq))

        np = NumberPlane()
        self.add(np)
        path = VMobject()
        dot = Dot()
        A = 1.5*RIGHT
        B = 1.5*UP
        dot.shift(A+B)
        lineC=Line(ORIGIN,A+B)
        lineA=Line(ORIGIN,A)
        lineB=Line(A,A+B)
        braceA =Brace(lineA,DOWN,buff = 0.1)
        braceB =Brace(lineB,RIGHT,buff = 0.1)
        # braceC =Brace(lineC,direction=lineC.copy().animate.rotate(PI / 2).get_unit_vector(),buff = 0.1)
        textA = Tex("b")
        textB = Tex("a")
        # textC = braceC.get_tex("c")
        textA.next_to(braceA,DOWN)
        textB.next_to(braceB,RIGHT)
        # textC.next_to(braceC,UP)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, 2*PI, about_point=ORIGIN, run_time=2),
        Rotating(lineC,2*PI, about_point=ORIGIN, run_time=2))
        self.play(ShowCreation(lineB),ShowCreation(lineA))
        self.play(ShowCreation(braceA),ShowCreation(braceB))
        self.play(ShowCreation(textC),ShowCreation(textA),ShowCreation(textB))
        self.play(Transform(sin_eq,cos_eq))
        self.remove(dot)
        self.wait()

class SineCosine_Curve(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()

        self.wait()

    def show_axis(self):
        x_start = np.array([-6,2,0])
        x_end = np.array([3,2,0])

        y_start = np.array([-4,-3,0])
        y_end = np.array([-4,3.5,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_xy_labels()

        self.orgin_point = np.array([-4,2,0])
        self.curve_start = np.array([-3,2,0])

    def add_xy_labels(self):
        x_labels = [
            Tex("\pi"), Tex("2 \pi"),
            Tex("3 \pi"), Tex("4 \pi"),
        ]

        y_labels = [
            Tex("\pi"), Tex("2 \pi"),
            Tex("3 \pi"), Tex("4 \pi"),
        ]

        for i in range(len(x_labels)):  # -2 -1 0 1
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([-2+i,2,0]), DOWN )
            self.add(x_labels[i])

        for i in range(len(y_labels)):  # 1 0 -1 -2
            y_labels[i].scale(0.6)
            y_labels[i].rotate(-PI/2)
            y_labels[i].next_to(np.array([-4, 1-i,0]), LEFT )
            self.add(y_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.orgin_point)

        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        orgin_point = self.orgin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        ### sine
        def get_line_to_sine():
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.sine_curve = VGroup()
        self.sine_curve.add(Line(self.curve_start,self.curve_start))
        def get_sine_curve():
            last_line = self.sine_curve[-1]
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.sine_curve.add(new_line)

            return self.sine_curve

        ### cosine
        def get_line_to_cosine():
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.cosine_curve = VGroup()
        self.cosine_curve.add(Line(self.curve_start, self.curve_start))

        def get_cosine_curve():
            last_line = self.cosine_curve[-1]
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.cosine_curve.add(new_line)

            return self.cosine_curve


        dot.add_updater(go_around_circle) #move dot around the circle

        origin_to_circle_line = always_redraw(get_line_to_circle) # from circle origin to dot

        dot_to_sine_line = always_redraw(get_line_to_sine) # from dot to sine curve
        sine_curve_line = always_redraw(get_sine_curve) # sine curve

        dot_to_cosine_line = always_redraw(get_line_to_cosine)  # from dot to cosine curve
        cosine_curve_line = always_redraw(get_cosine_curve)  # cosine curve

        self.add(dot, orbit)
        self.add(origin_to_circle_line,
                 dot_to_sine_line, sine_curve_line,
                 dot_to_cosine_line, cosine_curve_line,
         )
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class sin(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.orgin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            Tex("\\pi"), Tex("2 \\pi"),
            Tex("3 \\pi"), Tex("4 \\pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.orgin_point)

        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        orgin_point = self.orgin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class tangens(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        tan_graph = axes.get_graph(
            lambda x:  np.tan(x),
            color=BLUE,
        )
       
        cotan_graph = axes.get_graph(
            lambda x: 1/np.tan(x),
            use_smoothing=False,
            color=YELLOW,
        )
        

        
        sin_label = axes.get_graph_label(sin_graph, "tg(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ctg(x)"))
       

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait(pause_time)
        

        






























class TrigRepresentationsScene(Scene):
    CONFIG = {
        "unit_length" : 1.5,
        "arc_radius" : 0.5,
        "axes_color" : BLACK,
        "circle_color" : RED,
        "theta_color" : YELLOW,
        "theta_height" : 0.3,
        "theta_value" : np.pi/5,
        "x_line_colors" : MAROON_B,
        "y_line_colors" : BLUE,
    }
    def setup(self):
        self.init_axes()
        self.init_circle()
        self.init_theta_group()

    def init_axes(self):
        self.axes = Axes(
            unit_size = self.unit_length,center_point= ORIGIN,
        )
        self.axes.move_to(ORIGIN)
        self.axes.set_color(self.axes_color)

        self.add(self.axes)

    def init_circle(self):
        self.circle = Circle(
            radius = self.unit_length,
            color = self.circle_color
        )
        self.add(self.circle)

    def init_theta_group(self):
        self.theta_group = self.get_theta_group()
        self.add(self.theta_group)

    def add_trig_lines(self, *funcs, **kwargs):
        lines = VGroup(*[
            self.get_trig_line(func, **kwargs)
            for func in funcs
        ])
        self.add(*lines)

    def get_theta_group(self):
        arc = Arc(
            self.theta_value, 
            radius = self.arc_radius,
            color = self.theta_color,
        )
        theta = Tex("\\theta")
        theta.shift(1.5*arc.point_from_proportion(0.5))
        theta.set_color(self.theta_color)
        theta.set_height(self.theta_height)
        line = Line([0,0,0], self.get_circle_point())
        
        dot = Dot(line.get_end(), radius = 0.05)
        return VGroup(line, arc, theta, dot)

    def get_circle_point(self):
        return rotate_vector(self.unit_length*RIGHT, self.theta_value)

    def get_trig_line(self, func_name = "sin", color = BLACK):
        assert(func_name in ["sin", "tan", "sec", "cos", "cot", "csc"])
        is_co = func_name in ["cos", "cot", "csc"]
        if color is None:
            if is_co:
                color = self.y_line_colors 
            else:
                color = self.x_line_colors

        #Establish start point
        if func_name in ["sin", "cos", "tan", "cot"]:
            start_point = self.get_circle_point()
        else:
            start_point = ORIGIN

        #Establish end point
        if func_name is "sin":
            end_point = start_point[0]*RIGHT
        elif func_name is "cos":
            end_point = start_point[1]*UP
        elif func_name in ["tan", "sec"]:
            end_point = (1./np.cos(self.theta_value))*self.unit_length*RIGHT
        elif func_name in ["cot", "csc"]:
            end_point = (1./np.sin(self.theta_value))*self.unit_length*UP
        return Line(start_point, end_point, color = color)
       
class ExplainTrigFunctionDistances(TrigRepresentationsScene):
    CONFIG = {
        
        "alt_theta_val" : 2*np.pi/5,
    }
    def setup(self):
        TrigRepresentationsScene.setup(self)

    def construct(self):
        self.introduce_angle()
        self.show_sine_and_cosine()
        self.show_tangent_and_cotangent()
        self.show_secant_and_cosecant()
        self.explain_cosecant()
        self.summarize_full_group()

    def introduce_angle(self):
        self.remove(self.circle)
        self.remove(self.theta_group)
        line, arc, theta, dot = self.theta_group
        line.rotate(-self.theta_value)
        line.set_color(color = BLACK)
        print(line.get_start())
        print(ORIGIN)
        brace = Brace(line, UP, buff = SMALL_BUFF)
        brace.set_color(color = GREEN)
        arc.set_color(color = BLACK)
        ooo="1"
        #one = brace.get_text("1",buff = SMALL_BUFF)
        VGroup(line, brace).rotate(self.theta_value)
        #one.rotate_in_place(-self.theta_value)
        self.circle.rotate(self.theta_value)


        self.play(
            ShowCreation(line),
            ShowCreation(arc),
        )
        self.play(Write(theta))
        
        self.play(
            ShowCreation(self.circle),
            Rotating(line, rate_func = smooth, in_place = False),
            run_time = 2
        )
        self.play(
        
            ShowCreation(dot)
        )
        self.wait()
        self.play(
            GrowFromCenter(brace),
            
        )
        self.wait(2)
        self.play(*list(map(FadeOut, [
              brace
        ])))
        self.radial_line_label = VGroup(brace)

    def show_sine_and_cosine(self):
        sin_line, sin_brace, sin_text = sin_group = self.get_line_brace_text("sin")
        cos_line, cos_brace, cos_text = cos_group = self.get_line_brace_text("cos")

        self.play(ShowCreation(sin_line))
        self.play(
            GrowFromCenter(sin_brace),
            Write(sin_text),
        )
        
        self.play(ShowCreation(cos_line))
        self.play(
            GrowFromCenter(cos_brace),
            Write(cos_text),
        )
        self.wait()
       

        mover = VGroup(
            sin_group,
            cos_group,
            self.theta_group,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)
        targets = []
        for theta in thetas:
            self.theta_value = theta
            targets.append(VGroup(
                self.get_line_brace_text("sin"),
                self.get_line_brace_text("cos"),
                self.get_theta_group()
            ))
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ],
            run_time = 5, 
            rate_func = there_and_back
        ))
        self.theta_value = thetas[0]

       
        self.wait()
        self.sin_group, self.cos_group = sin_group, cos_group

    def show_tangent_and_cotangent(self):
        tan_group = self.get_line_brace_text("tan")
        cot_group = self.get_line_brace_text("cot")
        tan_text = tan_group[-1]
        cot_text = cot_group[-1]
        line = Line(UP, DOWN).scale(FRAME_Y_RADIUS)
        line.rotate(self.theta_value)
        line.move_to(self.theta_group[-1])
        line.set_stroke(width = 2)

        sin_tex = "{\\sin(\\theta)}"
        cos_tex = "{\\cos(\\theta)}"
        tan_frac = Tex("= \\frac" + sin_tex + cos_tex)
        cot_frac = Tex("= \\frac" + cos_tex + sin_tex)
        tan_frac.to_corner(UP+LEFT)
        tan_frac.shift(2*RIGHT)
        cot_frac.next_to(tan_frac, DOWN)


        for frac, text in (tan_frac, tan_text), (cot_frac, cot_text):
            frac.set_color(YELLOW)
            frac.scale_in_place(0.7)
            text.save_state()
            text.next_to(frac, LEFT)
            self.play(Write(VGroup(text, frac)))
            self.wait()
        
        self.wait()
        self.play(*list(map(FadeOut, [
            tan_frac, cot_frac, self.sin_group, self.cos_group
        ])))
        self.wait()

        self.play(
            self.theta_group[-1].set_color, YELLOW,
            ShowCreation(line),
            
        )
        small_lines = VGroup()
        for group in tan_group, cot_group:
            small_line, brace, text = group
            self.play(
                ShowCreation(small_line),
                GrowFromCenter(brace),
                text.restore,
            )
            self.wait()
            small_lines.add(small_line)
        self.play(FadeOut(line), Animation(small_lines))

        mover = VGroup(
            tan_group,
            cot_group,
            self.theta_group,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)
        targets = []
        for theta in thetas:
            self.theta_value = theta
            targets.append(VGroup(
                self.get_line_brace_text("tan"),
                self.get_line_brace_text("cot"),
                self.get_theta_group()
            ))
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ], 
            run_time = 5, 
            rate_func = there_and_back
        ))
        self.theta_value = thetas[0]

        self.wait(2)

        self.tangent_line = self.get_tangent_line()
        self.add(self.tangent_line)
        self.play(*it.chain(*[
            list(map(FadeOut, [tan_group, cot_group])),
            [Animation(self.theta_group[-1])]
        ]))

    def show_secant_and_cosecant(self):
        sec_group = self.get_line_brace_text("sec")
        csc_group = self.get_line_brace_text("csc")
        sec_line, sec_brace, sec_text = sec_group
        csc_line, csc_brace, csc_text = csc_group

        sec_frac = Tex("= \\frac{1}{\\cos(\\theta)}")
        sec_frac.to_corner(UP+LEFT).shift(2*RIGHT)
        csc_frac = Tex("= \\frac{1}{\\sin(\\theta)}")
        csc_frac.next_to(sec_frac, DOWN)

        sec_dot, csc_dot = [
            Dot(line.get_end(), color = line.get_color())
            for line in (sec_line, csc_line)
        ]
        sec_group.add(sec_dot)
        csc_group.add(csc_dot)

        for text, frac in (sec_text, sec_frac), (csc_text, csc_frac):
            frac.set_color(YELLOW)
            frac.scale_in_place(0.7)
            text.save_state()
            text.next_to(frac, LEFT)
            frac.add_to_back(text.copy())
            self.play(
                Write(frac),
                
            )
            self.wait()
        self.wait()
        for group in sec_group, csc_group:
            line, brace, text, dot = group
            dot.save_state()
            dot.move_to(text)
            dot.set_fill(opacity = 0)
            self.play(dot.restore)
            self.wait()
            self.play(
                ShowCreation(line),
                GrowFromCenter(brace),
                text.restore,
                
            )
            self.wait()

        mover = VGroup(
            sec_group,
            csc_group,
            self.theta_group,
            self.tangent_line,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)
        targets = []
        for theta in thetas:
            self.theta_value = theta
            new_sec_group = self.get_line_brace_text("sec")
            new_csc_group = self.get_line_brace_text("csc")
            for group in new_sec_group, new_csc_group:
                line = group[0]
                group.add(
                    Dot(line.get_end(), color = line.get_color())
                )
            targets.append(VGroup(
                new_sec_group,
                new_csc_group,
                self.get_theta_group(),
                self.get_tangent_line(),
            ))
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ], 
            run_time = 5, 
            rate_func = there_and_back
        ))
        self.theta_value = thetas[0]

        self.wait(2)

        self.play(*list(map(FadeOut, [
            sec_group, sec_frac
        ])))
        self.csc_group = csc_group
        self.csc_frac =csc_frac

    def explain_cosecant(self):
        sin_group = self.get_line_brace_text("sin")
        sin_line, sin_brace, sin_text = sin_group
        csc_line, csc_brace, csc_text, csc_dot = self.csc_group
        csc_subgroup = VGroup(csc_brace, csc_text)

        arc_theta = VGroup(*self.theta_group[1:3]).copy()
        arc_theta.rotate(-np.pi/2)
        arc_theta.shift(csc_line.get_end())
        arc_theta[1].rotate_in_place(np.pi/2)

        radial_line = self.theta_group[0]

        tri1 = Polygon(
            ORIGIN, radial_line.get_end(), sin_line.get_end(),
            color = GREEN,
            stroke_width = 8,
        )
        tri2 = Polygon(
            csc_line.get_end(), ORIGIN, radial_line.get_end(),
            color = GREEN,
            stroke_width = 8,
        )

        opp_over_hyp = Tex(
            "\\frac{\\text{Opposite}}{\\text{Hypotenuse}} ="
        )
        frac1 = Tex("\\frac{\\sin(\\theta)}{1}")
        frac1.next_to(opp_over_hyp)
        frac1.set_color(RED)
        frac2 = Tex("= \\frac{1}{\\csc(\\theta)}")
        frac2.next_to(frac1)
        frac2.set_color(RED)
        frac_group = VGroup(opp_over_hyp, frac1, frac2)
        frac_group.set_width(FRAME_X_RADIUS-1)
        frac_group.next_to(ORIGIN, RIGHT).to_edge(UP)

    def summarize_full_group(self):
        scale_factor = 1.5
        theta_subgroup = VGroup(self.theta_group[0], self.theta_group[-1])
        self.play(*it.chain(*[
            [mob.scale, scale_factor]
            for mob in [
                self.circle, self.axes, 
                theta_subgroup, self.tangent_line
            ]
        ]))
        self.unit_length *= scale_factor

        to_fade = VGroup()
        for func_name in ["sin", "tan", "sec", "cos", "cot", "csc"]:
            line, brace, text = self.get_line_brace_text(func_name)
            if func_name in ["sin", "cos"]:
                angle = line.get_angle()
                if np.cos(angle) < 0:
                    angle += np.pi
                if func_name is "sin":
                    target = line.get_center()+0.2*LEFT+0.1*DOWN
                else:
                    target = VGroup(brace, line).get_center_of_mass()
                text.scale(0.75)
                text.rotate(angle)
                text.move_to(target)
                line.set_stroke(width = 6)
                self.play(
                    ShowCreation(line),
                    Write(text, run_time = 1)
                )
            else:
                self.play(
                    ShowCreation(line),
                    GrowFromCenter(brace),
                    Write(text, run_time = 1)
                )
            if func_name in ["sec", "csc", "cot"]:
                to_fade.add(*self.get_mobjects_from_last_animation())
            if func_name is "sec":
                self.wait()
        self.wait()
       
        self.remove(self.tangent_line)
        self.play(
            FadeOut(to_fade),
           
        )
        self.wait(2)



    def get_line_brace_text(self, func_name = "sin"):
        line = self.get_trig_line(func_name)
        angle = line.get_angle()
        vect = rotate_vector(UP, angle)
        vect = np.round(vect, 1)
        if (vect[1] < 0) ^ (func_name is "sec"):
            vect = -vect
            angle += np.pi
        brace = Brace(
            Line(
                line.get_length()*LEFT/2,
                line.get_length()*RIGHT/2,
            ), 
            UP
        )
        brace.rotate(angle)
        brace.shift(line.get_center())
        brace.set_color(line.get_color())
        text = Tex("\\%s(\\theta)"%func_name)
        text.scale(0.75)
        #text[-2].set_color(self.theta_color)
        text.add_background_rectangle()
        text.next_to(brace.get_center_of_mass(), vect, buff = 1.2*MED_SMALL_BUFF)
        return VGroup(line, brace, text)

    def get_tangent_line(self):
        return Line(
            self.unit_length*(1./np.sin(self.theta_value))*UP,
            self.unit_length*(1./np.cos(self.theta_value))*RIGHT,
            color = BLUE
        )