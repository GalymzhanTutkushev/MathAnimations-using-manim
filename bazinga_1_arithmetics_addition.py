from manimlib import *


class slide1(Scene):
    def construct(self):
        m = 2
        side = 0.7
        square = Square(side_length = side)
        square.move_to(5*LEFT)
        square_group = VGroup(*[
                    square.copy().shift(side*x*RIGHT)
                    for x in range(m)
        
                ])
        square_group.set_stroke(color=BLACK, width = 5)
        square_group.set_fill(color=GREEN_SCREEN, opacity = 0.5)
        m_label = Tex(str(m))
        m_label.next_to(square_group,UP)
        sm =VGroup(square_group,m_label)
        self.play(ShowCreation(sm))
        n = 4
        square1 = Square(side_length = side)
        square1.next_to(square_group,RIGHT,buff = 1)
        square_group1 = VGroup(*[
                    square1.copy().shift(side*x*RIGHT)
                    for x in range(n)
        
                ])
        square_group1.set_stroke(color=BLACK, width = 5)
        square_group1.set_fill(color=GREEN_SCREEN, opacity = 0.5)
        n_label = Tex(str(n))
        n_label.next_to(square_group1,UP)
        sn =VGroup(square_group1,n_label)
        self.play(ShowCreation(sn))

        plus = Tex("+")
        plus.scale(2)
        plus.next_to(square_group, RIGHT,buff = 0.2)
        self.play(ShowCreation(plus))
        eq = Tex("=")
        eq.scale(2)
        eq.next_to(square_group1, RIGHT,buff = 0.2)
        self.play(ShowCreation(eq))


        mn_label = Tex(str(m+n))
        mn_label.move_to(m_label.get_center()+7.5*RIGHT)


        squareM = Square(side_length = side)
        squareM.next_to(eq,RIGHT)
        square_groupM = VGroup(*[
                    squareM.copy().shift(side*x*RIGHT)
                    for x in range(m)
        
                ])
        square_groupM.set_stroke(color=BLACK, width = 5)
        square_groupM.set_fill(color=GREEN_SCREEN, opacity = 0.5)

        squareN = Square(side_length = side)
        squareN.next_to(square_groupM,RIGHT,buff=0)
        square_groupN = VGroup(*[
                    squareN.copy().shift(side*x*RIGHT)
                    for x in range(n)
        
                ])
        square_groupN.set_stroke(color=BLACK, width = 5)
        square_groupN.set_fill(color=GREEN_SCREEN, opacity = 0.5)


        self.play(ReplacementTransform(square_group.copy(),square_groupM,path_arc = PI/2),
        ReplacementTransform(square_group1.copy(),square_groupN,path_arc = PI/2),run_time = play_time)
        self.play(ShowCreation(mn_label))
        # self.wait()
        # self.play(Swap(sn,sm),plus.shift,side*RIGHT,eq.shift,side/2*LEFT,run_time = play_time)
        self.wait(pause_time)

