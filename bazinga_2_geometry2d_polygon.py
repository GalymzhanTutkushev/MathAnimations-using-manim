from manimlib import *

class poly_slide1(Scene):
    def construct(self):
        A = 1*UP-2*RIGHT
        B = 2*UP-1*RIGHT
        C = 3*UP+1*RIGHT
        D = -1*UP-0*RIGHT
        E = -1*UP-2*RIGHT
        lineAC = Line(A,C)
        lineBD = Line(B,D)
        lineAD = Line(A,D)
        
        screen_grid = NumberPlane()
        self.add(screen_grid)
        paralelogram = Polygon(
                A, B,C,D,E,
                width = width_stroke,stroke_color = color_stroke,
                fill_color = color_fill,
                fill_opacity = opacity_fill
            )
        
        paralelogram.set_shadow(0.5)
        paralelogram.set_gloss(0.5)
        self.play(ShowCreation(paralelogram),run_time = play_time)
        self.play(ShowCreation(lineAC),ShowCreation(lineBD),ShowCreation(lineAD),run_time = play_time)
        self.wait(pause_time)

class poly_slide2(Scene):

    def construct(self):
        
        screen_grid = NumberPlane()
        self.add(screen_grid)
        t = Tex("180^\\circ \\cdot (n-2)")
        t3 = Tex("180^\\circ \\cdot (3-2)=180^\\circ")
        t4 = Tex("180^\\circ \\cdot (4-2)=360^\\circ")
        t5 = Tex("180^\\circ \\cdot (5-2)=540^\\circ=180^\\circ+360^\\circ")
        
        t.to_edge(UP)
        t3.next_to(t,DOWN)
        t4.next_to(t,DOWN)
        t5.next_to(t,DOWN)

        self.play(Write(t))
        
        A = 0.5*UP+0.84*RIGHT
        B = -1*UP-0*RIGHT
        C = -1*UP-2*RIGHT
        D = 1*UP-2*RIGHT
        E = 1.5*UP-1*RIGHT

        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(B)
        Ed = SmallDot(C)

        # треугольник
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)

        # четырехгольник
        CD = Line(C,D)
        DA = Line(D,A)

        # пятиугольник
        DE = Line(D,E)
        EA = Line(E,A)

        
        beta = CA.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()

        print(alpha)
        print(beta)
        print(gamma)
        print(alpha+beta+gamma)
        a = Tex("a")
        b = Tex("b")
        c = Tex("c")
        a.next_to(AB,RIGHT)
        b.next_to(BC,DOWN)
        c.next_to(CA,LEFT)
        self.save_state()
        alpha_sec = AnnularSector(start_angle=gamma,angle=-(PI+gamma-beta),outer_radius = 0.5,inner_radius = 0,arc_center = A,fill_color = RED)
        beta_sec =  AnnularSector(start_angle=PI+gamma,angle=-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,fill_color = GREEN)
        gamma_sec =  AnnularSector(start_angle=PI-alpha,angle=beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,fill_color = BLUE)
        alpha_sec.set_stroke(RED)
        beta_sec.set_stroke(RED)
        gamma_sec.set_stroke(RED)
        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CA),
        Write(Ad),Write(Bd),Write(Cd))
        self.play(Write(t3))
        self.play(ShowCreation(alpha_sec),ShowCreation(beta_sec),ShowCreation(gamma_sec))
        o = 3*LEFT+1*UP
        self.play(beta_sec.animate.move_arc_center_to(o))
        self.play(gamma_sec.animate.move_arc_center_to(o))
        self.play(Rotate(alpha_sec,PI))
        self.play(alpha_sec.animate.move_arc_center_to(o))
        self.play(FadeOut(t3))
        self.restore()

        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd))

        beta = CD.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        teta = DA.get_angle()
        alpha_sec = AnnularSector(start_angle=gamma,angle=-(PI+gamma-teta),outer_radius = 0.5,inner_radius = 0,arc_center = A,fill_color = RED)
        beta_sec =  AnnularSector(start_angle=PI+gamma,angle=-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,fill_color = GREEN)
        gamma_sec =  AnnularSector(start_angle=PI-alpha,angle=beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,fill_color = BLUE)
        teta_sec =  AnnularSector(start_angle=teta,angle=-(PI/2+teta),outer_radius = 0.5,inner_radius = 0,arc_center = D,fill_color = TEAL)
        self.play(Write(t4))
        self.play(ShowCreation(alpha_sec),ShowCreation(beta_sec),ShowCreation(gamma_sec),ShowCreation(teta_sec))
        o = 3*LEFT+1*UP
        self.play(beta_sec.animate.move_arc_center_to(o))
        self.play(Rotate(gamma_sec,PI))
        self.play(gamma_sec.animate.move_arc_center_to(o))
        self.play(teta_sec.animate.move_arc_center_to(o))
        self.play(Rotate(alpha_sec,PI))
        self.play(alpha_sec.animate.move_arc_center_to(o))
        self.play(FadeOut(t4))
        self.restore()


        self.restore()

        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DE),ShowCreation(EA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd),Write(Ed))

        beta = CD.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        teta = DE.get_angle()
        eps = EA.get_angle()
        alpha_sec = AnnularSector(start_angle=gamma,angle=-(PI+gamma-eps),outer_radius = 0.5,inner_radius = 0,arc_center = A,fill_color = RED)
        beta_sec =  AnnularSector(start_angle=PI+gamma,angle=-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,fill_color = GREEN)
        gamma_sec =  AnnularSector(start_angle=PI-alpha,angle=beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,fill_color = BLUE)
        teta_sec =  AnnularSector(start_angle=teta,angle=-(PI/2+teta),outer_radius = 0.5,inner_radius = 0,arc_center = D,fill_color = TEAL)
        eps_sec =  AnnularSector(start_angle=eps,angle=-(PI-teta+eps),outer_radius = 0.5,inner_radius = 0,arc_center = E,fill_color = PURPLE)
        self.play(Write(t5))
        self.play(ShowCreation(alpha_sec),ShowCreation(beta_sec),ShowCreation(gamma_sec),ShowCreation(teta_sec),ShowCreation(eps_sec))
        o = 3*LEFT+1*UP
        o1 = 3*LEFT
        self.play(beta_sec.animate.move_arc_center_to(o))
        self.play(Rotate(eps_sec,PI/2))
        self.play(eps_sec.animate.move_arc_center_to(o))
        self.play(Rotate(teta_sec,-PI/2))
        self.play(teta_sec.animate.move_arc_center_to(o))

        self.play(Rotate(gamma_sec,PI))
        self.play(gamma_sec.animate.move_arc_center_to(o1))
        
        self.play(Rotate(alpha_sec,2*PI/3))
        self.play(alpha_sec.animate.move_arc_center_to(o1))
        
        self.play(FadeOut(t5))
        self.restore()

        self.wait(5)

class poly_slide3(Scene):
    def construct(self):
       
        p4 = RegularPolygon(n=4)
        p5 = RegularPolygon(n=5)
        p6 = RegularPolygon(n=6)
        p7 = RegularPolygon(n=7)
        p8 = RegularPolygon(n=8)
       
        p4.scale(2)
        p5.scale(2)
        p6.scale(2)
        p7.scale(2)
        p8.scale(2)
        
        f4 = p4.get_end_anchors()
        line41 = Line(f4[0],f4[2])
        line42 = Line(f4[1],f4[3])
        

        f5 = p5.get_end_anchors()
        line51 = Line(f5[0],f5[2])
        line52 = Line(f5[0],f5[3])
        line53 = Line(f5[2],f5[4])

        f6 = p6.get_end_anchors()
        line61 = Line(f6[0],f6[2])
        line62 = Line(f6[0],f6[3])
        line63 = Line(f6[2],f6[4])
        line64 = Line(f6[1],f6[4])

        f7 = p7.get_end_anchors()
        line71 = Line(f7[0],f7[2])
        line72 = Line(f7[0],f7[3])
        line73 = Line(f7[2],f7[4])
        line74 = Line(f7[1],f7[4])
        line75 = Line(f7[1],f7[5])

        f8 = p8.get_end_anchors()
        line81 = Line(f8[0],f8[2])
        line82 = Line(f8[0],f8[3])
        line83 = Line(f8[2],f8[4])
        line84 = Line(f8[1],f8[4])
        line85 = Line(f8[2],f8[5])
        line86 = Line(f8[1],f8[5])

        self.play(ShowCreation(p4))
        self.play(ShowCreation(line41),ShowCreation(line42))
        self.wait()
        self.play(FadeOut(line41),FadeOut(line42))
        self.play(ReplacementTransform(p4,p5))
        self.play(ShowCreation(line51),ShowCreation(line52),ShowCreation(line53))
        self.wait()
        self.play(FadeOut(line51),FadeOut(line52),FadeOut(line53))
        self.play(ReplacementTransform(p5,p6))
        self.play(ShowCreation(line61),ShowCreation(line62),
        ShowCreation(line63),ShowCreation(line64))
        self.wait()
        self.play(FadeOut(line61),FadeOut(line62),
        FadeOut(line63),FadeOut(line64))
        self.play(ReplacementTransform(p6,p7))
        self.play(ShowCreation(line71),ShowCreation(line72),
        ShowCreation(line73),ShowCreation(line74),ShowCreation(line75))
        self.wait()
        self.play(FadeOut(line71),FadeOut(line72),
        FadeOut(line73),FadeOut(line74),FadeOut(line75))
        self.play(ReplacementTransform(p7,p8))
        self.play(ShowCreation(line81),ShowCreation(line82),
        ShowCreation(line83),ShowCreation(line84),ShowCreation(line85),ShowCreation(line86))
        self.wait()
        self.play(FadeOut(line81),FadeOut(line82),
        FadeOut(line83),FadeOut(line84),FadeOut(line85),FadeOut(line86))
        self.wait(pause_time)


class poly_slide4(Scene):
    def construct(self):
        #сумма внешних углов
        A = 0.7*UP+1*RIGHT
        B = -1*UP-0*RIGHT
        C = -1*UP-2*RIGHT
        D = 1*UP-2.2*RIGHT
        E = 1.5*UP-1*RIGHT
        a = Tex("A")
        b = Tex("B")
        c = Tex("C")
        d = Tex("D")
        e = Tex("E")
        a.next_to(A,UP)
        b.next_to(B,DOWN)
        c.next_to(C,DOWN)
        d.next_to(D,LEFT)
        e.next_to(E,UP)
        Ad = SmallDot(A)
        Bd = SmallDot(B)
        Cd = SmallDot(C)
        Dd = SmallDot(D)
        Ed = SmallDot(E)


        # треугольник
        AB = Line(A,B)
        CA = Line(C,A)
        BC = Line(B,C)

        # четырехгольник
        CD = Line(C,D)
        DA = Line(D,A)

        # пятиугольник
        DE = Line(D,E)
        EA = Line(E,A)

        self.play(ShowCreation(AB),ShowCreation(BC),ShowCreation(CD),ShowCreation(DE),ShowCreation(EA),
        Write(Ad),Write(Bd),Write(Cd),Write(Dd),Write(Ed),Write(a),Write(b),Write(c),Write(d),Write(e))

        beta = CD.get_angle()
        gamma = AB.get_angle()
        alpha = BC.get_angle()
        teta = DE.get_angle()
        eps = EA.get_angle()
        l = 0.8
        A1 = Line(A,A+[l*np.cos(eps),l*np.sin(eps),0])
        B1 = Line(B,B+[l*np.cos(gamma),l*np.sin(gamma),0])
        C1 = Line(C,C+[l*np.cos(alpha),l*np.sin(alpha),0])
        D1 = Line(D,D+[l*np.cos(beta),l*np.sin(beta),0])
        E1 = Line(E,E+[l*np.cos(teta),l*np.sin(teta),0])
        self.play(ShowCreation(A1),ShowCreation(B1),ShowCreation(C1),ShowCreation(D1),ShowCreation(E1))
        
        alpha_sec = AnnularSector(start_angle=gamma,angle=eps-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = A,fill_color = RED)
        beta_sec =  AnnularSector(start_angle=gamma,angle=-alpha-gamma,outer_radius = 0.5,inner_radius = 0,arc_center = B,fill_color = GREEN)
        gamma_sec =  AnnularSector(start_angle=beta,angle=alpha-beta,outer_radius = 0.5,inner_radius = 0,arc_center = C,fill_color = BLUE)
        teta_sec =  AnnularSector(start_angle=teta,angle=beta-teta,outer_radius = 0.5,inner_radius = 0,arc_center = D,fill_color = TEAL)
        eps_sec =  AnnularSector(start_angle=eps,angle=teta-eps,outer_radius = 0.5,inner_radius = 0,arc_center = E,fill_color = PURPLE)
        self.play(ShowCreation(alpha_sec),ShowCreation(beta_sec),ShowCreation(gamma_sec),ShowCreation(teta_sec),ShowCreation(eps_sec))
        
        o = 3*RIGHT-1*UP
        self.play(beta_sec.animate.move_arc_center_to(o))

        self.play(gamma_sec.animate.move_arc_center_to(o))
        self.play(teta_sec.animate.move_arc_center_to(o))

        self.play(alpha_sec.animate.move_arc_center_to(o))
        self.play(eps_sec.animate.move_arc_center_to(o))
        
        self.wait(5)


