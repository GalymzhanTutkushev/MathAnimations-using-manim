from manimlib import *
import numpy as np


class circle_slide1(Scene):
    def construct(self):
        np = NumberPlane()
        self.add(np)
        
        line_r1 = Line(ORIGIN,2*RIGHT)
        dot = SmallDot(2*RIGHT)
   
        o = SmallDot(ORIGIN)
        c = Circle(radius = 2)
        c.move_to(ORIGIN)
        arc = Arc(start_angle=0,angle=1,radius = 2)
        arc.set_color(RED)
        self.play(ShowCreation(o))
        self.play(ShowCreation(line_r1))
        self.play(ShowCreation(dot))
        self.play(ShowCreation(c),Rotate(line_r1,TAU,about_point = ORIGIN),
        Rotate(dot,TAU,about_point = ORIGIN),run_time = play_time)
        O_tex = Tex("O").next_to(o,DOWN)
        brace = Brace(line_r1,UP)
        r_tex = Tex("r").next_to(brace,UP)
        self.play(Write(O_tex))
        self.play(Write(brace),Write(r_tex))
        self.wait(pause_time)

class circle_slide2(Scene):
    def construct(self):
        R = 2
        c = Circle(radius = R)
        c.move_to(ORIGIN)
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,DOWN)
       
        # cord = Line(3*LEFT+2*DOWN,-2*LEFT-3*DOWN)
        # diametr = Line(3*LEFT+2*DOWN,-3*LEFT-2*DOWN)
        M = SmallDot([R*np.cos(60*DEGREES),R*np.sin(60*DEGREES),0])
        N = SmallDot([R*np.cos(190*DEGREES),R*np.sin(190*DEGREES),0])
        M1 = SmallDot([R*np.cos(60*DEGREES),R*np.sin(60*DEGREES),0])
        N1 = SmallDot([R*np.cos(240*DEGREES),R*np.sin(240*DEGREES),0])
        m = Tex("M").next_to(M,UP)
        n = Tex("N").next_to(N,LEFT)
        m1 = Tex("M").next_to(M1,UP)
        n1 = Tex("N").next_to(N1,DOWN)
        D= Tex("D=2R").to_edge(UP)
        cord = Line(M,N)
        diametr = Line(M1,N1)
        self.play(Write(c))
        self.play(Write(O),Write(o))
        self.play(Write(cord))
        self.play(Write(N),Write(n),Write(M),Write(m))
        self.wait(pause_time)
        self.play(ReplacementTransform(cord,diametr),ReplacementTransform(N,N1),ReplacementTransform(n,n1))
        diam = VGroup(diametr,M,N1)
        self.play(FadeOut(n1),FadeOut(m),FadeOut(o),Rotate(diam,-PI/3))
        d_brace = Brace(diametr,DOWN)
        d_tex = Tex("D").next_to(d_brace,DOWN)
        r1 = Line(ORIGIN,R*RIGHT)
        r2 = Line(ORIGIN,-R*RIGHT)
        brace_r1 = Brace(r1,UP)
        brace_r2 = Brace(r2,UP)
        r1_tex = Tex("R").next_to(brace_r1,UP)
        r2_tex = Tex("R").next_to(brace_r2,UP)
        self.play(Write(D),Write(d_brace),Write(d_tex))
        self.play(Write(r1_tex),Write(brace_r1),Write(r2_tex),Write(brace_r2))
        # self.play(Write(N1),Write(n1),Write(M1),Write(m1))
        self.wait(pause_time)


class circle_slide3(Scene):
    def construct(self):
        R = 2
       
        c = Circle(radius = R).set_color(PURPLE)
        c.move_to(3*RIGHT)
        c2 = Circle(radius = R).set_color(TEAL)
        # c2.set_fill(TEAL,1)
        c2.move_to(3*LEFT)
        tc = Text("Окружность").next_to(c,DOWN)
        tc2 = Text("Круг").next_to(c2,DOWN)
        self.play(ShowCreation(c))
        self.play(ShowCreation(c2))
        self.play(c2.animate.set_fill(TEAL,1))
        self.play(Write(tc))
        self.play(Write(tc2))
        self.wait(pause_time)

