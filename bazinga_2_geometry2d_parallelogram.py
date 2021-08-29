from manimlib import *

def get_risk(line,dl=0.3,n=1,pr=1,rt=0.01):
    lg=[]
    for i in range(n):
        l=line.copy().rotate(PI/2)
        l.set_length(dl)
        l.move_to((line.get_start()+pr*line.get_end())/(1+pr)+(1)*i*rt*(line.get_start()+line.get_end()))
        lg.append(l)
    lg = VGroup(*lg)
    return lg

class paral_slide1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        nup = NumberPlane()
        self.add(nup)
        lineA = Line(2*LEFT,2*RIGHT)
        lineB = Line(2*LEFT,2*UP+1*LEFT)
        self.play(Write(lineA))
        self.play(Write(lineB))
        self.wait()
        r1=get_risk(lineA,n=2)
        r12 = r1.copy().shift(2*UP).shift(RIGHT)
        r2=get_risk(lineB)
        r22 = r2.copy().shift(4*RIGHT)
        self.play(lineA.copy().move_to,2*UP+1*RIGHT)
        self.play(lineB.copy().shift,4*RIGHT)
        self.play(Write(r1),Write(r12))
        self.play(Write(r2),Write(r22))
        self.wait(pause_time)

class paral_slide2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        nup = NumberPlane()
        self.add(nup)
        A = 2*UP+1*RIGHT
        B = -1*UP-0*RIGHT
        C = -1*UP-3*RIGHT
        D = 2*UP-2*RIGHT
        

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(D)
       

        # треугольник
        AB = Line(A,B)
        
        BC = Line(B,C)

        # четырехгольник
        CD = Line(C,D)
        DA = Line(D,A)

        
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd))

        beta = CD.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        teta = DA.get_angle()
        alpha_sec = AnnularSector(start_angle=gamma,angle=-(PI+gamma-teta),outer_radius = 0.5,inner_radius = 0,arc_center = A,fill_color = TEAL)
        beta_sec =  AnnularSector(start_angle=PI+gamma,angle=-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,fill_color = RED)
        gamma_sec =  AnnularSector(start_angle=PI-alpha,angle=beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,fill_color = GREEN)
        teta_sec =  AnnularSector(start_angle=teta,angle=-(PI/2+teta),outer_radius = 0.5,inner_radius = 0,arc_center = D,fill_color = BLUE)

        self.play(ShowCreation(alpha_sec),ShowCreation(beta_sec),ShowCreation(gamma_sec))
        self.wait()
        o = 3*RIGHT+1*UP
        self.play(beta_sec.animate.move_arc_center_to(o))
        # self.play(gamma_sec.animate.rotate(PI))
        self.play(gamma_sec.animate.move_arc_center_to(o))
        self.wait(2)
        self.play(FadeOut(gamma_sec))
        # self.play(teta_sec.animate.move_arc_center_to(o))
        self.play(Rotate(alpha_sec,PI))
        self.play(alpha_sec.animate.move_arc_center_to(o))

        self.wait(pause_time)

class paral_slide3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        w = 8
        h = 4
        screen_grid = NumberPlane()
        self.add(screen_grid)
        paralelogram = Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP+2*RIGHT,h*UP+2*RIGHT,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        paralelogram.move_to(ORIGIN)
        d1 = Line(paralelogram.get_corner(UR),paralelogram.get_corner(DL))
        d2 = Line(paralelogram.get_corner(DR)-2*RIGHT,paralelogram.get_corner(UL)+2*RIGHT)
        h1 = DashedLine(paralelogram.get_corner(UL)+2*RIGHT,paralelogram.get_corner(UL)+2*RIGHT+h*DOWN)
        h2 = DashedLine(paralelogram.get_corner(DR)-2*RIGHT,paralelogram.get_corner(DR)-2*RIGHT-h*DOWN)
        self.play(ShowCreation(paralelogram))
        self.play(ShowCreation(d1),ShowCreation(d2))
        self.play(ShowCreation(h1))
        self.play(ShowCreation(h2))

        self.wait(pause_time)

