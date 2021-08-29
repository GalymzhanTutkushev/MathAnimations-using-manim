from manimlib import *


class vectors3d(Scene):
    def construct(self):
        tda = ThreeDAxes()
        i = Vector([1,0,0]).set_color(RED)
        j = Vector([0,1,0]).set_color(GREEN)
        k = Vector([0,0,1]).set_color(BLUE)
        w = 3
        xy = Polygon(ORIGIN,[w,0,0],[w,w,0],[0,w,0]).scale(0.8).set_fill(RED,0.5)
        yz = Polygon(ORIGIN,[0,0,w],[0,w,w],[0,w,0]).scale(0.8).set_fill(GREEN,0.5)
        xz = Polygon(ORIGIN,[0,0,w],[w,0,w],[w,0,0]).scale(0.8).set_fill(BLUE,0.5)
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=170 * DEGREES,
            phi=70 * DEGREES,
            # gamma  = 30*DEGREES
        )
        self.play(frame.animate.increment_phi(70 * DEGREES),
                frame.animate.increment_gamma(130 * DEGREES),
            frame.animate.increment_theta(-30 * DEGREES))
        
        self.play(ShowCreation(tda))
        self.play(ShowCreation(i),ShowCreation(j),ShowCreation(k))
        self.play(ShowCreation(xy),ShowCreation(yz),ShowCreation(xz))
        self.wait(pause_time)

        
class parallelipiped(ThreeDScene):
    def construct(self):
        
        prism = Prism(dimensions= [2, 1, 2])
        
        axes = ThreeDAxes()

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.add(axes)
        
        self.play(ShowCreation(prism))
        self.wait()
        self.remove(prism)
       
        self.move_camera(0.8*np.pi/2, -0.45*np.pi,10,-0.45*np.pi)
        # self.begin_ambient_camera_rotation()
        self.wait(pause_time)


class sphere4(ThreeDScene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):
        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

       
        sphere = Sphere(radius = 2)
        t = Torus()
        cyl = Cylinder()
        l3 = Line3D(ORIGIN,3*OUT+3*LEFT)
        d3 = Disk3D()
        sq = Square3D()
      
        self.play(ShowCreation(t))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(t))

        self.play(ShowCreation(cyl))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(cyl))
        self.play(ShowCreation(l3))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(l3))
        self.play(ShowCreation(d3))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(d3))
        self.play(ShowCreation(sq))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(sq))
        self.play(ShowCreation(c))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(c))
        self.play(ShowCreation(p))
        self.play(frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES))
        self.wait(3)
        self.play(FadeOut(p))