class circle_slide4(Scene):
    def construct(self):
        R = 2
        start = 0*DEGREES
        end = 30*DEGREES
        c = Circle(radius = R)
        c.move_to(ORIGIN)
        M = [R*np.cos(end),R*np.sin(end),0]
        N = [R*np.cos(start),R*np.sin(start),0]
        m = SmallDot(M)
        n = SmallDot(N)
        m_tex = Tex("M").next_to(m,RIGHT)
        n_tex = Tex("N").next_to(n,RIGHT)
        arc = Arc(start_angle=start,angle=end,radius = R).set_color(RED)
        arc2 = Arc(start_angle=start,angle=end,radius = 0.5)
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,UP)
        lineM = Line(ORIGIN,M)
        lineN = Line(ORIGIN,N)
  
        self.play(ShowCreation(c))
        self.play(ShowCreation(o),ShowCreation(O))
        self.play(ShowCreation(m_tex),ShowCreation(m))
        self.play(ShowCreation(n_tex),ShowCreation(n))
        self.play(ShowCreation(arc))
        self.play(ShowCreation(lineM),ShowCreation(lineN))
        self.play(ShowCreation(arc2))
        self.wait(pause_time)


class circle_slide5(Scene):
    def construct(self):
        R = 2
        start = 0*DEGREES
        end = 75*DEGREES
        c = Circle(radius = R)
        c.move_to(ORIGIN)
        M = [R*np.cos(end),R*np.sin(end),0]
        N = [R*np.cos(start),R*np.sin(start),0]
        m = SmallDot(M)
        n = SmallDot(N)
        m_tex = Tex("M").next_to(m,UP)
        n_tex = Tex("N").next_to(n,RIGHT)
        arc = Arc(start_angle=start,angle=end,radius = R).set_color(RED)
        arc2 = VMobject()
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,DOWN)
        lineM = Line(ORIGIN,M)
        lineN = Line(ORIGIN,N)
        MN = Line(M,N)
        line = Line(R*RIGHT,R*RIGHT+TAU*R*(end-start)/(360*DEGREES)*UP)
        line.set_color(RED)
        self.play(ShowCreation(c))
        self.play(ShowCreation(o),ShowCreation(O))
        self.play(ShowCreation(m_tex),ShowCreation(m))
        self.play(ShowCreation(n_tex),ShowCreation(n))
        self.play(ShowCreation(lineM),ShowCreation(lineN))
        self.play(ShowCreation(arc))
        self.save_state()
        self.play(ShowCreation(MN))
        self.play(ReplacementTransform(arc,line))
        self.play(line.animate.shift(RIGHT))
        
        self.play(MN.animate.rotate(-90*DEGREES+((180*DEGREES-(end-start)))/2))
        self.play(MN.animate.next_to(line,RIGHT,buff = SMALL_BUFF))
        self.wait(pause_time)
        self.restore()
        self.remove(arc)
        m_group = VGroup(lineM,m)
        always(m_tex.next_to,M,UP)
        arc2.add_updater(lambda x: x.become(Arc(0,lineM.get_angle(),radius=R)).set_stroke(RED))
        self.add(arc2)
        self.play(Rotate(m,-(end-end/3),about_point = ORIGIN),Rotate(lineM,-(end-end/3),about_point = ORIGIN),run_time = 5)
        
        self.wait(pause_time)


