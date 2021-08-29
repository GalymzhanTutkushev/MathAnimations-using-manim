from manimlib import *

class slide1(Scene):
    def construct(self):
        w=2
        h=0.3
        R = 0.5
        
        left_cup = Rectangle(w,h).shift(3*LEFT+1*UP)
        right_cup = Rectangle(w,h).shift(3*RIGHT+1*UP)
        left_cup.set_fill(GREY_A,1)
        right_cup.set_fill(GREY_A,1)
        ves_right = Square(0.5)
        ves_left = Square(1)
        ves_left.next_to(left_cup,UP,buff = 0)
        ves_right.next_to(right_cup,UP,buff = 0)
        ves_left.set_fill(BLUE,1)
        ves_right.set_fill(TEAL,1)
        c = Circle(radius = R).move_to(ORIGIN)
        d1 = 2*LEFT+2*DOWN
        d2 = -2*LEFT+2*DOWN
        metka = Line(0.25*UP,0.45*UP).set_color(RED)
        opora1  = Line([R*np.cos(225*DEGREES),R*np.sin(225*DEGREES),0],d1)
        opora2  = Line([R*np.cos(-45*DEGREES),R*np.sin(-45*DEGREES),0],d2)
        opora3  = Line(d2,d1)
        t = Triangle().scale(0.2).move_to(ORIGIN).set_fill(RED,1)
        v = VGroup(left_cup,right_cup,ves_right,ves_left,c,t,opora1,opora2,opora3,metka)
        self.play(ShowCreation(v))
        an = PI/18
        self.play(Rotate(t,an),
        left_cup.animate.shift(-np.sin(an)*UP),
        right_cup.animate.shift(np.sin(an)*UP),
        ves_left.animate.shift(-np.sin(an)*UP),
        ves_right.animate.shift(np.sin(an)*UP),
        
        )

        # self.play(
        # Rotate(left_cup,-PI/12,about_point = left_cup.get_center()),
        # Rotate(right_cup,-PI/12,about_point = right_cup.get_center()),
        # )
        self.wait(pause_time)

class slide7(Scene):
    def construct(self):
        eq = Tex("3x+50 = 200")
        eq1 = Tex("3x+50-50 = 200-50")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()


class slide8(Scene):
    def construct(self):
        eq = Tex("3x+50 = 200")
        eq1 = Tex("3x+50-50 = 200-50")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()


class slide9(Scene):
    def construct(self):
        eq = Tex("3x+50 = 200")
        eq1 = Tex("3x+50-50 = 200-50")
        eq2 = Tex("\\frac{1}{3}\\cdot 3x =\\frac{1}{3}\\cdot 150")
        eq3 = Tex("x= 50")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()

class slide10(Scene):
    def construct(self):
        eq = Tex("3x+50 = 200")
        eq1 = Tex("3x+50-50 = 200-50")
        eq2 = Tex("\\frac{1}{3}\\cdot 3x =\\frac{1}{3}\\cdot 150")
        eq3 = Tex("x= 50")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()

class slide11(Scene):
    def construct(self):
        eq = Tex("(x-1)(x-2) = 0")
        eq1 = Tex("{(x-1)(x-2) \\over (x-2)} = {0 \\over (x-2)}")
        eq2 =Tex("x-1 = 0")
        eq3 =Tex("x=1")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()


class slide12(Scene):
    def construct(self):
        eq = Tex("3x+7-x = 5-2x")
        eq1 = Tex("3x+7-x-5+2x=0")
        eq3 =Tex("4x+2 = 0")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()


class slide13(Scene):
    def construct(self):
        eq = Tex("50x+a = 10000")
        eq1 = Tex("x = {10000-a \\over 50}")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()


class slide14(Scene):
    def construct(self):
        eq = Tex("ax+b = 0")
        eq1 = Tex("x = -{b \\over a}")
        eq2 = Tex("0\\cdot x+0 = 0")
        eq3 = Tex("0 \\cdot x+b = 0")
        self.play(Write(eq))
        self.play(Transform(eq,eq1))
        self.wait()