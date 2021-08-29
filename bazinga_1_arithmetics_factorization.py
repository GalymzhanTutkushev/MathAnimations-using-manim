from manimlib import *


class slide3(Scene):
    def construct(self):
        addNums = Tex("a=","a+b","-b")
        addNums.set_color(color = BLACK)
        addNums.to_edge(UP)
        numberl = NumberLine(color = BLACK,x_range=np.array([0,12,1]), unit_size=1,include_numbers=True, include_tip=True, line_to_number_direction=UP,numbers_to_exclude=[12])
        numberl.move_to(0.5*LEFT)
        self.play(ShowCreation(numberl),Write(addNums[0]))

        vector2  = Arrow(numberl.get_start()+5.25*RIGHT+0.15*DOWN,numberl.get_start()+3.75*RIGHT+0.15*DOWN)
        vector2.set_color(color = BLUE)
        vector4  = Arrow(numberl.get_start()+1.75*RIGHT+0.15*UP,numberl.get_start()+3.25*RIGHT+0.15*UP)
        vector4.set_color(color = RED)
        
        v = VGroup(*[vector4.copy().shift(x*RIGHT)
                    for x in range(3)
                    ])
        v2 = VGroup(*[vector2.copy().shift(x*LEFT)
                    for x in range(3)
                    ])
        

        self.play(ShowCreation(vector4),ShowCreation(v),Write(addNums[1]),run_time = 4)
       
        self.play(ShowCreation(vector2),ShowCreation(v2),Write(addNums[2]),run_time = 4)
       
        
        

        self.wait(3)

class slide12(Scene):
    def construct(self):
        all_eq = Tex("525","=","5","\\cdot","5","\\cdot","3","\\cdot","7")

        all_eq[2].set_color(BLUE)
        all_eq[4].set_color(BLUE)
        all_eq[6].set_color(BLUE)
        all_eq[8].set_color(BLUE)

        all_eq.to_edge(DOWN)
        all_eq.scale(2)
        a525 = Tex("525")
        au5 = Tex("5")
        ad5 = Tex("5")
        a105 = Tex("105")
        a21 = Tex("21")
        a3 = Tex("3")
        a7 = Tex("7")
        au5.set_color(BLUE)
        ad5.set_color(BLUE)
        a3.set_color(BLUE)
        a7.set_color(BLUE)
        a525.scale(2)
        au5.scale(2)
        ad5.scale(2)
        a105.scale(2)
        a21.scale(2)
        a3.scale(2)
        a7.scale(2)
        a525.move_to(3*UP+1.5*LEFT)
        au5.move_to(a525.get_center()+1.5*DOWN+1.5*LEFT)
        a105.move_to(a525.get_center()+1.5*DOWN+1.5*RIGHT)
        ad5.move_to(a105.get_center()+1.5*DOWN+1.5*LEFT)
        a21.move_to(a105.get_center()+1.5*DOWN+1.5*RIGHT)
        a3.move_to(a21.get_center()+1.5*DOWN+1.5*LEFT)
        a7.move_to(a21.get_center()+1.5*DOWN+1.5*RIGHT)

        arr525tou5 = Arrow(a525.get_center()+0.25*DOWN,au5.get_center()+0.25*UP)
        arr525to105 = Arrow(a525.get_center()+0.25*DOWN,a105.get_center()+0.25*UP)
        arr105to21 = Arrow(a105.get_center()+0.25*DOWN,a21.get_center()+0.25*UP)
        arr105tod5 = Arrow(a105.get_center()+0.25*DOWN,ad5.get_center()+0.25*UP)
        arr21to3 = Arrow(a21.get_center()+0.25*DOWN,a3.get_center()+0.25*UP)
        arr21to7 = Arrow(a21.get_center()+0.25*DOWN,a7.get_center()+0.25*UP)
 

        self.play(Write(a525),Write(all_eq[0]))
        self.play(Write(arr525tou5),Write(arr525to105),Write(all_eq[1]))
        self.play(Write(au5),Write(all_eq[2]))
        self.play(Write(a105))
        self.play(Write(arr105tod5),Write(arr105to21),Write(all_eq[3]))
        self.play(Write(ad5),Write(all_eq[4]))
        self.play(Write(a21))
        self.play(Write(arr21to3),Write(arr21to7),Write(all_eq[5]))
        self.play(Write(a3),Write(all_eq[6]),Write(all_eq[7]))
        self.play(Write(a7),Write(all_eq[8]))
  

        self.wait(3)