class slide3(Scene):
    def construct(self):
        m = 2
        side = 0.7
        square = Square(side_length = side)
        square.move_to(5*LEFT+2*DOWN)
        square_group = VGroup(*[
                    square.copy().shift(side*x*RIGHT)
                    for x in range(m)
        
                ])
        square_group.set_stroke(color=BLACK, width = 5)
        square_group.set_fill(color=GREEN_SCREEN, opacity = 0.5)
        m_label = Tex(str(m))
        m_label.next_to(square_group,UP)
        sm =VGroup(square_group,m_label)
        
        n = 4
        square1 = Square(side_length = side)
        square1.next_to(square_group,RIGHT,buff = 1)
        square_group1 = VGroup(*[
                    square1.copy().shift(side*x*RIGHT)
                    for x in range(n)
        
                ])
        square_group1.set_stroke(color=BLACK, width = 5)
        square_group1.set_fill(color=GREEN_SCREEN, opacity = 0.5)
        n_label = Tex(str(n))
        n_label.next_to(square_group1,UP)
        sn =VGroup(square_group1,n_label)
        

        plus = Tex("+")
        plus.scale(2)
        plus.next_to(square_group, RIGHT,buff = 0.2)
        
        eq = Tex("=")
        eq.scale(2)
        eq.next_to(square_group1, RIGHT,buff = 0.2)
        


        mn_label = Tex(str(m+n))
        mn_label.move_to(m_label.get_center()+7.5*RIGHT)


        squareM = Square(side_length = side)
        squareM.next_to(eq,RIGHT)
        square_groupM = VGroup(*[
                    squareM.copy().shift(side*x*RIGHT)
                    for x in range(m)
        
                ])
        square_groupM.set_stroke(color=BLACK, width = 5)
        square_groupM.set_fill(color=GREEN_SCREEN, opacity = 0.5)

        squareN = Square(side_length = side)
        squareN.next_to(square_groupM,RIGHT,buff=0)
        square_groupN = VGroup(*[
                    squareN.copy().shift(side*x*RIGHT)
                    for x in range(n)
        
                ])
        square_groupN.set_stroke(color=BLACK, width = 5)
        square_groupN.set_fill(color=GREEN_SCREEN, opacity = 0.5)

        numberl = NumberLine(color = BLACK, x_range=np.array([0,9,1]), unit_size=1,include_numbers=True, include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[9])
        numberl.move_to(0.5*LEFT+1.4*UP)
        self.play(ShowCreation(numberl))

        vector2  = Arrow(numberl.get_start()+0.25*LEFT,numberl.get_start()+2.25*RIGHT)
        vector2.set_color(color = BLUE)
        vector4  = Arrow(numberl.get_start()+1.75*RIGHT,numberl.get_start()+6.25*RIGHT)
        vector4.set_color(color = RED)
        # vector3 = Arrow(numberl.get_start()+5.75*RIGHT,9.25*RIGHT+numberl.get_start())
        # vector3.set_color(color =GREEN)
        # vector1  = Arrow(numberl.get_start()+8.75*RIGHT,numberl.get_start()+10.25*RIGHT)
        # vector1.set_color(color = YELLOW)
        # vector1.scale(2)
        # vector2.move_to(numberl.get_start()+0.5*RIGHT)
        # vector2.stretch(2)
        self.play(ShowCreation(vector2),ShowCreation(sm))
        # self.play(vector2.copy().shift,RIGHT)
        # self.play(vector.move_to,DOWN+vector.get_center()+numberl.get_start()+2.5*RIGHT)

        v=VGroup(vector4,vector2)
        self.play(ShowCreation(vector4),ShowCreation(sn),run_time = 2)
        # self.play(ShowCreation(vector3))
        # self.play(ShowCreation(vector1))

        # brace1 = Brace(vector1,DOWN)
        brace2 = Brace(vector2,DOWN)
        # brace3 = Brace(vector3,DOWN)
        brace4 = Brace(vector4,DOWN)
        self.play(ShowCreation(brace2),ShowCreation(brace4),ShowCreation(plus),ShowCreation(eq))
        line11 = Line(numberl.get_start()+0.5*UP,numberl.get_start()+6*RIGHT+0.5*UP)
        
        brace11 = Brace(line11, UP)
        text11 = Tex("6")
        text11.next_to(brace11,UP)
       
        self.play(ReplacementTransform(square_group.copy(),square_groupM,path_arc = PI/2),
        ReplacementTransform(square_group1.copy(),square_groupN,path_arc = PI/2),run_time = play_time)
        self.play(ShowCreation(brace11),ShowCreation(mn_label))
        addNums = Tex("2+4=6")
        addNums.set_color(color = BLACK)
        addNums.to_edge(UP)
        self.play(Write(addNums))
        # self.play(FadeOut(v))
        # self.play(FadeOut(addNums))
        
        
        

        self.play(Swap(sn,sm),plus.shift,side*RIGHT,eq.shift,side/2*LEFT,vector2.shift,4*RIGHT,vector4.shift,2*LEFT,
        brace2.shift,4*RIGHT,brace4.shift,2*LEFT,run_time = play_time)
        self.wait(pause_time)
        
        # self.play(FadeIn(subNums))
        # groupAdd = VGroup (vector,vector_group)
        # self.play(FadeOut(groupAdd))
        # line4 = Line(numberl.get_start(),numberl.get_start()+2*RIGHT)
        # brace4 = Brace(line4, DOWN)
        # text4 = Tex("2")
        # text4.next_to(brace4,DOWN)
        # self.play(ShowCreation(brace4),Write(text4))
        # line7 = Line(numberl.get_start()+2*RIGHT,numberl.get_start()+6*RIGHT)
        # brace7 = Brace(line7, DOWN)
        # text7 = Tex("4")
        # text7.next_to(brace7,DOWN)
        # self.play(ShowCreation(brace7),Write(text7))
        # 
       
        # self.play(brace4.shift,4*RIGHT,brace7.shift,2*LEFT,vector2.shift,4*RIGHT,vector.shift,2*LEFT,text4.shift,4*RIGHT,text7.shift,2*LEFT)
        
        self.wait(pause_time)
       