class circle_slide6(Scene):
    def construct(self):
        np1 = NumberPlane()
        self.add(np1)

        R = 3
        start = 0*DEGREES
        end = 57.2958*DEGREES
        c = Circle(radius = R)
        c.move_to(ORIGIN)
        c2 = Circle(radius = R/2)
        c2.move_to(ORIGIN)
        M = [R*np.cos(end),R*np.sin(end),0]
        N = [R*np.cos(start),R*np.sin(start),0]
        m = SmallDot(M)
        n = SmallDot(N)
        m_tex = Tex("M").next_to(m,UP)
        n_tex = Tex("N").next_to(n,RIGHT)
        arc = Arc(start_angle=start,angle=end,radius = R).set_color(RED)
        arc2 = Arc(start_angle=start,angle=end,radius = R/2).set_color(RED)
        line = Line(R*RIGHT,R*RIGHT+TAU*R*(end-start)/(360*DEGREES)*UP).set_color(RED)
        line2 = Line(R/2*RIGHT,R/2*RIGHT+TAU*R/2*(end-start)/(360*DEGREES)*UP).set_color(RED)
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,DOWN)
        lineM = Line(ORIGIN,M)
        lineN = Line(ORIGIN,N)
        lineN2 = Line(ORIGIN,R/2*RIGHT)
        brace_r1 = Brace(lineN2,UP,buff=SMALL_BUFF)
        brace_r2 = Brace(lineN,DOWN,buff=SMALL_BUFF)
        brace_l2 = Brace(line,RIGHT,buff=SMALL_BUFF)
        brace_l1 = Brace(line2,RIGHT,buff=SMALL_BUFF)
        r1 = Tex("R").next_to(brace_r1,UP,buff=SMALL_BUFF).scale(0.5)
        r2 = Tex("2R").next_to(brace_r2,DOWN).scale(0.5)
        l1 = Tex("L").next_to(brace_l1,RIGHT,buff=SMALL_BUFF).scale(0.5)
        l2 = Tex("2L").next_to(brace_l2,RIGHT,buff=SMALL_BUFF).scale(0.5)
        self.play(ShowCreation(c))
        self.play(ShowCreation(c2))
        self.play(ShowCreation(o),ShowCreation(O))
        self.wait()
        self.play(Write(brace_r2),Write(r2))
        self.play(Write(brace_r1),Write(r1))
        self.wait()
        self.play(ShowCreation(m_tex),ShowCreation(m))
        self.play(ShowCreation(n_tex),ShowCreation(n))
        self.play(ShowCreation(lineM),ShowCreation(lineN))
        self.play(ShowCreation(arc))
        self.play(ShowCreation(arc2))
        self.wait()
        self.play(Transform(arc,line))
        self.play(Transform(arc2,line2))
        self.play(Write(brace_l2),Write(l2))
        self.play(Write(brace_l1),Write(l1))
        self.wait(pause_time)


class circle_slide7(Scene):
    def construct(self):
        np = NumberPlane()
        self.add(np)
        line = Line(2*RIGHT,ORIGIN)
        line.set_color(RED)
        line_r1 = Line(2*RIGHT,ORIGIN)
        line_r1.set_color(GREEN)
        line_r2 = line_r1.copy().rotate(1,about_point = ORIGIN)
        c = Circle(radius = 2)
        c.move_to(ORIGIN)
        arc = Arc(start_angle=0,angle=1,radius = 2)
        arc.set_color(RED)
        self.play(ShowCreation(c))
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,LEFT)
        brace = Brace(line,DOWN)
        r_tex = Tex("r").next_to(brace,DOWN)
     
        

        self.play(ShowCreation(O))
        self.play(ShowCreation(o))
        self.play(ShowCreation(line))
        self.play(Write(brace),Write(r_tex))
        self.play(Rotating(line, -PI/2,about_point = 2*RIGHT),run_time = 2)
        self.play(ReplacementTransform(line,arc))
        self.play(ShowCreation(line_r1),ShowCreation(line_r2))
        ac = arc.copy()
        lc1 = line_r1.copy()
        lc2 = line_r2.copy()
        # self.play(Rotating(ac, 1,about_point = ORIGIN),Rotating(lc1,1,about_point = ORIGIN),
        # Rotating(lc2, 1,about_point = ORIGIN),run_time = 2)
        # self.play(Rotating(ac.copy(),1,about_point = ORIGIN),Rotating(lc1.copy(),1,about_point = ORIGIN),
        # Rotating(lc2.copy(),1,about_point = ORIGIN),run_time = 2)
        self.wait(pause_time)