class MyCube(ThreeDScene):
    def construct(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        CONFIG = {
            "fill_opacity": 0.75,
            "fill_color": BLUE,
            "stroke_width": 0,    
        }
        side_length = 2
        faces = []
        
        for vect in IN, LEFT, RIGHT, UP, DOWN, OUT:
            face = Square(
                side_length=side_length,
                shade_in_3d=True,
                fill_opacity= 0.75,
                fill_color= BLUE,
            )
            face.flip()
            face.shift(side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            faces.append(face)
            self.play(ShowCreation(face))
        # vect =[DOWN,IN,IN,IN,IN]
        # axis = [RIGHT,RIGHT, LEFT, UP,DOWN]
        vect = [IN,IN,IN,IN,DOWN]
        axis = [DOWN,UP,LEFT,RIGHT,RIGHT]
        self.play(Rotating(faces[1], PI/2,axis = axis[0],about_edge = faces[1].get_edge_center(vect[0])),
        Rotating(faces[2], PI/2,axis = axis[1],about_edge = faces[2].get_edge_center(vect[1])),
        Rotating(faces[3], PI/2,axis = axis[2],about_edge = faces[3].get_edge_center(vect[2])),
        # Rotating(faces[4], radians=PI/2,axis = axis[3],about_edge = faces[4].get_edge_center(vect[3])),
        Rotating(faces[5], PI/2,axis = axis[4],about_point = faces[5].get_edge_center(vect[4])),
        )
        self.play(
        Rotating(faces[4], PI/2,axis = axis[3],about_edge = faces[4].get_edge_center(vect[3])),
        Rotating(faces[5], PI/2,axis = axis[3],about_point = faces[4].get_edge_center(vect[3])),
        )
        self.move_camera(0*np.pi/2, -0*np.pi,10,-0*np.pi)


class Cylinder(Sphere):

    def func(self, u, v):
        return np.array([
            np.cos(v),
            np.sin(v),
            np.cos(u)
        ])


class UnwrappedCylinder(Cylinder):
    def func(self, u, v):
        return np.array([
            v - PI,
            -self.radius,
            np.cos(u)
        ])

class SphereCylinderScene(ThreeDScene):
    CONFIG = {
        "cap_config": {
            "stroke_width": 1,
            "stroke_color": BLACK,
            "fill_color": BLUE_D,
            "fill_opacity": 1,
        }
    }

    def get_cylinder(self, **kwargs):
        config = merge_dicts_recursively(self.sphere_config, kwargs)
        return Cylinder(**config)

    def get_cylinder_caps(self):
        R = self.sphere_config["radius"]
        caps = VGroup(*[
            Circle(
                radius=R,
                **self.cap_config,
            ).shift(R * vect)
            for vect in [IN, OUT]
        ])
        caps.set_shade_in_3d(True)
        return caps

    def get_unwrapped_cylinder(self):
        return UnwrappedCylinder(**self.sphere_config)

    def get_xy_plane(self):
        pass

    def get_ghost_surface(self, surface):
        result = surface.copy()
        result.set_fill(BLUE_E, opacity=0.5)
        result.set_stroke(BLACK, width=0.5, opacity=0.5)
        return result

    def project_point(self, point):
        radius = self.sphere_config["radius"]
        result = np.array(point)
        result[:2] = normalize(result[:2]) * radius
        return result

    def project_mobject(self, mobject):
        return mobject.apply_function(self.project_point)

class MapSphereOntoCylinder(SphereCylinderScene):
    def construct(self):
        sphere = self.get_sphere()
        sphere_ghost = self.get_ghost_surface(sphere)
        sphere_ghost.set_stroke(width=0)
        axes = self.get_axes()
        cylinder = self.get_cylinder()
        cylinder.set_fill(opacity=0.75)
        radius = cylinder.get_width() / 2

        self.add(cylinder)
        self.wait()
        self.begin_ambient_camera_rotation()
        self.move_camera(
            **self.default_angled_camera_position,
            run_time=2,
        )
        # self.wait(2)
        # self.play(
        #     ReplacementTransform(sphere, cylinder),
        #     run_time=3
        # )
        self.wait(3)

        # Get rid of caps
        caps = self.get_cylinder_caps()
        caps[1].set_shade_in_3d(False)

        self.play(FadeIn(caps))
        self.wait()
        self.play(
            caps.space_out_submobjects, 2,
            caps.fade, 1,
            remover=True
        )
      
        # Unwrap
        unwrapped_cylinder = self.get_unwrapped_cylinder()
        unwrapped_cylinder.set_fill(opacity=0.75)
        self.play(
            ReplacementTransform(cylinder, unwrapped_cylinder),
            run_time=3
        )
        self.stop_ambient_camera_rotation()
        self.move_camera(
            phi=90 * DEGREES,
            theta=-90 * DEGREES,
        )

        # Show dimensions
        stroke_width = 5
        top_line = Line(
            PI * radius * LEFT + radius * OUT,
            PI * radius * RIGHT + radius * OUT,
            color=YELLOW,
            stroke_width=stroke_width,
        )
        side_line = Line(
            PI * radius * LEFT + radius * OUT,
            PI * radius * LEFT + radius * IN,
            color=RED,
            stroke_width=stroke_width,
        )
        lines = VGroup(top_line, side_line)
        lines.shift(radius * DOWN)
        two_pi_R = Tex("2\\pi R")
        two_R = Tex("2R")
        texs = VGroup(two_pi_R, two_R)
        for tex in texs:
            tex.scale(1.5)
            tex.rotate(90 * DEGREES, RIGHT)
        two_pi_R.next_to(top_line, OUT)
        two_R.next_to(side_line, RIGHT)

        self.play(
            ShowCreation(top_line),
            FadeInFrom(two_pi_R, IN)
        )
        self.wait()
        self.play(
            ShowCreation(side_line),
            FadeInFrom(two_R, RIGHT)
        )
        self.wait()

class CircumferenceOfCylinder(SphereCylinderScene):
    def construct(self):
        sphere = self.get_sphere()
        sphere_ghost = self.get_ghost_surface(sphere)
        cylinder = self.get_cylinder()
        cylinder_ghost = self.get_ghost_surface(cylinder)
        cylinder_ghost.set_stroke(width=0)

        radius = self.sphere_config["radius"]
        circle = Circle(radius=radius)
        circle.set_stroke(YELLOW, 5)
        circle.shift(radius * OUT)

        height = Line(radius * IN, radius * OUT)
        height.shift(radius * LEFT)
        height.set_stroke(RED, 5)

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.begin_ambient_camera_rotation(0.01)
        self.add(sphere_ghost, cylinder_ghost)
        self.wait()
        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(ShowCreation(height))
        self.wait(5)

class my_cylynder(ThreeDScene):
    def construct(self):

        cylinder = ParametricSurface(lambda u, v: np.array([np.cos(TAU * v), np.sin(TAU * v), 1.0 * (1 - u)]), resolution=(6, 32))

        self.play(ShowCreation(cylinder))
        self.wait()


class Cone(ThreeDScene):
    def construct(self):
        cone = ParametricSurface(lambda u, v: np.array( [u*np.cos(TAU * v), u*np.sin(TAU * v),  u]), resolution=(6, 32))
        coneUnrapped = ParametricSurface(lambda u, v: np.array( [4/3*u*np.cos(TAU * (v*0.75)),4/3*u* np.sin(TAU * (v*0.75)), 0]), resolution=(6, 32))
        coneUnrapped.set_color(RED)
        coneUnrapped.move_to(2*RIGHT)
        
        self.play(ShowCreation(coneUnrapped))
        self.play(ReplacementTransform(cone,coneUnrapped),run_time = 5)
        self.wait(5)

            
class TruncatedCone(ThreeDScene):
    def construct(self):
        cone = ParametricSurface(lambda u, v: np.array( [u*np.cos(TAU * v), u*np.sin(TAU * v),  u]), resolution=(6, 32))
        coneUnrapped = ParametricSurface(lambda u, v: np.array( [4/3*u*np.cos(TAU * (v*0.75)),4/3*u* np.sin(TAU * (v*0.75)), 0]), resolution=(6, 32))
        coneUnrapped.set_color(RED)
        coneUnrapped.move_to(2*RIGHT)
        
        self.play(ShowCreation(coneUnrapped))
        self.play(ReplacementTransform(cone,coneUnrapped),run_time = 5)

        cone = ParametricSurface(lambda u, v: np.array( [(2-u)*np.cos(TAU * v), (2-u)*np.sin(TAU * v),  u]), resolution=(6, 32))
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.play(ShowCreation(cone))
        self.move_camera(0.8*np.pi/2, -0.45*np.pi,10,-0.45*np.pi)

class MyPyramid(ThreeDScene):
    def construct(self):
        size = 3
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        osnova = Polygon(ORIGIN,size*LEFT,size*(UP+LEFT),size*UP)
        osnova.set_fill(color = BLUE,opacity = 0.75)
        
        print(ORIGIN)
        k = Polygon(size*LEFT,size*(UP+LEFT),size*(LEFT+UP)/2+[0,0,2])
        k1 = Polygon(size*(UP+LEFT),size*UP,size*(LEFT+UP)/2+[0,0,2])
        k2 = Polygon(size*UP,ORIGIN,size*(LEFT+UP)/2+[0,0,2])
        k3 = Polygon(ORIGIN,size*LEFT,size*(LEFT+UP)/2+[0,0,2])
        k3.set_fill(color = BLUE,opacity = 0.75)
        k2.set_fill(color = BLUE,opacity = 0.75)
        k1.set_fill(color = BLUE,opacity = 0.75)
        k.set_fill(color = BLUE,opacity = 0.75)
        pyramid_group = VGroup(osnova,k,k1,k2,k3)
        pyramid_group.move_to(ORIGIN)
        self.add(osnova)
        self.play(ShowCreation(k))
        self.play(ShowCreation(k1))
        self.play(ShowCreation(k2))
        self.play(ShowCreation(k3))
        print(osnova.get_edge_center(RIGHT))
        self.play(Rotating(k, PI/3*2,axis = DOWN,about_edge = [-1.5,-1.5,-1]))
        self.play(Rotating(k1, PI/3*2,axis = LEFT,about_edge = [1.5,1.5,-1]))
        self.play(Rotating(k2, PI*2/3,axis = UP,about_edge = [1.5,1.5,-1]))
        self.play(Rotating(k3, PI/3*2,axis = RIGHT,about_edge = [-1.5,-1.5,-1]))

        self.move_camera(0*np.pi/2, -0*np.pi,10,-0*np.pi)
        
class TruncatedPyramid(ThreeDScene):
    def construct(self):
        size = 3
        h = 2
        sizeU = 2
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        osnova = Polygon(ORIGIN,size*LEFT,size*(UP+LEFT),size*UP)
        osnova.set_fill(color = BLUE,opacity = 0.75)
        osnova2 = Polygon(ORIGIN,sizeU*LEFT,sizeU*(UP+LEFT),sizeU*UP)
        osnova2.set_fill(color = BLUE,opacity = 0.75)
        osnova2.move_to(osnova.get_center()+[0,0,h])

        k = Polygon(osnova.get_corner(DR),osnova.get_corner(DL),osnova2.get_corner(DL),osnova2.get_corner(DR))
        k1 = Polygon(osnova.get_corner(DL),osnova.get_corner(UL),osnova2.get_corner(UL),osnova2.get_corner(DL))
        k2 = Polygon(osnova.get_corner(UL),osnova.get_corner(UR),osnova2.get_corner(UR),osnova2.get_corner(UL))
        k3 = Polygon(osnova.get_corner(UR),osnova.get_corner(DR),osnova2.get_corner(DR),osnova2.get_corner(UR))
        k3.set_fill(color = BLUE,opacity = 0.75)
        k2.set_fill(color = BLUE,opacity = 0.75)
        k1.set_fill(color = BLUE,opacity = 0.75)
        k.set_fill(color = BLUE,opacity = 0.75)

        self.play(ShowCreation(osnova))
        self.play(ShowCreation(osnova2))
        self.play(ShowCreation(k))
        self.play(ShowCreation(k1))
        self.play(ShowCreation(k2))
        self.play(ShowCreation(k3))

class ro(Scene):
    def construct(self):
        line=ParametricCurve(lambda x: x**2+x**3+x**4)
        p=line.get_unit_normal()

        # print(p)
        self.play(Write(line))
        
        self.play(Write(p))
        self.wait(pause_time)

class rotate_cone(ThreeDScene):
    def construct(self):
        tr = Polygon([0,0,0],[0,0,3],[0,2,0])
        rect = Polygon([0,0,0],[0,0,3],[0,2,3],[0,2,0])
        axes = ThreeDAxes()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.add(axes)
        self.play(ShowCreation(tr))
        dot = Dot([0,2,0])
        dot.set_color(RED)
        path = VMobject()
        self.add(path, dot)
        print(np.arctan (dot.get_center()[1]/dot.get_center()[0]))
        path.add_updater(lambda x: x.become(Arc(start_angle=0, angle=4,radius = 2)))
        path.set_color(ORANGE)
        
        self.play(Rotating(dot, TAU, about_point=ORIGIN),
        Rotating(tr, TAU,axis = [0,0,1],about_edge = [0,-2,6]),run_time = play_time)
        self.wait(pause_time)

class rotate_cylinder(ThreeDScene):
    def construct(self):
       
        rect = Polygon([0,0,0],[0,0,3],[0,2,3],[0,2,0])
        axes = ThreeDAxes()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.add(axes)
        self.play(ShowCreation(rect))
        dot = Dot([0,2,0])
        dot.set_color(RED)
        path = VMobject()
        self.add(path, dot)
        path.add_updater(update_path)
        path.set_color(RED)
        

        dot2 = Dot([0,2,3])
        dot2.set_color(RED)
        path2 = VMobject()
        self.add(path2, dot2)
        path2.add_updater(update_path2)
        path2.set_color(RED)
        

        l = Line([0,2,0],[0,2,3])
        l.set_color(GREEN)
        path3 = VMobject()
        self.add(path3, l)
        path3.add_updater(update_path3)
        path3.set_color(RED)
        


        self.play(Rotating(dot,TAU, about_point=ORIGIN),Rotating(dot2, TAU, about_point=ORIGIN),
       Rotating(l, TAU, about_point=ORIGIN), Rotating(rect, PI*2,axis = [0,0,1],about_edge = [0,-2,3]))
        self.wait(3)

class rotate_con(ThreeDScene):
    def construct(self):
       
        rect = Polygon([0,0,0],[0,0,3],[0,1,3],[0,2,0])
        axes = ThreeDAxes()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.add(axes)
        self.play(ShowCreation(rect))
        dot = Dot([0,2,0])
        dot.set_color(RED)
        path = VMobject()
        self.add(path, dot)
        path.add_updater(update_path)
        path.set_color(RED)
        

        dot2 = Dot([0,1,3])
        dot2.set_color(RED)
        path2 = VMobject()
        self.add(path2, dot2)
        path2.add_updater(update_path2)
        path2.set_color(RED)
        

        l = Line([0,2,0],[0,1,3])
        l.set_color(GREEN)
        path3 = VMobject()
        self.add(path3, l)
        path3.add_updater(update_path3)
        path3.set_color(RED)
        


        self.play(Rotating(dot, TAU, about_point=ORIGIN),Rotating(dot2, TAU, about_point=ORIGIN),
       Rotating(l, TAU, about_point=ORIGIN), Rotating(rect, TAU,axis = [0,0,1],about_edge = [0,-2,3]))
        self.wait(3)

class rotate_sphere(ThreeDScene):
    def construct(self):
       
        rect = Arc(start_angle=-PI/2,angle=PI,radius = 1)
 
        axes = ThreeDAxes()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.add(axes)
        self.play(ShowCreation(rect))
        ans=[]
        for i in np.arange(-0.5,0.5,0.1):
           
            dot = Dot([np.cos(PI*i),-np.sin(PI*i),0])
            dot.set_color(RED)
            path = VMobject()
            self.add(path, dot)
            path.add_updater(update_path)
            path.set_color(RED)
                            
            an = Rotating(dot, TAU,axis = [0,1,0], about_point=ORIGIN)
            self.play(an)
            # ans.append(an)
                # path.clear_updaters()
                 

        # self.play(Rotating(rect, radians=PI*2,axis = [0,1,0],about_point = ORIGIN),AnimationGroup(*ans))
        # dot2 = Dot([np.sin(PI/4),-np.cos(PI/4),0])
        # dot2.set_color(RED)



    #     self.play(Rotating(dots[], radians=TAU,axis = [0,1,0], about_point=ORIGIN),Rotating(dot2, radians=TAU,axis = [0,1,0], about_point=ORIGIN),
    #    Rotating(l, radians=TAU,axis = [0,1,0], about_point=ORIGIN), Rotating(rect, radians=PI*2,axis = [0,1,0],about_point = ORIGIN))
        self.wait(3)


class parabaloid(ThreeDScene):
    def construct(self):
        a = 1/2
        b= 1/2
        para = ParametricSurface(lambda u, v: np.array([a*u*np.cos(TAU * v), b*u*np.sin(TAU * v), u**2]), resolution=(6, 32))
        axes = ThreeDAxes()
       
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        # self.add(axes)

        # self.wait()

        self.play(ShowCreation(para))
        self.move_camera(np.pi/2, np.pi,5,-np.pi)

class hyperboloid(ThreeDScene):
    def construct(self):
        a = 2
        b = 2
        c = 2

        hyp = ParametricSurface(lambda u, v: np.array([a*np.cosh(-PI+TAU*u)*np.cos(TAU*v), b*np.sinh(-PI+TAU*u)*np.sin(TAU*v), c*np.sinh(-PI+TAU*u)]), resolution=(6, 32))
        axes = ThreeDAxes()
        
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        
        # self.add(axes)
        
        # self.wait()

        self.play(ShowCreation(hyp))
        self.move_camera(np.pi/2, np.pi,5,-np.pi)

