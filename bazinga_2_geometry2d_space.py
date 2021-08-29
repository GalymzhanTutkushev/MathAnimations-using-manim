from manimlib import *

class d123(ThreeDScene):
    def construct(self):
        dotA = Dot(3*LEFT+2*UP)
        dotB = Dot(3*LEFT+2*UP)
        dotC = Dot(3*LEFT+2*UP)
        numberl = NumberLine(x_range=np.array([0,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberl))
        numberp = NumberPlane(x_range=np.array([0,7,1]),y_range=np.array([0,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        numberz = ThreeDAxes()
        self.play(ShowCreation(numberz))
        # self.play(numberl.copy().rotate,90*DEGREES)
        line = Line(ORIGIN+1.5*LEFT+1.5*DOWN,1.5*RIGHT+1.5*DOWN)
        square = Square(side_length = 3)
        cube = Cube(side_length = 3)
        line.set_color(color = BLUE)
        square.set_color(color = BLUE)
       
        
        cube.move_to([0,0,-1.5])

        brace_line = Brace(line,DOWN)
        brace_line.set_color(color = BLACK)
        brace_sq1 = Brace(square,RIGHT)
        brace_sq1.set_color(color = BLACK)
        brace_cube = Brace(cube,LEFT)
        brace_cube.set_color(color = BLACK)
        d1 = Tex("1D")
        d2 = Tex("2D")
        d3 = Tex("3D")
        d1.to_edge(UP)
        d2.to_edge(UP)
        d3.to_edge(UP)
        self.play(ShowCreation(line))
        self.play(ShowCreation(brace_line))
        self.play(Write(d1))
        self.wait()
        self.play(ShowCreation(square))
        self.play(ShowCreation(brace_sq1))
        self.play(ReplacementTransform(d1,d2))
        self.wait()
        self.play(ShowCreation(cube))
        self.play(ReplacementTransform(d2,d3))

        frame = self.camera.frame
        self.play(frame.animate.increment_phi(70 * DEGREES),
                frame.animate.increment_gamma(130 * DEGREES),
            frame.animate.increment_theta(-30 * DEGREES))
        # frame.set_euler_angles(
        #     theta=-30 * DEGREES,
        #     phi=70 * DEGREES,
        # )
        self.wait(3)


class space_slide3(Scene):
    def construct(self):
        tda = ThreeDAxes()
        cub = Cube()
        cub.scale(0.5)
        cub.move_to(ORIGIN)
        frame = self.camera.frame
        self.play(frame.animate.increment_phi(70 * DEGREES),
                frame.animate.increment_gamma(130 * DEGREES),
            frame.animate.increment_theta(-30 * DEGREES))
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.play(ShowCreation(tda))
        self.play(ShowCreation(cub))
        self.play(cub.shift,3*UP)
        self.play(cub.shift,-3*UP)
        self.play(cub.shift,3*IN)
        self.play(cub.shift,-3*IN)
        self.play(cub.shift,3*RIGHT)
        self.play(cub.shift,-3*RIGHT)
        self.play(cub.move_to,3*RIGHT+2*UP+2*OUT)
        self.play(cub.move_to,-3*RIGHT-2*UP+2*OUT)
        self.play(cub.move_to,3*RIGHT+2*UP-2*OUT)
        self.wait(3)


class space_slide4(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([0,12,1]), unit_size=1,
        include_numbers=True,include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[12])
        numberl.shift(2*DOWN)
        self.play(ShowCreation(numberl))
        w = 6
        h = 3.5
        
        paralelogram = Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP+2*RIGHT,h*UP+2*RIGHT,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        paralelogram.move_to(ORIGIN)
        self.play(ShowCreation(paralelogram))
        self.wait(3)



class space_slide5(Scene):
    def construct(self):
        A = 3.5
        dotA = Dot(A*RIGHT)
        numberl = NumberLine(x_range=np.array([0,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberl))
        self.play(ShowCreation(dotA))
        self.play(dotA.move_to,5*RIGHT)
        gd = VGroup(dotA,numberl)
        self.remove(gd)
        axes = Axes(
            
            x_range=(-1, 10),
           
            y_range=(-2, 2, 0.5),
           
            height=6,
            width=10,
            
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            
            y_axis_config={
                "include_tip": False,
            }
        )
        
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

       
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

       
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

       
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75),
            axes.animate.to_corner(UL),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))



class space_slide6(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([-7,7,1]), unit_size=1,
        include_numbers=True,include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
       
        self.play(ShowCreation(numberl))
        line1 = Line(ORIGIN,2*RIGHT)
        brace1 = Brace(line1,UP)
        self.play(ShowCreation(brace1))
        self.wait()
        self.play(FadeOut(brace1))
        line1 = Line(ORIGIN,5*RIGHT)
        brace1 = Brace(line1,UP)
        self.play(ShowCreation(brace1))
        self.wait()
        self.play(FadeOut(brace1))
        line1 = Line(ORIGIN,-4*RIGHT)
        brace1 = Brace(line1,UP)
        self.play(ShowCreation(brace1))
        self.play(FadeOut(brace1))
        self.wait(3)

class space_slide7(Scene):
    def construct(self):
        A = 3*UP+2*LEFT
        B = 2*UP+0*RIGHT
        C = -2*UP+2*RIGHT
        D = -3*UP-2*RIGHT
        E = 0*UP-4*RIGHT
        lineAB = Line(A,B)
        lineBC = Line(B,C)
        lineCD = Line(C,D)
        lineDE = Line(D,E)
        lineEA = Line(E,A)

        dotA  = SmallDot(A)
        dotB  = SmallDot(B)
        dotC  = SmallDot(C)
        dotD  = SmallDot(D)
        dotE  = SmallDot(E)

        self.play(ShowCreation(dotA),ShowCreation(dotB),
        ShowCreation(lineAB))
        
        self.play(ShowCreation(dotC),ShowCreation(lineBC))
        self.play(ShowCreation(dotD),ShowCreation(lineCD))
        self.play(ShowCreation(dotE),ShowCreation(lineDE))
        self.play(ShowCreation(lineEA))
        
        self.wait(3)
