from manimlib import *
import numpy as np

class fraction_on_squares(Scene):
    def construct(self):
        
       
        n = 3
        m = 3
        square = Square(side_length = 1)
        square.move_to(3*LEFT+DOWN)
        square_group = VGroup(*[
                    square.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        
        div = Tex("\\frac{3}{9}")
        div.next_to(square_group,UP)
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group))
        square_group_part =  VGroup(*[square_group[i] for i in [2,5,8]])

        self.play(square_group_part.set_color,RED)
        self.play(Write(div))
        #self.play(square_group_part.shift,LEFT)
        

        rect = Rectangle(width = 3,height = 1)
        rect.move_to(3*RIGHT+DOWN)
        rect_group = VGroup(*[
                    rect.copy().shift(y*UP)
                
                    for y in range(n)
                ])
        
        divR = Tex("\\frac{1}{3}")
        divR.next_to(rect_group,UP)
        rect_group.set_stroke(color=BLACK, width = 3)
        rect_group.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(rect_group))
        rect_group_part =  VGroup(*[rect_group[2]])
        eq=Tex("=")
        eq.scale(2)
        eq.move_to(ORIGIN+0.5*RIGHT)
        self.play(rect_group_part.set_color,RED)
        self.play(Write(divR))
        self.play(Write(eq))
        self.play(FadeOut(divR),FadeOut(div),FadeOut(square_group),FadeOut(rect_group),FadeOut(eq))
        self.wait()
        
        n = 3
        m = 3
        square = Square(side_length = 1)
        square.move_to(5*LEFT+1*DOWN)
        square_group = VGroup(*[
                    square.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        
        div = Tex("\\frac{3}{9}")
        div.next_to(square_group,UP)
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group))
        square_group_part =  VGroup(*[square_group[i] for i in [2,5,8]])

        self.play(square_group_part.set_color,RED)
        self.play(Write(div))
        #self.play(square_group_part.shift,LEFT)
        square1 = Square(side_length = 1)
        square1.move_to(1*LEFT+1*DOWN)
        square_group1 = VGroup(*[
                    square1.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        div1 = Tex("\\frac{2}{9}")
        div1.next_to(square_group1,UP)
        square_group1.set_stroke(color=BLACK, width = 3)
        square_group1.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group1))
        square_group_part1 =  VGroup(*[square_group1[i] for i in [1,4]])

        self.play(square_group_part1.set_color,RED)
        self.play(Write(div1))
        plus = Tex("+")
        plus.scale(2)
        eq = Tex("=")
        eq.scale(2)
        plus.next_to(square_group,RIGHT)
        eq.next_to(square_group1,RIGHT)
        self.play(Write(plus))
        self.play(Write(eq))


        square2 = Square(side_length = 1)
        square2.move_to(3*RIGHT+1*DOWN)
        square_group2 = VGroup(*[
                    square2.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        div2 = Tex("\\frac{5}{9}")
        div2.next_to(square_group2,UP)
        square_group2.set_stroke(color=BLACK, width = 3)
        square_group2.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group2))
        square_group_part2 =  VGroup(*[square_group2[i] for i in [2,5,8,1,4]])

        self.play(square_group_part2.set_color,RED)
        self.play(Write(div2))
        addf = VGroup(div2,square_group2,eq,plus,square_group,div)
        self.play(FadeOut(addf))
        ####

        n = 3
        m = 3
        rect = Rectangle(width = 3,height = 1)
        rect.move_to(4*LEFT+DOWN)
        rect_group = VGroup(*[
                    rect.copy().shift(y*UP)
                
                    for y in range(n)
                ])
        
        divR = Tex("\\frac{1}{3}")
        divR.next_to(rect_group,UP)
        rect_group.set_stroke(color=BLACK, width = 3)
        rect_group.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(rect_group))
        rect_group_part =  VGroup(*[rect_group[2]])
        self.play(rect_group_part.set_color,RED)
        self.play(Write(divR))

        square = Square(side_length = 1)
        square.move_to(5*LEFT+DOWN)
        square_group = VGroup(*[
                    square.copy().shift(x*RIGHT + y*UP)
                    for x in range(m)
                    for y in range(n)
                ])
        
        div = Tex("\\frac{3}{9}")
        div.next_to(square_group,UP)
        square_group.set_stroke(color=BLACK, width = 3)
        square_group.set_fill(color=BLUE, opacity = 0.5)
        
        square_group_part =  VGroup(*[square_group[i] for i in [2,5,8]])

        plus = Tex("+")
        plus.scale(2)
        eq = Tex("=")
        eq.scale(2)
        plus.next_to(rect_group,RIGHT)
        eq.next_to(square_group1,RIGHT)
        self.play(Write(plus))
        self.play(Write(eq))
        self.play(ReplacementTransform(rect_group,square_group),ReplacementTransform(divR,div))
        self.play(square_group_part.set_color,RED)
        div2 = Tex("\\frac{5}{9}")
        div2.next_to(square_group2,UP)
        square_group2.set_stroke(color=BLACK, width = 3)
        square_group2.set_fill(color=BLUE, opacity = 0.5)
        self.play(ShowCreation(square_group2))
        square_group_part2 =  VGroup(*[square_group2[i] for i in [2,5,8,1,4]])

        self.play(square_group_part2.set_color,RED)
        self.play(Write(div2))
        self.wait(3)

