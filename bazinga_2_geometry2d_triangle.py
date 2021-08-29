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

class Area(Scene):
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
        
        # rectangle = Rectangle(width = w, height =h,stroke_color = color_stroke,fill_color =color_fill, fill_opacity = opacity_fill)
        
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
       
        
     
        pb_label = Tex("a")
        pa_label = Tex("b")

        pb_label.next_to(triangle, DOWN)
      
        self.add(pb_label)
        pa_label.next_to(triangle, RIGHT)
      
        self.add(pa_label)  

        ### ТРЕУГОЛЬНИК
        self.play(ShowCreation(triangle),FadeIn(pa_label),FadeIn(pb_label))
        self.play(ShowCreation(triangle2))
        self.play(triangle2.move_to,[0.5*UP+0.5*LEFT],run_time = play_time)
        self.play(FadeOut(triangle2)) 
        self.play(FadeIn(triangle_area)) 
        self.wait(pause_time)
        self.play(FadeOut(triangle),FadeOut(triangle_area),FadeOut(pa_label),FadeOut(pb_label))
        triangle_areah = Tex("S=\\frac{1}{2}\\cdot a\\cdot h")
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
        self.wait(pause_time)

class tri_slide1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):

        dotA = SmallDot(4*LEFT+2*DOWN)
        dotB = SmallDot(2*UP)
        dotC = SmallDot(2*RIGHT+2*DOWN)
        A = Tex("A")
        B = Tex("B")
        C = Tex("C")
        A.next_to(dotA,LEFT)
        B.next_to(dotB,UP)
        C.next_to(dotC,RIGHT)
        lineAB = Line(4*LEFT+2*DOWN,2*UP)
        lineBC = Line(2*UP,2*RIGHT+2*DOWN)
        lineCA = Line(2*RIGHT+2*DOWN,4*LEFT+2*DOWN)
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        c.next_to(lineAB,LEFT,buff = -1.7)
        a.next_to(lineBC,buff = -0.7)
        b.next_to(lineCA,DOWN)
        r=0.5
        alpha = Angle(lineCA,lineAB,r,(-1,1))
        beta1 = Angle(lineAB,lineBC,r,(-1,1))
        beta2 = Angle(lineAB,lineBC,r+0.1,(-1,1))
        gamma1 = Angle(lineBC,lineCA,r,(-1,1))
        gamma2 = Angle(lineBC,lineCA,r+0.1,(-1,1))
        gamma3 = Angle(lineBC,lineCA,r+0.2,(-1,1))
        alpha_tex = Tex("\\alpha").next_to(alpha,RIGHT)
        beta_tex = Tex("\\beta").next_to(beta2,DOWN)
        gamma_tex = Tex("\\gamma").next_to(gamma3,LEFT)
        self.play(Write(dotA),Write(dotB),Write(dotC))
        self.play(Write(lineAB),Write(lineBC),Write(lineCA))
        self.play(Write(A),Write(B),Write(C))
        self.play(Write(a),Write(b),Write(c))
        self.play(Write(alpha),Write(beta1),Write(beta2),Write(gamma3),Write(gamma1),Write(gamma2))
        self.play(Write(alpha_tex),Write(beta_tex),Write(gamma_tex))
        
        self.wait(pause_time)
        
        self.wait(pause_time)