class paral_slide4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        ###
        romb_eq = Tex("S= \\frac{d_1 \\cdot d_2}{2}")
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
        
        d1_label = Tex("d_1")
        d2_label = Tex("d_2")

        # always(d1_label.next_to,lineD1, UP)
        # always(d2_label.next_to,lineD2, RIGHT)
        # d1_label.shift(0.5*LEFT)
        # d2_label.shift(0.5*DOWN)
        self.play(ShowCreation(romb))
        self.play(ShowCreation(lineD1))
        self.play(ShowCreation(lineD2))
        d1 = 6
        d2 = 6
        lineD11 = Line([-d1/2,0,0],[d1/2,0,0])
        lineD22 = Line([0,d2/2,0],[0,-d2/2,0])
        rombS = Polygon(
                [-d1/2,0,0],[0,d1/2,0],[d1/2,0,0],[0,-d1/2,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        self.wait(pause_time)
        
        self.play(ReplacementTransform(romb,rombS),ReplacementTransform(lineD1,lineD11)
        ,ReplacementTransform(lineD2,lineD22))
        self.wait(pause_time)
        rombS_group = VGroup(rombS,lineD11,lineD22)
        self.play(Rotate(rombS_group,PI/4))
        self.wait(pause_time)
        romb_group = VGroup(rombS,lineD11,lineD22)
        self.play(FadeOut(romb_group))
        self.wait(pause_time)


class paral_slide5(Scene):
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
        paralelogram = Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP+2*RIGHT,h*UP+2*RIGHT,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        paralelogram.move_to(ORIGIN)
        paralelogram.set_shadow(0.5)
        paralelogram.set_gloss(0.5)
        square = Square(side = w)
        # rectangle = Rectangle(width = w, height =h,stroke_color = color_stroke,fill_color =color_fill, fill_opacity = opacity_fill)
        rectangle =Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP,h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        rectangle.set_gloss(0.5)
        rectangle.move_to(ORIGIN)
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
        triangle_area = Tex("S=\\frac{1}{2}\\cdot a\\cdot b")
        triangle_area.to_edge(UP)
       
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
        self.play(Transform(rectangle,paralelogram),run_time = play_time)
        self.wait(pause_time)
        self.play(FadeOut(rectangle),FadeOut(rectangle_area),FadeOut(pb_label),FadeOut(pa_label))

        rectangleP = Rectangle(width = w, height =h,stroke_color = color_stroke,fill_color = color_fill, fill_opacity = opacity_fill)
        lineP = Line(rectangleP.get_corner(DL)+LEFT,rectangleP.get_corner(DR))
        braceP = Brace(lineP)
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
       
        self.add(hp_label,braceP)
        ap_label.next_to(braceP, DOWN)
      
        self.add(ap_label)

        trianglePS.next_to(rectangleP,LEFT,buff = 0)
      
        paraGroup = VGroup(trianglePM,trianglePS,rectangleP)
        aver_lineP = DashedLine(rectangleP.get_corner(UR),rectangleP.get_corner(DR))
        self.play(ShowCreation(paraGroup))
        self.play(ShowCreation(aver_lineP))
        self.play(trianglePS.shift,[(w+1)*RIGHT],ap_label.shift,RIGHT,lineP.shift,RIGHT,braceP.shift,RIGHT,run_time = play_time)
        parallelogram_eq =  Tex("S=a\\cdot h")
        parallelogram_eq.to_edge(UP)
      
        self.play(FadeIn(parallelogram_eq))
        self.wait(pause_time)
        self.play(FadeOut(paraGroup),FadeOut(aver_lineP),FadeOut(parallelogram_eq),FadeOut(hp_label),FadeOut(ap_label),FadeOut(lineP),FadeOut(braceP))

        ###
        romb_eq = Tex("S= \\frac{d_1 \\cdot d_2}{2}")
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
        self.wait(pause_time)
        romb_group = VGroup(romb,romb_eq,lineD1,lineD2,line1,line2,line3,line4,d1_label,d2_label)
        self.play(FadeOut(romb_group))
        
        self.wait(pause_time)
