from manimlib import *
import numpy as np

class elem_slide1(Scene):
    def construct(self):
        lineA = Line(1*DOWN+3*LEFT,5*UP+2*RIGHT)
        lineB = Line(3*DOWN+3*LEFT,3*UP+2*RIGHT)
        lineC = Line(ORIGIN,3*RIGHT)
        dotA  = SmallDot(2*UP+3*RIGHT)
        dotB  = SmallDot(-2*UP-3*RIGHT)
        dotC  = SmallDot(1*UP+2*RIGHT)
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.wait(3)

class elem_slide2(Scene):
    def construct(self):
        lineA = Line(1*DOWN+3*LEFT,3*UP+2*RIGHT)
        lineB = Line(2*DOWN+2*LEFT,1*UP+3*RIGHT)
        lineC = Line(1*DOWN+3*LEFT,-2*UP+3*RIGHT)
        dotA  = SmallDot(1*DOWN+3*LEFT)
        dotB  = SmallDot(2*DOWN+2*LEFT)
        self.play(ShowCreation(dotB))
        # self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.wait()
        self.play(FadeOut(lineB),FadeOut(dotB))
        self.play(ShowCreation(dotA))
        self.play(ShowCreation(lineC))
        self.wait(3)



class elem_slide3(Scene):
    def construct(self):

        lineA = Line(1*DOWN+3*LEFT,3*UP+2*RIGHT)
        lineB = Line(3*DOWN+3*LEFT,1*UP+2*RIGHT)
        dot1 = line_intersection(lineA,lineB)
        print(dot1)
        dot = SmallDot(dot1)
        d = Tex("A")
        d.next_to(dot)
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.wait()
        self.play(lineA.rotate,-PI/4)
        self.wait(3)

class elem_slide4(Scene):
    def construct(self):
        d = SmallDot(3*UP)
        lineA = Line(3*LEFT,3*RIGHT)
        lineB = Line(3*UP,ORIGIN)
        lineC = Line(ORIGIN,3*RIGHT)
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(d))
        self.play(ShowCreation(lineB))
        el = Elbow(width=0.2,angle = 0)
        self.play(ShowCreation(el))
        self.wait(3)

class elem_slide5(Scene):
    def construct(self):
        lineA = Line(ORIGIN,2*UP+2*RIGHT)
        lineB = Line(ORIGIN,2*1.41*RIGHT)
        
        dotA  = SmallDot(ORIGIN)
        arc = Arc(start_angle=0,angle=PI/4,radius = 0.4).add_tip()
        arc1 = Arc(start_angle=PI/4,angle=TAU-PI/4,radius = 0.4,include_tip = True).set_color(TEAL).add_tip()
        self.play(ShowCreation(dotA))
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.wait()
        self.play(ShowCreation(arc))
        self.wait()
        self.play(FadeOut(arc))
        self.play(ShowCreation(arc1))
        self.wait(3)


class elem_slide6(Scene):
    
        
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)
        
        line_r1 = Line(ORIGIN,2*RIGHT)
        dot = SmallDot(2*RIGHT)
   
        o = SmallDot(ORIGIN)
        c = Circle(radius = 0.5)
        c.move_to(ORIGIN)
        arc = Arc(start_angle=0,angle=1,radius = 2)
        arc.set_color(RED)
        self.play(ShowCreation(o))
        self.play(ShowCreation(line_r1))
        # self.play(ShowCreation(dot))
        self.play(ShowCreation(c),Rotate(line_r1,TAU,about_point = ORIGIN),
        # Rotate(dot,TAU,about_point = ORIGIN),
        run_time = play_time)
       
        self.wait(pause_time)


class elem_slide8(Scene):
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)
        t1 = Text("Острый угол").to_edge(DOWN)
        t2 = Text("Прямой угол").to_edge(DOWN)
        t3 = Text("Тупой угол").to_edge(DOWN)
        lineA = Line(1*DOWN+2*LEFT,3*UP+2*RIGHT)
        lineB = Line(1*DOWN+2*LEFT,-1*UP+3*RIGHT)
        # dot1 = line_intersection(lineA,lineB)
        # print(dot1)
        dot = SmallDot(1*DOWN+2*LEFT)
        
        self.play(ShowCreation(dot))
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.play(Write(t1))
        self.wait()
        self.play(Rotate(lineA,PI/4,about_point = 1*DOWN+2*LEFT))
        self.play(ReplacementTransform(t1,t2))
        self.wait()
        self.play(Rotate(lineA,PI/3,about_point = 1*DOWN+2*LEFT))
        self.play(Transform(t2,t3))
        self.wait()
        self.wait(pause_time)


class elem_slide9(Scene):
    def construct(self):
        lineA = Line(3*LEFT,3*RIGHT)
        lineB = Line(3*DOWN+3*LEFT,3*UP+3*RIGHT)
        lineC = Line(ORIGIN,3*RIGHT)
        
        arc = Arc(start_angle=0,angle=PI/4,radius = 0.5)
        arc2 = Arc(start_angle=PI,angle=PI/4,radius = 0.5)

        arc3 = Arc(start_angle=PI/4,angle=3*PI/4,radius = 0.3)
        arc33 = Arc(start_angle=PI/4,angle=3*PI/4,radius = 0.35)
        arc4 = Arc(start_angle=5*PI/4,angle=3*PI/4,radius = 0.3)
        arc44 = Arc(start_angle=5*PI/4,angle=3*PI/4,radius = 0.35)
        self.play(ShowCreation(lineA))
        self.play(ShowCreation(lineB))
        self.play(ShowCreation(arc))
        self.play(ShowCreation(arc2))
        self.play(ShowCreation(arc3),ShowCreation(arc33))
        self.play(ShowCreation(arc4),ShowCreation(arc44))
        self.wait(3)


class elem_slide10(Scene):
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

class sm_angle(Scene):
    def construct(self):
        lineA = Line(ORIGIN,3*RIGHT)
        lineB = Line(ORIGIN,3*RIGHT)
        lineC = Line(ORIGIN,3*RIGHT)
        
        arc = Arc(start_angle=0,angle=PI/4,radius = 1)
        arc.add_tip()
        self.play(ShowCreation(lineA),ShowCreation(lineB))
        self.play(Rotating(lineB, PI, about_point=ORIGIN, run_time=2), run_time=2)
        self.play(Rotating(lineC, PI/4, about_point=ORIGIN, run_time=2), run_time=2)
        self.play(ShowCreation(arc))
        self.wait(3)
