from manimlib import *


side = 0.8
m = 15
class slide1(Scene):
    def construct(self):
        square = Square(side_length = side)
        square_group = VGroup(*[
                    square.copy().shift(side*x*RIGHT)
                    for x in range(m)   
                ])
        square_group.move_to(ORIGIN)
        square_group.set_stroke(color=color_stroke, width = width_stroke)
        square_group.set_fill(color=color_fill, opacity = opacity_fill)
        self.play(ShowCreation(square_group))
        div_eq = Tex("15:5=3")
        div_eq.to_edge(UP)
        self.play(Write(div_eq))
        for s in range(5):
            square_group_part =  VGroup(*[square_group[i] for i in range(s*3,(s+1)*3)])
            self.play(square_group_part.move_to,(5-s)/15*0.8*LEFT+s/16*LEFT+(2-s)*UP)
        t3 = Tex("3")
        t5 = Tex("5")
        t3.next_to(square_group_part,DOWN)
        t5.next_to(square_group_part,RIGHT)
        t5.shift(2*UP)
        self.play(Write(t3),Write(t5))
        self.wait(pause_time)

class slide2(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([0,16,1]),  unit_size=0.8,color="#000000",
        include_numbers=True,include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[16])
        # numberl.shift(6.5*LEFT)
        self.play(ShowCreation(numberl))
        vector15 = Vector([15*0.8,0])
        vector15.set_color(color = BLUE)
        vector15.move_to(numberl.get_start()+15*0.8/2*RIGHT+0.3*DOWN)
        vector3  = Vector([3*0.8,0])
        vector3.set_color(color = BLUE)
        vector3.move_to(numberl.get_start()+3*0.8/2*RIGHT+0.3*DOWN)
        self.play(ShowCreation(vector15))
        brace = Brace(vector3,DOWN)
        vector_group = VGroup(*[
                    vector3.copy().shift(3*x*0.8*RIGHT)
                    for x in range(5)   
                ])
        brace_group = VGroup(*[
                    brace.copy().shift(3*x*0.8*RIGHT)
                    for x in range(5) 
                ])
        div_eq = Tex("15: 5=3")
        div_eq.to_edge(UP)
        self.play(Write(div_eq))
        v = VGroup(vector3,vector_group)
        self.play(ReplacementTransform(vector15,v),run_time = play_time)
        self.play(ShowCreation(vector3),ShowCreation(brace))
        self.play(ShowCreation(brace_group),run_time = play_time)
        self.wait()
        self.play(FadeOut(vector_group),FadeOut(brace_group))
        self.wait(pause_time)

class slide5(Scene):
    def construct(self):
        square = Square(side_length = side)
        square_group = VGroup(*[
                    square.copy().shift(side*x*RIGHT)
                    for x in range(m)       
                ])
        square_group.move_to(ORIGIN)
        square_group.set_stroke(color=color_stroke, width = width_stroke)
        square_group.set_fill(color=color_fill, opacity = opacity_fill)
        t15 = Tex("15")
        t15.next_to(square_group,DOWN)
        self.play(ShowCreation(square_group),Write(t15),run_time = 3)
        div_eq = Tex("15=","2\\cdot6","+","3")
        div_eq[3].set_color(BLUE)
        div_eq.to_edge(UP)
        self.play(Write(div_eq[0]))
        self.remove(t15)
        for s in range(2):
            square_group_part =  VGroup(*[square_group[i] for i in range(s*6,(s+1)*6)])
            self.play(square_group_part.move_to,(5-s)/15*0.8*LEFT+s/15*LEFT+(2-s)*UP,run_time = 3)
        t3 = Tex("6")
        t5 = Tex("2")
        t3.next_to(square_group_part,DOWN)
        tr = Tex("3")
        tr.set_color(BLUE)
        tr.next_to(square_group,DOWN)
        tr.shift(3.2*RIGHT)
        t5.next_to(square_group_part,RIGHT)
        t5.shift(0.5*UP)
        self.play(Write(t3),Write(t5),Write(div_eq[1]),run_time = 4)
        self.wait()
        self.play(Write(tr),Write(div_eq[2:4]),run_time = 3)
        self.wait(pause_time)

class slide6(Scene):
    def construct(self):
        side = 0.5
        for m in range(18,25):
            div_eq = Tex(str(m),"=",str(m//6),"\\cdot 6+",str(m%6))
            div_eq.to_edge(UP)
            div_eq[4].set_color(BLUE)
            square = Square(side_length = side)
            mt = Tex(str(m))
            square_group = VGroup(*[
                    square.copy().shift(side*x*RIGHT)
                    for x in range(m) 
                ])
            square_group.move_to(ORIGIN)
            mt.next_to(square_group,DOWN)
            square_group.set_stroke(color=color_stroke, width = width_stroke)
            square_group.set_fill(color=color_fill, opacity = opacity_fill)
            self.play(ShowCreation(square_group),Write(mt),Write(div_eq[0:2]))
            tr = Tex(str(m%6))
            tm = Tex(str(m//6))
            t6 = Tex(str(6))
            self.remove(mt)
            for s in range(m//6):
                square_group_part =  VGroup(*[square_group[i] for i in range(s*6,(s+1)*6)])
                self.play(square_group_part.move_to,(5-s)/15*0.8*LEFT+s/15*LEFT+(2-s)*UP,run_time = play_time/3)
            tm.next_to(square_group_part,RIGHT)
            tm.shift(UP)
            t6.next_to(square_group_part,DOWN)
            tr.next_to(square_group_part,DOWN)
            tr.shift(4.75*RIGHT)
            tr.set_color(BLUE)
            self.play(Write(tm),Write(t6),Write(tr),Write(div_eq[2:5]))
            self.wait()
            self.play(FadeOut(square_group),FadeOut(div_eq),FadeOut(tm),FadeOut(t6),FadeOut(tr))  
        self.wait(pause_time)