class tri_slide2(Scene):

    def construct(self):
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        A = 2*UP+1*RIGHT
        B = -1*UP+3*RIGHT
        C = -1*UP-2*RIGHT
        Ad =SmallDot(A)
        Bd =SmallDot(B)
        Cd =SmallDot(C)
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        

        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)
        a.next_to(AB,RIGHT)
        b.next_to(BC,DOWN)
        c.next_to(CA,LEFT)
        beta = CA.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        print(alpha)
        print(beta)
        print(gamma)
        print(alpha+beta+gamma)
        abc = Tex("a+b>c")
        bca = Tex("b+c>a")
        cab = Tex("c+a>b")
        abc.to_edge(UP)
        bca.to_edge(UP)
        cab.to_edge(UP)

        ab_group = VGroup(AB,BC,Bd)
        bc_group = VGroup(CA,BC,Cd)
        ca_group = VGroup(AB,CA,Ad)

        brace_ab = Brace(ab_group,DOWN)
        brace_bc = Brace(bc_group,DOWN)
        brace_ca = Brace(ca_group,DOWN)

        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CA),
        Write(Ad),Write(a),Write(Bd),Write(b),Write(Cd),Write(c))
        self.save_state()
        self.play(Write(bca))
        self.play(Rotating(AB,-gamma,about_point=A),run_time = 3)
        self.play(Rotating(CA,PI-beta,about_point=C),run_time = 3)
        self.play(FadeOut(bca))
        self.restore()
        self.play(Write(cab))
        self.play(Rotating(AB,-gamma,about_point=A),run_time = 3)
        self.play(Rotating(CA,-beta,about_point=A),run_time = 3)
        self.play(FadeOut(cab))
        self.restore()
        self.play(Write(abc))
        self.play(Rotating(AB,-(PI+gamma),about_point=B),run_time = 3)
        self.play(Rotating(CA,-beta,about_point=A),run_time = 3)
        self.play(FadeOut(abc))
        self.restore()
        self.wait(pause_time)


class tri_slide3(Scene):

    def construct(self):
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        A = 2*UP+1*RIGHT
        B = -1*UP+3*RIGHT
        C = -1*UP-2*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)
        a.next_to(BC,DOWN)
        b.next_to(CA,LEFT,buff=-1.2)
        c.next_to(AB,RIGHT,buff=-0.8)
        beta = CA.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        print(alpha)
        print(beta)
        print(gamma)
        print(alpha+beta+gamma)
        abc = Tex("\\alpha+\\beta+\\gamma=180^\\circ")
        abc.to_edge(UP)

        alpha_sec = AnnularSector(start_angle=gamma,angle=-(PI+gamma-beta),outer_radius = 0.5,inner_radius = 0,arc_center = A,fill_color = RED)
        beta_sec =  AnnularSector(start_angle=PI+gamma,angle=-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,fill_color = GREEN)
        gamma_sec =  AnnularSector(start_angle=PI-alpha,angle=beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,fill_color = BLUE)
        alpha_sec.set_stroke(RED)
        beta_sec.set_stroke(RED)
        gamma_sec.set_stroke(RED)
        alpha_tex = Tex("\\alpha").next_to(alpha_sec,DOWN)
        beta_tex = Tex("\\beta").next_to(beta_sec,LEFT)
        gamma_tex = Tex("\\gamma").next_to(gamma_sec,RIGHT)
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CA),
        Write(Ad),Write(a),Write(Bd),Write(b),Write(Cd),Write(c))
        self.play(Write(alpha_tex),Write(beta_tex),Write(gamma_tex))
        self.play(Write(abc))
        self.play(ShowCreation(alpha_sec),ShowCreation(beta_sec),ShowCreation(gamma_sec))
        o = 3*LEFT+1*UP
        self.play(beta_sec.animate.move_arc_center_to(o))
        self.play(gamma_sec.animate.move_arc_center_to(o))
        self.play(Rotate(alpha_sec,PI))
        self.play(alpha_sec.animate.move_arc_center_to(o))
        self.wait(5)




