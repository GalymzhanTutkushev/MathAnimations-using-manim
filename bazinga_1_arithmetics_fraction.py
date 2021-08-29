from manimlib import *


class slide2(Scene):
    def construct(self):
        f16 = Tex("\\frac{1}{6}")
        f16.move_to(2*UP+2*RIGHT)
        n = 3
        c = Circle(radius = 3)
        c.set_fill(color=BLUE, opacity = 0.5)
        c.set_stroke(BLACK)
        self.play(ShowCreation(c))
        self.wait()
        # sec = Sector(outer_radius = 3,angle = 2*PI/n)
        # sec.set_stroke(color = BLACK,width = 1,opacity =0 )
        # square_group = VGroup(*[
        #             sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
        #             for x in range(n)
        #         ])
        line = Line(3*DOWN,3*UP)
        line_group = VGroup(*[
                    line.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        f_group = VGroup(*[
                    f16.copy().move_to([2*np.sin(x/6*2*PI+PI/6),2*np.cos(x/6*2*PI+PI/6),0])
                    for x in range(2*n)
                ])
        # square_group.set_fill(color=BLUE, opacity = 0.5)
        # square_group.set_stroke(color=BLACK, width = 1,opacity=1)
        self.play(ShowCreation(line_group),run_time = 5)
        self.play(ShowCreation(f_group),run_time = 5)
        # square_group_part =  VGroup(*[square_group[i] for i in [0,1,2]])

        # self.play(square_group_part.set_fill,RED)
       
        self.wait(3)

class slide5(Scene):
    def construct(self):
        
        for n in range(6,11):

            f16 = Tex("\\frac{1}{"+str(n)+"}")
            f16.move_to(2*UP+1.8*RIGHT)
            # n = 3
            c = Circle(radius = 3)
            c.set_fill(color=BLUE, opacity = 0.5)
            c.set_stroke(BLACK)
            self.play(ShowCreation(c))
            self.wait()
            # sec = Sector(outer_radius = 3,angle = 2*PI/n)
            # sec.set_stroke(color = BLACK,width = 1,opacity =0 )
            # square_group = VGroup(*[
            #             sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
            #             for x in range(n)
            #         ])
            line = Line(ORIGIN,3*UP)
            line_group = VGroup(*[
                        line.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                        for x in range(n)
                    ])
            f_group = VGroup(*[
                        f16.copy().move_to([2*np.sin(x/n*2*PI+PI/n),2*np.cos(x/n*2*PI+PI/n),0])
                        for x in range(n)
                    ])
            # square_group.set_fill(color=BLUE, opacity = 0.5)
            # square_group.set_stroke(color=BLACK, width = 1,opacity=1)
            self.play(ShowCreation(line_group),run_time = 3)
            self.play(ShowCreation(f_group),run_time = 5)
            # square_group_part =  VGroup(*[square_group[i] for i in [0,1,2]])

            self.play(FadeOut(line_group),FadeOut(f_group))
        self.play(FadeOut(c))
        self.wait(3)
       

class slide6(Scene):
    def construct(self):
        f16 = Tex("\\frac{1}{9}")
        f16.to_corner(UR,buff = 2)
        f26 = Tex("\\frac{2}{9}")
        f26.to_corner(UR,buff = 2)
        f36 = Tex("\\frac{3}{9}")
        f36.to_corner(UR,buff = 2)
        f16.scale(2)
        f26.scale(2)
        f36.scale(2)
        n = 9
        sec = Sector(outer_radius = 3,angle = 2*PI/n)
        sec.set_stroke(color = BLACK,width = 3)


        square_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group),run_time = 3)

        square_group_part =  VGroup(*[square_group[i] for i in [0,1,2]])
        self.play(square_group_part[0].set_fill,RED)
        self.play(Write(f16))
        self.wait(1)
        self.play(square_group_part[1].set_fill,RED)
        self.play(ReplacementTransform(f16,f26))
        self.wait(1)
        self.play(square_group_part[2].set_fill,RED)
        self.play(ReplacementTransform(f26,f36))
        self.wait(3)