class ShowArrayOfEccentricities(Scene):
    def construct(self):
        eccentricities = np.linspace(0, 0.99, 6)
        eccentricity_labels = VGroup(*list(map(
            DecimalNumber, eccentricities
        )))
        ellipses = self.get_ellipse_row(eccentricities)
        ellipses.set_color_by_gradient(BLUE, YELLOW)
        ellipses.move_to(DOWN)

        for label, ellipse in zip(eccentricity_labels, ellipses):
            label.next_to(ellipse, UP)

      

       

        
       
        self.add(ellipses[0])
        for e1, e2 in zip(ellipses[:-1], ellipses[1:]):
            self.play(ReplacementTransform(
                e1.copy(), e2,
                path_arc=10 * DEGREES
            ))
        self.wait()


        self.wait()

        

        for i in 0, -1:
            e_copy = ellipses[i].copy()
            e_copy.set_color(RED)
            self.play(ShowCreation(e_copy))
            self.play(
                ShowCreationThenFadeAround(
                    eccentricity_labels[i],
                ),
                FadeOut(e_copy)
            )
        self.wait()

        circle = ellipses[0]
        group = VGroup(*it.chain(
            eccentricity_labels,
            ellipses[1:],
          
 
        ))
        self.play(
            LaggedStartMap(FadeOutAndShiftDown, group),
            circle.set_height, 5,
            circle.center,
        )

    def get_ellipse(self, eccentricity, width=2):
        result = Circle(color=WHITE)
        result.set_width(width)
        a = width / 2.0
        c = eccentricity * a
        b = np.sqrt(a**2 - c**2)
        result.stretch(b / a, 1)
        result.shift(c * LEFT)

        result.eccentricity = eccentricity
        return result

    def get_ellipse_row(self, eccentricities, buff=MED_SMALL_BUFF, **kwargs):
        result = VGroup(*[
            self.get_ellipse(e, **kwargs)
            for e in eccentricities
        ])
        result.arrange(RIGHT, buff=buff)
        return result

    def get_eccentricity(self, ellipse):
        """
        Assumes that it's major/minor axes line up
        with x and y axes
        """
        a = ellipse.get_width()
        b = ellipse.get_height()
        if b > a:
            a, b = b, a
        c = np.sqrt(a**2 - b**2)
        return fdiv(c, a)
class EccentricityInThumbtackCase(ShowArrayOfEccentricities):
    def construct(self):
        ellipse = self.get_ellipse(0.2, width=5)
        ellipse_target = self.get_ellipse(0.9, width=5)
        ellipse_target.scale(fdiv(
            sum(self.get_abc(ellipse)),
            sum(self.get_abc(ellipse_target)),
        ))
        for mob in ellipse, ellipse_target:
            mob.center()
            mob.set_color(BLUE)
        
        ellipse_point_update = self.get_ellipse_point_update(ellipse)
        focal_lines_update = self.get_focal_lines_update(
            ellipse, ellipse_point_update.mobject
        )
        focus_to_focus_line_update = self.get_focus_to_focus_line_update(ellipse)
        eccentricity_label = self.get_eccentricity_label()
        eccentricity_value_update = self.get_eccentricity_value_update(
            eccentricity_label, ellipse,
        )
        inner_brace_update = self.get_focus_line_to_focus_line_brace_update(
            focus_to_focus_line_update.mobject
        )
        outer_lines = self.get_outer_dashed_lines(ellipse)
        outer_lines_brace = Brace(outer_lines, DOWN)

        focus_distance = TextMobject("Focus distance")
        focus_distance.set_color(GREEN)
        focus_distance.next_to(inner_brace_update.mobject, DOWN, SMALL_BUFF)
        focus_distance.add_to_back(focus_distance.copy().set_stroke(BLACK, 5))
        focus_distance_update = Mobject.add_updater(
            focus_distance,
            lambda m: m.set_width(
                inner_brace_update.mobject.get_width(),
            ).next_to(inner_brace_update.mobject, DOWN, SMALL_BUFF)
        )
        diameter = TextMobject("Diameter")
        diameter.set_color(RED)
        diameter.next_to(outer_lines_brace, DOWN, SMALL_BUFF)

        fraction = Tex(
            "{\\text{Focus distance}", "\\over",
            "\\text{Diameter}}"
        )
        numerator = fraction.get_part_by_tex("Focus")
        numerator.set_color(GREEN)
        fraction.set_color_by_tex("Diameter", RED)
        fraction.move_to(2 * UP)
        fraction.to_edge(RIGHT, buff=MED_LARGE_BUFF)
        numerator_update = Mobject.add_updater(
            numerator,
            lambda m: m.set_width(focus_distance.get_width()).next_to(
                fraction[1], UP, MED_SMALL_BUFF
            )
        )

        fraction_arrow = Arrow(
            eccentricity_label.get_right(),
            fraction.get_top() + MED_SMALL_BUFF * UP,
            path_arc=-60 * DEGREES,
        )
        fraction_arrow.pointwise_become_partial(fraction_arrow, 0, 0.95)

        ellipse_transformation = Transform(
            ellipse, ellipse_target,
            rate_func=there_and_back,
            run_time=8,
        )

        self.add(ellipse)
        
        self.add(ellipse_point_update)
        self.add(focal_lines_update)
        self.add(focus_to_focus_line_update)
        self.add(eccentricity_label)
        self.add(eccentricity_value_update)

        self.play(ellipse_transformation)

        self.add(inner_brace_update)
        self.add(outer_lines)
        self.add(outer_lines_brace)

        self.add(fraction)
        self.add(fraction_arrow)
        self.add(focus_distance)
        self.add(diameter)

        self.add(focus_distance_update)
        self.add(numerator_update)

        self.play(
            ellipse_transformation,
            VFadeIn(inner_brace_update.mobject),
            VFadeIn(outer_lines),
            VFadeIn(outer_lines_brace),
            VFadeIn(fraction),
            VFadeIn(fraction_arrow),
            VFadeIn(focus_distance),
            VFadeIn(diameter),
        )

    def get_ellipse_point_update(self, ellipse):
        dot = Dot(color=RED)
        return cycle_animation(MoveAlongPath(
            dot, ellipse,
            run_time=5,
            rate_func=linear
        ))

    def get_focal_lines_update(self, ellipse, ellipse_point):
        lines = VGroup(*[Line(LEFT, RIGHT) for x in range(2)])
        lines.set_color_by_gradient(YELLOW, PINK)

        def update_lines(lines):
            foci = self.get_foci(ellipse)
            Q = ellipse_point.get_center()
            for line, focus in zip(lines, foci):
                line.put_start_and_end_on(focus, Q)
            return lines

        return Mobject.add_updater(lines, update_lines)

    def get_focus_to_focus_line_update(self, ellipse):
        return Mobject.add_updater(
            Line(LEFT, RIGHT, color=WHITE),
            lambda m: m.put_start_and_end_on(*self.get_foci(ellipse))
        )

    def get_focus_line_to_focus_line_brace_update(self, line):
        brace = Brace(Line(LEFT, RIGHT))
        brace.add_to_back(brace.copy().set_stroke(BLACK, 5))
        return Mobject.add_updater(
            brace,
            lambda b: b.match_width(line, stretch=True).next_to(
                line, DOWN, buff=SMALL_BUFF
            )
        )

    def get_eccentricity_label(self):
        words = TextMobject("Eccentricity = ")
        decimal = DecimalNumber(0, num_decimal_places=2)
        group = VGroup(words, decimal)
        group.arrange(RIGHT)
        group.to_edge(UP)
        return group

    def get_eccentricity_value_update(self, eccentricity_label, ellipse):
        decimal = eccentricity_label[1]
        decimal.add_updater(lambda d: d.set_value(
            self.get_eccentricity(ellipse)
        ))
        return decimal

    def get_outer_dashed_lines(self, ellipse):
        line = DashedLine(2.5 * UP, 2.5 * DOWN)
        return VGroup(
            line.move_to(ellipse, RIGHT),
            line.copy().move_to(ellipse, LEFT),
        )

    #
    def get_abc(self, ellipse):
        a = ellipse.get_width() / 2
        b = ellipse.get_height() / 2
        c = np.sqrt(a**2 - b**2)
        return a, b, c

    def get_foci(self, ellipse):
        a, b, c = self.get_abc(ellipse)
        return [
            ellipse.get_center() + c * RIGHT,
            ellipse.get_center() + c * LEFT,
        ]

class ClockOrganization(VGroup):
    CONFIG = {
        "numbers" : 4,
        "radius" : 3.1,
        "color" : BLACK
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs, locals())
        self.generate_nodes()
        VGroup.__init__(self, *self.node_list,**kwargs)

    def generate_nodes(self):
        self.node_list = []
        for i in range(self.numbers):
            mobject = VMobject()
            number = Tex(str(i))
            circle = Circle(radius=0.4,color=self.color)
            mobject.add(number)
            mobject.add(circle)
            mobject.move_to(
                self.radius * np.cos((-TAU / self.numbers) * i + 17*TAU / 84) * RIGHT
                + self.radius * np.sin((-TAU / self.numbers) * i + 17*TAU / 84) * UP
            )
            self.node_list.append(mobject)

    def select_node(self, node):
        selected_node = self.node_list[node]
        selected_node.scale(1.2)
        selected_node.set_color(RED)

    def deselect_node(self, selected_node):
        node = self.node_list[selected_node]
        node.scale(0.8)
        node.set_color(self.color)
class ClockOrganizationScene(Scene):
    def construct(self):
        test = ClockOrganization(numbers=10)
        self.add(test)
        animation_steps = []
        vect = Arrow(ORIGIN+0.5*UP,ORIGIN+2.5*UP+0.7*RIGHT)
        num_circ = 10
        for k in range(3):
            for i in range(num_circ):
                thing = test.deepcopy()
                thing.select_node((i)%test.numbers-1)
                animation_steps.append(thing)
            anims = []
            theta = 180 * DEGREES / num_circ
            lag_constant = 5
            n = Tex(str(k))
            n.move_to(ORIGIN+0.3*LEFT)
            self.play(Write(n))
            for i in range(0,num_circ):
                # mi = Tex(str(i+1))
                # mi.to_corner(DR)
                # mi.set_color(color = RED)
                m = Tex(str(i))
                # m.to_corner(DR)
                # m.set_color(color = RED)
                # self.play(vect.rotate,-theta)
                test.node_list[(i)%test.numbers].generate_target()
                test.node_list[(i)%test.numbers].target.scale(1.2)
                test.node_list[(i)%test.numbers].target.set_color(RED)
                stop_smooth = lag_constant * np.sin(i*theta)
                self.play(Write(m),MoveToTarget(test.node_list[(i)%test.numbers],rate_func=linear),Rotating(vect,-theta*2,about_point = ORIGIN),run_time = 0.5)
                # self.play(Animation(Mobject(),run_time=stop_smooth))
                self.play(FadeOut(m))
            self.play(FadeOut(n))


   
            # self.play(
            # AnimationGroup(*anims,lag_ratio=0.1)
            # )
        self.wait(3)

class ios(Scene):
    def construct(self):

        m = 10
        square = Square(side_length = 0.5)
        square.move_to(1.5*UP)
        square.set_color(color = RED)
        
        square_group1 = VGroup(*[
                    square.copy().shift(x*RIGHT)
                    for x in range(3)
                ])
        square_group1.set_stroke(color=BLACK, width = 3)
        self.play(ShowCreation(square_group1))
        square_group = []
        for x in range(m):
            n = Tex(str(x))
            square_group.append(n.shift(0.5*x*DOWN+1.5*UP))

        square_group = VGroup(*square_group)
        self.play(ShowCreation(square_group))
        

        n_group = []
        for x in range(m):
            n = Tex(str(x))
            n_group.append(n.shift(0.5*x*DOWN+1.5*UP+1*RIGHT))

        n_group = VGroup(*n_group)
        self.play(ShowCreation(n_group))


        
        n0_group = []
        for x in range(m):
            n = Tex(str(x))
            n0_group.append(n.shift(0.5*x*DOWN+1.5*UP+2*RIGHT))

        n0_group = VGroup(*n0_group)
        self.play(ShowCreation(n0_group))

        self.play(square_group.move_to,1.3*UP,n_group.move_to,2.8*UP+1*RIGHT,n0_group.move_to,0.3*UP+2*RIGHT,run_time = 3)
        self.wait(3)

class sys(Scene):
    def construct(self):
        
        num_square = Square(side_length = 1)
        num_square.to_edge(UP)
        self.add(num_square)
        m = 10
        n_group = []
        for x in range(m):
            n = Tex(str(x))
            n.scale(1.4)
            n_group.append(n.shift(1.4*x*RIGHT+1.5*UP+6*LEFT))

        n_group = VGroup(*n_group)
        self.play(ShowCreation(n_group))

        n0_group = []
        for x in range(m):
            n = Tex(str(x))
            n.scale(1.4)
            n0_group.append(n.shift(1.4*x*RIGHT+6*LEFT))

        n0_group = VGroup(*n0_group)
        self.play(ShowCreation(n0_group))

        n2_group1 = []
        for x in range(m):
            n2 = Tex(str(x))
            n2.scale(1.4)
            n2_group1.append(n2.shift(1.4*x*RIGHT+6*LEFT+1.5*DOWN))

        n2_group = VGroup(*n2_group1)
        self.play(ShowCreation(n2_group))

        p0 = Tex("0")
        p0.scale(1)
        p0.move_to(6.8*LEFT+1.5*UP)
        p0.set_color(color = BLUE)

        p1 = Tex("1")
        p1.scale(1)
        p1.move_to(6.8*LEFT)
        p1.set_color(color = BLUE)
        p2 = Tex("2")
        p2.scale(1)
        p2.move_to(6.8*LEFT+1.5*DOWN)
        p2.set_color(color = BLUE)

        self.play(ShowCreation(p0),ShowCreation(p1),ShowCreation(p2))

        square = Square(side_length = 1)
        square.set_color(color = RED)
        squareR = Square(side_length = 1)
        squareR.move_to(3*UP+1*LEFT)
        self.add(squareR)
        for k in range(3):
            r1 = Tex(str(k))
            r1.move_to(3*UP+1*LEFT)
            r1.set_color(color = BLUE)
            self.add(r1)
            square.move_to(6*LEFT+(1.5-1.5*k)*UP)
            for i in range(m-1):
            
                num = Tex(str(i+1))
                num.move_to(3*UP)
                self.add(num)
                self.play(square.shift,1.4*RIGHT,run_time = 0.5)
                self.remove(num)
                if ((k*10+i+1) == 23):
                    break
            self.remove(r1)
        self.play(n2_group[3].set_color,RED)
        r1 = Tex(str(2))
        r1.move_to(3*UP+1*LEFT)
        r1.set_color(color = BLUE)
        self.add(r1)
        num = Tex(str(3))
        num.move_to(3*UP)
        self.add(num)
        self.remove(square)

        self.wait(3)
        p0_group = VGroup(*[
                    p0.copy().shift(1.4*x*RIGHT)
                    for x in range(m)
                ])
        
        p1_group = VGroup(*[
                    p1.copy().shift(1.4*x*RIGHT)
                    for x in range(m)
                ])

        p2_group = VGroup(*[
                    p2.copy().shift(1.4*x*RIGHT)
                    for x in range(m)
                ])
        # self.play(ShowCreation(p0_group),ShowCreation(p1_group),ShowCreation(p2_group),run_time = 5)

