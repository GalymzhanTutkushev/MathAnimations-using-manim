from manimlib import *
import numpy as np




class axioms_slide3(Scene):
    def construct(self):
        lineA = Line(3*DOWN+3*LEFT,3*UP+3*RIGHT)
        # lineC = Line(2.5*DOWN+3*LEFT,1*UP+3*RIGHT)
        dotA  = Dot(2*UP+2*RIGHT)
        dotB  = Dot(-2*UP-2*RIGHT)
        # dotC = Dot(0.6*UP+2*RIGHT)
        self.play(ShowCreation(dotA),ShowCreation(dotB))
        self.play(ShowCreation(lineA))
        self.wait()
        # self.play(FadeOut(dotA),FadeOut(lineA))
        # self.play(ShowCreation(dotC))
        # self.play(ShowCreation(lineC))
        self.wait(3)

class axioms_slide4(Scene):
    def construct(self):
        lineA = Line(3*DOWN+3*LEFT,3*UP+3*RIGHT)

        dotA  = Dot(2*UP+2*RIGHT)
        dotB  = Dot(-2*UP-2*RIGHT)
        dotC = Dot(ORIGIN)
        A = Tex("A")
        A.next_to(dotA,UP)
        B = Tex("B")
        B.next_to(dotB,UP)
        C = Tex("C")
        C.next_to(dotC,UP)
        self.play(ShowCreation(dotA),ShowCreation(dotB),ShowCreation(dotC))
        self.play(ShowCreation(A),ShowCreation(B),ShowCreation(C))
        self.play(ShowCreation(lineA))
        
        self.wait(3)

class axioms_slide5(Scene):
    def construct(self):
        
        START_6 = (-2,0,0)
        END_6 =   (2,0,0)

        line_6 = Line(START_6,END_6)


        point_1 = Dot((1,0,0),color = RED)
        point_2 = Dot((-1,0,0),color = RED)
        point_3 = Dot((1,0,0),color = RED)


        line1 = Line(point_3,START_6)
        line2 = Line(point_3,END_6)
        a_1 = Brace(line1,UP)
        # a_1.set_color_by_tex("AC", BLUE)
        # a_1.move_to((0.5*LEFT+0.3*UP))
        # a_1.scale(0.75)

        b_1 = Brace(line2,UP)
        # b_1.set_color_by_tex("CB", GREEN)
        # b_1.move_to(1.5*RIGHT+0.3*UP)
        # b_1.scale(0.75)
        
        brace_1=Brace(line_6,DOWN)
        brace_1.set_color(color=BLACK)

        ab_1 = Tex("(AC + CB)")
        ab_1.next_to(brace_1, DOWN)
        ab_1.scale(0.75)
        A = Dot(START_6)
        B = Dot(END_6)
        a = Tex("A").next_to(A,LEFT)
        b = Tex("B").next_to(B,RIGHT)
        self.play(ShowCreation(line_6),ShowCreation(B),ShowCreation(A),ShowCreation(b),ShowCreation(a))
        self.wait(1)
        self.play(FadeIn(point_1))

        self.play(Transform(point_1, point_2), run_time = 2.5)
        self.play(Transform(point_1, point_3), run_time = 1.8)
        c = Tex("C").next_to(point_3,UP)
        self.play(Write(c))
        self.play(Write(a_1))
        self.play(Write(b_1))
        self.play(GrowFromCenter(brace_1))
        self.play(Write(ab_1), run_time = 1.5)
        self.wait(3)


class axioms_slide6(Scene):
    def construct(self):
       
        lineB = Line(ORIGIN,3*RIGHT)
        alpha = PI/4
        beta = 2*PI/3
        lineA = lineB.copy().rotate_about_origin(alpha)
        lineC = lineB.copy().rotate_about_origin(beta)
        
        arc1 = Sector(0,alpha,outer_radius = 0.65,fill_color = TEAL)
        arc2 = Sector(alpha,beta-alpha,outer_radius = 0.65,fill_color = BLUE)
        # arc22 = Arc(alpha,beta-alpha,radius = 0.45)
        # arc222 = VGroup(arc2,arc22)
        arc = Arc(0,beta,radius = 0.7)
        lineA1 = Line(ORIGIN,0.7*RIGHT)
        lineA2 = Line(ORIGIN,[0.7*np.cos(beta),0.7*np.sin(beta),0])
        full_angle = VGroup(arc,lineA1,lineA2)
        dotA  = Dot(ORIGIN)
        
        self.play(ShowCreation(dotA))
        self.play(ShowCreation(lineB))
        self.play(ShowCreation(lineC))
        self.play(ShowCreation(full_angle))
        self.wait()
        o=3*RIGHT+2*UP
        self.play(full_angle.animate.move_to(o+0.32*UP+0.164*RIGHT))
        self.wait()
        self.play(ShowCreation(lineA))
        self.wait()
        self.play(ShowCreation(arc1))
        self.play(ShowCreation(arc2))
        self.play(arc1.animate.move_arc_center_to(o))
        self.play(arc2.animate.move_arc_center_to(o))
        self.wait(3)




