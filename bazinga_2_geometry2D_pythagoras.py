from manimlib import *



class pifagor_slide1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        
        START_1 = (-1.5,-1.5,0)
        END_1 =   (-1.5,1.5,0)

        START_2 = (-1.5,1.5,0)
        END_2 =   (1.5,-1.5,0)

        START_3 = (1.5,-1.5,0)
        END_3 =   (-1.5025,-1.5,0)

        START_4 = (-1.2,-1.5,0)
        END_4 =   (-1.2,-1.2,0)

        START_5 = (-1.2,-1.2,0)
        END_5 =   (-1.5025,-1.2,0)




        line_1 = Line(START_1,END_1)
        line_2 = Line(START_2,END_2)
        line_3 = Line(START_3,END_3)
        line_4 = Line(START_4,END_4)
        line_5 = Line(START_5,END_5)
        line_1.set_color(color = BLACK)
        line_2.set_color(color = BLACK)
        line_3.set_color(color = BLACK)
        line_4.set_color(color = BLACK)
        line_5.set_color(color = BLACK)

        x = Tex("a")
        x.set_color_by_tex("a", BLUE)
        x.next_to(line_1, LEFT)
        x.scale(0.75)

        y = Tex("b")
        y.set_color_by_tex("b", GREEN)
        y.next_to(line_3, DOWN)
        y.scale(0.75)

        z = Tex("c")
        z.set_color_by_tex("c", RED)
        z.move_to(0.4*RIGHT)
        z.scale(0.75)


        self.play(ShowCreation(line_1))
        self.play(ShowCreation(line_2))
        self.play(ShowCreation(line_3))
        self.wait(1.5)
        self.play(ShowCreation(line_4))
        self.play(ShowCreation(line_5))


        self.play(Write(x))
        self.play(Write(y))
        self.play(Write(z))
        self.wait(1.5)


class pifagor_slide2(Scene):
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
        screen_grid = NumberPlane()
        self.add(screen_grid)
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
        triangle_area = Tex("S={a\\cdot b","\\over 2}")
        triangle_area.to_edge(UP)
       
       
        pb_label = Tex("a")
        pa_label = Tex("b")

        pb_label.next_to(triangle, DOWN)
      
        self.add(pb_label)
        pa_label.next_to(triangle, RIGHT)
      
        self.add(pa_label)
        ### ТРЕУГОЛЬНИК
        self.play(ShowCreation(triangle),FadeIn(pa_label),FadeIn(pb_label))
        self.play(ShowCreation(triangle2))
        self.play(Write(triangle_area[0]))
        self.play(triangle2.move_to,[0.5*UP+0.5*LEFT],run_time = play_time)
        self.play(FadeOut(triangle2)) 
        self.play(Write(triangle_area[1])) 
        self.wait(pause_time)
        self.play(FadeOut(triangle),FadeOut(triangle_area),FadeOut(pa_label),FadeOut(pb_label))

class pifagor_slide3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        screen_grid = NumberPlane()
        self.add(screen_grid)
        triangle_areah = Tex("S=\\frac{1}{2}\\cdot a\\cdot h")
        triangle_areah.to_edge(UP)

        triangle_areah2 = Tex("S=\\frac{1}{2}\\cdot (a+x)\\cdot h-\\frac{1}{2}\\cdot x\\cdot h=\\frac{1}{2}\\cdot a\\cdot h")
        triangle_areah2.to_edge(UP)
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
        self.play(Transform(triangle_areah,triangle_areah2))
        self.wait(pause_time)
        self.play(FadeOut(line_t),FadeOut(triangleHP),FadeOut(trianglehT),FadeOut(line_left),FadeOut(line_right),FadeOut(ht),FadeOut(at))

        self.wait(pause_time)


A_COLOR = BLUE
B_COLOR = GREEN
C_COLOR = YELLOW
SIDE_COLORS = [A_COLOR, B_COLOR, C_COLOR]
U_COLOR = GREEN
V_COLOR = RED


