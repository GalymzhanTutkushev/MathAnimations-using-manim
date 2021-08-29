from manimlib import *

class prob(Scene):
    def construct(self):
        pa = Tex("P(A)=\\frac{m}{n}")
        pa.to_edge(UP)
        self.play(Write(pa))

class geo_prob(Scene):
    def construct(self):
        Arcs = []
        Lines = []
        for a in range(3):
            r = (a+0.4)/2
            arc = Arc(start_angle=PI/2,angle=2*PI,radius = r)
            if (a== 0):
                arc.set_color(RED)
            elif (a== 1):
                arc.set_color(BLUE)
            else:
                arc.set_color(GREEN)
            arc.set_stroke(width = 50)
            
            self.play(ShowCreation(arc))
            
        self.wait(3)
            
class space(Scene):
    def construct(self):
        s = SampleSpace()
        self.play(ShowCreation(s))


class tree(Scene):
    def construct(self):
        R = 0.4
        t1 = Tex("A")
        t2 = Tex("C")
        t3 = Tex("B")
        n1 = 3
        n2 = 2
        n3 = 1
        md = "r"
        if (md == "r"):
            for i in range(n1):
                c = Circle(radius = R)
                it = t1.copy()
                it.move_to([n1*(i-1),3,0])
                c.surround(it)
                self.play(ShowCreation(c),Write(it))
                for j in range(n2):
                    c2 = Circle(radius = R)
                    jt=t2.copy()
                    jt.move_to(c.get_center()+1.5*DOWN+[j,0,0])
                    c2.surround(jt)
                    line2 = Line(c.get_bottom(),c2.get_top())
                    self.play(ShowCreation(c2),Write(jt),Write(line2))
                    for k in range(n3):
                        c3 = Circle(radius = R)
                        kt = t3.copy()
                        kt.move_to(c2.get_center()+1.5*DOWN+[n3*k,0,0])
                        c3.surround(kt)
                        line3 = Line(c2.get_bottom(),c3.get_top())
                        self.play(ShowCreation(c3),Write(kt),Write(line3))
        elif(md=="p"):
            t11 = [t1,      t2,      t3]
            t12 = [t2,t3,   t1,t3,   t2,t1]
            t13 = [t3,t2,   t3,t1,   t1,t2]
            for i in range(len(t11)):
                c = Circle(radius = R)
                it = t11[i].copy()
                it.move_to([n1*(i-1),3,0])
                c.surround(it)
                self.play(ShowCreation(c),Write(it))
                for j in range(int(len(t12)/len(t11))):
                    c2 = Circle(radius = R)
                    jt=t12[(len(t11)-1)*i+j].copy()
                    jt.move_to(c.get_center()+1.5*DOWN+[j,0,0])
                    c2.surround(jt)
                    line2 = Line(c.get_bottom(),c2.get_top())
                    self.play(ShowCreation(c2),Write(jt),Write(line2))
                    for k in range(int(len(t13)/len(t12))):
                        c3 = Circle(radius = R)
                        
                        kt = t13[(len(t11)-1)*(i)+(j)].copy()
                        kt.move_to(c2.get_center()+1.5*DOWN+[n3*k,0,0])
                        c3.surround(kt)
                        line3 = Line(c2.get_bottom(),c3.get_top())
                        self.play(ShowCreation(c3),Write(kt),Write(line3))



class binom(Scene):
    def construct(self):
        Cnk = Tex("C_n = \\frac{n!}{n!\\cdot (n-k)!}")
        Ank = Tex("A_n = n!")
        Ank.to_edge(UP)
        c = Circle()
        s = Square()
        t =Triangle()
        c.set_fill(color = RED,opacity = 0.5)
        s.set_fill(color = GREEN,opacity = 0.5)
        t.set_fill(color = BLUE,opacity = 0.5)
        s.next_to(c,RIGHT,buff=2)
        t.next_to(c,LEFT,buff=2)
        self.play(ShowCreation(c),ShowCreation(s),ShowCreation(t))
        self.play(Swap(c,s))
        self.play(Write(Ank))
        self.wait()
        

class pascal(Scene):
    def construct(self):
        cell_height = 1
        cell_width = 1
        nrows = 6
        pt = GeneralizedPascalsTriangle(nrows = nrows, 
            height = nrows * cell_height, 
            width = nrows * cell_width, )
        pt.set_color(color = BLACK)
        self.play(ShowCreation(pt))



class gaus(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "my_color":BLUE,
        "axes_color": BLUE,
        "include_numbers":True
    }

    def construct(self):
        #Make graph

        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.my_color)
        graph_lab = self.get_graph_label(func_graph, label = "y = exp(-x)")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab),run_time = 5)
        
        self.wait(3)


    def func_to_graph(self, x):
        a = 2
        m = 1
        sigma = 1
        return (1/(np.sqrt(2*PI)*sigma)*np.exp(-(x-m)**2/(2*sigma**2)))

    







# полигон частот. плотности вероятности
def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords
# LEARN MORE HERE:
# https://www.youtube.com/watch?v=Xi52tx6phRU


class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

class CustomGraph1(GraphFromData):
    def construct(self):
        self.setup_axes()
        coords = get_coords_from_csv("custom_graphs/data")
        dots = self.get_dots_from_coords(coords)
        self.add(dots)

# Discrete Graph
class CustomGraph2(GraphFromData):
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv("custom_graphs/data")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        # Set dots
        dots = self.get_dots_from_coords(coords)
        self.add(dots)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)

# Smooth graph
class CustomGraph3(GraphFromData):
    CONFIG = {
        "y_max": 25,
    }
    def construct(self):
        self.setup_axes()
        x = [0 , 1, 2, 3,  4,  5,  6,  7]
        y = [0 , 1, 4, 9, 16, 25, 20, 10]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(coords)
        
        graph = SmoothGraphFromSetPoints(points,color=GREEN)
        dots = self.get_dots_from_coords(coords)

        self.add(graph,dots)

# But, we can do the same thing with a simple SCENE
class CustomGraph4(Scene):
    def construct(self):
        axes = Axes()
        x = [0 , 1, 2, 3,  4, 5,  6]
        y = [0 , 1, 0, -1, 0,  1, 0]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(axes,coords)

        dots = self.get_dots_from_coords(axes,coords)
        graph = SmoothGraphFromSetPoints(points,color=GREEN)

        self.add(axes,graph,dots)

    def get_points_from_coords(self,axes,coords):
        return [axes.coords_to_point(px,py)
            for px,py in coords
            ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,axes,coords,radius=0.1):
        points = self.get_points_from_coords(axes,coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots