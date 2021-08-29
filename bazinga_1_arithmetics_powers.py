from manimlib import *
from numpy import *

class power_definition(Scene):
    def construct(self):

        power_eq = Tex("3\\cdot 3","=","3^","{2}")
        power_eq3 = Tex("3\\cdot 3\\cdot 3","=","3^","{3}")
        brace2 = Brace(power_eq[0], DOWN)
        p_label2 = Tex("2")
        p_label2.next_to(brace2, DOWN, SMALL_BUFF)
        brace3 = Brace(power_eq3[0], DOWN)
        p_label3 = Tex("3")
        p_label3.next_to(brace3, DOWN, SMALL_BUFF)
        self.play(Write(power_eq[0]))
        self.play(FadeIn(brace2),FadeIn(p_label2))
        t = VGroup(brace2,power_eq[0],p_label2)
        self.play(TransformFromCopy(t,power_eq[1:4]),run_time = 5)
        self.wait(3)
        self.play(FadeOut(power_eq),FadeOut(brace2),FadeOut(p_label2))
        self.play(Write(power_eq3[0]))
        self.play(FadeIn(brace3),FadeIn(p_label3))
        t3 = VGroup(brace3,power_eq3[0],p_label3)
        self.play(TransformFromCopy(t3,power_eq3[1:4]),run_time = 5)
        self.wait(3)
        self.play(FadeOut(t3),FadeOut(power_eq3),FadeOut(brace3),FadeOut(p_label3))
        self.wait()


class powers_slide2(Scene):
    def construct(self):
        power_eq = Tex("3","^{2}","=","9")
        power_eq.to_edge(UP)
        power_eq3 = Tex("3^{3}","=","27")
        power_eq3.to_edge(UP)
        numberl = NumberLine(x_range=np.array([0,3,1]), unit_size=1,
        include_numbers=True,include_tip=False, line_to_number_direction=DOWN,numbers_to_exclude=[12])
        numberl.shift(0.5*RIGHT)
        numberl.shift(DOWN)
        self.play(ShowCreation(numberl),Write(power_eq[0]))
        numberl2 = NumberLine(x_range=np.array([0,3,1]), unit_size=1,
        include_numbers=True,include_tip=False, line_to_number_direction=UP,numbers_to_exclude=[12])
        numberl2.shift(1.25*LEFT)
        numberl2.shift(0.25*UP)
        numberl2.rotate(90*DEGREES)
        self.play(ShowCreation(numberl2),Write(power_eq[1])) 
        self.wait()
        self.play(Write(power_eq[2]))
        n = 3
        square = Square(2)
        # square.move_to(numberl.get_left())

        square.set_color(BLACK)
        square.set_fill(TEAL,0.5)
        square_group = VGroup(*[
                    square.copy().shift(x*RIGHT + y*UP)
                    for x in range(n-1)
                    for y in range(n-1)
                ])
        nt = [[1,2,3],[4,5,6],[7,8,9]]
        n_group = VGroup(*[
                    Tex(str(nt[y][x])).shift(x*RIGHT +0.5*LEFT+0.5*DOWN + y*UP)
                    for x in range(n)
                    for y in range(n)
                ])
        self.play(ShowCreation(square_group),ShowCreation(n_group),Write(power_eq[3])) 
        self.wait()
        self.play(FadeOut(square_group),FadeOut(n_group)
        ,FadeOut(power_eq),FadeOut(numberl),FadeOut(numberl2)) 
        cube = Cube()
        cube.scale(0.1)
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    cube = Cube()
                    cube.scale(0.5)
                    cube.move_to(x*RIGHT+y*UP+z*OUT)
                    self.play(ShowCreation(cube))

class powers_slide5(Scene):
    def construct(self):
        lines = VGroup(
            Tex("a^n\\cdot a^m",isolate = ["a","n","m"]),
            Tex("="),
            Tex("a^{n+m}",isolate = ["a","n","m"])
        )
        lines.arrange(RIGHT, buff=SMALL_BUFF)
        self.play(Write(lines[0:2]),
            run_time = 5)
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            run_time = 5
        )
        self.play(FadeOut(lines))
        self.wait(3)
        power_sump0 = Tex("2^{2}\\cdot 2^{3}=2^{2+3}")
        power_sump1 = Tex("(2\\cdot 2\\cdot 2)\\cdot (2\\cdot 2)=2^5")

