from manimlib import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 1,
        "grid_color": GREY,
        "axis_color": GREY,
        "axis_stroke": 1,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes)


class area(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        
        w = 8
        h = 4
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        self.save_state()
        
        # paralelogram.set_shadow(0.5)
        # paralelogram.set_gloss(0.5)
        
        # rectangle = Rectangle(width = w, height =h,stroke_color = color_stroke,fill_color =color_fill, fill_opacity = opacity_fill)
        rectangle =Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP,h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        # rectangle.set_gloss(0.5)
        rectangle.move_to(ORIGIN)
        
       
        rectangle_area = Tex("S=a\\cdot b")
        rectangle_area.to_edge(UP)
     
        pb_label = Tex("a")
        pa_label = Tex("b")

        pb_label.next_to(rectangle, DOWN)
      
        self.add(pb_label)
        pa_label.next_to(rectangle, RIGHT)
      
        self.add(pa_label)
        self.play(ShowCreation(rectangle))

        self.play(ShowCreation(rectangle_area))
        # параллелограмм
        paralelogram = Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP+2*RIGHT,h*UP+2*RIGHT,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        paralelogram.move_to(ORIGIN)
        self.play(Transform(rectangle,paralelogram),run_time = play_time)
        self.wait(pause_time)
        self.play(FadeOut(rectangle),FadeOut(rectangle_area),FadeOut(pb_label),FadeOut(pa_label))

        rectangleP = Rectangle(width = w, height =h,stroke_color = color_stroke,fill_color = color_fill, fill_opacity = opacity_fill)
        lineP = Line(rectangleP.get_corner(UL),rectangleP.get_corner(UR)+RIGHT)
        # braceP = Brace(lineP,UP)
        trianglePM = Polygon(
                ORIGIN, 1*RIGHT, 1*RIGHT+h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color =color_fill,
                fill_opacity = opacity_fill
            )
        trianglePS = Polygon(
                ORIGIN, 1*RIGHT, 1*RIGHT+h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
       
        trianglePM.rotate(PI)
        trianglePM.next_to(rectangleP,RIGHT,buff = 0)
        hp_label = Tex("h")
        hp_label.next_to(rectangleP, RIGHT, buff = 1.4)
       
        ap_label = Tex("a")
       
        self.add(hp_label)
        ap_label.next_to(lineP, UP,SMALL_BUFF)
      
        self.add(ap_label)

        trianglePS.next_to(rectangleP,LEFT,buff = 0)
      
        paraGroup = VGroup(trianglePM,trianglePS,rectangleP)
        aver_lineP = DashedLine(rectangleP.get_corner(UR),rectangleP.get_corner(DR))
        self.play(ShowCreation(paraGroup))
        self.play(ShowCreation(aver_lineP))
        self.play(trianglePS.shift,[(w+1)*RIGHT],run_time = play_time)
        parallelogram_eq =  Tex("S=a\\cdot h")
        parallelogram_eq.to_edge(UP)
      
        self.play(FadeIn(parallelogram_eq))
        self.wait(2*pause_time)
        self.play(FadeOut(paraGroup),FadeOut(aver_lineP),FadeOut(parallelogram_eq),FadeOut(hp_label),FadeOut(ap_label),FadeOut(lineP))

        # квадрат
        square = Square(4,stroke_color = color_stroke,
        fill_color = color_fill, fill_opacity = opacity_fill)
        square_area = Tex("S=a\\cdot a = a^2")
        square_area.to_edge(UP)
     
        pb_label = Tex("a")
        pa_label = Tex("a")

        pb_label.next_to(square, DOWN)
      
        self.add(pb_label)
        pa_label.next_to(square, RIGHT)
      
        self.add(pa_label)
        self.play(ShowCreation(square))

        self.play(ShowCreation(square_area))
        self.wait(2*pause_time)
        self.play(FadeOut(square),FadeOut(square_area),FadeOut(pa_label),FadeOut(pb_label))
        
        ###
        romb_eq = Tex("S={d_1 \\cdot d_2 \\over 2}")
        romb_eq.to_edge(UP)
        d1 = 6
        d2 = 4
        romb = Polygon(
                [-d1/2,0,0],[0,d2/2,0],[d1/2,0,0],[0,-d2/2,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        lineD1 = DashedLine([-d1/2,0,0],[d1/2,0,0])
        lineD2 = DashedLine([0,d2/2,0],[0,-d2/2,0])
        line1 = DashedLine([-d1/2,d2/2,0],[d1/2,d2/2,0])
        line2 = DashedLine([d1/2,d2/2,0],[d1/2,-d2/2,0])
        line3 = DashedLine([d1/2,-d2/2,0],[-d1/2,-d2/2,0])
        line4 = DashedLine([-d1/2,-d2/2,0],[-d1/2,d2/2,0])
        d1_label = Tex("d_1")
        d2_label = Tex("d_2")
        d1_label.next_to(lineD1, UP)
        d2_label.next_to(lineD2, RIGHT)
        d1_label.shift(0.5*LEFT)
        d2_label.shift(0.5*DOWN)
        self.play(ShowCreation(romb))
        self.play(ShowCreation(lineD1),ShowCreation(d1_label))
        self.play(ShowCreation(lineD2),ShowCreation(d2_label))
        self.play(ShowCreation(line1))
        self.play(ShowCreation(line2))
        self.play(ShowCreation(line3))
        self.play(ShowCreation(line4))
        self.play(Write(romb_eq))
        self.wait(2*pause_time)
        romb_group = VGroup(romb,romb_eq,lineD1,lineD2,line1,line2,line3,line4,d1_label,d2_label)
        self.play(FadeOut(romb_group))
        ### ТРЕУГОЛЬНИК
        triangle = Polygon(
                ORIGIN, w*RIGHT, w*RIGHT+h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
       

        triangle.move_to(ORIGIN)
        triangle2 = Polygon(
                ORIGIN, h*UP, w*RIGHT+h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
      
        triangle2.move_to(ORIGIN)
        triangle_area = Tex("S={a\\cdot b \\over 2} ")
        triangle_area.to_edge(UP)
        self.play(ShowCreation(triangle),FadeIn(pa_label),FadeIn(pb_label))
        self.play(ShowCreation(triangle2))
        self.play(triangle2.move_to,[0.5*UP+0.5*LEFT],run_time = play_time)
        self.play(FadeOut(triangle2)) 
        self.play(FadeIn(triangle_area)) 
        self.wait(pause_time)
        self.play(FadeOut(triangle),FadeOut(triangle_area),FadeOut(pa_label),FadeOut(pb_label))
        triangle_areah = Tex("S={a\\cdot h \\over 2}")
        triangle_areah.to_edge(UP)
        h = 4
        a = 7
        am = 3
        triangleh = Polygon(
                [am-a,0,0], [am,0,0], [0, h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        trianglehT = Polygon(
                [am-a,0,0], [am,0,0], [am, h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        triangleHP = Polygon(
                [am-a,0,0], [am,0,0], [5, h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        trianglehT.shift(h/2*DOWN)
        triangleHP.shift(h/2*DOWN)
        lineHP = DashedLine([am-a,0,0],[5-a,h,0])
        lineHPup = DashedLine([5-a,h,0],[5,h,0])
        line_t = DashedLine([0, h,0],[0, 0,0])
        line_left = DashedLine([am-a,0,0],[am-a,h,0])
        line_right = DashedLine([am-a,h,0],[am,h,0])
        line_up = DashedLine([am,h,0],[am, 0,0])
        triangleh.shift(h/2*DOWN)
        lineHP.shift(h/2*DOWN)
        lineHPup.shift(h/2*DOWN)
        line_t.shift(h/2*DOWN)
        line_left.shift(h/2*DOWN)
        line_right.shift(h/2*DOWN)
        line_up.shift(h/2*DOWN)
        ht = Tex("h")
        at = Tex("a")
        at.next_to(triangleh,DOWN)
        ht.next_to(line_t,RIGHT)
        ht.add_updater(lambda m: m.next_to(line_t,RIGHT))
        self.play(ShowCreation(triangleh))
        self.play(ShowCreation(line_t))
        self.play(ShowCreation(ht),ShowCreation(at))
        self.play(ShowCreation(line_left),run_time= 2)
        self.play(ShowCreation(line_right),run_time= 2)
        self.play(ShowCreation(line_up),run_time= 2)
        self.play(FadeIn(triangle_areah))
        self.wait(pause_time)
        self.play(ReplacementTransform(triangleh,trianglehT),line_t.shift,am*RIGHT,run_time = play_time)
        self.remove(line_up)
        self.play(Transform(trianglehT,triangleHP),Transform(line_left,lineHP),Transform(line_right,lineHPup),line_t.shift,(a-5)*RIGHT,run_time = play_time)
        self.play(FadeOut(triangle_areah))
        self.play(FadeOut(line_t),FadeOut(triangleHP),FadeOut(trianglehT),FadeOut(line_left),FadeOut(line_right),FadeOut(ht),FadeOut(at))

        a = 6
        b = 4
        h = 3
        trapezoid = Polygon(
                ORIGIN,[a,0,0],[a-1,h,0],[a-b-1,h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        trapezoid.move_to(ORIGIN)

        at_label = Tex("a")
        bt_label = Tex("b")
        ht_label = Tex("h")
        ab = Tex("b+a")
        ba = Tex("a+b")
        bt_label.next_to(trapezoid, UP)
        ab.next_to(trapezoid, UP)
     
        self.add(bt_label)
        at_label.next_to(trapezoid, DOWN)
        ba.next_to(trapezoid, DOWN)
      
        self.add(at_label)

        ht_label.next_to(trapezoid,LEFT)
        ht = DashedLine([a-b-1-3,h-h/2,0],[a-b-1-3,-h/2,0])
        
        self.play(ShowCreation(trapezoid),run_time = 3)
        self.play(ShowCreation(ht_label),ShowCreation(ht))
        self.play(trapezoid.shift,3*LEFT,ht.shift,3*LEFT,ht_label.shift,3*LEFT,run_time = play_time)
        tr = trapezoid.copy()
        self.play(tr.shift,(b+1)*RIGHT,run_time = play_time)
        self.play(tr.flip,LEFT,run_time = play_time)
        
        trapezion_eq = Tex("S={(a+b)\\cdot h \\over 2}")
        trapezion_eq.to_edge(UP)
        self.play(FadeIn(trapezion_eq),Transform(at_label,ba),Transform(bt_label,ab))
        self.wait(2*pause_time)
        self.play(FadeOut(trapezion_eq))
        self.wait(pause_time)

        self.restore()
        # окружности
        Arcs = []
        Lines = []
        
        for a in range(10):
            r = (a+0.2)/5
            arc = Arc(start_angle=PI/2,angle=2*PI,radius = r)
        
            line = Line([-PI*r,0,0],[PI*r,0,0])
            line.move_to([0,-r,0])
            arc.set_stroke(width = 20)
            line.set_stroke(width = 20)
            arc.set_color(GREEN)
            line.set_color(GREEN)
            Arcs.append(arc)
            Lines.append(line)
            self.play(ShowCreation(arc),run_time=0.5)
        r=line.get_bottom()[1]-0.1
        lineR = Line([0,0,0],[0,r,0])
        R = Tex("R")
        R.next_to(lineR,RIGHT)
        self.play(Write(R),ShowCreation(lineR))
        
        for a in range(9,-1,-1):
           
            self.play(Transform(Arcs[a],Lines[a]),run_time = 0.4)
            # self.play(ShowCreation(line))
        lineA =Line([r*PI,r,0],[-r*PI,r,0])
        lineB =Line([0,0,0],[-r*PI,r,0])
        lineC =Line([0,0,0],[r*PI,r,0])
        
        self.play(ShowCreation(lineA),ShowCreation(lineB),ShowCreation(lineC))
        trLeft = Polygon([r*PI,r,0],ORIGIN,[0,r,0])
        trRight = Polygon([-r*PI,r,0],ORIGIN,[0,r,0])
        # trLeft.set_fill(color = GREEN,opacity = 0.5)
        # trRight.set_fill(color = GREEN,opacity = 0.5)
        self.play(ShowCreation(trLeft),ShowCreation(trRight))
        self.wait()
        f = Tex("S=","{2 \\pi R","\\cdot R","\\over 2}","=\\pi R^2")
        f.to_edge(UP)
        self.play(Write(f[0]))
        
        pir = Tex("2\\pi R")
        pir.next_to(lineR,DOWN)
        
        self.play(Write(pir),Write(f[1]))
        self.wait()
        self.play(Write(f[2:5]))

        self.wait(2*pause_time)
        self.restore()

        n=6
        R=2
        sec = Sector(outer_radius = R,angle = 2*PI/n)
        sec_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        sec_group.set_stroke(color=BLACK, width = 3)
        sec_group.set_fill(color=GREEN, opacity = 0.5)
        self.play(ShowCreation(sec_group))
        sec_group_part1 =  VGroup(*[sec_group[i] for i in [0,3]])
        sec_group_part2 =  VGroup(*[sec_group[i] for i in [2,5]])
        
        self.play(Rotating(sec_group[0],2*PI/n*(1),about_point =[R*np.cos(2*PI/n),R*np.sin(2*PI/n),0]),
        Rotating(sec_group[3],2*PI/n*(1),about_point =[R*np.cos(-2*2*PI/n),R*np.sin(-2*2*PI/n),0]),
        Rotating(sec_group[2],2*PI/n*(-1),about_point =[R*np.cos(2*2*PI/n),R*np.sin(2*2*PI/n),0]),
        Rotating(sec_group[5],2*PI/n*(-1),about_point =[R*np.cos(-2*PI/n),R*np.sin(-2*PI/n),0]),run_time = 2)
        UPsec = VGroup(sec_group[0],sec_group[1],sec_group[2])
        self.play(UPsec.shift,R/2*RIGHT)
        self.play(UPsec.shift,R*np.sin(2*PI/n)*DOWN)
        self.play(FadeOut(sec_group))
        n=10
        R=2
        sec = Sector(outer_radius = R,angle = 2*PI/n)
    
        sec_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        sec_group.set_stroke(color=BLACK, width = 3)
        sec_group.set_fill(color=GREEN, opacity = 0.5)
        self.play(ShowCreation(sec_group))
        sec_group_part1 =  VGroup(*[sec_group[i] for i in [0,3]])
        sec_group_part2 =  VGroup(*[sec_group[i] for i in [2,5]])
        
        self.play(
        Rotating(sec_group[0],4*PI/n*(1),about_point =[1.25,1.72,0]),
        Rotating(sec_group[4],4*PI/n*(-1),about_point =[-1.25,1.72,0]),

        Rotating(sec_group[5], 4*PI/n*(1),about_point =[-1.25,-1.72,0]),
        Rotating(sec_group[9], 4*PI/n*(-1),about_point =[1.25,-1.72,0]),

        Rotating(sec_group[1],2*PI/n*(1),about_point =[R*np.cos(2*2*PI/n),R*np.sin(2*2*PI/n),0]),
        Rotating(sec_group[3],2*PI/n*(-1),about_point =[R*np.cos(3*2*PI/n),R*np.sin(3*2*PI/n),0]),
        
        Rotating(sec_group[6],2*PI/n*(1),about_point =[R*np.cos(-3*2*PI/n),R*np.sin(-3*2*PI/n),0]),
        Rotating(sec_group[8],2*PI/n*(-1),about_point =[R*np.cos(-4*PI/n),R*np.sin(-4*PI/n),0]),
        run_time = 2)
        UPsec = VGroup(sec_group[0],sec_group[1],sec_group[2],sec_group[3],sec_group[4])
        self.play(UPsec.shift,R*np.sin(PI/n)*RIGHT)
        self.play(UPsec.shift,R*np.cos(PI/n)*DOWN)
        braceR = Brace(UPsec,RIGHT)
        r_1 = Tex("R").next_to(braceR,RIGHT)
        bracePI = Brace(UPsec,DOWN)
        r_pi = Tex("\\pi R").next_to(bracePI,DOWN)
        
        self.play(ShowCreation(braceR),Write(r_1),ShowCreation(bracePI),Write(r_pi))
        self.play(FadeOut(sec_group),FadeOut(braceR),FadeOut(r_1),FadeOut(bracePI),FadeOut(r_pi))

        n=30
        R=2
        secUP = Sector(start_angle = (n/2-1)/2*2*PI/n,outer_radius = R,angle = 2*PI/n)
        sec_groupUP = VGroup(*[
                    secUP.copy().shift(2*x*R*np.sin(PI/n)*RIGHT+RIGHT)
                    for x in range(int(n/2))
                ])
        sec_groupUP.shift(R*np.sin(PI/n)*LEFT*(n-2)/2)
        sec_groupUP.shift(R*np.cos(PI/n)*DOWN)
        sec_groupUP.set_stroke(color=BLACK, width = 3)
        sec_groupUP.set_fill(color=GREEN, opacity = 0.5)
        self.play(ShowCreation(sec_groupUP))

        self.wait()
       
        secDOWN = Sector(start_angle = -((n/2-1)/2+1)*2*PI/n,outer_radius = R,angle = 2*PI/n)
        sec_groupDOWN = VGroup(*[
                    secDOWN.copy().shift(2*x*R*np.sin(PI/n)*RIGHT+RIGHT)
                    for x in range(int(n/2))
                ])
        sec_groupDOWN.shift(2*R*np.sin(PI/n)*LEFT*n/4)
        sec_groupDOWN.set_stroke(color=BLACK, width = 3)
        sec_groupDOWN.set_fill(color=GREEN, opacity = 0.5)
        self.play(ShowCreation(sec_groupDOWN))
        self.wait()
        braceR = Brace(sec_groupDOWN,RIGHT)
        r_1 = Tex("R").next_to(braceR,RIGHT)
        bracePI = Brace(sec_groupDOWN,DOWN)
        r_pi = Tex("\\pi R").next_to(bracePI,DOWN)
        pir = Tex("S=\\pi \\cdot R\\cdot R=\\pi \\cdot R^2")
        pir.to_edge(UP)
        self.play(ShowCreation(braceR),Write(r_1),ShowCreation(bracePI),Write(r_pi))
        self.wait()
        self.play(Write(pir))
        self.wait()
        self.wait(2*pause_time)


class UnfoldCircles(Scene):
    CONFIG = {
        "circle_style": {
            "fill_color": GREY_BROWN,
            "fill_opacity": 0,
            "stroke_color": GREY_BROWN,
            "stroke_width": 2,
        },
        "radius": 1.0,
        "dr": 0.01,
    }

    def construct(self):
        
        self.add_four_circles()

    def add_four_circles(self):

        radius = self.radius

        radii_lines = VGroup(*[
            Line(radius * UP, ORIGIN).set_stroke(WHITE, 2)
            for x in range(1)
        ])
        radii_lines.arrange_in_grid(buff=1.3)
        radii_lines[2:].shift(RIGHT)
        #radii_lines.next_to(rect_group, DOWN, buff=1.3)
        R_labels = VGroup(*[
            Tex("R").next_to(line, LEFT, SMALL_BUFF)
            for line in radii_lines
        ])

        unwrap_factor_tracker = ValueTracker(0)

        def get_circle(line):
            return always_redraw(
                lambda: self.get_unwrapped_circle(
                    radius=radius, dr=self.dr,
                    unwrap_factor=unwrap_factor_tracker.get_value(),
                    center=line.get_top()
                )
            )

        circles = VGroup(*[get_circle(line) for line in radii_lines])
        circle_copies = circles.copy()
        for mob in circle_copies:
            mob.clear_updaters()

        self.play(
            LaggedStartMap(Write, circle_copies, lag_ratio=0.7),
            LaggedStartMap(Write, R_labels),
            LaggedStartMap(ShowCreation, radii_lines),
        )
        self.remove(circle_copies)
        self.add(circles, radii_lines, R_labels)
        self.wait()
        self.play(
            radii_lines[2:].shift, 2.9 * RIGHT,
            R_labels[2:].shift, 2.9 * RIGHT,
            VGroup(
                radii_lines[:2], R_labels[:2]
            ).to_edge, LEFT, {"buff": 1.0}
        )
        self.play(
            unwrap_factor_tracker.set_value, 1,
            run_time=2
        )
        self.wait()

       
    def get_unwrapped_circle(self, radius, dr, unwrap_factor=0, center=ORIGIN):
        radii = np.arange(0, radius + dr, dr)
        rings = VGroup()
        for r in radii:
            r_factor = 1 + 3 * (r / radius)
            alpha = unwrap_factor**r_factor
            alpha = np.clip(alpha, 0, 0.9999)
            angle = interpolate(TAU, 0, alpha)
            length = TAU * r
            arc_radius = length / angle
            ring = Arc(
                start_angle=-90 * DEGREES,
                angle=angle,
                radius=arc_radius,
                **self.circle_style
            )
            ring.shift(center + (r - arc_radius) * DOWN)
            rings.add(ring)
        return rings

class UnwrappedCircleLogic(UnfoldCircles):
    CONFIG = {
        "radius": 1.25,
        "dr": 0.01,
    }

    def construct(self):
        radius = self.radius
        dr = self.dr

        Tex.CONFIG["background_stroke_width"] = 2
        unwrap_factor_tracker = ValueTracker(0)
        center_tracker = VectorizedPoint()
        highligt_prop_tracker = ValueTracker(0.5)

        def get_highlight_prop():
            return highligt_prop_tracker.get_value()

        def get_r():
            return radius * get_highlight_prop()

        center_tracker.move_to(4.5 * LEFT)

        def get_unwrapped_circle():
            result = self.get_unwrapped_circle(
                radius=radius, dr=dr,
                unwrap_factor=unwrap_factor_tracker.get_value(),
                center=center_tracker.get_center()
            )
            self.get_submob_from_prop(
                result, get_highlight_prop()
            ).set_stroke(YELLOW, 2)
            return result

        unwrapped_circle = always_redraw(get_unwrapped_circle)
        circle = unwrapped_circle.copy()
        circle.clear_updaters()
        R_line = Line(circle.get_center(), circle.get_bottom())
        R_line.set_stroke(WHITE, 2)
        R_label = Tex("R")
        R_label.next_to(R_line, LEFT)
        circle_group = VGroup(circle, R_line, R_label)

        tri_R_line = always_redraw(
            lambda: Line(
                ORIGIN, radius * DOWN
            ).shift(center_tracker.get_center())
        )

        # Unwrap
        self.play(FadeIn(circle_group))
        self.add(circle_group, unwrapped_circle, tri_R_line, R_label)
        circle_group.set_stroke(opacity=0.5)
        self.play(
            unwrap_factor_tracker.set_value, 1,
            run_time=2
        )
        self.play(
            center_tracker.move_to,
            circle.get_right() + (radius + MED_SMALL_BUFF) * RIGHT,
            circle_group.set_stroke, {"opacity": 1},
        )
        self.wait(3)

        # # Change radius
        # r_line = always_redraw(
        #     lambda: Line(
        #         ORIGIN, get_r() * DOWN,
        #         stroke_width=2,
        #         stroke_color=WHITE,
        #     ).shift(circle.get_center())
        # )
        # r_label = Tex("r")
        # r_label.add_updater(
        #     lambda m: m.next_to(r_line, LEFT, SMALL_BUFF)
        # )
        # two_pi_r_label = Tex("2\\pi r")
        # two_pi_r_label.add_updater(
        #     lambda m: m.next_to(
        #         self.get_submob_from_prop(
        #             unwrapped_circle,
        #             get_highlight_prop(),
        #         ), DOWN, SMALL_BUFF
        #     )
        # )

        # circle.add_updater(
        #     lambda m: m.match_style(unwrapped_circle)
        # )

        # self.play(
        #     ReplacementTransform(R_line, r_line),
        #     ReplacementTransform(R_label, r_label),
        #     FadeInFromDown(
        #         two_pi_r_label.copy().clear_updaters(),
        #         remover=True
        #     )
        # )
        # self.add(two_pi_r_label)
        # for prop in [0.2, 0.8, 0.5]:
        #     self.play(
        #         highligt_prop_tracker.set_value, prop,
        #         run_time=2
        #     )

        # # Show line
        # line = Line(*[
        #     unwrapped_circle.get_corner(vect)
        #     for vect in (UL, DR)
        # ])
        # line.set_color(PINK)
        # line.set_fill(BLACK, 1)
        # # line_word = TextMobject("Line")
        # # line_word.next_to(ORIGIN, UP, SMALL_BUFF)
        # # line_word.rotate(line.get_angle(), about_point=ORIGIN)
        # # line_word.shift(line.get_center())

        # curve = line.copy()
        # curve.points[1] = unwrapped_circle.get_corner(DL)
        # # not_line = TextMobject("Not line")
        # # not_line.rotate(line.get_angle() / 2)
        # # not_line.move_to(line_word)
        # # not_line.shift(0.3 * DOWN)

        # self.play(
        #     ShowCreation(line),
     
        # )
        # self.wait()
        # self.play(highligt_prop_tracker.set_value, 1)
        # self.wait()

        # # Bend
        # line.save_state()

        # self.play(
        #     Transform(line, curve),

        # )
        # self.wait()
        # self.play(
        #     Restore(line),

        #     # FadeIn(two_pi_r_label),
        # )
        # self.wait()

    def get_submob_from_prop(self, mob, prop):
        n = len(mob.submobjects)
        return mob[min(int(prop * n), n - 1)]