from manimlib import *


class slide3(Scene):
    def construct(self):
        
        to_isolate = ["-21", "x", "y", "z"]
        lines = VGroup(
            Tex("-21 \\cdot x \\cdot y \\cdot y \\cdot z^2 \\cdot z", isolate=to_isolate),
            Tex("-21 \\cdot x  \\cdot y \\cdot y \\cdot z^3", isolate=to_isolate),
            Tex("-21 x y^2 z^3", isolate=to_isolate)
           
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

class slide4(Scene):
    def construct(self):
        t = Tex("6\\cdot x^2 \\cdot y")

        to_isolate = ["2", "1", "y", "x"]
        lines = VGroup(
            Tex("6\\cdot x^2 \\cdot y", isolate=to_isolate),
            Tex("6\\cdot x^2 \\cdot y^1", isolate=to_isolate),
            Tex("2 + 1", isolate=to_isolate),
            
           
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()


class slide5(Scene):
    def construct(self):
       

        
        
        to_isolate = ["6", "a", "b", "2"]
        lines = VGroup(
            Tex("6\\cdot a^2 \\cdot b", isolate=to_isolate),
            Tex("-2\\cdot b \\cdot a^2", isolate=to_isolate),
           
        )
        lines.arrange(RIGHT, buff=LARGE_BUFF)
        play_kw = {"run_time": 2}
        self.save_state()
        self.add(lines[0])
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        
        self.wait()
        self.restore()


        to_isolate = ["6", "a", "b", "2"]
        lines = VGroup(
            Tex("-6\\cdot b \\cdot a^2", isolate=to_isolate),
            Tex("6\\cdot b \\cdot a^2", isolate=to_isolate),
           
        )
        lines.arrange(RIGHT, buff=LARGE_BUFF)
        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        
        self.wait()
        self.restore()


        to_isolate = ["6", "a", "b", "2"]
        lines = VGroup(
            Tex("6\\cdot a^2 \\cdot b", isolate=to_isolate),
            Tex("6\\cdot b \\cdot a^2", isolate=to_isolate),
           
        )
        lines.arrange(RIGHT, buff=LARGE_BUFF)
        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        
        self.wait()



class slide6(Scene):
    def construct(self):
        t = Tex("6ab^2\\cdot(-3a^3c^2)=-18a^4b^2c^2")
        t2 = Tex("\\frac{6ab^2}{-3a^3c^2}")

class slide7(Scene):
    def construct(self):
        t = Tex("\\frac{6a^2b^3}{2ab^2c}")
        self.play(Write(t))

class slide9(Scene):
    def construct(self):


        t = Tex("2x^2yz+3xy^2z+4xyz^2=xyz\\cdot(2x+3y+4z)")


class slide10(Scene):
    def construct(self):


        t = Tex("(p+q)(a+b+c)=pa+pb+pc+qa+qb+qc")


class Groups(Scene):
    def construct(self):
        # Формулы многочленов и свойств
        many_eq = Tex("a","\\cdot","(","b","+","c",")","=","a","\\cdot","b","+","a","\\cdot" ,"c")
         #                    0       1    2   3   4   5   6   7   8       9    10  11  12     13     14
        many_eq.scale(2)
        # self.play(Write(many_eq[0:7]),run_time = 3)
        # self.play(Write(many_eq[7]))
        # self.play(ReplacementTransform(many_eq[0].copy(),many_eq[8],path_arc = PI/2),
        # ReplacementTransform(many_eq[1].copy(),many_eq[9],path_arc = PI/2),
        # ReplacementTransform(many_eq[3].copy(),many_eq[10],path_arc = PI/2),run_time = 5)
        # self.play(ReplacementTransform(many_eq[4].copy(),many_eq[11],path_arc = PI/2),run_time = 3)
        # self.play(ReplacementTransform(many_eq[0].copy(),many_eq[12],path_arc = PI/2),
        # ReplacementTransform(many_eq[1].copy(),many_eq[13],path_arc = PI/2),
        # ReplacementTransform(many_eq[5].copy(),many_eq[14],path_arc = PI/2),run_time = 5)
        many_eq2 = Tex("(","a","+","b",")","\\cdot","(","c","+","d",")","=","a","\\cdot","c","+","a","\\cdot" ,"d","+","b","\\cdot","c","+","b","\\cdot" ,"d")
        #                      0   1   2   3   4      5     6   7   8   9   10  11  12     13    14  15  16    17     18  19   20     21    22  23  24     25     26
        many_eq2.scale(1.5)
        self.play(Write(many_eq2[0:11]),run_time = 3)
        self.play(Write(many_eq2[11]))
        self.play(ReplacementTransform(many_eq2[1].copy(),many_eq2[12],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[13],path_arc = PI/2),
        ReplacementTransform(many_eq2[7].copy(),many_eq2[14],path_arc = PI/2),run_time = 5)
        self.play(ReplacementTransform(many_eq2[8].copy(),many_eq2[15],path_arc = PI/2),run_time = 3)
        self.play(ReplacementTransform(many_eq2[1].copy(),many_eq2[16],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[17],path_arc = PI/2),
        ReplacementTransform(many_eq2[9].copy(),many_eq2[18],path_arc = PI/2),run_time = 5)
        self.play(ReplacementTransform(many_eq2[2].copy(),many_eq2[19],path_arc = PI/2),run_time = 3)
        self.play(ReplacementTransform(many_eq2[3].copy(),many_eq2[20],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[21],path_arc = PI/2),
        ReplacementTransform(many_eq2[7].copy(),many_eq2[22],path_arc = PI/2),run_time = 5)
        self.play(ReplacementTransform(many_eq2[8].copy(),many_eq2[23],path_arc = PI/2),run_time = 3)
        self.play(ReplacementTransform(many_eq2[3].copy(),many_eq2[24],path_arc = PI/2),
        ReplacementTransform(many_eq2[5].copy(),many_eq2[25],path_arc = PI/2),
        ReplacementTransform(many_eq2[9].copy(),many_eq2[26],path_arc = PI/2),run_time = 5)
        self.wait(3)
        
class Equations(Scene):
    def construct(self):
        
        # Формулы многочленов и свойств
        many_eq = Tex("a\\cdot (b+c-d)=a\\cdot b+a\\cdot c-a\\cdot d")
        # Формулы сокращенного умножения
        sum_of_cube_eq = Tex("a^3+b^3=(a+b)(a^2-ab+b^2)")
        sub_of_cube_eq = Tex("a^3-b^3=(a-b)(a^2+ab+b^2)")
        # Формулы логарифмов
        log_eq = Tex("log_2 10=\ln10/\ln2\simeq3.3")
        # Формулы квадратного уравнения
        square_eq = Tex("ax^2+bx+c=0")
        roots_of_square_eq = Tex("x_{1,2}=\\frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        viet_teorem = Tex("x_1=\\frac{-b}{a}  x_2=\\frac{c}{a}")
        # Формулы пределов
        log_eq = Tex("lim_{x\to0}\\frac{\sin x}{x}=1")       




class slide11(Scene):
    def construct(self):
        square_of_sum_eq = Tex("(a+b)^2=a^2+2ab+b^2")
        square_of_sum_eq.to_edge(UP)
        rectA = Rectangle(width = 1, height = 1)
        rectA.set_color(color = BLACK)
        rectA.set_fill(color = GREEN, opacity = 1.0)
        rectB = Rectangle(width = 2, height = 2)
        rectB.set_color(color = BLACK)
        rectB.set_fill(color = RED, opacity = 1.0)
        rectBA = Rectangle(width = 2, height = 1)
        rectBA.set_color(color = BLACK)
        rectBA.set_fill(color = YELLOW, opacity = 1.0)
        rectAB = Rectangle(width = 1, height = 2)
        rectAB.set_color(color = BLACK)
        rectAB.set_fill(color = YELLOW, opacity = 1.0)
        rectA.to_edge(LEFT,buff=5)
        rectAB.next_to(rectA,DOWN,buff = 0)
        rectBA.next_to(rectA,RIGHT,buff = 0)
        rectB.next_to(rectAB,RIGHT,buff = 0)
        labelA = Tex("a")
        labelA1 = Tex("a")
        labelA2 = Tex("a")
        labelA3 = Tex("a")
        
        labelA.next_to(rectA, UP,buff = SMALL_BUFF)
        labelA1.next_to(rectA, LEFT,buff = SMALL_BUFF)
        labelA2.next_to(rectAB, DOWN,buff = SMALL_BUFF)
        labelA3.next_to(rectBA, RIGHT,buff = SMALL_BUFF)
        labelB = Tex("b")
        labelB1 = Tex("b")
        labelB2 = Tex("b")
        labelB3 = Tex("b")
        labelB.next_to(rectB, DOWN,buff = SMALL_BUFF)
        labelB1.next_to(rectB, RIGHT,buff = SMALL_BUFF)
        labelB2.next_to(rectAB, LEFT,buff = SMALL_BUFF)
        labelB3.next_to(rectBA, UP,buff = SMALL_BUFF)

        aa = Tex("a^2")
        bb = Tex("b^2")
        ab = Tex("a\\cdot b")
        ba = Tex("a\\cdot b")
        aa.move_to(rectA)
        bb.move_to(rectB)
        ab.move_to(rectAB)
        ba.move_to(rectBA)
        
        rectGroup = VGroup(rectA,rectB,rectAB,rectBA,labelA,labelB,labelA1,labelB1,labelA2,labelB2,labelA3,labelB3,aa,bb,ab,ba)
        groupA = VGroup(rectA,labelA,labelA1,aa)
        groupB = VGroup(rectB,labelB,labelB1,bb)
        groupAB = VGroup(rectAB,labelA2,labelB2,ab)
        groupBA = VGroup(rectBA,labelA3,labelB3,ba)
        self.play(ShowCreation(rectGroup))
        self.wait(5)
        self.play(groupA.to_edge,LEFT)
        self.play(groupAB.move_to,rectA.get_center()+2*RIGHT)
        self.play(groupBA.move_to,rectA.get_center()+5*RIGHT)
        self.play(groupB.move_to,rectA.get_center()+9*RIGHT)
        self.play(Write(square_of_sum_eq))
        self.wait(5)
        self.play(FadeOut(rectGroup))
        self.play(FadeOut(square_of_sum_eq))

class slide12(Scene):
    def construct(self):
        sum_of_square_eq = Tex("a^2-b^2=(a+b)(a-b)")
        sum_of_square_eq.to_edge(UP)
        rectA = Rectangle(width = 4, height = 3)
        rectA.set_color(color = BLACK)
        rectA.set_fill(color = GREEN, opacity = 1.0)
        rectB = Rectangle(width = 1, height = 1)
        rectB.set_color(color = BLACK)
        rectB.set_fill(color = GREEN, opacity = 1.0)
        rectAB = Rectangle(width = 3, height = 1)
        rectAB.set_color(color = BLACK)
        rectAB.set_fill(color = GREEN, opacity = 1.0)

        rectA.move_to([0,0,0])
        rectAB.move_to([-0.5,-2,0 ])
        rectB.next_to(rectAB,RIGHT,buff = 0)
        labelA = Tex("a")
        labelA1 = Tex("a")
        labelAB = Tex("a-b")
        labelAB1 = Tex("a+b")

        labelA.next_to(rectA, UP,buff = SMALL_BUFF)
        labelA1.next_to(rectA, LEFT,buff = SMALL_BUFF)

        labelB = Tex("b")
        labelB1 = Tex("b")

        labelB.next_to(rectB, DOWN,buff = SMALL_BUFF)
        labelB1.next_to(rectB, RIGHT,buff = SMALL_BUFF)

        aa = Tex("a^2")
        bb = Tex("b^2")

        aa.move_to(rectA)
        bb.move_to(rectB)
 
        rectGroup = VGroup(rectA,rectB,rectAB,labelA,labelB,labelA1,labelB1,aa,bb)
        groupA = VGroup(rectA,labelA,labelA1,aa)
        groupB = VGroup(rectB,labelB,labelB1,bb)
        sum_of_square_eq.to_edge(DOWN)


        self.play(ShowCreation(rectGroup))
        self.wait(5)
        self.play(groupB.to_corner,DR)
        self.play(rectAB.move_to,3.5*RIGHT+2*DOWN)
        self.play(Rotating(
                        rectAB,
                        PI/2,
                        about_point=rectAB.get_corner(UL),
                        run_time = 1.0
                    ),FadeOut(labelA1),FadeOut(aa))
        self.play(labelAB.next_to,rectA, LEFT)
        b_label = Tex("b")
        b_label.set_color(color = BLACK)
        self.play(b_label.next_to,rectAB, UP)
        self.play(FadeOut(b_label),FadeOut(labelA),labelAB1.next_to,rectA,UP)
        self.play(Write(sum_of_square_eq))
        self.wait(5)
        self.play(FadeOut(sum_of_square_eq),FadeOut(rectA),FadeOut(rectB),FadeOut(rectAB),FadeOut(labelAB1),FadeOut(labelAB),FadeOut(labelB),FadeOut(labelB1),FadeOut(bb))
        

class slide13(Scene):
    def construct(self):

        square_of_sub_eq = Tex("(a-b)^2=a^2-2ab+b^2")
        square_of_sub_eq.to_edge(UP)
        rectAmB = Rectangle(width = 2, height = 2)
        rectAmB.set_color(color = BLACK)
        rectAmB.set_fill(color = GREEN, opacity = 1.0)
        rectB = Rectangle(width = 1, height = 1)
        rectB.set_color(color = BLACK)
        rectB.set_fill(color = RED, opacity = 1.0)
        rectBA = Rectangle(width = 1, height = 2)
        rectBA.set_color(color = BLACK)
        rectBA.set_fill(color = YELLOW, opacity = 1.0)
        rectAB = Rectangle(width = 2, height = 1)
        rectAB.set_color(color = BLACK)
        rectAB.set_fill(color = YELLOW, opacity = 1.0)
        rectAmB.move_to(ORIGIN)
        rectAB.next_to(rectAmB,DOWN,buff = 0)
        rectBA.next_to(rectAmB,RIGHT,buff = 0)
        rectB.next_to(rectAB,RIGHT,buff = 0)
        labelA = Tex("a-b")
        labelA1 = Tex("a-b")
        labelA2 = Tex("a-b")
        labelA3 = Tex("a-b")
        
        labelA.next_to(rectAmB, UP,buff = SMALL_BUFF)
        labelA1.next_to(rectAmB, LEFT,buff = SMALL_BUFF)
        labelA2.next_to(rectAB, DOWN,buff = SMALL_BUFF)
        labelA3.next_to(rectBA, RIGHT,buff = SMALL_BUFF)
        labelB = Tex("b")
        labelB1 = Tex("b")
        labelB2 = Tex("b")
        labelB3 = Tex("b")
        labelB.next_to(rectB, DOWN,buff = SMALL_BUFF)
        labelB1.next_to(rectB, RIGHT,buff = SMALL_BUFF)
        labelB2.next_to(rectAB, LEFT,buff = SMALL_BUFF)
        labelB3.next_to(rectBA, UP,buff = SMALL_BUFF)

        aa = Tex("(a-b)^2")
        bb = Tex("b^2")
        ab = Tex("a\\cdot b")
        ba = Tex("a\\cdot b")
        aa.move_to(rectAmB)
        bb.move_to(rectB)
        ab.move_to(rectAB)
        ba.move_to(rectBA)
        
        rectGroup = VGroup(rectAmB,rectB,rectAB,rectBA,labelA,labelB,labelA1,labelB1,labelA2,labelB2,labelA3,labelB3,aa,bb,ab,ba)
        groupA = VGroup(rectAmB,labelA,labelA1,aa)
        groupB = VGroup(rectB,labelB,labelB1,bb)
        groupAB = VGroup(rectAB,labelA2,labelB2,ab)
        groupBA = VGroup(rectBA,labelA3,labelB3,ba)
        self.play(Write(square_of_sub_eq))
        self.play(ShowCreation(rectGroup))
        self.wait(5)
        self.play(groupA.to_edge,LEFT)
        self.play(groupAB.move_to,rectAmB.get_center()+3*RIGHT)
        self.play(groupBA.move_to,rectAmB.get_center()+6*RIGHT)
        self.play(groupB.move_to,rectAmB.get_center()+8*RIGHT)
        self.wait(5)
        self.play(FadeOut(rectGroup))
        self.play(FadeOut(square_of_sub_eq))
        self.wait()

class Binom(Scene):
    def construct(self):
        # Формулы сокращенного умножения
        
        sum_of_cube_eq = Tex("a^3+b^3=(a+b)(a^2-ab+b^2)")
        sub_of_cube_eq = Tex("a^3-b^3=(a-b)(a^2+ab+b^2)")

        # cell_height = 1
        # cell_width = 1
        # nrows = 6
        # pt = GeneralizedPascalsTriangle(nrows = nrows, 
        #     height = nrows * cell_height, 
        #     width = nrows * cell_width, )
        # pt.set_color(color = BLACK)
        # self.play(ShowCreation(pt))
        self.wait(3)




class binom3d_1(ThreeDScene):
    def construct(self):
        a = 0.5
        b = 1.5

        cubeA = Cube(side_length = a)
        cubeB = Cube(side_length = b)
        cubeA.set_color(color = RED)
        cubeB.set_color(color = BLUE)

        prismAAB = Prism(dimensions= [a, a, b])
        prismABA = Prism(dimensions= [a, b, a])
        prismBAA = Prism(dimensions= [b, a, a])

        prismAAB.set_color(color = YELLOW)
        prismABA.set_color(color = YELLOW)
        prismBAA.set_color(color = YELLOW)
        
        prismBBA = Prism(dimensions= [b, b, a])
        prismBAB = Prism(dimensions= [b, a, b])
        prismABB = Prism(dimensions= [a, b, b])
       
        prismBBA.set_color(color = GREEN)
        prismBAB.set_color(color = GREEN)
        prismABB.set_color(color = GREEN)

        cube_of_sum_eq = Tex("(a+b)^3=a^3+3a^2b+3ab^2+b^3")
        cube_of_sum_eq.set_color(color = BLACK)

        #axes = ThreeDAxes()
        self.set_camera_orientation(phi = 75 * DEGREES, theta = 30 * DEGREES)
        #self.add(axes)

        cubeA.move_to([0,0,0])
        cubeB.move_to([1,1,1])
        prismAAB.move_to([0,0,1])
        prismABA.move_to([0,1,0])
        prismBAA.move_to([1,0,0])
        prismBBA.move_to([1,1,0])
        prismBAB.move_to([1,0,1])
        prismABB.move_to([0,1,1])
        
        self.play(ShowCreation(cubeA))
        self.play(ShowCreation(prismAAB))
        self.play(ShowCreation(prismABA))
        self.play(ShowCreation(prismBAA))
        self.play(ShowCreation(prismBBA))
        self.play(ShowCreation(prismBAB))
        self.play(ShowCreation(prismABB))
        self.play(ShowCreation(cubeB))
        
        self.play(cubeA.move_to,[-1,-1,-1])
        self.play(cubeB.move_to,[2,2,2])
        self.play(prismAAB.move_to,[0,-1,1])
        self.play(prismABA.move_to,[-1,1,0])
        self.play(prismBAA.move_to,[1,0,-1])
        self.play(prismBBA.move_to,[1,1,-2])
        self.play(prismBAB.move_to,[1,-2,1])
        self.play(prismABB.move_to,[-2,1,1])
        

        self.wait()

        
        #self.play(Write(cube_of_sum_eq))
       # self.play(cube2.rotate,[PI/2])
        self.move_camera(0.8*np.pi/2, 1*np.pi,10)

        self.wait()

        #self.begin_ambient_camera_rotation()
        self.wait()
        self.remove(prismAAB)
        self.remove(prismABA)
        self.remove(prismBAA)
        self.remove(prismABB)
        self.remove(prismBAB)
        self.remove(prismBBA)
        self.remove(cubeA)
        self.remove(cubeB)

        self.wait()
        
class binom3d(ThreeDScene):
    def construct(self):
        A = 3
        B = 1
        AmB = A - B
        cubeb = Cube(side_length = B)

        cubeb.set_color(color = RED)

        prismAAmBB = Prism(dimensions= [A, AmB, A])
        prismABAmB= Prism(dimensions= [A , B, AmB])
        prismBAmBB = Prism(dimensions= [AmB, B, B])

        prismAAmBB.set_color(color = YELLOW)
        prismABAmB.set_color(color = GREEN)
        prismBAmBB.set_color(color = BLUE)

        cube_of_sub_eq = Tex("(a-b)^3=a^3-3a^2b+3ab^2-b^3")
        cube_of_sub_eq.set_color(color = BLACK)

        prismAAmBB.move_to([0,-1.5,1])
        cubeb.move_to([1,0,0])
        prismABAmB.move_to([0,0,1.5])
        prismBAmBB.move_to([-0.5,0,0])

        self.play(ShowCreation(cubeb))
        self.play(ShowCreation(prismAAmBB))
        self.play(ShowCreation(prismABAmB))
        self.play(ShowCreation(prismBAmBB))

        self.move_camera(0.8*np.pi/2, 1*np.pi,10)

        self.wait(3)