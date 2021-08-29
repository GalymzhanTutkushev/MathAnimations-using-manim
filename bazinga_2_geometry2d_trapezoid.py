from manimlib import *


class trap_slide1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        screen_grid = NumberPlane()
        self.add(screen_grid)
        self.save_state()
        a = 6
        b = 4
        h = 3
        trapezoid = Polygon(
                ORIGIN,[a,0,0],[a-1,h,0],[a-b-1,h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        trapezoid.move_to(ORIGIN)

        at_label = Tex("a")
        bt_label = Tex("b")
        ht_label = Tex("h")
        
        bt_label.next_to(trapezoid, UP)
        
     
        self.add(bt_label)
        at_label.next_to(trapezoid, DOWN)
       
      
        self.add(at_label)

        
        ht = DashedLine([a-b-1-3,h-h/2,0],[a-b-1-3,-h/2,0])
        ht_label.next_to(ht,RIGHT)
        self.play(ShowCreation(trapezoid),run_time = 3)
        self.play(ShowCreation(ht_label),ShowCreation(ht))
        self.wait(pause_time)
        self.restore()
        
        a = 6
        b = 4
        h = 3
        trapezoid = Polygon(
                ORIGIN,[a,0,0],[a,h,0],[a-b-1,h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        trapezoid.move_to(ORIGIN)

        at_label = Tex("a")
        bt_label = Tex("b")
        ht_label = Tex("h")
        
        bt_label.next_to(trapezoid, UP)
        
     
        self.add(bt_label)
        at_label.next_to(trapezoid, DOWN)
       
      
        self.add(at_label)

        
        ht = DashedLine([a-b-1-3,h-h/2,0],[a-b-1-3,-h/2,0])
        ht_label.next_to(ht,RIGHT)
        self.play(ShowCreation(trapezoid),run_time = 3)
        self.play(ShowCreation(ht_label),ShowCreation(ht))
        self.wait(pause_time)
        self.play(FadeOut(bt_label),FadeOut(at_label))
        self.restore()
        
      

        
        a = 6
        b = 6
        h = 3
        trapezoid = Polygon(
                ORIGIN,[a,0,0],[a,h,0],[a-b,h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        trapezoid.move_to(ORIGIN)

        ht = DashedLine([a-b-1-3,h-h/2,0],[a-b-1-3,-h/2,0])
        ht_label.next_to(ht,RIGHT)
        self.play(ShowCreation(trapezoid),run_time = 3)
        
        self.wait(pause_time)
        self.restore()
        
        w = 6
        h = 3
        
        paralelogram = Polygon(
                ORIGIN, w*RIGHT,w*RIGHT+h*UP+2*RIGHT,h*UP+2*RIGHT,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        paralelogram.move_to(ORIGIN)
        ht = DashedLine([a-b-2,h-h/2,0],[a-b-2,-h/2,0])
        ht_label.next_to(ht,LEFT)
        
        self.play(ShowCreation(paralelogram),run_time = 3)
        self.play(ShowCreation(ht_label),ShowCreation(ht))
        
     
        self.restore()
        self.wait(pause_time)
        
class trap_slide2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        a = 6
        b = 4

        h = 3
        trapezoid = Polygon(
                ORIGIN,[a,0,0],[a-2,h,0],[a-b-1,h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        trapezoid.move_to(ORIGIN)

        at_label = Tex("a")
        bt_label = Tex("b")
        ht_label = Tex("h")
        ab2_label = Tex("\\frac{a+b}{2}")
        bt_label.next_to(trapezoid, UP)
        
     
        self.add(bt_label)
        at_label.next_to(trapezoid, DOWN)
        
      
        self.add(at_label)

        
        ht = DashedLine([a-b-4,h-h/2,0],[a-b-4,-h/2,0])
        ab2 = DashedLine(2.5*LEFT,2*RIGHT)
        ab2_label.next_to(ab2,UP,buff = SMALL_BUFF)
        ab2_label.scale(0.6)
        ht_label.next_to(trapezoid,LEFT,buff = SMALL_BUFF)
        self.play(ShowCreation(trapezoid),run_time = 3)
        self.play(Write(ht_label),ShowCreation(ht))
        self.play(ShowCreation(ab2),run_time = 3)
        self.play(Write(ab2_label),run_time = 3)
        self.wait(pause_time)


class trap_slide3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        
        
        screen_grid = NumberPlane()
        self.add(screen_grid)
        
        a = 6
        b = 4
        h = 3
        trapezoid = Polygon(
                ORIGIN,[a,0,0],[a-1,h,0],[a-b-1,h,0],
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
        )
        trapezoid.move_to(ORIGIN)

        at_label = Tex("a")
        bt_label = Tex("b")
        ht_label = Tex("h")
        ab = Tex("b+a")
        ba = Tex("a+b")
        bt_label.next_to(trapezoid, UP)
        ab.next_to(trapezoid, UP)
     
        self.add(bt_label)
        at_label.next_to(trapezoid, DOWN)
        ba.next_to(trapezoid, DOWN)
      
        self.add(at_label)

        ht_label.next_to(trapezoid,LEFT)
        ht = DashedLine([a-b-1-3,h-h/2,0],[a-b-1-3,-h/2,0])
        
        self.play(ShowCreation(trapezoid),run_time = 3)
        self.play(ShowCreation(ht_label),ShowCreation(ht))
        self.play(trapezoid.shift,3*LEFT,ht.shift,3*LEFT,ht_label.shift,3*LEFT,run_time = play_time)
        tr = trapezoid.copy()
        self.play(tr.shift,(b+1)*RIGHT,run_time = play_time)
        self.play(tr.flip,LEFT,run_time = play_time)
        
        trapezion_eq = Tex("S=\\frac{a+b}{2}\\cdot h")
        trapezion_eq.to_edge(UP)
        self.play(FadeIn(trapezion_eq),Transform(at_label,ba),Transform(bt_label,ab))
        self.wait(pause_time)
        self.play(FadeOut(trapezion_eq))
        self.wait(pause_time)
