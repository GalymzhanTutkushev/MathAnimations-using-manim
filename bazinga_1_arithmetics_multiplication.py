from manimlib import *


class slide2(Scene):
    def construct(self):
        
        n = 3
        m = 5
        square = Square(side_length = 1)
        square.move_to(2*LEFT+1*DOWN)
        square_group = VGroup(*[
                    square.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group))
        square_group.save_state()
        mn = Tex("3\\cdot5=15")
        mn.to_edge(UP)
        self.play(Write(mn))
        
        a3 = Tex("3")
        a3_group = VGroup(*[
                    a3.copy().shift(2*(m-x)*LEFT+5*RIGHT)
                    for x in range(m)
                ])
        a3_group.shift(1.8*UP)
        for s in range(m):
            square_group_part =  VGroup(*[square_group[i] for i in range(s*n,(s+1)*n)])
           
            self.play(square_group_part.shift,(m-s)*LEFT+2*RIGHT)
           
            self.play(Write(a3_group[s]))
           
            
        plus = Tex("+")
        plus.scale(2)
        plus.move_to(4*LEFT)
        plus_group = VGroup(*[
                    plus.copy().shift((x)*RIGHT*2)
                    for x in range(m-1)

                ])
        
        self.play(Write(plus_group))
        eq = Tex("=\\;15")
        eq.scale(2)
        eq.next_to(square_group,RIGHT)
            
        self.play(Write(eq))

        self.play(FadeOut(plus_group),FadeOut(eq),FadeOut(a3_group))

        self.play(square_group.restore)
        
        nm = Tex("5\\cdot3=15")
        nm.to_edge(UP)
        self.play(ReplacementTransform(mn,nm))
        a5 = Tex("5")
        a5_group = VGroup(*[
                    a5.copy().shift(2*(n-x)*DOWN+4*UP)
                    for x in range(n)
                ])
        a5_group.shift(3*RIGHT)
        for s in range(n):
            square_group_part =  VGroup(*[square_group[i] for i in range(s,(n)*m+s,n)])
 
            self.play(square_group_part.shift,(n-s)*DOWN+2*UP)
            
            self.play(Write(a5_group[s]))

        

        plus1 = Tex("+")
        plus1.scale(2)
        plus1.move_to(UP)
        plus_group1 = VGroup(*[
                    plus1.copy().shift((x)*2*DOWN)
                    for x in range(n-1)

                ])
        
        self.play(Write(plus_group1))
        eq1 = Tex("=\\;15")
        eq1.scale(2)
        eq1.next_to(square_group,DOWN)
            
        self.play(Write(eq1))

        self.play(FadeOut(plus_group1),FadeOut(eq1),FadeOut(a5_group))
        self.play(square_group.restore)
        self.wait(pause_time)

        # self.play(Write(add53))

class slide3(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([0,16,1]),  unit_size=0.8,color="#000000",include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[16])

        numberl.shift(6.5*LEFT)
        self.play(ShowCreation(numberl))

       


        vector7  = Vector([3*0.8,0])
        vector7.set_color(color = BLUE)
        vector7.move_to(numberl.get_start()+3*0.8/2*RIGHT)
        self.play(ShowCreation(vector7))
        brace = Brace(vector7,DOWN)
        self.play(ShowCreation(brace))
        vector_group = VGroup(*[
                    vector7.copy().shift(3*x*0.8*RIGHT)
                    for x in range(5)
                    
                ])
        brace_group = VGroup(*[
                    brace.copy().shift(3*x*0.8*RIGHT)
                    for x in range(5)
                    
                ])
        mult = Tex("3\\cdot5=15")
        mult.set_color(color = BLACK)
        mult.to_edge(UP)
        
        self.play(ShowCreation(vector_group),ShowCreation(brace_group),FadeIn(mult),run_time = 5)
        # self.play(vector7.copy().shift,3*0.8*RIGHT,vector7.copy().shift,6*0.8*RIGHT,
        # vector7.copy().shift,9*0.8*RIGHT,vector7.copy().shift,12*0.8*RIGHT,run_time = 5)
        # self.play(vector7.stretch, 5,0,{"about_edge": LEFT},run_time = 5)
        
        self.wait()
        groupMminm = VGroup (mult,vector7,vector_group,brace_group,brace)
        self.play(FadeOut(groupMminm))

        vector7  = Vector([5*0.8,0])
        vector7.set_color(color = BLUE)
        vector7.move_to(numberl.get_start()+5*0.8/2*RIGHT)
        self.play(ShowCreation(vector7))
        brace = Brace(vector7,DOWN)
        self.play(ShowCreation(brace))
        vector_group = VGroup(*[
                    vector7.copy().shift(5*x*0.8*RIGHT)
                    for x in range(3)
                    
                ])
        brace_group = VGroup(*[
                    brace.copy().shift(5*x*0.8*RIGHT)
                    for x in range(3)
                    
                ])
        mult = Tex("5\\cdot3=15")
        mult.set_color(color = BLACK)
        mult.to_edge(UP)
    
        self.play(ShowCreation(brace_group),ShowCreation(vector_group),FadeIn(mult),run_time = 5)
        # self.play(vector7.copy().shift,5*0.8*RIGHT,vector7.copy().shift,10*0.8*RIGHT,run_time = 5)
        # self.play(vector7.stretch, 3,0,{"about_edge": LEFT},run_time = 5)
        
        self.wait()
        groupMminm = VGroup (mult,vector7,vector_group,brace_group,brace)
        self.play(FadeOut(groupMminm))

        self.wait(pause_time)