class tri_slide4(Scene):

    def construct(self):
        aa = 4*LEFT+2*DOWN
        bb = 2*UP
        cc = 2*RIGHT+2*DOWN
        dotA = Dot(aa)
        dotB = Dot(bb)
        dotC = Dot(cc)
        
        A = Tex("A")
        B = Tex("B")
        C = Tex("C")
        D = Tex("D")
        A.next_to(dotA,LEFT)
        B.next_to(dotB,UP)
        C.next_to(dotC,DOWN)
        

        lineAB = Line(aa,bb)
        lineBC = Line(bb,cc)
        lineCA = Line(cc,aa)

        lineAD = Line(aa,aa-[np.cos(lineAB.get_angle()),np.sin(lineAB.get_angle()),0])
        lineBD = Line(bb,bb-[np.cos(lineBC.get_angle()),np.sin(lineBC.get_angle()),0])
        lineCD = Line(cc,cc-[np.cos(lineCA.get_angle()),np.sin(lineCA.get_angle()),0])
        r=0.5
        alpha = Angle(lineCA,lineAD,r,(1,-1))
        beta = Angle(lineAB,lineBD,r,(-1,-1))
        gamma = Angle(lineBC,lineCD,r,(-1,1))
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        
        a.next_to(lineAB,LEFT,buff = -0.7)
        b.next_to(lineBC,buff = -0.7)
        c.next_to(lineCA,DOWN)
        # alpha = ArcBetweenPoints(lineAB.get_points(),lineCA.get_points())
        self.play(Write(dotA),Write(dotB),Write(dotC))
        self.play(Write(lineAB),Write(lineBC),Write(lineCA))
        self.play(Write(A),Write(B),Write(C))
        self.play(Write(a),Write(b),Write(c))
 
        self.play(Write(lineAD))
        self.play(Write(lineBD))
        self.play(Write(lineCD))
        self.play(Write(alpha),Write(gamma),Write(beta))
       
        
        self.wait(pause_time)


class tri_slide5(Scene):

    def construct(self):
        h = 4
        a = 6
        am = 3
        triangleh = Polygon(
                [am-a,0,0], [am,0,0], [0, h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        a = 1
        am = 0.5
        trianglehT = Polygon(
                [am-a,0,0], [am,0,0], [0, h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        
        trianglehT.shift(h/2*DOWN)
        triangleh.shift(h/2*DOWN)
       
        
        self.play(ShowCreation(triangleh))
 
        self.play(Transform(triangleh,trianglehT),run_time = play_time)
        self.play(Transform(trianglehT,triangleh),run_time = play_time)
        self.wait(5)


class tri_slide6(Scene):
    def construct(self):
        #высота
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        A = 2*UP+1*RIGHT
        B = -1*UP+3*RIGHT
        C = -1*UP-2*RIGHT
        Ad =SmallDot(A)
        Bd =SmallDot(B)
        Cd =SmallDot(C)
        a = Tex("A")
        b = Tex("B")
        c = Tex("C")
        a.next_to(Ad,UP)
        b.next_to(Bd,RIGHT)
        c.next_to(Cd,LEFT)
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)
        gamma = (PI-angle_between_vectors(AB.get_vector(),BC.get_vector()))/PI*180
        alpha = (PI-angle_between_vectors(BC.get_vector(),CA.get_vector()))/PI*180
        beta = (PI-angle_between_vectors(CA.get_vector(),AB.get_vector()))/PI*180
        
        cd=AB.get_projection(C)
        CD = Line(C,cd)
        bd=CA.get_projection(B)
        BD = Line(B,bd)
        ad=BC.get_projection(A)
        AD = Line(A,ad)
        O = line_intersection([AD.get_start(),AD.get_end()],[BD.get_start(),BD.get_end()])
        o_dot = Dot(O).set_color(RED)
        r1 = Elbow(width=0.2,angle = 0).move_to(ad+0.1*UP+0.1*RIGHT)
        r2 = Elbow(width=0.2,angle = 0).move_to(bd-0.025*UP+0.15*RIGHT).rotate(BD.get_angle()+PI)
        r3 = Elbow(width=0.2,angle = 0).move_to(cd-0.15*UP-0.05*RIGHT).rotate(CD.get_angle()+PI)
        # r1 = RightAngle(BD,CA,0.1)
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CA),
        Write(Ad),Write(a),Write(Bd),Write(b),Write(Cd),Write(c))
        self.play(ShowCreation(CD),ShowCreation(BD),ShowCreation(AD))
        self.play(ShowCreation(o_dot))
        self.play(ShowCreation(r1),ShowCreation(r2),ShowCreation(r3))

        self.wait(pause_time)

class tri_slide7(Scene):
    def construct(self):
        #меддиана
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        A = 2*UP+1*RIGHT
        B = -1*UP+3*RIGHT
        C = -1*UP-2*RIGHT
        Ad =SmallDot(A)
        Bd =SmallDot(B)
        Cd =SmallDot(C)
        a = Tex("A")
        b = Tex("B")
        c = Tex("C")
        a.next_to(Ad,UP)
        b.next_to(Bd,RIGHT)
        c.next_to(Cd,LEFT)
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)
        
        
        cd=AB.get_center()
        CD = Line(C,cd)
        bd=CA.get_center()
        BD = Line(B,bd)
        ad=BC.get_center()
        AD = Line(A,ad)
        O = line_intersection([AD.get_start(),AD.get_end()],[BD.get_start(),BD.get_end()])
        o_dot = Dot(O).set_color(RED)
        r11 = get_risk(AB,n=1,pr=3/8,rt=0.025)
        r12 = get_risk(AB,n=1,pr=8/3,rt=0.025)
        r21 = get_risk(BC,n=3,pr=3/8,rt=0.025)
        r22 = get_risk(BC,n=3,pr=8/3,rt=0.025)
        r31 = get_risk(CA,n=2,pr=3/8,rt=0.025)
        r32 = get_risk(CA,n=2,pr=8/3,rt=0.025) 
        
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CA),
        Write(Ad),Write(a),Write(Bd),Write(b),Write(Cd),Write(c))
        self.play(ShowCreation(CD),ShowCreation(BD),ShowCreation(AD))
        self.play(ShowCreation(o_dot))
        self.play(
            ShowCreation(r11),ShowCreation(r12),
        ShowCreation(r21),ShowCreation(r22),
        ShowCreation(r31),ShowCreation(r32)
        )
        
        self.wait(pause_time)


