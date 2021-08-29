from manimlib import *


class rational_slide1(Scene):
    def construct(self):
        line = Line(ORIGIN,2*RIGHT)
        arr = Arrow(5.5*RIGHT,7*RIGHT).set_color(BLACK)
        
        # arr.shift(5.5*RIGHT)
        # arr.set_stroke(BLACK,line.get_stroke_width())
        arr.scale(0.5)
        self.play(ShowCreation(line))
        tick = Line(0.1*DOWN,0.1*UP,include_tip = True)
        
        x0 = Tex("0")
        x1 = Tex("1")
        x2 = Tex("2")
        x3 = Tex("3")
        x0.move_to(0.7*DOWN)
        x1.move_to(0.7*DOWN+2*RIGHT)
        x2.move_to(0.7*DOWN+4*RIGHT)
        x3.move_to(0.7*DOWN+6*RIGHT)
        x_1 = Tex("-1")
        x_2 = Tex("-2")
        x_3 = Tex("-3")
        
        x_3.move_to(0.7*DOWN+6*LEFT)
        x_2.move_to(0.7*DOWN+4*LEFT)
        x_1.move_to(0.7*DOWN+2*LEFT)
        
        
        
        self.play(ShowCreation(tick),Write(x0),Write(x1),tick.copy().shift,2*RIGHT)
        
        self.play(line.copy().animate.shift(2*RIGHT),tick.copy().animate.shift(4*RIGHT),Write(x2))
        self.play(line.copy().animate.shift(4*RIGHT),tick.copy().animate.shift(6*RIGHT),Write(x3))
        self.play(Write(x_1),tick.copy().shift,2*LEFT,line.copy().shift,2*LEFT)
        self.play(line.copy().animate.shift(4*LEFT),tick.copy().animate.shift(4*LEFT),Write(x_2))
        self.play(line.copy().animate.shift(6*LEFT),tick.copy().animate.shift(6*LEFT),Write(x_3))
        self.play(ShowCreation(arr))
        self.wait(3)


class slide2(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([-6,6.5,1]),  unit_size=1,include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[6.5])
        numberl.shift(0.25*RIGHT)
        print(numberl.get_center())
        self.play(ShowCreation(numberl))

        vector3  = Vector([3,0])
        print(vector3.get_center())
        vector3.set_color(color = RED)
        vector3.move_to(0.5*DOWN+vector3.get_center())
        self.play(ShowCreation(vector3))
        vector4  = Vector([-5,0])
        vector4.set_color(color = BLUE)
        vector4.move_to(0.5*DOWN+vector4.get_center())
        self.play(ShowCreation(vector4))
        self.play(vector3.move_to,0.5*UP+vector3.get_center())
        self.play(vector4.move_to,0.5*UP+vector4.get_center()+2*vector3.get_center())
        subNums = Tex("3-5=-2")
        
        subNums.to_edge(UP)
        self.play(FadeIn(subNums))
        self.wait(3)
        groupSub = VGroup (subNums,vector3,vector4,numberl)
        self.play(FadeOut(groupSub))

        numberl = NumberLine(x_range=np.array([-2,2.2,1]),  unit_size=3*1,include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[2.2])
       
        r25 = Tex("\\frac{2}{5}")
        r65 = Tex("-\\frac{6}{5}")
        r45 = Tex("-\\frac{4}{5}")
        tick25 = Line([3*2/5,0,0]+0.1*UP,[3*2/5,0,0]+0.1*DOWN)
        tick65 = Line([-6/5*3,0,0]+0.1*UP,[-6/5*3,0,0]+0.1*DOWN)
        tick45 = Line([-4/5*3,0,0]+0.1*UP,[-4/5*3,0,0]+0.1*DOWN)
        r25.next_to(tick25,DOWN)
        r65.next_to(tick65,DOWN)
        r45.next_to(tick45,DOWN)
        r25.scale(0.8)
        r65.scale(0.8)
        r45.scale(0.8)
        t = VGroup(r25,r65,r45,tick25,tick65,tick45)
        self.play(ShowCreation(numberl),ShowCreation(t))
        vector3  = Vector([3*2/5,0])
        vector3.set_color(color = RED)
        vector3.move_to(0.5*UP+vector3.get_center())
        self.play(ShowCreation(vector3))
        vector4  = Vector([-6/5*3,0])
        vector4.set_color(color = BLUE)
        vector4.move_to(0.5*UP+vector4.get_center())
        self.play(ShowCreation(vector4))
        self.play(vector3.move_to,0.5*DOWN+vector3.get_center())
        self.play(vector4.move_to,0.5*DOWN+vector4.get_center()+2*vector3.get_center())
        subNums = Tex("\\frac{2}{5}-\\frac{6}{5}=-\\frac{4}{5}")
        
        subNums.to_edge(UP)
        self.play(FadeIn(subNums))
        self.wait(3)
        groupSub = VGroup (subNums,vector3,vector4,t,numberl)
        self.play(FadeOut(groupSub))
        self.wait(3)