class circle_3rad(Scene):
    def construct(self):

        np = NumberPlane()
        self.add(np)
        rad1 = Text("1 рад.")
        rad2 = Text("2 рад.")
        rad3 = Text("3 рад.")
        rad1.to_edge(UP)
        rad2.to_edge(UP)
        rad3.to_edge(UP)

        line = Line(2*RIGHT,ORIGIN)
        line.set_color(RED)
        line_r1 = Line(2*RIGHT,ORIGIN)
        line_r1.set_color(GREEN)
        line_r2 = line_r1.copy().rotate(1,about_point = ORIGIN)
        c = Circle(radius = 2)
        c.move_to(ORIGIN)
        arc = Arc(start_angle=0,angle=1,radius = 2)
        arc.set_color(RED)
        self.play(ShowCreation(c))
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,DOWN)
        self.play(ShowCreation(O),ShowCreation(o))
        self.play(Rotating(line, -PI/2,about_point = 2*RIGHT),run_time = 2)
        self.play(ReplacementTransform(line,arc))
        self.play(ShowCreation(line_r1),ShowCreation(line_r2))
        self.play(Write(rad1))
        ac = arc.copy()
        lc1 = line_r1.copy()
        lc2 = line_r2.copy()
        self.play(Rotating(ac, 1,about_point = ORIGIN),Rotating(lc1,1,about_point = ORIGIN),
        Rotating(lc2, 1,about_point = ORIGIN),run_time = 2)
        self.play(ReplacementTransform(rad1,rad2))
        self.play(Rotating(ac.copy(),1,about_point = ORIGIN),Rotating(lc1.copy(),1,about_point = ORIGIN),
        Rotating(lc2.copy(),1,about_point = ORIGIN),run_time = 2)
        self.play(ReplacementTransform(rad2,rad3))
        self.wait(pause_time)


class circle_slide9(Scene):
    def construct(self):
       
        R = 1
        c = Circle(radius = R).set_color(BLACK)
        c.move_to(+LEFT)
        tip = Polygon(R*DOWN+LEFT,0.1*LEFT+R*DOWN+0.1*UP+LEFT,0.1*RIGHT+R*DOWN+0.1*UP+LEFT)
        tip.set_color(BLUE)
        
        line = Line(ORIGIN+LEFT,R*DOWN+LEFT)
        arc2 = VMobject().set_color(RED)
        gr = VGroup(c,tip,line)

        square2 = gr.set_x(-5)

        path = Line(LEFT,LEFT+TAU*R*RIGHT,stroke_opatity=0.5)
        # path.points[1:3] += UP*2

        square2.save_state()
        def update_rotate_move(mob,alpha):
            square2.restore()
            square2.move_to(path.point_from_proportion(alpha))
            square2.rotate(-TAU*alpha)

        
        arc1 = Arc(-PI/2,-TAU).set_color(BLUE)
        
        d1 = SmallDot((R+0.03)*DOWN+LEFT).set_color(ORANGE).scale(0.5)
        l1 = Line((R+0.03)*DOWN+LEFT, (R+0.03)*DOWN+TAU*RIGHT+LEFT)
        l2 = VMobject()

        self.add(square2)
        self.add(d1, l2,line)
        
        l2.add_updater(lambda x: x.become(Line(R*DOWN+LEFT, d1.get_center()).set_color(RED)))
        arc2.add_updater(lambda x: x.become(Arc(-PI/2,TAU-(d1.get_center()-((R+0.03)*DOWN+LEFT))[0]/R,radius=R+0.03).shift((R+0.03)*UP).shift(d1.get_center())).set_stroke(RED))
        
        
        self.add(arc2)
        self.play(UpdateFromAlphaFunc(square2,update_rotate_move),
        MoveAlongPath(d1, l1),
        
        rate_func=linear,run_time = 8)

        self.wait(pause_time)

        
class circle_slide11(Scene):
    def construct(self):
        
        t360 = Tex("360^\\circ\\longleftrightarrow 2\\pi").to_edge(UP)
        t180 = Tex("180^\\circ\\longleftrightarrow \\pi").to_edge(UP)
        t90 = Tex("90^\\circ\\longleftrightarrow \\frac{\pi}{2}").to_edge(UP)
        t60 = Tex("60^\\circ\\longleftrightarrow \\frac{\pi}{3}").to_edge(UP)
        t45 = Tex("45^\\circ\\longleftrightarrow \\frac{\pi}{4}").to_edge(UP)
        t30 = Tex("30^\\circ\\longleftrightarrow \\frac{\pi}{6}").to_edge(UP)
        ts = [t30,t45,t60,t90,t180,t360]
        angles = [30*DEGREES,45*DEGREES,60*DEGREES,90*DEGREES,180*DEGREES,360*DEGREES]
        np1 = NumberPlane()
        self.add(np1)
        R = 2
        O = SmallDot(ORIGIN)
        o = Tex("O").next_to(O,DOWN)
        start = 0*DEGREES
            # end = 75*DEGREES
        c = Circle(radius = R)
        c.move_to(ORIGIN)
        self.play(ShowCreation(c))
        self.play(ShowCreation(o),ShowCreation(O))
        for end,t in zip(angles,ts):
           
            
            M = [R*np.cos(end),R*np.sin(end),0]
            N = [R*np.cos(start),R*np.sin(start),0]
            m = SmallDot(M)
            n = SmallDot(N)

            m_tex = Tex("M")
            if (end ==180*DEGREES):
                m_tex.next_to(m,LEFT)
            else:
                m_tex.next_to(m,UP)
            n_tex = Tex("N").next_to(n,RIGHT)
            arc2 = Arc(start_angle=start,angle=end,radius = 0.5).set_color(RED)
            arc = Arc(start_angle=start,angle=end,radius = R).set_color(RED)
            
           
            lineM = Line(ORIGIN,M)
            lineN = Line(ORIGIN,N)
            
            self.play(ShowCreation(m_tex),ShowCreation(m),ShowCreation(n_tex),ShowCreation(n))
            self.play(ShowCreation(lineM),ShowCreation(lineN))
            self.play(ShowCreation(arc),ShowCreation(arc2))
            self.play(Write(t))
            
            self.wait(pause_time)
            self.play(FadeOut(arc2),FadeOut(arc),FadeOut(t),FadeOut(m),FadeOut(n),FadeOut(m_tex),FadeOut(n_tex),FadeOut(lineN),FadeOut(lineM))


