from manimlib import *


class real_slide5(Scene):
    def construct(self):
        n = 4
        for i in range(-n,n+1):
            if(i<0):
                t = Tex("10^{"+str(i)+"}=","{1\\over"+str(10**abs(i))+"}")
            else:
                t = Tex("10^{"+str(i)+"}=",str(10**i))
            t.scale(3)
            self.play(Write(t[0]))   
            self.play(TransformFromCopy(t[0],t[1]))     
            self.wait()
            self.play(FadeOut(t))
            self.wait()


class real_slide6(Scene):
    def construct(self):
       
        num = 7108739
        arr = [6,5,4,3, 2, 1, 0]
        arr_n = []
        arr_f = []
        arr_n10 = []
        for i in '{:}'.format(num):     
            arr_n.append(i)
        for k in range(len(arr)):
            arr_n10.append(Tex(str(int(arr_n[k])*10**arr[k])))
            text = arr_n[k] + "*10" + "^" + str(arr[k])
            arr_f.append(text)

        arr_group = VGroup(*[
                    arr_n10[x].shift(x*DOWN/2+x*0.1*RIGHT)
                    for x in range(len(arr))
                ])
        
        n6 = Tex(arr_n[0])
        n5 = Tex(arr_n[1])
        n4 = Tex(arr_n[2])
        n3 = Tex(arr_n[3])
        n2 = Tex(arr_n[4])
        n1 = Tex(arr_n[5])
        n0 = Tex(arr_n[6])
        n6.move_to(3*UP+2*LEFT)
        n5.move_to(3*UP+1.5*LEFT)
        n4.move_to(3*UP+1*LEFT)
        n3.move_to(3*UP+0.5*LEFT)
        n2.move_to(3*UP+0*RIGHT)
        n1.move_to(3*UP+0.5*RIGHT)
        n0.move_to(3*UP+1*RIGHT)
        s6 = Tex(str(arr[0]))
        s5 = Tex(str(arr[1]))
        s4 = Tex(str(arr[2]))
        s3 = Tex(str(arr[3]))
        s2 = Tex(str(arr[4]))
        s1 = Tex(str(arr[5]))
        s0 = Tex(str(arr[6]))
        s6.scale(0.5)
        s5.scale(0.5)
        s4.scale(0.5)
        s3.scale(0.5)
        s2.scale(0.5)
        s1.scale(0.5)
        s0.scale(0.5)
        s6.set_color(BLUE)
        s5.set_color(BLUE)
        s4.set_color(BLUE)
        s3.set_color(BLUE)
        s2.set_color(BLUE)
        s1.set_color(BLUE)
        s0.set_color(BLUE)
        s6.next_to(n6,UP)
        s5.next_to(n5,UP)
        s4.next_to(n4,UP)
        s3.next_to(n3,UP)
        s2.next_to(n2,UP)
        s1.next_to(n1,UP)
        s0.next_to(n0,UP)
        
        self.play(Write(n6),Write(n5),Write(n4),Write(n3),Write(n2),Write(n1),Write(n0))
        self.play(Write(s6),Write(s5),Write(s4),Write(s3),Write(s2),Write(s1),Write(s0))
        # self.play(n6.shift,DOWN,n5.shift,DOWN,n4.shift,DOWN,n3.shift,DOWN,n2.shift,DOWN,n1.shift,DOWN,n0.shift,DOWN)
        d = 0.8
        z6 = Tex("0")
        z6.next_to(n6,RIGHT)
        self.play(n5.shift,d*DOWN,n4.shift,d*DOWN,n3.shift,d*DOWN,n2.shift,d*DOWN,n1.shift,d*DOWN,n0.shift,d*DOWN)
        self.play(Write(z6),z6.copy().shift,2.5*RIGHT,z6.copy().shift,2*RIGHT
        ,z6.copy().shift,1.5*RIGHT,z6.copy().shift,1*RIGHT
        ,z6.copy().shift,0.5*RIGHT)
        
        z5 = Tex("0")
        z5.next_to(n5,RIGHT)
        self.play(n4.shift,d*DOWN,n3.shift,d*DOWN,n2.shift,d*DOWN,n1.shift,d*DOWN,n0.shift,d*DOWN)
        self.play(Write(z5),z5.copy().shift,2*RIGHT
        ,z5.copy().shift,1.5*RIGHT,z5.copy().shift,1*RIGHT
        ,z5.copy().shift,0.5*RIGHT)

        z4 = Tex("0")
        z4.next_to(n4,RIGHT)
        self.play(n3.shift,d*DOWN,n2.shift,d*DOWN,n1.shift,d*DOWN,n0.shift,d*DOWN)
        self.play(Write(z4) ,z4.copy().shift,1.5*RIGHT,z4.copy().shift,1*RIGHT
        ,z4.copy().shift,0.5*RIGHT)

        z3 = Tex("0")
        z3.next_to(n3,RIGHT)
        
        self.play(n2.shift,d*DOWN,n1.shift,d*DOWN,n0.shift,d*DOWN)
        self.play(Write(z3),z3.copy().shift,1*RIGHT,z3.copy().shift,0.5*RIGHT)
        z2 = Tex("0")
        z2.next_to(n2,RIGHT)
        self.play(n1.shift,d*DOWN,n0.shift,d*DOWN)
        self.play(Write(z2),z2.copy().shift,0.5*RIGHT)
        
        z1 = Tex("0")
        z1.next_to(n1,RIGHT)
        self.play(n0.shift,d*DOWN)
        self.play(Write(z1))

        line = Line(2.2*DOWN+2.4*LEFT,2.2*DOWN+1.4*RIGHT)
        self.play(Write(line))
        
        plus = Tex("+")
        plus.move_to(2.5*LEFT+2.5*UP)
        self.play(Write(plus),plus.copy().shift,d*DOWN,plus.copy().shift,2*d*DOWN,
        plus.copy().shift,3*d*DOWN,plus.copy().shift,4*d*DOWN,plus.copy().shift,5*d*DOWN)
        nnn = VGroup(n6.copy().move_to(2.5*DOWN+2*LEFT),
        n5.copy().move_to(2.5*DOWN+1.5*LEFT),
        n4.copy().move_to(2.5*DOWN+1*LEFT),
        n3.copy().move_to(2.5*DOWN+0.5*LEFT),
        n2.copy().move_to(2.5*DOWN+0*LEFT),
        n1.copy().move_to(2.5*DOWN+0.5*RIGHT),
        n0.copy().move_to(2.5*DOWN+1*RIGHT))
        self.play(Write(nnn))
        self.wait(3)
         