class slide3(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([-6,6.5,1]),  unit_size=1,include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[6.5])
        numberl.shift(0.25*RIGHT)
        self.play(ShowCreation(numberl))

        vector3  = Vector([4,0])
        vector3.set_color(color = RED)
        vector3.move_to(0.5*DOWN+vector3.get_center())
        self.play(ShowCreation(vector3))
        vector4  = Vector([-6,0])
        vector4.set_color(color = BLUE)
        vector4.move_to(0.5*DOWN+vector4.get_center())
        self.play(ShowCreation(vector4))
        self.play(vector3.move_to,0.5*UP+vector3.get_center())
        self.play(vector4.move_to,0.5*UP+vector4.get_center()+2*vector3.get_center())
        subNums = Tex("4+(-6)=-2")
        
        subNums.to_edge(UP)
        self.play(FadeIn(subNums))
        self.wait(3)
        groupSub = VGroup (subNums,vector3,vector4,numberl)
        self.play(FadeOut(groupSub))

        
        
        numberl = NumberLine(x_range=np.array([-6,6.5,1]),  unit_size=1,include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[6.5])
        numberl.shift(0.25*RIGHT)
        self.play(ShowCreation(numberl))

        vector3  = Vector([-2,0])
        vector3.set_color(color = RED)
        vector3.move_to(0.5*DOWN+vector3.get_center())
        self.play(ShowCreation(vector3))
        vector4  = Vector([-4,0])
        vector4.set_color(color = BLUE)
        vector4.move_to(0.5*DOWN+vector4.get_center())
        self.play(ShowCreation(vector4))
        self.play(vector3.move_to,0.5*UP+vector3.get_center())
        self.play(vector4.move_to,0.5*UP+vector4.get_center()+2*vector3.get_center())
        subNums = Tex("-2+(-4)=-6")
        
        subNums.to_edge(UP)
        self.play(FadeIn(subNums))
        self.wait(3)
        groupSub = VGroup (subNums,vector3,vector4)
        self.play(FadeOut(groupSub))

        vector3  = Vector([-2,0])
        vector3.set_color(color = RED)
        vector3.move_to(0.5*DOWN+vector3.get_center())
        self.play(ShowCreation(vector3))
        vector4  = Vector([4,0])
        vector4.set_color(color = BLUE)
        vector4.move_to(0.5*DOWN+vector4.get_center())
        self.play(ShowCreation(vector4))
        
        vector5  = Vector([-5,0])
        vector5.set_color(color = GREEN)
        vector5.move_to(0.5*DOWN+vector5.get_center())
        self.play(ShowCreation(vector5))
        vector1  = Vector([-1,0])
        vector1.set_color(color = PINK)
        vector1.move_to(0.5*DOWN+vector1.get_center())
        self.play(ShowCreation(vector1))
        self.play(vector3.move_to,0.5*UP+vector3.get_center())
        self.play(vector4.move_to,0.5*UP+vector4.get_center()+2*vector3.get_center())
        self.play(vector5.move_to,0.5*LEFT)

        self.play(vector1.move_to,3.5*LEFT)
        subNums = Tex("-2+4-5-1=-4")
        
        subNums.to_edge(UP)
        self.play(FadeIn(subNums))
        self.wait(3)
        groupSub = VGroup (subNums,vector3,vector4,vector5,vector1,numberl)
        self.play(FadeOut(groupSub))

        self.wait(3)
        