class FunctionTracker(Scene):
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = Tex("x = ")
        fx_label = Tex("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2.6)
        # VGroup(x_tex, fx_tex).arrange_submobjects(DOWN,buff=3)
        # Align labels and numbers
        x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())

        self.add(group.move_to(ORIGIN))
        self.wait(3)
        self.play(
            x_value.set_value,30,
            rate_func=linear,
            run_time=10
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=10
            )
        self.wait(3)

class FunctionTrackerWithNumberLine(Scene):






    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = Tex("x = ")
        fx_label = Tex("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2)
        # Set the labels position
        x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())
        # Grouping numbers and labels
        x_group = VGroup(x_label,x_tex)
        fx_group = VGroup(fx_label,fx_tex)
        # Align labels and numbers
        # VGroup(x_group, fx_group).arrange_submobjects(RIGHT,buff=2,aligned_edge=DOWN).to_edge(UP)
        # Get NumberLine,Arrow and label from x
        x_number_line_group = self.get_number_line_group(
            "x",30,0.2,step_label=10,v_tracker=x_value,tick_frequency=2
            )
        x_number_line_group.to_edge(LEFT,buff=1)
        # Get NumberLine,Arrow and label from f(x)
        fx_number_line_group = self.get_number_line_group(
            "x^2",900,0.012,step_label=100,v_tracker=fx_tex,
            tick_frequency=50
            )
        fx_number_line_group.next_to(x_number_line_group,DOWN,buff=1).to_edge(LEFT,buff=1)

        self.add(
            x_number_line_group,
            fx_number_line_group,
            group
            )
        self.wait()
        self.play(
            x_value.set_value,30,
            rate_func=linear,
            run_time=10
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=10
            )
        self.wait(3)


    def get_numer_labels_to_numberline(self,number_line,x_max=None,x_min=0,buff=0.2,step_label=1,**tex_kwargs):
        # This method return the labels of the NumberLine
        labels = VGroup()
        x_max = number_line.x_max
        for x in range(x_min,x_max+1,step_label):
            x_label = Tex(f"{x}",**tex_kwargs)
            # See manimlib/mobject/number_line.py CONFIG dictionary
            x_label.next_to(number_line.number_to_point(x),DOWN,buff=buff)
            labels.add(x_label)
        return labels

    def get_number_line_group(self,label,x_max,unit_size,v_tracker,step_label=1,**number_line_config):
        # Set the Label (x,or x**2)
        number_label = Tex(label)
        # Set the arrow 
        arrow = Arrow(UP,DOWN,buff=0).set_height(0.5)
        # Set the number_line
        number_line = NumberLine(
            x_range=np.array([0,x_max,1]),
            unit_size=unit_size,
            numbers_with_elongated_ticks=[],
            **number_line_config
            )
        # Get the labels from number_line
        labels = self.get_numer_labels_to_numberline(number_line,step_label=step_label,height=0.2)
        # Set the arrow position
        arrow.next_to(number_line.number_to_point(0),UP,buff=0)
        # Grouping arrow and number_label
        label = VGroup(arrow,number_label)
        # Set the position of number_label
        number_label.next_to(arrow,UP,buff=0.1)
        # Grouping all elements
        numer_group = VGroup(label,number_line,labels)
        # Set the updater to the arrow and number_label
        label.add_updater(lambda mob: mob.next_to(number_line.number_to_point(v_tracker.get_value()),UP,buff=0))

        return numer_group





