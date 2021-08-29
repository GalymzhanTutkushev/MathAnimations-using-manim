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

class rect_slide1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)
        
        a = 3
        b = 6
        A = a/2*UP+b/2*RIGHT
        B = -a/2*UP+b/2*RIGHT
        C = -a/2*UP-b/2*RIGHT
        D = a/2*UP-b/2*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(D)

        a_tex = Tex("B")
        
        b_tex = Tex("C")
        c_tex = Tex("D")
        d_tex = Tex("A")
       
        AB = Line(A,B)
        BC = Line(B,C)
        CD = Line(C,D)
        DA = Line(D,A)

        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd))

        
        always(a_tex.next_to,Ad,UP)
        always(b_tex.next_to,Bd,DOWN)
        always(c_tex.next_to,Cd,DOWN)
        always(d_tex.next_to,Dd,UP)
        elA = Elbow(angle=0,width=0.2).rotate(PI).move_to(A+0.1*DOWN+0.1*LEFT)
        elB = Elbow(angle=0,width=0.2).rotate(PI/2).move_to(B-0.1*DOWN+0.1*LEFT)
        elC = Elbow(angle=0,width=0.2).move_to(C-0.1*DOWN-0.1*LEFT)
        elD = Elbow(angle=0,width=0.2).rotate(-PI/2).move_to(D+0.1*DOWN-0.1*LEFT)
        self.wait()
        self.play(Write(a_tex),Write(b_tex),Write(c_tex),Write(d_tex))
        self.wait()
        self.play(Write(elA),Write(elB),Write(elC),Write(elD))
        self.wait()
        rect = VGroup(AB,BC,CD,DA,Ad,Bd,Cd,Dd,elA,elB,elC,elD)
        self.play(Rotate(rect,16*DEGREES))

        self.wait(pause_time)

class rect_slide3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)
        a = 3
        b = 6
        A = a/2*UP+b/2*RIGHT
        B = -a/2*UP+b/2*RIGHT
        C = -a/2*UP-b/2*RIGHT
        D = a/2*UP-b/2*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(D)

        a_tex = Tex("A").next_to(Ad,UP)
        b_tex = Tex("B").next_to(Bd,DOWN)
        c_tex = Tex("C").next_to(Cd,DOWN)
        d_tex = Tex("D").next_to(Dd,UP)
       
        AB = Line(A,B)
        BC = Line(B,C)
        CD = Line(C,D)
        DA = Line(D,A)

        AC = Line(A,C)
        BD = Line(B,D)
        O=Dot(ORIGIN)
        pr = Line(ORIGIN,a/2*DOWN)
        el = Elbow(width=0.2,angle=0)
        el.shift(a/2*DOWN)
        pr2 = Line(ORIGIN,b/2*LEFT)
        el2 = Elbow(width=0.2,angle=0)
        el2.shift(b/2*LEFT)
        r1 = get_risk(AC,n=1,pr=3/8,rt=0.025)
        r2 = get_risk(AC,n=1,pr=8/3,rt=0.025)
        r3 = get_risk(BD,n=1,pr=3/8,rt=0.025)
        r4 = get_risk(BD,n=1,pr=8/3,rt=0.025)

        r11 = get_risk(BC,n=1,pr=3/8,rt=0.025)
        r22 = get_risk(BC,n=1,pr=8/3,rt=0.025)
        r11 = VGroup(r11.copy().shift(0.15*LEFT),r11)
        r22 = VGroup(r22.copy().shift(-0.15*LEFT),r22)
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd))
        self.wait()
        self.play(Write(a_tex),Write(b_tex),Write(c_tex),Write(d_tex))
        self.play(ShowCreation(AC),ShowCreation(BD))
        self.wait()
        self.play(ShowCreation(O))
        self.wait()
        self.play(Write(r1),Write(r2),Write(r3),Write(r4))
        self.wait()
        self.play(Write(pr),Write(el))
        self.play(Write(r11),Write(r22))
        self.wait(pause_time)

class rect_slide4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)
        a = 3
        b = 6
        A = a/2*UP+b/2*RIGHT
        B = -a/2*UP+b/2*RIGHT
        C = -a/2*UP-b/2*RIGHT
        D = a/2*UP-b/2*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(D)
       
        AB = Line(A,B).set_stroke(BLUE,7)
        BC = Line(B,C).set_stroke(PURPLE,7)
        CD = Line(C,D).set_stroke(BLUE,7)
        DA = Line(D,A).set_stroke(PURPLE,7)

        a_tex = Tex("a").next_to(AB,RIGHT)
        b_tex = Tex("b").next_to(BC,DOWN)
        a2 = Tex("2a")
        b2 = Tex("2b")
        p = Tex("P=","2a","+","2b").to_edge(UP)
        p[1].set_color(BLUE)
        p[3].set_color(PURPLE)
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DA))

        self.play(Write(a_tex),Write(b_tex))
        self.play(Write(p[0]))
        self.wait()
        self.play(FadeOut(a_tex),FadeOut(b_tex))
        self.play(CD.animate.shift(LEFT))
        self.play(AB.animate.next_to(CD,1*RIGHT))
        a2.next_to(CD,DOWN)
        self.play(Write(a2))
        self.play(TransformFromCopy(a2,p[1]))
        self.play(DA.animate.shift(2.8*DOWN))
        self.play(Write(p[2]))
        b2.next_to(BC,DOWN)
        self.play(Write(b2))
        self.play(TransformFromCopy(b2,p[3]))

        self.wait(pause_time)

class rect_slide5(Scene):
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)
        

        w = 6
        h = 3
        rectangle =Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP,h*UP,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
       
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
        self.wait(pause_time)
        self.play(FadeOut(rectangle),FadeOut(rectangle_area),FadeOut(pb_label),FadeOut(pa_label))

class rect_slide6(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        a = 5
        b = a
        A = a/2*UP+b/2*RIGHT
        B = -a/2*UP+b/2*RIGHT
        C = -a/2*UP-b/2*RIGHT
        D = a/2*UP-b/2*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(D)

        per = Tex("P=4a")
        

        area = Tex("S=a^2")
        area.to_edge(UP)

        AB = Line(A,B)
        BC = Line(B,C)
        CD = Line(C,D)
        DA = Line(D,A)

        AC = DashedLine(A,C)
        BD = DashedLine(B,D)
        O=Dot(ORIGIN)
        a_tex = Tex("a").next_to(AB,UP)
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd))
        self.save_state()
        self.play(BC.animate.move_to(a/4*LEFT))
        
        
        self.play(BC.animate.rotate(90*DEGREES))
        self.play(DA.animate.move_to(-a/4*LEFT))
        self.play(DA.animate.rotate(90*DEGREES))
        per.next_to(O,DOWN,buff = 3)
        self.play(Write(per))
        self.wait(pause_time)
        self.restore()
        self.play(Write(a_tex))
        self.play(ShowCreation(AC),ShowCreation(BD))
        self.play(ShowCreation(O))

        self.wait(pause_time)