class slide4(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([-6,7,1]),  unit_size=1,include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[7])

        numberl.shift(0.5*RIGHT)
        self.play(ShowCreation(numberl))

        vector5  = Vector([3,0])
        vector5.set_color(color = RED)
        
        self.play(ShowCreation(vector5))
        
        multiply = Tex("3\\cdot(-1)=-3")
        
        multiply.to_edge(UP)
        self.play(Write(multiply))
        self.play(Rotating(
                        vector5,
                        PI,
                        about_point=[0,0,0],
                        run_time = 1.5
                    ))
        self.wait(2)
        
        multiplym = Tex("-3\\cdot(-1)=3")
        self.remove(multiply)
        multiplym.to_edge(UP)
        self.play(Write(multiplym))
        self.play(Rotating(
                        vector5,
                        PI,
                        about_point=[0,0,0],
                        run_time = 1.5
                    ))
        
        self.wait(2)
        
        self.remove(multiplym)
        self.play(Write(multiply))
        self.play(Rotating(
                        vector5,
                        PI,
                        about_point=[0,0,0],
                        run_time = 1.5
                    ))
        self.wait(2)
        self.remove(multiply)
        self.play(Write(multiplym))
        self.play(Rotating(
                        vector5,
                        PI,
                        about_point=[0,0,0],
                        run_time = 1.5
                    ))
        self.wait(2)
        groupMmin = VGroup (multiplym,vector5)
        self.play(FadeOut(groupMmin))
        self.wait(3)


class slide5(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([-7,7.5,1]),  unit_size=0.8,include_numbers=True,
       include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[7.5])
        numberl.shift(0.25*RIGHT)
        numberl.shift(2*DOWN)
        self.play(ShowCreation(numberl))       
        mult = Tex("3\\cdot(-2)","=(-1)\\cdot 3\\cdot 2","=-6")
        mult.set_color(color = BLACK)
        mult.to_edge(UP)

        vector7  = Vector([0.8*3,0])
        vector7.set_color(color = BLUE)
        
        vector6  = Vector([0.8*6,0])
        vector6.set_color(color = BLUE)
        vector6.shift(2*DOWN)
        vector7.shift(2*DOWN)
        self.play(ShowCreation(vector7),Write(mult[0]),run_time = 5)

        self.play(ReplacementTransform(vector7,vector6),Write(mult[1]),run_time = 5)

        brace = Brace(vector7,DOWN)

        
        
        self.play(Write(mult[2]),Rotating(
                        vector6,
                        PI,
                        about_point=[0,-2,0],
                        run_time = 5
                    ))

        # self.play(ShowCreation(vector_group),ShowCreation(brace_group),FadeIn(mult),run_time = 5)
        # self.play(vector7.copy().shift,3*0.8*RIGHT,vector7.copy().shift,6*0.8*RIGHT,
        # vector7.copy().shift,9*0.8*RIGHT,vector7.copy().shift,12*0.8*RIGHT,run_time = 5)
        # self.play(vector7.stretch, 5,0,{"about_edge": LEFT},run_time = 5)
        
        self.wait()
        vector_group = VGroup(*[
                    vector7.copy().shift(3*x*0.8*RIGHT)
                    for x in range(5)
                    
                ])
        brace_group = VGroup(*[
                    brace.copy().shift(3*x*0.8*RIGHT)
                    for x in range(5)
                    
                ])
        # groupMminm = VGroup (mult,vector7,vector_group,brace_group,brace)
        # self.play(FadeOut(groupMminm))

        # vector7  = Vector([5*0.8,0])
        # vector7.set_color(color = BLUE)
        # vector7.move_to(numberl.get_start()+5*0.8/2*RIGHT)
        # self.play(ShowCreation(vector7))
        # brace = Brace(vector7,DOWN)
        # self.play(ShowCreation(brace))
        # vector_group = VGroup(*[
        #             vector7.copy().shift(5*x*0.8*RIGHT)
        #             for x in range(3)
                    
        #         ])
        # brace_group = VGroup(*[
        #             brace.copy().shift(5*x*0.8*RIGHT)
        #             for x in range(3)
                    
        #         ])
        # mult = Tex("5\\cdot3=15")
        # mult.set_color(color = BLACK)
        # mult.to_edge(UP)
    
        # self.play(ShowCreation(brace_group),ShowCreation(vector_group),FadeIn(mult),run_time = 5)
        # # self.play(vector7.copy().shift,5*0.8*RIGHT,vector7.copy().shift,10*0.8*RIGHT,run_time = 5)
        # # self.play(vector7.stretch, 3,0,{"about_edge": LEFT},run_time = 5)
        
        # self.wait()
        # groupMminm = (groupMminm))

        self.wait(3)