class Pendulum(VGroup):
    CONFIG = {
        "theta_max": 10 * DEGREES,
        "theta_offset": 0,
        "theta_start": None,
        "length": 5,
        "origin": ORIGIN,
        "mass_config": {
            "radius": 0.5,
            "color": RED
        },
        "line_config": {
            "color": WHITE,
            "stroke_width": 3
        }
    }
    def __init__(self,**kwargs):
        digest_config(self,kwargs)
        super().__init__(**kwargs)
        self.mass = self.get_mass()
        self.string = self.get_string()
        self.vertical_line = self.string.copy()
        self.string.save_state()
        self.string.initial_state = self.string.copy()
        if self.theta_start == None:
            self.theta_start = self.theta_max
        self.mass.add_updater(lambda mob: mob.move_to(self.string.get_end()))
        self.rotate(self.theta_start)
        self.add(self.string,self.mass)

    def get_mass(self):
        return Dot(**self.mass_config)

    def get_string(self):
        return Line(
            self.origin,
            self.origin + DOWN * self.length,
            **self.line_config
        )

    def rotate(self,angle):
        self.string.rotate(angle, about_point=self.origin)

    def restore_string(self):
        self.string.restore()
        

    def get_angle(self):
        return angle_between(self.string.get_unit_vector(), DOWN) * 180 / PI

    def add_mass_updater(self):
        self.mass.add_updater(lambda mob: mob.move_to(self.string.get_end()))


class PendulumScene(Scene):
    CONFIG = {
        "total_time": 13,
        "dt_factor": 3,
        "gravity": 9.8
    }
    def construct(self):
        dt_calculate = 1 / self.camera.frame_rate
        roof = self.get_roof()
        roof.to_edge(UP)
        pendulum = Pendulum(
            origin=roof.get_bottom()
        )
        pendulum.restore_string()
        # equation = Tex("\\theta = \\theta_{max}\\cos\\left(\\sqrt{\\frac{g}{L}}\\cdot t\\right)")
        # equation.to_corner(DR)
        self.play(ShowCreation(roof))
        self.play(
            AnimationGroup(
                ShowCreation(pendulum.string),
                GrowFromCenter(pendulum.mass),
                lag_ratio=1
            )
        )
        self.play(
            Rotating(
                pendulum.string,
                radians=10*DEGREES,
                about_point=pendulum.origin,
                rate_func=smooth,
                run_time=1
            )
        )
        self.wait()
        # self.play(
        #     Write(equation)
        # )
        pendulum.add_updater(self.get_theta_func(pendulum))
        self.add(pendulum)
        self.wait(self.total_time)

    def get_theta_func(self,mob):
        func = lambda t: mob.theta_max * np.cos(
            t * np.sqrt(
                ( self.gravity / mob.length )
            )
        )
        def updater_func(mob,dt):
            mob.theta_offset += dt * self.dt_factor
            new_theta = func(mob.theta_offset)
            mob.restore_string()
            mob.rotate(new_theta)
        return updater_func

    def get_roof(self,size=0.2,**line_config):
        line = Line(
            ORIGIN, UR * size, **line_config
        )
        lines = VGroup(*[
            line.copy() for _ in range(30)
        ])
        lines.arrange(RIGHT,buff=0)
        down_line = Line(
            lines.get_corner(DL),
            lines.get_corner(DR),
            **line_config
        )
        return VGroup(lines, down_line)




class Ball(Circle):
    CONFIG = {
        "radius": 0.4,
        "fill_color": BLUE,
        "fill_opacity": 1,
        "color": BLUE
    }

    def __init__(self, ** kwargs):
        Circle.__init__(self, ** kwargs)
        self.velocity = np.array((2, 0, 0))

    def get_top(self):
        return self.get_center()[1] + self.radius

    def get_bottom(self):
        return self.get_center()[1] - self.radius

    def get_right_edge(self):
        return self.get_center()[0] + self.radius

    def get_left_edge(self):
        return self.get_center()[0] - self.radius

class Box(Rectangle):
    CONFIG = {
        "height": 6,
        "width": FRAME_WIDTH - 2,
        "color": GREEN_C
    }

    def __init__(self, ** kwargs):
        Rectangle.__init__(self, ** kwargs)  # Edges
        self.top = 0.5 * self.height
        self.bottom = -0.5 * self.height
        self.right_edge = 0.5 * self.width
        self.left_edge = -0.5 * self.width