class tri_slide8(Scene):
    def construct(self):
        #биссектриса
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        A = 2*UP+1*RIGHT
        B = -1*UP+3*RIGHT
        C = -1*UP-2*RIGHT
        Ad =SmallDot(A)
        Bd =SmallDot(B)
        Cd =SmallDot(C)
        a = Tex("A")
        b = Tex("B")
        c = Tex("C")
        a.next_to(Ad,UP)
        b.next_to(Bd,RIGHT)
        c.next_to(Cd,LEFT)
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)
        beta = (PI-angle_between_vectors(AB.get_vector(),BC.get_vector()))
        gamma = (PI-angle_between_vectors(BC.get_vector(),CA.get_vector()))
        alpha = (PI-angle_between_vectors(CA.get_vector(),AB.get_vector()))
        print(alpha)
        print(beta)
        print(gamma)
        print(alpha+beta+gamma)

        mc = gamma/2
        ma = -(beta+alpha/2)
        mb = (PI-beta)+beta/2
       
        p = (AB.get_length()+BC.get_length()+CA.get_length())/2
        ha = 2*np.sqrt(AB.get_length()*CA.get_length()*p*(p-BC.get_length()))/(AB.get_length()+CA.get_length())
        hb = 2*np.sqrt(AB.get_length()*BC.get_length()*p*(p-CA.get_length()))/(AB.get_length()+BC.get_length())
        hc = 2*np.sqrt(BC.get_length()*CA.get_length()*p*(p-AB.get_length()))/(BC.get_length()+CA.get_length())
        AD = Line(A,A+[ha*np.cos(ma),ha*np.sin(ma),0])
        CD = Line(C,C+[hc*np.cos(mc),hc*np.sin(mc),0])
        BD = Line(B,B+[hb*np.cos(mb),hb*np.sin(mb),0])
        O = line_intersection([AD.get_start(),AD.get_end()],[BD.get_start(),BD.get_end()])
        o_dot = Dot(O).set_color(RED)
        r = 0.5
        angleBAD = Angle(AD,AB,r,(1,1))
        angleCAD = Angle(CA,AD,r,(-1,1))
        angleCBD1 = Angle(BD,BC,r,(1,1))
        angleABD1 = Angle(AB,BD,r,(-1,1))
        angleCBD2 = Angle(BD,BC,r+0.1,(1,1))
        angleABD2 = Angle(AB,BD,r+0.1,(-1,1))
        angleACD1 = Angle(CD,CA,r)
        angleBCD1 = Angle(BC,CD,r,(-1,1))
        angleACD2 = Angle(CD,CA,r+0.1)
        angleBCD2 = Angle(BC,CD,r+0.1,(-1,1))
        angleACD3 = Angle(CD,CA,r+0.2)
        angleBCD3 = Angle(BC,CD,r+0.2,(-1,1))
        
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CA),
        Write(Ad),Write(a),Write(Bd),Write(b),Write(Cd),Write(c))
        self.play(ShowCreation(CD),ShowCreation(BD),ShowCreation(AD))
        self.play(ShowCreation(o_dot))
        self.play(ShowCreation(angleBAD),
        ShowCreation(angleCAD)
        )
        self.play(
            ShowCreation(angleCBD1),ShowCreation(angleCBD2),
        ShowCreation(angleABD1),ShowCreation(angleABD2)
        )
        self.play(
            ShowCreation(angleACD1),ShowCreation(angleACD2),ShowCreation(angleACD3),
            ShowCreation(angleBCD1), ShowCreation(angleBCD2), ShowCreation(angleBCD3)
        )
        
        self.wait(pause_time)

