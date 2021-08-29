from manimlib import *
import numpy as np


class slide3(Scene):
    def construct(self):
        nl = NumberLine(x_range=np.array([0,12,1]),
         unit_size=1,include_numbers=True,include_tip=True, 
         line_to_number_direction=UP,numbers_to_exclude=[12])
        self.play(ShowCreation(nl))


class slide4(Scene):
    def construct(self):
        nl = NumberLine(x_range=np.array([0,12,1]),
         unit_size=1,include_numbers=True,include_tip=True, 
         line_to_number_direction=UP,numbers_to_exclude=[12])
        self.play(ShowCreation(nl))

class slide5(Scene):
    def construct(self):
        nl = NumberLine(x_range=np.array([0,12,1]),
         unit_size=1,include_numbers=True,include_tip=True, 
         line_to_number_direction=UP,numbers_to_exclude=[12])
        self.play(ShowCreation(nl))

class slide7(Scene):
    def construct(self):
        t =Tex("ax+b\\geqslant0")
        t1 = Tex("ax\\geqslant -b")
        t2 = Tex("x\\geqslant -\\frac{b}{a}")
        nl = NumberLine(x_range=np.array([0,12,1]),
         unit_size=1,include_numbers=True,include_tip=True, 
         line_to_number_direction=UP,numbers_to_exclude=[12])
        self.play(ShowCreation(nl))