class BouncingBall(Scene):
    CONFIG = {
        "bouncing_time": 10,
    }
    def construct(self):
        box = Box()
        ball = Ball()
        self.play(FadeIn(box))
        self.play(FadeIn(ball))

        def update_ball(ball,dt):
            ball.acceleration = np.array((0, -5, 0))
            ball.velocity = ball.velocity + ball.acceleration * dt
            ball.shift(ball.velocity * dt)  # Bounce off ground and roof
            if ball.get_bottom() <= box.bottom*0.96 or \
                    ball.get_top() >= box.top*0.96:
                ball.velocity[1] = -ball.velocity[1]
            # Bounce off walls
            if ball.get_left_edge() <= box.left_edge or \
                    ball.get_right_edge() >= box.right_edge:
                ball.velocity[0] = -ball.velocity[0]

        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(self.bouncing_time)
        ball.clear_updaters()
        self.wait(3)



def get_risk(line,dl=0.3,n=1,pr=1):
    lg=[]
    for i in range(n):
        l=line.copy().rotate(PI/2)
        l.set_length(dl)
        l.move_to((line.get_start()+pr*line.get_end())/(1+pr)+(1)*i*0.01*(line.get_start()+line.get_end()))
        lg.append(l)
    lg = VGroup(*lg)
    return lg

class arc_test(Scene):

    def construct(self):
        line1 = Line(DOWN,5*RIGHT)
        l=get_risk(line1,0.3,3,16/3)
        self.play(ShowCreation(line1))
        self.play(ShowCreation(l))
        self.wait(10)




