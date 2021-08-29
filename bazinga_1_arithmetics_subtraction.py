from manimlib import *

class slide1(Scene):
    def construct(self):
        m = 2
        side = 0.7
        
        m_label = Tex(str(m))
        
        n = 4
        
        n_label = Tex(str(n))
        
        plus = Tex("-")
        plus.scale(2)
        
        eq = Tex("=")
        eq.scale(2)
        
        mn_label = Tex(str(m+n))
        mn_label.shift(0.8*UP)
        mn_label.shift(0.2*LEFT)


        squareM = Square(side_length = side)
        squareM.shift(2*LEFT)
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

        self.play(ShowCreation(square_groupM),ShowCreation(square_groupN),ShowCreation(mn_label))
        self.play(FadeOut(square_groupN,DOWN))
    
        self.wait(pause_time)