class NewRegularPolygon(RegularPolygon):
    def get_sides(self,**kwargs):
        vertices = [*self.get_vertices(), self.get_vertices()[0]]
        sides = VGroup(*[
                Line(vertices[i],vertices[i+1],**kwargs)
                for i in range(len(vertices)-1)
            ])
        return sides

    def get_external_sides(self,size=1,**kwargs):
        sides = self.get_sides()
        external_sides = VGroup()
        kwargs["stroke_width"] = self.get_stroke_width()
        for side in sides:
            unit_vector = side.get_unit_vector()
            start = side.get_end()
            line = Line(
                    start,
                    start + size * unit_vector,
                    **kwargs   
                )
            external_sides.add(line)
        return external_sides

    def get_external_angles(self,radius=0.7,**kwargs):
        external_sides = self.get_external_sides()
        sides = self.get_sides()
        ind = -1 if self.start_angle == 0 else 1
        angle = abs(external_sides[0].get_angle() - sides[ind].get_angle())
        arcs = VGroup(*[
            Arc(
                sides[n].get_angle(),
                angle,
                radius=radius,
                arc_center=external_sides[n].get_start(),
                **kwargs
            ) for n in range(len(sides))
        ])
        return arcs

class GroupRegularPolygon(VGroup):
    CONFIG = {
        "polygon_color": RED,
        "ext_side_color": BLUE,
        "ext_angle_color": TEAL
    }
    def __init__(self,n,size=1,radius=0.7,height=2,**kwargs):
        regular_polygon = NewRegularPolygon(n,**kwargs)
        regular_polygon.set_height(height)
        super().__init__(
            regular_polygon.get_external_sides(**kwargs),
            regular_polygon.get_external_angles(**kwargs),
            regular_polygon
        )
        self[0].set_color(self.ext_side_color)
        self[1].set_color(self.ext_angle_color)
        self[2].set_color(self.polygon_color)
        self.regular_polygon = regular_polygon

    def get_number_sides(self):
        return len(self.regular_polygon.get_sides())

    def get_figure_height(self):
        return self.regular_polygon.get_height()

    def get_polygon_external_sides(self):
        return self[0]

    def get_polygon_external_angles(self):
        return self[1]

    def get_regular_polygon(self):
        return self[2]

class poly_slide4a(Scene):
    CONFIG = {
        "polygon_sides": [3,5,6,7,4],
        "init_buff": 0.6
    }
    def construct(self):
        figures = VGroup(*[GroupRegularPolygon(n) for n in self.polygon_sides])
        for figure in figures:
            figure.save_state()
            figure.height = figure.get_figure_height()

        def shrink_polygon(vgroup,alpha):
            buff = interpolate(self.init_buff,2,alpha)
            for mob in vgroup:
                mob.restore()
                d_height = interpolate(mob.height,0.0001,alpha)
                mob.become(
                    GroupRegularPolygon(
                            mob.get_number_sides(),
                            height = d_height
                        )
                )
            vgroup.arrange(RIGHT,buff=buff)
            vgroup.set_width(FRAME_WIDTH-0.2)

        shrink_polygon(figures,0)
        regular_polygons = VGroup(*[
            figure.get_regular_polygon()
            for figure in figures
        ])
        external_sides = VGroup(*[
            figure.get_polygon_external_sides()
            for figure in figures
        ])
        external_angles = VGroup(*[
            figure.get_polygon_external_angles()
            for figure in figures
        ])
        self.play(LaggedStartMap(GrowFromCenter,regular_polygons),run_time=2)
        self.play(*list(map(ShowCreation,external_sides)))
        self.play(*list(map(ShowCreation,external_angles)))
        self.wait()
        self.play(
            UpdateFromAlphaFunc(figures,shrink_polygon),
            run_time = 8,
            rate_func = there_and_back
        )
        self.wait(3)