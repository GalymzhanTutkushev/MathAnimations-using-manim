from manimlib import *
import numpy as np

class sym_slide2(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        rect = Rectangle()
        arr1 = Arrow(ORIGIN,2*LEFT)
        arr2 = Arrow(2*LEFT,2*LEFT+2.5*UP)
        arr3 = Arrow(2*LEFT+2.5*UP,3*RIGHT+2*DOWN)
        self.play(ShowCreation(rect))
        self.play(ShowCreation(arr1))
        self.play(FadeOut(arr1))
        self.play(rect.shift,2*LEFT)
        self.wait()
        self.play(ShowCreation(arr2))
        self.play(FadeOut(arr2))
        self.play(rect.shift,2.5*UP)
        self.wait()
        self.play(ShowCreation(arr3))
        self.play(FadeOut(arr3))
        self.play(rect.move_to,3*RIGHT+2*DOWN)
        
        self.wait(3)

class sym_slide3(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        line  = Line(2*LEFT+1*DOWN,2*RIGHT + 2*UP)
        brace = Brace(line)
        brace_label = Tex("5")
        brace_label.next_to(brace,UP)
        self.play(ShowCreation(line),ShowCreation(brace),ShowCreation(brace_label))

        # curve = ParametricCurve()


class sym_slide4(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        rect = Rectangle()
        self.play(ShowCreation(rect))
        self.save_state()
        dotC = 3*LEFT
        dot = Dot(dotC)

        D = -0.5*LEFT
        dotD = Dot(D)

        self.play(ShowCreation(dot))
        self.play(Rotating(rect, about_point = dotC,angle = 90 * DEGREES))
        self.restore()
        self.play(ShowCreation(dotD))
        self.play(Rotating(rect, about_point = dotD,angle =- 190 * DEGREES))
        self.wait(3)

class sym_slide5(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        rect = Rectangle()
        rect.scale(0.5)
        rect.shift(2*RIGHT)
        self.play(ShowCreation(rect))
        dotC = ORIGIN
        dot = SmallDot(dotC)
        self.play(ShowCreation(dot))
        dl = DashedLine(dotC,RIGHT)
        self.play(ShowCreation(dl))
        self.play(Rotating(rect, about_point = dotC,angle = 30 * DEGREES),
        Rotating(dl, about_point = dotC,angle = 30 * DEGREES))
        arr = Arc(0,30*DEGREES,radius = 0.5)
        
        arr2 = Arc(0,(80+30)*DEGREES,radius = 0.5)
       
        arr3 = Arc(0,TAU,radius = 0.5)
        
        self.play(ShowCreation(arr))
        self.wait()
        self.play(Rotating(rect, about_point = dotC,angle = 80 * DEGREES),
        Rotating(dl, about_point = dotC,angle = 80 * DEGREES))
        self.play(TransformFromCopy(arr,arr2))
        self.wait()
        self.play(Rotating(rect, about_point = dotC,angle = 250 * DEGREES),
        Rotating(dl, about_point = dotC,angle = 250 * DEGREES))
        self.play(TransformFromCopy(arr2,arr3))
        self.wait(3)
        


class sym_slide6(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        rect = Rectangle()
        rect.scale(0.5)
        rect.shift(2*RIGHT)
        self.play(ShowCreation(rect))
        dotC = ORIGIN
        dot = SmallDot(dotC)
        self.play(ShowCreation(dot))
        dl = DashedLine(dotC,RIGHT)
        self.play(ShowCreation(dl))
        self.play(Rotating(rect, about_point = dotC,angle = 30 * DEGREES),
        Rotating(dl, about_point = dotC,angle = 30 * DEGREES))
        arr = Arc(0,30*DEGREES,radius = 0.5)
        
        arr2 = Arc(0,(80+30)*DEGREES,radius = 0.5)
       
        arr3 = Arc(0,TAU,radius = 0.5)
        
        self.play(ShowCreation(arr))
        self.wait()
        self.play(Rotating(rect, about_point = dotC,angle = 80 * DEGREES),
        Rotating(dl, about_point = dotC,angle = 80 * DEGREES))
        self.play(TransformFromCopy(arr,arr2))
        self.wait()
        self.play(Rotating(rect, about_point = dotC,angle = 250 * DEGREES),
        Rotating(dl, about_point = dotC,angle = 250 * DEGREES))
        self.play(TransformFromCopy(arr2,arr3))
        self.wait(3)


class sym_slide7(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        rect = Rectangle()
        self.play(ShowCreation(rect))
        self.play(rect.animate.scale(2))
        self.play(rect.animate.scale(0.25))

class sym_slide8(Scene):
    def construct(self):
        numberp = NumberPlane(x_range=np.array([-7,7,1]),y_range=np.array([-7,7,1]),  unit_size=1,include_numbers=False,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[8])
        self.play(ShowCreation(numberp))
        rect = Rectangle()
        self.play(ShowCreation(rect))
        parabola = FunctionGraph(
            lambda x : (3-x)*(3+x)/4,
            x_min = -2, 
            x_max = 2
        )
        self.play(
            MoveAlongPath(rect, parabola.copy(),run_time = 6),
            # ShowCreation(parabola)
        )