class slide4(Scene):
    def construct(self):
        numberl = NumberLine(color = BLACK, x_range=np.array([0,12,1]), unit_size=1,include_numbers=True, include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[12])

        numberl.move_to(0.5*LEFT)
        self.play(ShowCreation(numberl))

        vector2  = Arrow(numberl.get_start()+0.25*LEFT,numberl.get_start()+2.25*RIGHT)
        vector2.set_color(color = BLUE)
        vector4  = Arrow(numberl.get_start()+1.75*RIGHT,numberl.get_start()+6.25*RIGHT)
        vector4.set_color(color = RED)
        vector3 = Arrow(numberl.get_start()+5.75*RIGHT,9.25*RIGHT+numberl.get_start())
        vector3.set_color(color =GREEN)
        vector1  = Arrow(numberl.get_start()+8.75*RIGHT,numberl.get_start()+10.25*RIGHT)
        vector1.set_color(color = YELLOW)
       
        self.play(ShowCreation(vector2))
       
        v=VGroup(vector4,vector2)
        self.play(ShowCreation(vector4),run_time = 2)
        self.play(ShowCreation(vector3))
        self.play(ShowCreation(vector1))

        brace1 = Brace(vector1,DOWN)
        brace2 = Brace(vector2,DOWN)
        brace3 = Brace(vector3,DOWN)
        brace4 = Brace(vector4,DOWN)
        self.play(ShowCreation(brace1),ShowCreation(brace2),ShowCreation(brace3),ShowCreation(brace4))
        addNums = Tex("2+4+3+1=10")
        addNums.set_color(color = BLACK)
        addNums.to_edge(UP)
        self.play(FadeIn(addNums))
       
        
        
        line11 = Line(numberl.get_start()+0.5*UP,numberl.get_start()+10*RIGHT+0.5*UP)
        
        brace11 = Brace(line11, UP)
        text11 = Tex("10")
        text11.next_to(brace11,UP)
        self.play(ShowCreation(brace11),Write(text11))

        self.play(vector1.shift,4*LEFT,vector2.shift,3*RIGHT,vector3.shift,6*LEFT,vector4.shift,4*RIGHT,
        brace1.shift,4*LEFT,brace2.shift,3*RIGHT,brace3.shift,6*LEFT,brace4.shift,4*RIGHT,run_time = play_time)
        self.wait(pause_time)
        self.play(vector1.shift,5*LEFT,vector2.shift,2*LEFT,vector3.shift,3*RIGHT,
        brace1.shift,5*LEFT,brace2.shift,2*LEFT,brace3.shift,3*RIGHT,run_time = play_time)
        self.wait(pause_time)
        self.play(vector1.shift,4*RIGHT,vector2.shift,4*RIGHT,vector3.shift,4*RIGHT,vector4.shift,6*LEFT,
        brace1.shift,4*RIGHT,brace2.shift,4*RIGHT,brace3.shift,4*RIGHT,brace4.shift,6*LEFT,run_time = play_time)

        self.wait(pause_time)