class powers_slide6(Scene):
    def construct(self):
        lines = VGroup(
            Tex("(a^n)^m",isolate = ["a","n","m"]),
            Tex("="),
            Tex("a^{m\\cdot n}",isolate = ["a","n","m"])
        )
        lines.arrange(RIGHT, buff=SMALL_BUFF)
        self.play(Write(lines[0:2]))
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            run_time = 5
        )
        self.play(FadeOut(lines))
        # power_power = Tex("(a^n)^m=","a^{m\\cdot n}")
        # self.play(Write(power_power[0]))
        # self.play(TransformFromCopy(power_power[0],power_power[1]),run_time = 5)
        # self.wait(pause_time)
        # self.play(FadeOut(power_power))
        power_power = Tex("(2^3)^4","=","8^{4}","=","16^{3}")
        self.play(Write(power_power[0:2]))
        self.play(TransformFromCopy(power_power[0],power_power[2]),run_time = 5)
        self.play(Write(power_power[3]))
        self.play(TransformFromCopy(power_power[0],power_power[4]),run_time = 5)
        self.wait(pause_time)
        self.play(FadeOut(power_power))

        # power_power0 = Tex("(2^2)^3=2^{2\\cdot 3}")
        # self.play(Write(power_power0))
        # self.play(FadeOut(power_power0))
        # power_power1 = Tex("2^{2\\cdot 3}=2^6")
        # self.play(Transform(power_power0,power_power1))
        self.wait()
        # self.play(FadeOut(power_power1))

class powers_slide7(Scene):
    def construct(self):
        
        power_sqrt = Tex("a^{1\\over {{n}}}","=","\\sqrt[n]{a}",isolate = ["a"])
        self.play(Write(power_sqrt[0:2]))
        self.wait()
        self.play(TransformMatchingTex(power_sqrt[0],power_sqrt[2]),run_time = 5)
        self.play(FadeOut(power_sqrt))
        self.wait()

class powers_slide8(Scene):
    def construct(self):
        sqrt_eq = Tex("\\sqrt{4}","=","\\pm 2")
        self.play(Write(sqrt_eq[0:2]))
        self.wait()
        self.play(TransformFromCopy(sqrt_eq[0],sqrt_eq[2]),run_time = 5)
        self.play(FadeOut(sqrt_eq))
        self.wait()

class powers_slide9(Scene):
    def construct(self):
        
        sqrt_eqb = Tex("\\sqrt[n]{a}","=","\\pm b")
        self.play(Write(sqrt_eqb[0:2]))
        self.wait()
        self.play(TransformFromCopy(sqrt_eqb[0],sqrt_eqb[2]),run_time = 5)
        self.play(FadeOut(sqrt_eqb))
        self.wait()

class powers_slide10(Scene):
    def construct(self):
        lines = VGroup(
            Tex("a^{-n}",isolate = ["a","n"]),
            Tex("="),
            Tex("{1\\over {a^n}}",isolate = ["a","n"])
        )
        lines.arrange(RIGHT, buff=SMALL_BUFF)
        self.play(Write(lines[0:2]))
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            run_time = 5
        )
        self.wait()

class powers_slide11(Scene):
    def construct(self):
        power_sqrtmn = Tex("a^{1\\over {n}","=","\\sqrt[n]{a}",isolate = ["a"])
        self.play(Write(power_sqrtmn[0:2]))
        self.wait()
        self.play(TransformMatchingTex(power_sqrtmn[0],power_sqrtmn[2]),run_time = 5)
        self.play(FadeOut(power_sqrtmn))
        self.wait()

class powers_slide12(Scene):
    def construct(self):
        power_sqrtmn = Tex("a^{m\\over n}","=","\\sqrt[n]{a^m}")
        self.play(Write(power_sqrtmn[0:2]))
        self.wait()
        self.play(FadeTransformPieces(power_sqrtmn[0],power_sqrtmn[2]),run_time = 5)
        self.play(FadeOut(power_sqrtmn))
        self.wait()
        power_sqrtmn = Tex("a^{-m\\over n}","=","\\frac{1}{a^{m\\over n}}","=","\\frac{1}{\\sqrt[n]{a^m}}")
        self.play(Write(power_sqrtmn[0:2]))
        self.wait()
        self.play(FadeTransformPieces(power_sqrtmn[0],power_sqrtmn[2]),run_time = 5)
        self.play(FadeOut(power_sqrtmn))
        self.wait()

class power(Scene):
    def construct(self):

        power_0 = Tex("a^0=1")
        power_0p = Tex("a^{n-n}=\\frac{a^n}{a^n}=1")
        self.play(Write(power_0p))
        self.play(Transform(power_0p,power_0))
        self.wait()
        self.play(FadeOut(power_0))
        self.play(FadeOut(power_0p))

        power_1 = Tex("a^1=a")
        self.play(Write(power_1))
        self.wait()
        self.play(FadeOut(power_1))
        self.wait()

        power_subp0 = Tex("\\frac{2^4}{2^2}\\cdot =2^{4-2}")
        power_subp1 = Tex("\\frac{2\\cdot 2\\cdot 2\\cdot 2}{2\\cdot 2}=2^2")
        self.play(Write(power_subp0))
        self.play(Transform(power_subp0,power_subp1))
        self.wait()
        self.play(FadeOut(power_subp1))
        self.play(FadeOut(power_subp0))

        power_sub = Tex("\\frac{a^n}{a^m}=a^{n-m}")
        self.play(Write(power_sub))
        self.play(FadeOut(power_sub))
        self.wait(3)