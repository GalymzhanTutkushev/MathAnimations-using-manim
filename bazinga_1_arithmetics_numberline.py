from manimlib import *


class slide2(Scene):
    def construct(self):
       
        line = Line(6*LEFT,3*LEFT)
        self.play(ShowCreation(line))
        tick = Line(6*LEFT+0.1*DOWN,6*LEFT+0.1*UP,include_tip = True)
        brace = Brace(line,DOWN)
        x0 = Tex("0")
        x1 = Tex("1")
        x2 = Tex("2")
        x0.move_to(0.7*DOWN+6*LEFT)
        x1.move_to(0.7*DOWN+3*LEFT)
        x2.move_to(0.7*DOWN)
        x3 = Tex("3")
        x3.move_to(0.7*DOWN+3*RIGHT)
        x4 = Tex("4")
        x4.move_to(0.7*DOWN+6*RIGHT)
        nl_group = VGroup(x0,x1,x2,brace,tick,line)
        
        self.play(ShowCreation(brace),Write(x0),Write(x1))
        self.play(ShowCreation(tick),tick.copy().shift,3*RIGHT)
        self.play(ApplyMethod(line.copy().shift,3*RIGHT,tick.copy().shift,6*RIGHT,Write(x2)))

        self.play(ApplyMethod(line.copy().shift,6*RIGHT,tick.copy().shift,9*RIGHT,Write(x3)))
        self.play(ApplyMethod(line.copy().shift,9*RIGHT,tick.copy().shift,12*RIGHT,Write(x4)))
        
        
        self.wait(pause_time)

class slide3(Scene):
    def construct(self):
       
        line = Line(6*LEFT,3*LEFT)
        vector = Vector(3*RIGHT)
        vector.move_to(4.5*LEFT+0.3*DOWN)
        self.add(line)
        tick = Line(6*LEFT+0.15*DOWN,6*LEFT+0.15*UP,include_tip = True)
        line_group = VGroup(*[
                    line.copy().shift(3*x*RIGHT)
                    for x in range(4)
          
                ])
        tick_group = VGroup(*[
                    tick.copy().shift(3*x*RIGHT)
                    for x in range(4+1)
          
                ])
        brace = Brace(line,UP)
        x0 = Tex("0")
        x1 = Tex("1")
        x2 = Tex("2")      
        x3 = Tex("3")
        x4 = Tex("4")
        x0.move_to(0.7*DOWN+6*LEFT)
        x1.shift(0.7*DOWN+3*LEFT)
        x2.move_to(0.7*DOWN)
        x3.move_to(0.7*DOWN+3*RIGHT)
        x4.move_to(0.7*DOWN+6*RIGHT)
        nl_group = VGroup(x0,x1,x2,brace,tick,line)
        vector_group = VGroup(*[
                    vector.copy().shift(3*x*RIGHT)
                    for x in range(4)
          
                ])
        brace_group = VGroup(*[
                    brace.copy().shift(3*x*RIGHT)
                    for x in range(4)
          
                ])
        self.add(x0,x1,x2,x3,x4)
        self.add(tick_group,line_group)
        
        self.play(ShowCreation(vector_group),ShowCreation(vector),ShowCreation(brace_group),ShowCreation(brace),play_time = 5)
        v = VGroup(vector_group,vector)
        vvv = Vector(12*RIGHT)
        vvv.move_to(0.3*DOWN)
        b = VGroup(brace_group,brace)
        bbb = Brace(vvv,UP,buff = 0.25)
        self.wait(3)
        
        self.play(ReplacementTransform(v,vvv),ReplacementTransform(b,bbb),play_time = 5)
        self.play(FadeOut(brace))
        arr = Vector(0.5*RIGHT)
        arr.shift(6*RIGHT)
        arr.scale(2)
        arr.set_color(color = BLACK)
        self.wait(pause_time)


class slide5(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([0,12,1]), unit_size=1,include_numbers=True,include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[12])
        numberl.shift(6*LEFT)
        self.play(ShowCreation(numberl))
        ab = Tex("3<6")
        ba = Tex("8>6")
        abba = Tex("a=b")
       
        ab.to_edge(UP)
        ba.to_edge(UP)
        abba.to_edge(UP)
        a = Dot(-3*RIGHT)
        b = Dot(0*RIGHT)
        c = Dot(2*RIGHT)
       
        a_label = Tex("3")
        b_label = Tex("6")
        c_label = Tex("8")
        
        a_label.next_to(a,DOWN)
        b_label.next_to(b,DOWN)
        c_label.next_to(c,DOWN)
       
        a_dot = VGroup(a,a_label)
        b_dot = VGroup(b,b_label)
        c_dot = VGroup(c,c_label)
        a.scale(1.2)
        b.scale(1.2)
        c.scale(1.2)
        self.play(ShowCreation(a_dot))
        self.play(ShowCreation(b_dot))
        
        self.play(ShowCreation(ab))
        self.wait(pause_time)
        self.play(FadeOut(a_dot))
        self.play(ShowCreation(c_dot))
       
        self.play(ReplacementTransform(ab,ba))
        self.wait(pause_time)
        # self.play(ReplacementTransform(abba,ba))
        self.play(FadeOut(ba))
       
        self.wait(pause_time)

class slide6(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([0,12,1]), unit_size=1,include_numbers=True,include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[12])
        numberl.shift(6*LEFT)
        self.play(ShowCreation(numberl))
        ab = Tex("a<b")
        ba = Tex("a>b")
        abba = Tex("a=b")
        abc1 = Tex("a<b")
        abc1.move_to(3*DOWN+2*LEFT)
        abc2 = Tex("b<c")
        abc2.move_to(3*DOWN)
        abc3 = Tex("a<c")
        abc3.move_to(3*DOWN+2*RIGHT)
        ab.to_edge(DOWN)
        ba.to_edge(DOWN)
        abba.to_edge(DOWN)
        a = Dot(-3*RIGHT)
        b = Dot(2*RIGHT)
        c = Dot(3*RIGHT)
        a_label = Tex("a")
        b_label = Tex("b")
        c_label = Tex("c")
        
        a_label.next_to(a,DOWN)
        b_label.next_to(b,DOWN)
        c_label.next_to(c,DOWN)
        a_dot = VGroup(a,a_label)
        b_dot = VGroup(b,b_label)
        c_dot = VGroup(c,c_label)
        self.play(ShowCreation(a_dot))
        self.play(ShowCreation(b_dot))
        self.play(ShowCreation(ab))
        self.play(a_dot.shift,5*RIGHT)
        self.play(ReplacementTransform(ab,abba))
        self.play(a_dot.shift,2*RIGHT)
        self.play(ReplacementTransform(abba,ba))
        self.play(FadeOut(ba))
        self.play(a_dot.shift,7*LEFT)
        self.play(ShowCreation(c_dot))
        self.play(ShowCreation(abc1))
        self.play(ShowCreation(abc2))
        self.play(ShowCreation(abc3))
        self.wait(pause_time)