class tri_slide9(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        aa = 4*LEFT+2*DOWN
        bb = 2*UP
        cc = 4*RIGHT+2*DOWN
        dotA = SmallDot(aa)
        dotB = SmallDot(bb)
        dotC = SmallDot(cc)
        A = Tex("A")
        B = Tex("B")
        C = Tex("C")
        A.next_to(dotA,LEFT)
        B.next_to(dotB,UP)
        C.next_to(dotC,RIGHT)
        lineAB = Line(aa,bb)
        lineBC = Line(bb,cc)
        lineCA = Line(cc,aa)
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        c.next_to(lineAB,LEFT,buff = -1.7)
        a.next_to(lineBC,buff = -1.7)
        b.next_to(lineCA,DOWN)
        r=0.7
        alpha = Angle(lineCA,lineAB,r,(-1,1))
       
        gamma3 = Angle(lineBC,lineCA,r,(-1,1))
        r1 = get_risk(lineAB)
        r2 = get_risk(lineBC)
        self.play(Write(dotA),Write(dotB),Write(dotC))
        self.play(Write(lineAB),Write(lineBC),Write(lineCA))
        self.play(Write(A),Write(B),Write(C))
        self.play(Write(a),Write(b),Write(c))
        self.play(Write(alpha),Write(gamma3))
        self.play(Write(r1),Write(r2))
       
        
        self.wait(pause_time)
        

class tri_slide10(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
   

        
    def construct(self):
        aa = 2*LEFT+2*DOWN
        bb = 4*np.sqrt(3)/2*UP+2*DOWN
        cc = 2*RIGHT+2*DOWN
        dotA = SmallDot(aa)
        dotB = SmallDot(bb)
        dotC = SmallDot(cc)
        A = Tex("A")
        B = Tex("B")
        C = Tex("C")
        A.next_to(dotA,LEFT)
        B.next_to(dotB,UP)
        C.next_to(dotC,RIGHT)
        lineAB = Line(aa,bb)
        lineBC = Line(bb,cc)
        lineCA = Line(cc,aa)
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        c.next_to(lineAB,LEFT,buff = -0.7)
        a.next_to(lineBC,buff = -0.7)
        b.next_to(lineCA,DOWN)
        r=0.7
        alpha = Angle(lineCA,lineAB,r,(-1,1))
        beta1 = Angle(lineAB,lineBC,r,(-1,1))
        gamma3 = Angle(lineBC,lineCA,r,(-1,1))
        r1 = get_risk(lineAB)
        r2 = get_risk(lineBC)
        r3 = get_risk(lineCA)
        self.play(Write(dotA),Write(dotB),Write(dotC))
        self.play(Write(lineAB),Write(lineBC),Write(lineCA))
        self.play(Write(A),Write(B),Write(C))
        self.play(Write(a),Write(b),Write(c))
        self.play(Write(alpha),Write(gamma3),Write(beta1))
        self.play(Write(r1),Write(r2),Write(r3))
        
        self.wait(pause_time)
        

class tri_slide11(Scene):
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

class tri_slide12(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        #равенство треугольников
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        A = 2*UP+1*RIGHT
        B = -1*UP+3*RIGHT
        C = -1*UP-2*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)
        
        a.next_to(AB,RIGHT)
        b.next_to(BC,DOWN)
        c.next_to(CA,LEFT)
        beta = CA.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        print(alpha)
        print(beta)
        print(gamma)
        print(alpha+beta+gamma)
        

        alpha_sec = AnnularSector(start_angle=gamma,angle=-(PI+gamma-beta),outer_radius = 0.5,inner_radius = 0,arc_center = A,color = BLACK)
        beta_sec =  AnnularSector(start_angle=PI+gamma,angle=-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,color = BLACK)
        gamma_sec =  AnnularSector(start_angle=PI-alpha,angle=beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,color = BLACK)
        alpha_sec.set_stroke(RED)
        beta_sec.set_stroke(RED)
        gamma_sec.set_stroke(RED)
        tr1 = VGroup(Ad,Bd,Cd,AB,BC,CA)
        tr2 = tr1.copy()
        tr1.shift(3*LEFT)
        alpha_sec.shift(3*LEFT)
        beta_sec.shift(3*LEFT)
        gamma_sec.shift(3*LEFT)
        tr2.shift(3*RIGHT)
        tr2.rotate(30*DEGREES)
        self.play(ShowCreation(tr1))
        
        self.play(ShowCreation(tr2))
        # по трем сторонам
        eq1 = Line(AB.get_center()+0.1*DOWN+0.1*LEFT,AB.get_center()-0.1*DOWN-0.1*LEFT)
        eq2 = Line(BC.get_center()+0.1*DOWN,BC.get_center()-0.1*DOWN)
        eq2 = VGroup(eq2,eq2.copy().move_to(BC.get_center()-[0.1*np.cos(alpha),0.1*np.sin(alpha),0]))
        eq3 = Line(CA.get_center()+0.1*DOWN+0.1*RIGHT,CA.get_center()-0.1*DOWN-0.1*RIGHT)
        eq3 = VGroup(eq3,eq3.copy().move_to(CA.get_center()-[0.1*np.cos(alpha),0.1*np.sin(alpha),0])
        ,eq3.copy().move_to(CA.get_center()+[0.1*np.cos(alpha),0.1*np.sin(alpha),0]))
        self.play(ShowCreation(eq1))
        self.play(ShowCreation(eq2))
        self.play(ShowCreation(eq3))
        self.play(FadeOut(eq1),FadeOut(eq2),FadeOut(eq3))
        # по углу и двум сторонам
        self.play(ShowCreation(eq1))
        self.play(ShowCreation(eq2))
        self.play(ShowCreation(beta_sec))
        self.play(FadeOut(eq1),FadeOut(eq2),FadeOut(beta_sec))
        # по двум углам и двум сторонe
        self.play(ShowCreation(eq1))
        self.play(ShowCreation(beta_sec))
        self.play(ShowCreation(alpha_sec))
        self.play(FadeOut(eq1),FadeOut(beta_sec),FadeOut(alpha_sec))
        self.wait(pause_time)