class slide7(Scene):
    def construct(self):
        n = 8
        line = Line(4*LEFT,4*RIGHT)
      
        self.play(ShowCreation(line))
        tick = Line(4*LEFT+0.1*DOWN,4*LEFT+0.1*UP)
        tick_group = VGroup(*[
                    tick.copy().shift(x*RIGHT)
                    for x in range(n+1)
                ])
        brace = Brace(line,DOWN)
        line8 = Line(4*LEFT,3*LEFT)
        line8.set_stroke(width = 8)
        line8.set_color(TEAL)
        
        x0 = Tex("0")
        x1 = Tex("1")
        x12 = Tex("\\frac{1}{2}")
        x0.move_to(0.9*DOWN+4*LEFT)
        x1.move_to(0.9*DOWN+4*RIGHT)
        x12.move_to(0.9*DOWN)
        x14 = Tex("\\frac{1}{4}")
        x14.move_to(0.9*DOWN+2*LEFT)
        x18 = Tex("\\frac{1}{8}")
        x18.move_to(0.9*DOWN+3*LEFT)
        self.play(Write(tick),Write(tick_group[8]))
        self.wait()  
        self.play(Write(x0),Write(x1))
        self.wait()  
        self.play(Write(x12),Write(tick_group[4]))
        self.wait()  
        self.play(Write(x14),Write(tick_group[2]),Write(tick_group[6]))
        self.wait() 
        self.play(Write(x18),Write(tick_group[1]),Write(tick_group[3]),Write(tick_group[5]),Write(tick_group[7]))
        self.play(Write(line8),FadeOut(x14),FadeOut(x12))
        d28=Tex("\\frac{2}{8}")
        d28.next_to(tick_group[2],DOWN)
        d38=Tex("\\frac{3}{8}")
        d38.next_to(tick_group[3],DOWN)
        d48=Tex("\\frac{4}{8}")
        d48.next_to(tick_group[4],DOWN)
        d58=Tex("\\frac{5}{8}")
        d58.next_to(tick_group[5],DOWN)
        self.play(line8.copy().shift,RIGHT,Write(d28))
        self.play(line8.copy().shift,2*RIGHT,Write(d38))
        self.play(line8.copy().shift,3*RIGHT,Write(d48))
        self.play(line8.copy().shift,4*RIGHT,Write(d58))
        self.wait(3)

class slide8(Scene):
    def construct(self):
        
        n = 6
        sec = Sector(outer_radius = 2,angle = 2*PI/n)
        sec.set_stroke(color = BLACK,width = 3)
        sec.shift(1.5*DOWN)

        square_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = 1.5*DOWN)
                    for x in range(n)
                ])
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)
        

        square_group_part =  VGroup(*[square_group[i] for i in [0,1,2,3,4,5]])
        
       
        n = 6
        line = Line(3*LEFT+3*UP,3*RIGHT+3*UP)
      
        self.play(ShowCreation(line))
        self.play(ShowCreation(square_group),run_time = 3)
        tick = Line(3*LEFT+0.1*DOWN+3*UP,3*LEFT+0.1*UP+3*UP)
        tick_group = VGroup(*[
                    tick.copy().shift(x*RIGHT)
                    for x in range(n+1)
                ])
        brace = Brace(line,DOWN)
        x0 = Tex("0")
        x1 = Tex("1")
        x0.move_to(2.3*UP+3*LEFT)
        x1.move_to(2.3*UP+3*RIGHT)
        x16 = Tex("\\frac{1}{6}")
        x16.move_to(2.3*UP+2*LEFT)
        x26 = Tex("\\frac{2}{6}")
        x26.move_to(2.3*UP+LEFT)
        x36 = Tex("\\frac{3}{6}")
        x36.move_to(2.3*UP)
        x46 = Tex("\\frac{4}{6}")
        x46.move_to(2.3*UP+RIGHT)
        x56 = Tex("\\frac{5}{6}")
        x56.move_to(2.3*UP+2*RIGHT)
        x66 = Tex("\\frac{6}{6}")
        x66.move_to(2.3*UP+3*RIGHT)
        self.play(Write(tick),Write(tick_group[6]))
        
        self.wait()  
        self.play(Write(x0),Write(x1))
        
        self.wait()  
        self.play(Write(x16),Write(tick_group[1]))
        self.play(square_group_part[0].set_fill,RED)
       
        self.wait()  
        self.play(Write(x26),Write(tick_group[2]))
        self.play(square_group_part[1].set_fill,RED)
        
        self.wait() 
        self.play(Write(x36),Write(tick_group[3]))
        self.play(square_group_part[2].set_fill,RED)
        
        self.wait()
        self.play(Write(x46),Write(tick_group[4]))
        self.play(square_group_part[3].set_fill,RED)
        self.wait()
        self.play(Write(x56),Write(tick_group[5]))
        self.play(square_group_part[4].set_fill,RED)
        self.wait()
        self.play(ReplacementTransform(x1,x66),Write(tick_group[6]))
        self.play(square_group_part[5].set_fill,RED)
        self.wait(3)