class real_slide7(Scene):
    def construct(self):
        to_isolate = ["3", "4", "2"]
        lines = VGroup(
            Tex("{{1}}\\cdot 10^{0}","+","{{3}}\\cdot 10^{-1}","+","{{4}}\\cdot 10^{-2}","+","{{2}}\\cdot 10^{-3}"),
            Tex("{{1}}","+","{{3}}\\cdot {1\\over {{10}}}","+","{{4}}\\cdot {1\\over {{100}}}","+","{{2}}\\cdot {1\\over {{1000}}}"),
            Tex("{{1}}","+","{ {{3}}\\over {{10}}}","+","{ {{4}}\\over {{100}}}","+","{ {{2}}\\over {{1000}}}"),
            Tex("{ {{1}}000\\over 1000}","+","{ {{3}}00\\over 1000}","+","{ {{4}}0\\over 1000}","+","{ {{2}}\\over 1000}"),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        
        play_kw = {"run_time": 5}
        self.add(lines[0])
        
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
            ),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[2].copy(), lines[3]),
            **play_kw
        )
        self.wait()


class real_slide8(Scene):
    def construct(self):
        t = Tex("{671\\over 500}","=","{1342\\over 1000}","=","{2013\\over 1500}","=","1.342")
        self.play(Write(t[0]))
        self.wait()
        self.play(Write(t[1]))

        self.play(Write(t[2]))
        self.wait()
        self.play(Write(t[3]))

        self.play(Write(t[4]))
        self.wait()
        self.play(Write(t[5]))
        self.play(Write(t[6]))
        self.wait()

class real_slide9(Scene):
    def construct(self):
        numberl = NumberLine(x_range=np.array([0,2.5,1]),  unit_size=3,include_numbers=True,
                            include_tip=True, line_to_number_direction=DOWN,numbers_to_exclude=[3])
        num = 1.342
        
        
        numberl.shift(0.5*RIGHT)
        self.play(ShowCreation(numberl))
        print(numberl.get_start())
        d = Dot(numberl.get_start()+3*1.342*RIGHT+0.125*LEFT)
        d.set_color(RED)
        d.scale(0.5)
        ds = Dot(numberl.get_start())
        ds.set_color(RED)
        ds.scale(0.5)
        t_num = Tex(str(num))
        t_num.next_to(d,UP)
        self.play(Write(d),Write(ds),Write(t_num))
        frame = self.camera.frame
        self.play(frame.animate.scale(0.3).move_to(1.5*RIGHT))
        numberl = NumberLine(x_range=np.array([0,2.5,0.1]),  unit_size=3,include_numbers=False,
                           numbers_to_exclude=[2.5])
        numberl.shift(0.5*RIGHT)
        self.play(numberl.animate.add_ticks())
        self.play(frame.animate.scale(0.3).move_to(0.5*RIGHT))
        numberl = NumberLine(x_range=np.array([0,2.5,0.01]),  unit_size=3,tick_size = 0.01,include_numbers=False,
                           numbers_to_exclude=[2.5])
        numberl.shift(0.5*RIGHT)
        self.play(numberl.animate.add_ticks())