class circle_slide12(Scene):
    def construct(self):
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
        lineA =Line([r*PI,r,0],[r*PI,r,0])
        lineB =Line([-r*PI,r,0],[0,0,0])
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
        self.wait()
        self.wait(pause_time)

class circle_slide12a(Scene):
    def construct(self):
        nnn = NumberPlane()
        self.add(nnn)
        n=6
        R=2
        sec = Sector(outer_radius = R,angle = 2*PI/n)
        sec_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        sec_group.set_stroke(color=BLACK, width = 3)
        sec_group.set_fill(color=BLUE, opacity = 0.5)
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
        sec_group.set_fill(color=BLUE, opacity = 0.5)
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
        self.play(FadeOut(sec_group))

        n=30
        R=2
        secUP = Sector(start_angle = (n/2-1)/2*2*PI/n,outer_radius = R,angle = 2*PI/n)
        sec_groupUP = VGroup(*[
                    secUP.copy().shift(2*x*R*np.sin(PI/n)*RIGHT)
                    for x in range(int(n/2))
                ])
        sec_groupUP.shift(R*np.sin(PI/n)*LEFT*(n-2)/2)
        sec_groupUP.shift(R*np.cos(PI/n)*DOWN)
        sec_groupUP.set_stroke(color=BLACK, width = 3)
        sec_groupUP.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(sec_groupUP))

        self.wait()
       
        secDOWN = Sector(start_angle = -((n/2-1)/2+1)*2*PI/n,outer_radius = R,angle = 2*PI/n)
        sec_groupDOWN = VGroup(*[
                    secDOWN.copy().shift(2*x*R*np.sin(PI/n)*RIGHT)
                    for x in range(int(n/2))
                ])
        sec_groupDOWN.shift(2*R*np.sin(PI/n)*LEFT*n/4)
        sec_groupDOWN.set_stroke(color=BLACK, width = 3)
        sec_groupDOWN.set_fill(color=BLUE, opacity = 0.5)
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
        self.wait(pause_time)


class circle_slide12b(Scene):
    CONFIG = {
        "circle_style": {
            "fill_color": PURPLE,
            "fill_opacity": 0,
            "stroke_color": GREEN,
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
        s= Tex("S=","{2\\pi R","\\cdot R","\\over 2}","=\\pi R^2").to_edge(UP)
        self.play(Write(s[0]))
        self.wait()
        self.play(
            radii_lines[2:].shift, 2.9 * RIGHT,
            R_labels[2:].shift, 2.9 * RIGHT,
            VGroup(
                radii_lines[:2], R_labels[:2]
            ).to_edge, LEFT, {"buff": 5.0}
        )
        self.play(
            unwrap_factor_tracker.set_value, 1,
            run_time=3
        )
        self.wait(pause_time)
        pir = Tex("2\\pi R").next_to(radii_lines,DOWN).shift(3*RIGHT)
        self.play(Write(pir))
        self.wait(pause_time)
        self.play(Write(s[1]))
        self.play(Write(s[2]))
        self.play(Write(s[3]))
        self.play(Write(s[4]))
        self.wait(pause_time)
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