class slide9(Scene):
    def construct(self):
        l = 13
        u = 2
        line = Line(l/2*LEFT+u*UP,l/2*RIGHT+u*UP)
        n = 18
        self.play(ShowCreation(line))
        tick = Line(line.get_left()+0.1*UP,line.get_left()+0.1*DOWN)
        
        tick_line = Line(line.get_left(),line.get_left()+line.get_length()/n*RIGHT)
        line_group = VGroup(*[
                    tick_line.copy().shift(x*line.get_length()/n*RIGHT)
                    for x in range(n+1)
                ])
        line_group.set_color(RED)
        tick_group = VGroup(*[
                    tick.copy().shift(x*line.get_length()/n*RIGHT)
                    for x in range(n+1)
                ])
        brace = Brace(line,DOWN)
        x0 = Tex("0")
        x1 = Tex("1")
        x2 = Tex("2")
        x3 = Tex("3")

        x0.next_to(tick,DOWN)
        x1.next_to(tick_group[6],DOWN)
        x2.next_to(tick_group[12],DOWN)
        x3.next_to(tick_group[n],DOWN)

        n = 6
        sec = Sector(outer_radius = 2,angle = 2*PI/n)
        sec.set_stroke(color = BLACK,width = 1)

        square_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group.shift(4.5*LEFT)
        square_group.shift(1.5*DOWN)
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)

        sec2 = Sector(outer_radius = 2,angle = 2*PI/n)
        sec2.set_stroke(color = BLACK,width = 1)


        square_group2 = VGroup(*[
                    sec2.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group2.shift(ORIGIN)
        square_group2.shift(1.5*DOWN)
        square_group2.set_stroke(color=BLACK, width = 3)
        square_group2.set_fill(color=BLUE, opacity = 0.5)

        sec3 = Sector(outer_radius = 2,angle = 2*PI/n)
        sec3.set_stroke(color = BLACK,width = 1)
        square_group3 = VGroup(*[
                    sec3.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group3.shift(4.5*RIGHT)
        square_group3.shift(1.5*DOWN)
        square_group3.set_stroke(color=BLACK, width = 3)
        square_group3.set_fill(color=BLUE, opacity = 0.5)

        self.play(ShowCreation(square_group),ShowCreation(square_group2),ShowCreation(square_group3),
        Write(x1),Write(tick_group[n]),Write(x2),Write(tick_group[2*n]),
        Write(x0),Write(x3),Write(tick),Write(tick_group[3*n]),run_time = 3)
        self.wait(1)  

        for i in range(n):
            f = Tex("\\frac{"+str(i+1)+"}{6}")
            f.next_to(tick_group[i+1],UP)
            self.play(Write(f),Write(tick_group[i+1]),Write(line_group[i]),square_group[i].set_fill,RED)
        for i in range(n-1):
            f = Tex("\\frac{"+str(6+i+1)+"}{6}")
            f.next_to(tick_group[6+i+1],UP)
            fd = Tex("1\\frac{"+str(i+1)+"}{6}")
            fd.scale(0.8)
            fd.next_to(tick_group[6+i+1],DOWN)
            self.play(Write(fd),Write(f),Write(tick_group[i+1+6]),Write(line_group[6+i]),square_group2[i].set_fill,RED)
        f = Tex("\\frac{"+str(12)+"}{6}")
        f.next_to(tick_group[6+6],UP)
            
        self.play(Write(f),Write(tick_group[6+6]),Write(line_group[6+6-1]),square_group2[5].set_fill,RED)
        for i in range(1):
            f = Tex("\\frac{"+str(12+i+1)+"}{6}")
            f.next_to(tick_group[12+i+1],UP)
            fd = Tex("2\\frac{"+str(i+1)+"}{6}")
            fd.scale(0.8)
            fd.next_to(tick_group[12+i+1],DOWN)
            self.play(Write(fd),Write(f),Write(tick_group[i+1+12]),Write(line_group[i+12]),square_group3[i].set_fill,RED)

        
        

class slide11(Scene):
    def construct(self):
        div1 = Tex("{a","\\over", " n}","+","{b","\\over"," n}", "=", "{a","+","b","\\over", " n}")
#                           0      1       2    3    4      5      6      7    8   9   10     11      12

        div1.to_edge(UP)
        self.wait()
        plus = Tex("+")
        eq = Tex("=")
        plus.scale(2)
        eq.scale(2)
        n = 8
        sec = Sector(outer_radius = 2,angle = 2*PI/n)
        sec.set_stroke(color = BLACK,width = 1)


        square_group = VGroup(*[
                    sec.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group.shift(5*LEFT)
        square_group.shift(1.5*DOWN)
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)

        self.play(ShowCreation(square_group),Write(div1[0:3]),run_time = 5)

        square_group_part =  VGroup(*[square_group[i] for i in [0]])

        self.play(square_group_part[0].set_fill,RED)
        self.wait(1)
        plus.next_to(square_group)
        self.play(ShowCreation(plus),Write(div1[3]))

        sec2 = Sector(outer_radius = 2,angle = 2*PI/n)
        sec2.set_stroke(color = BLACK,width = 1)


        square_group2 = VGroup(*[
                    sec2.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group2.shift(ORIGIN)
        square_group2.shift(1.5*DOWN)
        square_group2.set_stroke(color=BLACK, width = 3)
        square_group2.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group2),Write(div1[4:7]),run_time = 5)

        square_group_part2 =  VGroup(*[square_group2[i] for i in [1,2]])


        
        self.play(square_group_part2.set_fill,RED)
        eq.next_to(square_group2)
        self.play(ShowCreation(eq),Write(div1[7]))
        self.wait(1)

        sec3 = Sector(outer_radius = 2,angle = 2*PI/n)
        sec3.set_stroke(color = BLACK,width = 1)


        square_group3 = VGroup(*[
                    sec3.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        square_group3.shift(5*RIGHT)
        square_group3.shift(1.5*DOWN)
        square_group3.set_stroke(color=BLACK, width = 3)
        square_group3.set_fill(color=BLUE, opacity = 0.5)
        self.play(
        ShowCreation(square_group3),run_time=2)

        square_group_part3 =  VGroup(*[square_group3[i] for i in [0,1,2]])
        square_group_part3.set_fill(RED)
        self.play(ReplacementTransform(div1[0].copy(),div1[8],path_arc = -PI/2),
        ReplacementTransform(div1[3].copy(),div1[9],path_arc = -PI/2),
        ReplacementTransform(div1[4].copy(),div1[10],path_arc = -PI/2),Write(div1[11:13]),
        ReplacementTransform(square_group_part.copy(),square_group_part3[0],path_arc = -PI/2),
        ReplacementTransform(square_group_part2.copy(),square_group_part3[1:3],path_arc = -PI/2),run_time =5)
        
        self.wait(3)
        

class slide12(Scene):
    def construct(self):
        div_mulc_eq = Tex("3","\\cdot","{5\\over 8}","=","{3","\\cdot", "5\\over 8}","={15\\over 8}")
        #                         0      1          2        3     4       5       6
        div_mulc_eq.to_edge(UP)
        
        n = 2
        m = 4
        s = 0.7
        square = Square(side_length = s)
        square.move_to(5*LEFT+1*UP)
        square_group = VGroup(*[
                    square.copy().shift(x*s*RIGHT + y*s*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=WHITE, opacity = 0.5)
        
        
        self.play(ShowCreation(square_group))
        square_group_part =  VGroup(*[square_group[i] for i in [0,1,3,5,7]])
        self.play(square_group_part.set_fill,BLUE)
        self.play(Write(div_mulc_eq[2]))
        self.wait(3)
        square2 = Square(side_length = s)
        square2.move_to(5*LEFT+1*DOWN)
        square_group2 = VGroup(*[
                    square2.copy().shift(x*s*RIGHT + y*s*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        square_group2.set_stroke(color=BLACK, width = 3)
        square_group2.set_fill(color=WHITE, opacity = 0.5)
        
        square_group_part2 =  VGroup(*[square_group2[i] for i in [0,1,3,5,7]])
        

        square3 = Square(side_length = s)
        square3.move_to(5*LEFT+3*DOWN)
        square_group3 = VGroup(*[
                    square3.copy().shift(x*s*RIGHT + y*s*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        square_group3.set_stroke(color=BLACK, width = 3)
        square_group3.set_fill(color=WHITE, opacity = 0.5)
        square_group_part3 =  VGroup(*[square_group3[i] for i in [0,1,3,5,7]])
        square_group_part2.set_fill(BLUE)
        square_group_part3.set_fill(BLUE)
        self.play(ShowCreation(square_group2),ShowCreation(square_group3),Write(div_mulc_eq[0:2]),Write(div_mulc_eq[3]))
        self.wait(3)
        square11 = Square(side_length = s)
        square11.move_to(3*RIGHT+0*UP)
        square_group11 = VGroup(*[
                    square11.copy().shift(x*s*RIGHT + y*s*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        square_group11.set_stroke(color=BLACK, width = 3)
        square_group11.set_fill(color=WHITE, opacity = 0.5)
        self.play(ShowCreation(square_group11))

        square22 = Square(side_length = s)
        square22.move_to(3*RIGHT+2*DOWN)
        square_group22 = VGroup(*[
                    square22.copy().shift(x*s*RIGHT + y*s*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        square_group22.set_stroke(color=BLACK, width = 3)
        square_group22.set_fill(color=WHITE, opacity = 0.5)
        self.play(ShowCreation(square_group22))
        sss = square_group_part3[0:2].copy()
        self.play(ReplacementTransform(div_mulc_eq[0].copy(),div_mulc_eq[4],path_arc = -PI/2))
        self.play(ReplacementTransform(div_mulc_eq[1].copy(),div_mulc_eq[5],path_arc = -PI/2))
        self.play(Write(div_mulc_eq[6]))
        self.play(square_group_part.copy().move_to,square_group11.get_center())
        self.play(square_group_part2.copy().move_to,square_group22.get_center())
        self.play(square_group_part3[2:5].copy().move_to,square_group11.get_center()+s/2*DOWN+s/2*RIGHT)
        self.play(sss.rotate,PI/2,sss.move_to,square_group22.get_center()+s/2*DOWN)
        self.play(Write(div_mulc_eq[7]))
        self.wait(3)

class slide13(Scene):
    def construct(self):
        div = Tex("{{a","\\over", "n}","\\over"," b}","="," {a","\\over"," n","\\cdot"," b}")
        #                   0       1     2       3      4    5     6      7      8      9      10
        div.to_edge(UP)
        n = 6
        f13 = Tex("{{1\\over 3}\\over 2}")
        f13.to_corner(UR,buff = 3)
        f26 = Tex("\\frac{1}{6}")
        f26.to_corner(UR,buff = 3)
        
        f13.scale(1.5)
        f26.scale(1.5)
        r = 2
        c = Circle(radius = r)
        c.set_fill(color=BLUE, opacity = 0.5)
        c.set_stroke(BLACK)
        sec = Sector(outer_radius = r,start_angle=PI/2,angle = 2*PI/3)
        sec.set_color(color = RED)
        sec2 = Sector(outer_radius = r,start_angle=PI/2,angle = 2*PI/6)
        sec2.set_color(color = RED)
        line = Line(ORIGIN,r*UP)
        line_group = VGroup(*[
                    line.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        line_group_part3 =  VGroup(*[line_group[i] for i in [0,2,4]])
        vc = VGroup(c,sec,sec2,line_group)
        vc.shift(1.5*DOWN)

        self.play(ShowCreation(c))
        self.play(ShowCreation(sec))

        self.play(ShowCreation(line_group_part3),Write(f13),Write(div[0:6]),run_time = 5)

        line_group_part6 =  VGroup(*[line_group[i] for i in [0,1,2,3,4,5]])

        self.play(ReplacementTransform(div[0].copy(),div[6],path_arc = -PI/2),
        Write(div[7]),
        ReplacementTransform(div[2].copy(),div[8],path_arc = PI/2),
        Write(div[9]),
        ReplacementTransform(div[4].copy(),div[10],path_arc = PI/2),
        ShowCreation(line_group_part6),ReplacementTransform(sec,sec2),ReplacementTransform(f13,f26),run_time = 7)

        self.wait(3)

class slide14(Scene):
    def construct(self):
        div_mulcd_eq = Tex("\\frac{a\\cdot n}{b\\cdot n}=\\frac{a}{b}  ")
        n = 12
        f13 = Tex("\\frac{1}{3}")
        f13.to_corner(UR,buff = 2)
        f26 = Tex("\\frac{2}{6}")
        f26.to_corner(UR,buff = 2)
        f39 = Tex("\\frac{3}{9}")
        f39.to_corner(UR,buff = 2)
        f412 = Tex("\\frac{4}{12}")
        f412.to_corner(UR,buff = 2)
        f13.scale(2)
        f26.scale(2)
        f39.scale(2)
        f412.scale(2)
        c = Circle(radius = 3)
        c.set_fill(color=BLUE, opacity = 0.5)
        c.set_stroke(BLACK)
        self.play(ShowCreation(c))
        line = Line(ORIGIN,3*UP)
        line_group = VGroup(*[
                    line.copy().rotate(x*2*PI/n,about_point = ORIGIN)
                    for x in range(n)
                ])
        line_group_part3 =  VGroup(*[line_group[i] for i in [0,4,8]])
        self.play(ShowCreation(line_group_part3))
        
        self.wait()
        sec = Sector(outer_radius = 3,start_angle=PI/2,angle = 2*PI/3)
        sec.set_color(color = RED)
        self.play(ShowCreation(sec))
        self.play(Write(f13))
        self.wait(3)
        self.play(FadeOut(line_group_part3))
        line_group_part6 =  VGroup(*[line_group[i] for i in [0,2,4,6,8,10]])
        self.play(ShowCreation(line_group_part6))
        self.play(ReplacementTransform(f13,f26))
        self.wait(3)
        self.play(FadeOut(line_group_part6))

        line_group9 = VGroup(*[
                    line.copy().rotate(x*2*PI/9,about_point = ORIGIN)
                    for x in range(9)
                ])
        line_group_part9 =  VGroup(*[line_group9[i] for i in range(9)])
        self.play(ShowCreation(line_group_part9))
        self.play(ReplacementTransform(f26,f39))
        self.wait(3)
        self.play(FadeOut(line_group_part9))

        line_group_part12 =  VGroup(*[line_group[i] for i in range(n)])
        self.play(ShowCreation(line_group_part12))
        self.play(ReplacementTransform(f39,f412))
        self.wait(3)
        self.play(FadeOut(line_group_part12),FadeOut(f412),FadeOut(c),FadeOut(sec))



class slide15(Scene):
    def construct(self):
         # Формулы дробей
        # div1 = Tex("a","\\cdot",r"{1}",r"\\over",r"{a}","=",r"{a\\cdot 1}",r"\\over",r"{a}=\\frac{a}{a}=1")
        # div1.split()
        #                  0      1            2        3      4         5  
        div1 = Tex("a","\\cdot","{1","\\over","a}","=","{a","\\cdot","1","\\over","a}","=","\\frac{a}{a}","=","1")
        #                  0      1      2       3    4    5    6     7      8     9      10   11     12          13  14
        self.play(Write(div1[0]))
        self.play(Write(div1[1]))
        self.play(Write(div1[2]))
        self.play(Write(div1[3]))
        self.play(Write(div1[4]))
        self.play(Write(div1[5]))


        self.play(ReplacementTransform(div1[0].copy(),div1[6],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[1].copy(),div1[7],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[2].copy(),div1[8],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[3].copy(),div1[9],path_arc = PI/2))
        self.play(ReplacementTransform(div1[4].copy(),div1[10],path_arc = PI/2))
        self.play(Write(div1[11]))
        self.play(Write(div1[12]))
        self.play(Write(div1[13]))
        self.play(Write(div1[14]))
        self.wait()
        self.play(FadeOut(div1))
        div3 = Tex("{1","\\over"," {1","\\over"," a}} ","="," {a","\\cdot","1"," \\over"," 1}"," =","a")
        #                   0       1      2      3       4     5     6     7     8        9       10    11  12
        self.play(Write(div3[0]))
        self.play(Write(div3[1]))
        self.play(Write(div3[2]))
        self.play(Write(div3[3]))
        self.play(Write(div3[4]))
        self.play(Write(div3[5]))

        self.play(ReplacementTransform(div3[4].copy(),div3[6],path_arc = PI/2))
        self.play(Write(div3[7]))
        self.play(ReplacementTransform(div3[0].copy(),div3[8],path_arc = PI/2))
        self.play(ReplacementTransform(div3[1].copy(),div3[9],path_arc = PI/2))
        self.play(ReplacementTransform(div3[2].copy(),div3[10],path_arc = PI/2))
        self.play(Write(div3[11]))
        self.play(Write(div3[12]))
        
        self.wait(3)

class slide16(Scene):
    def construct(self):
         # Формулы дробей
        div1 = Tex("\\frac{a}{b}","=","{a","\\cdot","1","\\over","b}","=","a","\\cdot","{1","\\over","b}")
        #                       0         1     2     3      4    5      6    7    8     9      10   11      
        self.play(Write(div1[0]))
        self.play(Write(div1[1]))
        self.play(Write(div1[2]))
        self.play(Write(div1[3]))
        self.play(Write(div1[4]))
        self.play(Write(div1[5]))
        self.play(Write(div1[6]))
        self.play(Write(div1[7]))


        self.play(ReplacementTransform(div1[2].copy(),div1[8],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[3].copy(),div1[9],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[4].copy(),div1[10],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[5].copy(),div1[11],path_arc = -PI/2))
        self.play(ReplacementTransform(div1[6].copy(),div1[12],path_arc = PI/2))
        

        self.wait()
        self.play(FadeOut(div1))

        div_mulcd_eq = Tex("{a", "\\over", "b}","\\cdot" ,"{m","\\over", "n}" ,"=", "{a","\\cdot","m","\\over", "b","\\cdot", "n}")
        #                           0         1     2     3         4    5       6     7     8     9      10     11     12   13       14  
        
        self.play(Write(div_mulcd_eq[0]))
        self.play(Write(div_mulcd_eq[1]))
        self.play(Write(div_mulcd_eq[2]))
        self.play(Write(div_mulcd_eq[3]))
        self.play(Write(div_mulcd_eq[4]))
        self.play(Write(div_mulcd_eq[5]))
        self.play(Write(div_mulcd_eq[6]))
        self.play(Write(div_mulcd_eq[7]))


        self.play(ReplacementTransform(div_mulcd_eq[0].copy(),div_mulcd_eq[8],path_arc = -PI/2))
        self.play(ReplacementTransform(div_mulcd_eq[3].copy(),div_mulcd_eq[9],path_arc = -PI/2))
        self.play(ReplacementTransform(div_mulcd_eq[4].copy(),div_mulcd_eq[10],path_arc = -PI/2))
        self.play(Write(div_mulcd_eq[11]))
        self.play(ReplacementTransform(div_mulcd_eq[2].copy(),div_mulcd_eq[12],path_arc = PI/2))
        self.play(ReplacementTransform(div_mulcd_eq[3].copy(),div_mulcd_eq[13],path_arc = PI/2))
        self.play(ReplacementTransform(div_mulcd_eq[6].copy(),div_mulcd_eq[14],path_arc = PI/2))
        

        self.wait()
        self.play(FadeOut(div_mulcd_eq))
        
        
        
        
        div3 = Tex("{1","\\over","{a","\\over"," b}}","=","{b","\\cdot","1","\\over"," a}","=","{b","\\over"," a}")
                     #     0        1      2     3       4      5  6      7     8       9     10   11   12    13      14  
        
        self.play(Write(div3[0]))
        self.play(Write(div3[1]))
        self.play(Write(div3[2]))
        self.play(Write(div3[3]))
        self.play(Write(div3[4]))
        self.play(Write(div3[5]))

        self.play(ReplacementTransform(div3[4].copy(),div3[6],path_arc = PI/2))
        self.play(Write(div3[7]))
        self.play(ReplacementTransform(div3[0].copy(),div3[8],path_arc = -PI/2))
        self.play(ReplacementTransform(div3[1].copy(),div3[9],path_arc = PI/2))
        self.play(ReplacementTransform(div3[2].copy(),div3[10],path_arc = PI/2))
        self.play(Write(div3[11]))
        self.play(ReplacementTransform(div3[6].copy(),div3[12],path_arc = -PI/2))
        self.play(ReplacementTransform(div3[9].copy(),div3[13],path_arc = PI/2))
        self.play(ReplacementTransform(div3[10].copy(),div3[14],path_arc = PI/2))
        
        self.wait(3)
        self.play(FadeOut(div3))
        div_muldc_eq = Tex("{{a","\\over", "b}","\\over", "{m","\\over"," n}}" ,"=","{a","\\cdot","n","\\over"," b","\\cdot"," m}")
            #                        0      1      2       3       4      5     6       7    8       9    10    11      12    13      14  

        self.play(Write(div_muldc_eq[0]))
        self.play(Write(div_muldc_eq[1]))
        self.play(Write(div_muldc_eq[2]))
        self.play(Write(div_muldc_eq[3]))
        self.play(Write(div_muldc_eq[4]))
        self.play(Write(div_muldc_eq[5]))
        self.play(Write(div_muldc_eq[6]))
        self.play(Write(div_muldc_eq[7]))


        self.play(ReplacementTransform(div_muldc_eq[0].copy(),div_muldc_eq[8],path_arc = -PI/2))
        self.play(Write(div_muldc_eq[9]))
        self.play(ReplacementTransform(div_muldc_eq[6].copy(),div_muldc_eq[10],path_arc = PI/2))
        self.play(ReplacementTransform(div_muldc_eq[3].copy(),div_muldc_eq[11],path_arc = -PI/2))
        
        self.play(ReplacementTransform(div_muldc_eq[2].copy(),div_muldc_eq[12],path_arc = PI/2))
        self.play(Write(div_muldc_eq[13]))
        self.play(ReplacementTransform(div_muldc_eq[4].copy(),div_muldc_eq[14],path_arc = PI/2))
  
        
        self.wait(3)

class slide17(Scene):
    def construct(self):
        div_add = Tex("{a","\\over"," b}","+","{m","\\over", " n}", "=","{a","\\cdot", "n","+","b","\\cdot"," m","\\over","b","\\cdot"," n}")
             #                 0      1      2    3    4      5       6     7    8      9      10  11  12    13      14    15    16     17     18
        self.play(Write(div_add[0]))
        self.play(Write(div_add[1]))
        self.play(Write(div_add[2]))
        self.play(Write(div_add[3]))
        self.play(Write(div_add[4]))
        self.play(Write(div_add[5]))
        self.play(Write(div_add[6]))
        self.play(Write(div_add[7]))

        self.play(ReplacementTransform(div_add[0].copy(),div_add[8],path_arc = -PI/2))
        self.play(Write(div_add[9]))
        self.play(ReplacementTransform(div_add[6].copy(),div_add[10],path_arc = PI/2))
        self.play(Write(div_add[11]))
        self.play(ReplacementTransform(div_add[2].copy(),div_add[12],path_arc = PI/2))
        self.play(Write(div_add[13]))
        self.play(ReplacementTransform(div_add[4].copy(),div_add[14],path_arc = -PI/2))
        self.play(Write(div_add[15]))
        self.play(ReplacementTransform(div_add[2].copy(),div_add[16],path_arc = PI/2))
        self.play(Write(div_add[17]))
        self.play(ReplacementTransform(div_add[6].copy(),div_add[18],path_arc = PI/2))
        
        
        self.wait(3)
        self.play(FadeOut(div_add))
        div_sub = Tex("{a","\\over"," b}","-","{m","\\over", " n}", "=","{a","\\cdot", "n","-","b","\\cdot"," m","\\over","b","\\cdot"," n}")
        self.play(Write(div_sub[0]))
        self.play(Write(div_sub[1]))
        self.play(Write(div_sub[2]))
        self.play(Write(div_sub[3]))
        self.play(Write(div_sub[4]))
        self.play(Write(div_sub[5]))
        self.play(Write(div_sub[6]))
        self.play(Write(div_sub[7]))

        self.play(ReplacementTransform(div_sub[0].copy(),div_sub[8],path_arc = -PI/2))
        self.play(Write(div_sub[9]))
        self.play(ReplacementTransform(div_sub[6].copy(),div_sub[10],path_arc = PI/2))
        self.play(Write(div_sub[11]))
        self.play(ReplacementTransform(div_sub[2].copy(),div_sub[12],path_arc = PI/2))
        self.play(Write(div_sub[13]))
        self.play(ReplacementTransform(div_sub[4].copy(),div_sub[14],path_arc = -PI/2))
        self.play(Write(div_sub[15]))
        self.play(ReplacementTransform(div_sub[2].copy(),div_sub[16],path_arc = PI/2))
        self.play(Write(div_sub[17]))
        self.play(ReplacementTransform(div_sub[6].copy(),div_sub[18],path_arc = PI/2))
        
        self.wait(3)