class axioms_slide7(Scene):
    def construct(self):
        lineAB = Line(2*UP-2*RIGHT,3*UP+3*RIGHT)
       
        dotA  = SmallDot(2*UP-2*RIGHT)
        dotB  = SmallDot(3*UP+3*RIGHT)
        
        otrezok = VGroup(lineAB,dotA,dotB)

        lineC = Line(-1*UP-2*RIGHT,-2*UP+3*RIGHT)
       
        dotC  = SmallDot(-1*UP-2*RIGHT)
        self.play(ShowCreation(dotA),ShowCreation(dotB))
        self.play(ShowCreation(lineAB))
        
        self.wait()
        self.play(ShowCreation(dotC))
        self.play(ShowCreation(lineC))
        
        self.play(otrezok.shift,3*DOWN)
        self.wait(3)


class axioms_slide10(Scene):
    def construct(self):

        lineA = Line(1*DOWN+3*LEFT,3*UP+2*RIGHT)
        lineB = Line(3*DOWN+3*LEFT,1*UP+2*RIGHT)
        
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.wait()
        
        self.play(Rotate(lineA,-PI/3))
        d = line_intersection([lineA.get_start(),lineA.get_end()],[lineB.get_start(),lineB.get_end()])
        D=SmallDot(d).set_color(RED)
        self.play(ShowCreation(D))
        self.wait(3)


class axioms_slide11(Scene):
  

    def construct(self):

        lineA = Line(1*UP+3*LEFT,1*UP+2*RIGHT)
        lineB = Line(1*DOWN+3*LEFT,-1*UP+2*RIGHT)
        lineC  = Line(3*DOWN-1*LEFT,3*UP-1*RIGHT)
        
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.wait()
        self.play(ShowCreation(lineC))
        r = 0.3

        a1 = Angle(lineA,lineC,r-0.1,(1,1))
        a3 = Angle(lineA,lineC,r-0.1,(-1,-1))

        a2 = Angle(lineC,lineA,r,(-1,1))
        a22 = Angle(lineC,lineA,r+0.1,(-1,1))
        a4 = Angle(lineC,lineA,r,(1,-1))
        a44 = Angle(lineC,lineA,r+0.1,(1,-1))
        self.play(ShowCreation(a1),ShowCreation(a3))
        self.wait()
        self.play(ShowCreation(a2),ShowCreation(a22),ShowCreation(a4),ShowCreation(a44))
        b1 = Angle(lineB,lineC,r-0.1,(1,1))
        b3 = Angle(lineB,lineC,r-0.1,(-1,-1))

        b2 = Angle(lineC,lineB,r,(-1,1))
        b22 = Angle(lineC,lineB,r+0.1,(-1,1))
        b4 = Angle(lineC,lineB,r,(1,-1))
        b44 = Angle(lineC,lineB,r+0.1,(1,-1))
        self.play(ShowCreation(b1),ShowCreation(b3))
        self.wait()
        self.play(ShowCreation(b2),ShowCreation(b22),ShowCreation(b4),ShowCreation(b44))

        t1 = Tex("1").next_to(a1,UP).shift(-0.3*LEFT)
        t2 = Tex("2").next_to(a44,LEFT).shift(-0.3*DOWN)
        t3 = Tex("3").next_to(a3,DOWN).shift(0.3*LEFT)
        t4 = Tex("4").next_to(a22,RIGHT).shift(0.3*DOWN)
        t5 = Tex("5").next_to(b1,UP).shift(-0.3*LEFT)
        t6 = Tex("6").next_to(b22,RIGHT).shift(0.3*DOWN)
        t7 = Tex("7").next_to(b3,DOWN).shift(0.3*LEFT)
        t8 = Tex("8").next_to(b44,LEFT).shift(-0.3*DOWN)
        self.play(Write(t1),Write(t2),Write(t3),Write(t4),Write(t5),Write(t6),Write(t7),Write(t8))
        self.wait(3)