class pifagor_slide4(Scene):
    def construct(self):
        title = Tex("a", "^2", "+", "b", "^2", "=", "c", "^2")
        for color, char in zip(SIDE_COLORS, "abc"):
            title.set_color_by_tex(char, color)
        title.to_corner(UP + RIGHT)

        triples = [
            (3, 4, 5), 
            (5, 12, 13),
            (8, 15, 17),
            (7, 24, 25),
        ]

        self.add(title)
        for a, b, c in triples:
            triangle = Polygon(
                ORIGIN, a*RIGHT, a*RIGHT+b*UP,
                stroke_width = 0,
                fill_color = BLUE,
                fill_opacity = 0.5
            )
            hyp_line = Line(ORIGIN, a*RIGHT+b*UP)
            elbow = VMobject()
            elbow.set_points_as_corners([LEFT, LEFT+UP, UP])
            elbow.set_width(0.2*triangle.get_width())
            elbow.move_to(triangle, DOWN+RIGHT)
            triangle.add(elbow)

            square = Square(side_length = 1)
            square_groups = VGroup()
            for n, color in zip([a, b, c], SIDE_COLORS):
                square_group = VGroup(*[
                    square.copy().shift(x*RIGHT + y*UP)
                    for x in range(n)
                    for y in range(n)
                ])
                square_group.set_stroke(color, width = 3)
                square_group.set_fill(color, opacity = 0.5)
                square_groups.add(square_group)
            a_square, b_square, c_square = square_groups
            a_square.move_to(triangle.get_bottom(), UP)
            b_square.move_to(triangle.get_right(), LEFT)
            c_square.move_to(hyp_line.get_center(), DOWN)
            c_square.rotate(
                hyp_line.get_angle(),
                about_point = hyp_line.get_center()
            )
            if c in [5, 13, 25]:
                if c == 5:
                    keys = list(range(0, 5, 2))
                elif c == 13:
                    keys = list(range(0, 13, 3))
                elif c == 25:
                    keys = list(range(0, 25, 4))
                i_list = [i for i in range(c**2) if (i%c) in keys and (i//c) in keys]
            else:
                i_list = list(range(a**2))
            not_i_list = list(filter(
                lambda i : i not in i_list,
                list(range(c**2)),
            ))
            c_square_parts = [
                VGroup(*[c_square[i] for i in i_list]),
                VGroup(*[c_square[i] for i in not_i_list]),
            ]
            full_group = VGroup(triangle, square_groups)
            full_group.set_height(4)
            full_group.center()
            full_group.to_edge(UP)

            equation = Tex(
                str(a), "^2", "+", str(b), "^2", "=", str(c), "^2"
            )
            for num, color in zip([a, b, c], SIDE_COLORS):
                equation.set_color_by_tex(str(num), color)
            equation.next_to(title, DOWN, MED_LARGE_BUFF)
            equation.shift_onto_screen()
            
            self.play(
                FadeIn(triangle))
                
            
            self.play(LaggedStartMap(FadeIn, a_square))
            
            self.play(
                LaggedStartMap(FadeIn, b_square)
            )
           
            for start, target in zip([a_square, b_square], c_square_parts):
                mover = start.copy().set_fill(opacity = 0)
                target.set_color(start.get_color())
                self.play(ReplacementTransform(
                    mover, target,
                    run_time = 2,
                    path_arc = np.pi/2
                ))
            self.play(Write(equation))
            self.play(c_square.set_color, C_COLOR)
            self.wait()
            self.play(*list(map(FadeOut, [full_group, equation])))



class pifagor_slide5(Scene):
    def construct(self):
        self.add_title()
        self.show_proof()

    def add_title(self):
        title = Tex("a^2", "+", "b^2", "=", "c^2")
        for color, char in zip(SIDE_COLORS, "abc"):
            title.set_color_by_tex(char, color)
        title.to_edge(UP)
        self.add(title)
        self.title = title

    def show_proof(self):
        triangle = Polygon(
            ORIGIN, 5*RIGHT, 5*RIGHT+12*UP,
            stroke_color = BLACK,
            stroke_width = 2,
            fill_color = GREEN,
            fill_opacity = 0.5
        )
        triangle.set_height(3)
        triangle.center()
        side_labels = self.get_triangle_side_labels(triangle)
        triangle_copy = triangle.copy()
        squares = self.get_abc_squares(triangle)
        a_square, b_square, c_square = squares


        self.add(triangle, triangle_copy)
        self.play(Write(side_labels))
        self.wait()
        self.play(*list(map(DrawBorderThenFill, squares)))
        self.add_labels_to_squares(squares, side_labels)
        self.wait()
        self.play(
            VGroup(triangle_copy, a_square, b_square).move_to, 
                4*LEFT+2*DOWN, DOWN,
            VGroup(triangle, c_square).move_to, 
                4*RIGHT+2*DOWN, DOWN,
            run_time = 2,
            path_arc = np.pi/2,
        )
        self.wait(pause_time)
        self.add_new_triangles(
            triangle, 
            self.get_added_triangles_to_c_square(triangle, c_square)
        )
        self.wait(pause_time)
        self.add_new_triangles(
            triangle_copy,
            self.get_added_triangles_to_ab_squares(triangle_copy, a_square)
        )
        self.wait(pause_time)

        big_squares = VGroup(*list(map(
            self.get_big_square,
            [triangle, triangle_copy]
        )))


        self.play(
            FadeIn(big_squares), 

            *list(map(FadeOut, squares))
        )
        self.wait(pause_time)
        self.play(*it.chain(
            list(map(FadeIn, squares)),
            list(map(Animation, big_squares)),
        ))
        self.wait(pause_time)

    def add_labels_to_squares(self, squares, side_labels):
        for label, square in zip(side_labels, squares):
            label.target = Tex(label.get_tex() + "^2")
            label.target.set_color(label.get_color())
            label.target.scale(0.7)
            label.target.move_to(square)
            square.add(label)

        self.play(LaggedStartMap(MoveToTarget, side_labels))

    def add_new_triangles(self, triangle, added_triangles):
        brace = Brace(added_triangles, DOWN)
        label = Tex("a", "+", "b")
        label.set_color_by_tex("a", A_COLOR)
        label.set_color_by_tex("b", B_COLOR)
        label.next_to(brace, DOWN)

        self.play(ReplacementTransform(
            VGroup(triangle.copy().set_fill(opacity = 0)),
            added_triangles,
            run_time = 2,
        ))
        self.play(GrowFromCenter(brace))
        self.play(Write(label))
        triangle.added_triangles = added_triangles

    def get_big_square(self, triangle):
        square = Square(stroke_color = RED)
        square.replace(
            VGroup(triangle, triangle.added_triangles),
            stretch = True
        )
        square.scale(1.01)
        return square

    #####

    def get_triangle_side_labels(self, triangle):
        a, b, c = list(map(Tex, "abc"))
        for mob, color in zip([a, b, c], SIDE_COLORS):
            mob.set_color(color)
        a.next_to(triangle, DOWN)
        b.next_to(triangle, RIGHT)
        c.next_to(triangle.get_center(), LEFT)
        return VGroup(a, b, c)

    def get_abc_squares(self, triangle):
        a_square, b_square, c_square = squares = [
            Square(
                stroke_color = color,
                fill_color = color,
                fill_opacity = 0.5,
            )
            for color in SIDE_COLORS
        ]
        a_square.set_width(triangle.get_width())
        a_square.move_to(triangle.get_bottom(), UP)
        b_square.set_height(triangle.get_height())
        b_square.set_color(color=GREEN)
        b_square.move_to(triangle.get_right(), LEFT)
        hyp_line = Line(
            triangle.get_corner(UP+RIGHT),
            triangle.get_corner(DOWN+LEFT),
        )
        c_square.set_width(hyp_line.get_length())
        c_square.move_to(hyp_line.get_center(), UP)
        c_square.rotate(
            hyp_line.get_angle(), 
            about_point = hyp_line.get_center()
        )

        return a_square, b_square, c_square

    def get_added_triangles_to_c_square(self, triangle, c_square):
        return VGroup(*[
            triangle.copy().rotate(i*np.pi/2, about_point = c_square.get_center())
            for i in range(1, 4)
        ])

    def get_added_triangles_to_ab_squares(self, triangle, a_square):
        t1 = triangle.copy()
        
        t1.rotate(np.pi)
        group = VGroup(triangle, t1).copy()
        group.rotate(-np.pi/2)
        group.move_to(a_square.get_right(), LEFT)
        t2, t3 = group
        return VGroup(t1, t2, t3)





class pifagor_slide6(Scene):
    def construct(self):
        w = 120*0.07
        h = 70*0.07
        rect = Rectangle(width = w,height = h)
        a = Tex("a")
        a.next_to(rect,DOWN)
        b = Tex("b")
        b.next_to(rect,RIGHT)
        c = Tex("c")
        c.move_to(0.2*UP+0.2*LEFT)
        d = DashedLine(rect.get_corner(DL),rect.get_corner(UR))
        self.play(ShowCreation(rect))
        self.play(Write(a),Write(b))
        self.play(ShowCreation(d))
        self.play(Write(c))
        abc = Tex("c = \\sqrt{a^2+b^2}","=\\sqrt{120^2+70^2}","\\approx 139")
        abc.to_edge(UP)
        self.play(Write(abc[0]))
        self.play(Write(abc[1]))
        self.play(Write(abc[2]))





class pifagor_area(Scene):
    def construct(self):
        circle = Circle(radius = 2)
        square = Square(side = 6)
        rectangle = Rectangle(width = 4, height =3)
        rectangle.set_color(color = BLUE)
        triangle = Polygon(
                ORIGIN, 4*RIGHT, 4*RIGHT+3*UP,
                stroke_width = 0,
                fill_color = BLUE,
                fill_opacity = 1
            )
        triangle.move_to([0,0,0])
        triangle_area = Tex("S=\\frac{1}{2}\\cdot a\\cdot b")

        d = Line()
        self.play(ShowCreation(triangle))
        self.play(ShowCreation(rectangle))
        triangle_area.to_edge(DOWN)
        triangle_area.set_color(BLACK)
        self.play(FadeIn(triangle_area))
        self.play(FadeOut(rectangle))
        self.play(FadeOut(triangle_area))


        squareA = Rectangle(width = 3, height =3,fill_color = BLUE,
                fill_opacity = 1)
        squareA.next_to(triangle, RIGHT+[-0.9,0,0])
        squareB = Rectangle(width = 4, height =4,fill_color = BLUE,
                fill_opacity = 1)
        squareB.next_to(triangle, DOWN+[0,0.9,0])
        squareC = Rectangle(width = 5, height =5,fill_color = BLUE,
                fill_opacity = 1)
        squareC.rotate(0.643501109)
        squareC.move_to([-1.5,2,0])
        squareA.set_color(color = RED)
        squareB.set_color(color = GREEN)
        squareC.set_color(color = BLUE)
        squareA.set_fill(color = RED)
        squareB.set_fill(color = GREEN)
        squareC.set_fill(color = YELLOW)
        self.add(squareA)
        self.add(squareB)
        self.add(squareC)

        pifagor_eq = Tex("a^2+b^2=c^2")
        pifagor_eq.to_edge(DOWN)
        pifagor_eq.set_color(BLACK)
        self.play(FadeIn(pifagor_eq))
        self.play(FadeOut(pifagor_eq))
        self.wait(3)