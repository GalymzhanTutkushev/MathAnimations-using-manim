from manimlib import *



class set(Scene):
    def construct(self):
        R=2
        c1sc2 = Tex("A\\subset B")
        c1uc2 = Tex("A\\cup B")
        c1nc2 = Tex("A\\cap B")
        c1_c2 = Tex("A-B")
        c1uc2.to_edge(UP)
        c1nc2.to_edge(UP)
        c1_c2.to_edge(UP)
        c1 = Circle(radius = R)
        c1.shift(RIGHT)
        c2 = Circle(radius = R)
        c2.move_to(LEFT)
        sc1 = Sector(PI/2,PI)
        sc2 = Sector(-PI/2,PI)
        sc1.set_stroke(width = 0)
        sc1.set_stroke(width = 0)
        sc1.stretch_about_point(1.5,1,DOWN)
        sc2.stretch_about_point(1.5,1,DOWN)
        sc1.shift(0.5*DOWN)
        sc2.shift(0.5*DOWN)
        sc1.set_fill(color = BLUE,opacity = 0.5)
        sc2.set_fill(color = BLUE,opacity = 0.5)
        # c1.set_fill(color = BLUE,opacity = 0.5)
        # c2.set_fill(color = BLUE,opacity = 0.5)
        self.play(Write(c1),Write(c2),(Write(c1uc2)))
        self.play(Write(sc1),Write(sc2))