class CircleScene(Scene):
    CONFIG = {
        "radius" : 1.5,
        "stroke_color" : WHITE,
        "fill_color" : BLUE_E,
        "fill_opacity" : 0.75,
        "radial_line_color" : MAROON_B,
        "outer_ring_color" : GREEN_E,
        "ring_colors" : [BLUE, GREEN],
        "dR" : 0.1,
        "dR_color" : YELLOW,
        "unwrapped_tip" : ORIGIN,
        
        "circle_corner" : UP+LEFT,
    }
    def setup(self):
       
        self.circle = Circle(
            radius = self.radius,
            stroke_color = self.stroke_color,
            fill_color = self.fill_color,
            fill_opacity = self.fill_opacity,
        )
        self.circle.to_corner(self.circle_corner, buff = MED_LARGE_BUFF)
        self.radius_line = Line(
            self.circle.get_center(),
            self.circle.get_right(),
            color = self.radial_line_color
        )
        self.radius_brace = Brace(self.radius_line, buff = SMALL_BUFF)
        self.radius_label = self.radius_brace.get_text("$R$", buff = SMALL_BUFF)

        self.radius_group = VGroup(
            self.radius_line, self.radius_brace, self.radius_label
        )
        self.add(self.circle, *self.radius_group)


    def introduce_circle(self, added_anims = []):
        self.remove(self.circle)
        self.play(
            ShowCreation(self.radius_line),
            GrowFromCenter(self.radius_brace),
            Write(self.radius_label),
        )
        self.circle.set_fill(opacity = 0)

        self.play(
            Rotate(
                self.radius_line, 2*np.pi-0.001, 
                about_point = self.circle.get_center(),
            ),
            ShowCreation(self.circle),
            *added_anims,
            run_time = 2
        )
        self.play(
            # self.circle.set_fill, self.fill_color, self.fill_opacity,
            Animation(self.radius_line),
            Animation(self.radius_brace),
            Animation(self.radius_label),
        )

    def increase_radius(self, numerical_dr = True, run_time = 2):
        radius_mobs = VGroup(
            self.radius_line, self.radius_brace, self.radius_label
        )
        nudge_line = Line(
            self.radius_line.get_right(),
            self.radius_line.get_right() + self.dR*RIGHT,
            color = self.dR_color
        )
        nudge_arrow = Arrow(
            nudge_line.get_center() + 0.5*RIGHT+DOWN,
            nudge_line.get_center(),
            color = YELLOW,
            buff = SMALL_BUFF,
            tip_length = 0.2,
        )
        if numerical_dr:
            nudge_label = Tex("%.01f"%self.dR)
        else:
            nudge_label = Tex("dr")
        nudge_label.set_color(self.dR_color)
        nudge_label.scale(0.75)
        nudge_label.next_to(nudge_arrow.get_start(), DOWN)

        radius_mobs.add(nudge_line, nudge_arrow, nudge_label)

        outer_ring = self.get_outer_ring()

        self.play(
            FadeIn(outer_ring),            
            ShowCreation(nudge_line),
            ShowCreation(nudge_arrow),
            Write(nudge_label),
            run_time = run_time/2.
        )
        self.wait(run_time/2.)
        self.nudge_line = nudge_line
        self.nudge_arrow = nudge_arrow
        self.nudge_label = nudge_label
        self.outer_ring = outer_ring
        return outer_ring

    def get_ring(self, radius, dR, color = GREEN):
        ring = Circle(radius = radius + dR).center()
        inner_ring = Circle(radius = radius)
        inner_ring.rotate(np.pi, RIGHT)
        ring.append_vectorized_mobject(inner_ring)
        ring.set_stroke(width = 0)
        ring.set_fill(color)
        ring.move_to(self.circle)
        ring.R = radius 
        ring.dR = dR
        return ring

    def get_rings(self, **kwargs):
        dR = kwargs.get("dR", self.dR)
        colors = kwargs.get("colors", self.ring_colors)
        radii = np.arange(0, self.radius, dR)
        colors = color_gradient(colors, len(radii))

        rings = VGroup(*[
            self.get_ring(radius, dR = dR, color = color)
            for radius, color in zip(radii, colors)
        ])
        return rings

    def get_outer_ring(self):
        return self.get_ring(
            radius = self.radius, dR = self.dR,
            color = self.outer_ring_color
        )

    def unwrap_ring(self, ring, **kwargs):
        self.unwrap_rings(ring, **kwargs)

    def unwrap_rings(self, *rings, **kwargs):
        added_anims = kwargs.get("added_anims", [])
        rings = VGroup(*rings)
        unwrapped = VGroup(*[
            self.get_unwrapped(ring, **kwargs)
            for ring in rings
        ])
        self.play(
            rings.rotate, np.pi/2,
            rings.next_to, unwrapped.get_bottom(), UP,
            run_time = 2,
            path_arc = np.pi/2,
        )
        self.play(
            Transform(rings, unwrapped, run_time = 3),
            *added_anims
        )

    def get_unwrapped(self, ring, to_edge = LEFT, **kwargs):
        R = ring.R
        R_plus_dr = ring.R + ring.dR
        n_anchors = ring.get_num_curves()
        result = VMobject()
        result.set_points_as_corners([
            interpolate(np.pi*R_plus_dr*LEFT,  np.pi*R_plus_dr*RIGHT, a)
            for a in np.linspace(0, 1, n_anchors//2)
        ]+[
            interpolate(np.pi*R*RIGHT+ring.dR*UP,  np.pi*R*LEFT+ring.dR*UP, a)
            for a in np.linspace(0, 1, n_anchors//2)
        ])
        # result.set_style_data(
        #     stroke_color = ring.get_stroke_color(),
        #     stroke_width = ring.get_stroke_width(),
        #     fill_color = ring.get_fill_color(),
        #     fill_opacity = ring.get_fill_opacity(),
        # )
        result.move_to(self.unwrapped_tip, aligned_edge = DOWN)
        result.shift(R_plus_dr*DOWN)
        if to_edge is not None:
            result.to_edge(to_edge)

        return result



#############


class circle(CircleScene):
    CONFIG = {
        
        "unwrapped_tip" : 2*RIGHT
    }
    def construct(self):
        self.force_skipping()

        # self.introduce_area()
        self.question_area()
        # self.show_calculus_symbols()

    def introduce_area(self):
        area = Tex("\\text{Area}", "=", "\\pi", "R", "^2")
        

        self.remove(self.circle, self.radius_group)
        
        self.introduce_circle()
        self.wait()
        R_copy = self.radius_label.copy()
        self.play(
            
            Transform(R_copy, area.get_part_by_tex("R"))
        )
        self.play(Write(area))
        self.remove(R_copy)
        self.wait()

        self.area = area

    def question_area(self):
        q_marks = Tex("???")
        
        rings = VGroup(*reversed(self.get_rings()))
        unwrapped_rings = VGroup(*[
            self.get_unwrapped(ring, to_edge = None)
            for ring in rings
        ])
        unwrapped_rings.arrange(UP, buff = SMALL_BUFF)
        unwrapped_rings.move_to(self.unwrapped_tip, UP)
        ring_anim_kwargs = {
            "run_time" : 3,
            "lag_ratio" : 0.5
        }

        self.play(
            # Animation(self.area),
            Write(q_marks),
            
        )
        self.wait()
        self.play(
            FadeIn(rings, **ring_anim_kwargs),
            Animation(self.radius_group),
            FadeOut(q_marks),
           
        )
        self.wait()
        self.play(
            rings.animate.rotate(np.pi/2),
            rings.animate.move_to(unwrapped_rings.get_top()),
            Animation(self.radius_group),
            # path_arc = np.pi/2,
            # **ring_anim_kwargs
        )
        self.play(
            Transform(rings, unwrapped_rings, **ring_anim_kwargs),
        )
        self.wait()

    def show_calculus_symbols(self):
        ftc = Tex(
            "\\int_0^R", "\\frac{dA}{dr}", "\\,dr",
            "=", "A(R)"
        )
        ftc.shift(2*UP)

        self.play(
            ReplacementTransform(
                self.area.get_part_by_tex("R").copy(),
                ftc.get_part_by_tex("int")
            ),
           
        )
        self.wait()
        self.play(
            ReplacementTransform(
                self.area.get_part_by_tex("Area").copy(),
                ftc.get_part_by_tex("frac")
            ),
            ReplacementTransform(
                self.area.get_part_by_tex("R").copy(),
                ftc.get_part_by_tex("\\,dr")
            )
        )
        self.wait()
        self.play(Write(VGroup(*ftc[-2:])))
        self.wait(2)