class slide4(Scene):
    def construct(self):

        n = 3
        m = 2
        c = 5
        abc = Tex("2 \\cdot 3\\cdot 5","=6\\cdot 5","=30")
        abc.to_edge(DOWN)
        square1 = Square(side_length = 1)
        square1.move_to(3*LEFT+1.8*DOWN)
        square_group1 = VGroup(*[
                    square1.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
       
        square_group1.set_stroke(color=BLACK, width = 3)
        square_group1.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group1))
        square_group1.save_state()
        square_group_part1 =  VGroup(*[square_group1[i] for i in [0,1,2]])
        div1 = Tex(str(n))
        div2 = Tex(str(m))
        div1.next_to(square_group1,LEFT)
        div2.next_to(square_group1,UP)
        self.play(Write(div1),Write(div2))
        self.play(Write(abc[0]))
        # self.play(Write(abc[0]))
        # self.play(square_group_part1.set_color,RED,run_time = 3)
        self.play(square_group_part1.shift,3*UP,FadeOut(div2),run_time = 3)
        self.play(square_group_part1.shift,RIGHT,FadeOut(div1),run_time = 3)
        # self.remove(div2,div1)
        
        div5 = Tex(str(m*n))
        div3 = Tex(str(c))
        
        div5.next_to(square_group1,LEFT)
      
        self.play(Write(div5))

        
        squareC = Square(side_length = 1)
        squareC.move_to(2*LEFT+1.8*DOWN)
        square_groupC = VGroup(*[
                    squareC.copy().shift(x*RIGHT + y*UP)
                    for x in range(c)
                    for y in range(m*n)
                ])
       
        square_groupC.set_stroke(color=BLACK, width = 3)
        square_groupC.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_groupC))
        div3.next_to(square_groupC,DOWN)
        self.play(Write(div3))
        self.play(Write(abc[1]))
        self.play(Write(abc[2]))
        nmc = VGroup(abc,div3,div5,square_groupC,square_group1)
        self.play(FadeOut(nmc))

        self.wait(3)

        n = 2
        m = 5
        c = 3
        abc = Tex("2 \\cdot 3\\cdot 5","=10\\cdot 3","=30")
        abc.to_edge(DOWN)
        square1 = Square(side_length = 1)
        square1.move_to(5*LEFT+1*UP)
        square_group1 = VGroup(*[
                    square1.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
       
        square_group1.set_stroke(color=BLACK, width = 3)
        square_group1.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group1))
        square_group1.save_state()
        square_group_part1 =  VGroup(*[square_group1[i] for i in [0,2,4,6,8]])
        div1 = Tex(str(n))
        div2 = Tex(str(m))
        div1.next_to(square_group1,LEFT)
        div2.next_to(square_group1,UP)
        self.play(Write(div1),Write(div2))
        self.play(Write(abc[0]))
        # self.play(Write(abc[0]))
        # self.play(square_group_part1.set_color,RED,run_time = 3)
        self.play(square_group_part1.shift,m*RIGHT,FadeOut(div1),run_time = 3)
        self.play(square_group_part1.shift,UP,FadeOut(div2),run_time = 3)
       
        div5 = Tex(str(c))
        div3 = Tex(str(m*n))
        
        
        squareC = Square(side_length = 1)
        squareC.move_to(5*LEFT+2*UP)
        square_groupC = VGroup(*[
                    squareC.copy().shift(x*RIGHT + y*DOWN)
                    for x in range(m*n)
                    for y in range(c)
                ])
       
        square_groupC.set_stroke(color=BLACK, width = 3)
        square_groupC.set_fill(color=BLUE, opacity = 0.5)
        div3.next_to(square_groupC,DOWN)
        div5.next_to(square_groupC,LEFT)
       
        self.play(Write(div5))

        self.play(ShowCreation(square_groupC))
        
        self.play(Write(div3))
        self.play(Write(abc[1]))
        self.play(Write(abc[2]))
        nmc = VGroup(abc,div3,div5,square_groupC,square_group1)
        self.play(FadeOut(nmc))

        self.wait(3)
        
        
        n = 3
        m = 5
        c = 2
        abc = Tex("2 \\cdot 3\\cdot 5","=15\\cdot 2","=30")
        abc.to_edge(DOWN)
        side = 0.8
        square1 = Square(side_length = side)
        square1.move_to(2*LEFT+1*UP)
        square_group1 = VGroup(*[
                    square1.copy().shift(x*side*RIGHT + side*y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
       
        square_group1.set_stroke(color=BLACK, width = 3)
        square_group1.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group1))
        square_group1.save_state()
        square_group_part1 =  VGroup(*[square_group1[i] for i in [0,3,6,9,12]])
        div1 = Tex(str(n))
        div2 = Tex(str(m))
        div1.next_to(square_group1,LEFT)
        div2.next_to(square_group1,UP)
        self.play(Write(div1),Write(div2))
        self.play(Write(abc[0]))
        # self.play(Write(abc[0]))
        # self.play(square_group_part1.set_color,RED,run_time = 3)
        square_group_part2 =  VGroup(*[square_group1[i] for i in [2,5,8,11,14]])
        self.play(square_group_part1.shift,m*side*RIGHT,FadeOut(div1),run_time = 3)
        self.play(square_group_part1.shift,side*UP,FadeOut(div2),run_time = 3)
        self.play(square_group_part2.shift,m*side*LEFT,run_time = 3)
        self.play(square_group_part2.shift,side*DOWN,run_time = 3)
        # self.remove(div2,div1)
        
        

        
        squareC = Square(side_length = side)
        squareC.move_to(side*7.5*LEFT+(side+1)*UP)
        square_groupC = VGroup(*[
                    squareC.copy().shift(x*side*RIGHT + side*y*DOWN)
                    for x in range(m*n)
                    for y in range(c)
                ])
       
        square_groupC.set_stroke(color=BLACK, width = 3)
        square_groupC.set_fill(color=BLUE, opacity = 0.5)
        div5 = Tex(str(c))
        div3 = Tex(str(m*n))
        div3.next_to(square_groupC,DOWN)
        div5.next_to(square_groupC,LEFT)
       
        self.play(Write(div5))
        self.play(ShowCreation(square_groupC))
        
        self.play(Write(div3))
        self.play(Write(abc[1]))
        self.play(Write(abc[2]))
        nmc = VGroup(abc,div3,div5,square_groupC,square_group1)
        self.play(FadeOut(nmc))

        self.wait(pause_time)

class slide8(Scene):
    def construct(self):

        n = 5
        m = 5
        abc = Tex("5\\cdot (2+3)","=5\\cdot 2+5\\cdot 3","=25")
        abc.to_edge(UP)
        square1 = Square(side_length = 1)
        square1.move_to(2*LEFT+2*DOWN)
        square_group1 = VGroup(*[
                    square1.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        div1 = Tex("5")
        div2 = Tex("2+3")
        div1.next_to(square_group1,LEFT)
        div2.next_to(square_group1,DOWN)
        square_group1.set_stroke(color=BLACK, width = 3)
        square_group1.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group1))
        square_group1.save_state()
        square_group_part1 =  VGroup(*[square_group1[i] for i in [0,1,2,3,4,5,6,7,8,9]])
        self.play(Write(div1),Write(div2))
        self.play(Write(abc[0]))
        self.play(square_group_part1.set_fill,RED,run_time = 3)
        self.play(FadeOut(div1))
        self.play(FadeOut(div2),square_group_part1.move_to,3*LEFT,run_time = 3)
               
        div3 = Tex("2")
        div5 = Tex("3")
        div3.next_to(square_group_part1,DOWN)
        div5.next_to(square_group1,DOWN)
        div5.shift(1.7*RIGHT)
        dd1=div1.copy().next_to(square_group1,RIGHT)
        dd2=div1.copy().next_to(square_group_part1,LEFT)
        self.play(Write(abc[1]),Write(div3),Write(div5),Write(dd1),Write(dd2),run_time = 5)

        div55 = Tex("5")
        # div3.next_to(square_group_part1,UP)
        div55.next_to(square_group1,DOWN)
        div55.shift(0.8*RIGHT)
        
        self.wait(pause_time)
        self.remove(div3,div5,div1)
        
        self.play(square_group1.restore,FadeOut(dd2))
        self.play(Write(div55),Write(abc[2]))
        self.wait(pause_time)


class slide9(Scene):
    def construct(self):

        # Формулы многочленов и свойств
        many_eq = Tex("a","\\cdot","(","b","+","c",")","=","a","\\cdot","b","+","a","\\cdot" ,"c")
         #                    0       1    2   3   4   5   6   7   8       9    10  11  12     13     14
        many_eq.scale(2)
        # self.play(Write(many_eq[0:7]),run_time = 3)
        # self.play(Write(many_eq[7]))
        # self.play(ReplacementTransform(many_eq[0].copy(),many_eq[8],path_arc = PI/2),
        # ReplacementTransform(many_eq[1].copy(),many_eq[9],path_arc = PI/2),
        # ReplacementTransform(many_eq[3].copy(),many_eq[10],path_arc = PI/2),run_time = 5)
        # self.play(ReplacementTransform(many_eq[4].copy(),many_eq[11],path_arc = PI/2),run_time = 3)
        # self.play(ReplacementTransform(many_eq[0].copy(),many_eq[12],path_arc = PI/2),
        # ReplacementTransform(many_eq[1].copy(),many_eq[13],path_arc = PI/2),
        # ReplacementTransform(many_eq[5].copy(),many_eq[14],path_arc = PI/2),run_time = 5)

        
        many_eq2 = Tex("(","a","+","b",")","\\cdot","(","c","+","d",")","=","a","\\cdot","c","+","a","\\cdot" ,"d","+","b","\\cdot","c","+","b","\\cdot" ,"d")
        #                      0   1   2   3   4      5     6   7   8   9   10  11  12     13    14  15  16    17     18  19   20     21    22  23  24     25     26
        many_eq2.scale(1.5)
        self.play(Write(many_eq2[0:11]),run_time = 3)
        self.play(Write(many_eq2[11]))
        self.play(ReplacementTransform(many_eq2[1].copy(),many_eq2[12],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[13],path_arc = PI/2),
        ReplacementTransform(many_eq2[7].copy(),many_eq2[14],path_arc = PI/2),run_time = 5)
        self.play(ReplacementTransform(many_eq2[8].copy(),many_eq2[15],path_arc = PI/2),run_time = 3)
        self.play(ReplacementTransform(many_eq2[1].copy(),many_eq2[16],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[17],path_arc = PI/2),
        ReplacementTransform(many_eq2[9].copy(),many_eq2[18],path_arc = PI/2),run_time = 5)
        self.play(ReplacementTransform(many_eq2[2].copy(),many_eq2[19],path_arc = PI/2),run_time = 3)

        self.play(ReplacementTransform(many_eq2[3].copy(),many_eq2[20],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[21],path_arc = PI/2),
        ReplacementTransform(many_eq2[7].copy(),many_eq2[22],path_arc = PI/2),run_time = 5)
        self.play(ReplacementTransform(many_eq2[8].copy(),many_eq2[23],path_arc = PI/2),run_time = 3)
        self.play(ReplacementTransform(many_eq2[3].copy(),many_eq2[24],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[25],path_arc = PI/2),
        ReplacementTransform(many_eq2[9].copy(),many_eq2[26],path_arc = PI/2),run_time = 5)

        # self.play(Write(many_eq2))
        # self.play(FadeOut(many_eq2))
        self.wait(pause_time)