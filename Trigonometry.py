from manim import *

class CTriangle(VMobject):
    """
    This is an equilateral triangle.
    Use indexes as follows to get each length
    base side : 0
    right side : 1
    left side : 2
    """
    def __init__(self):
        super().__init__()
        l1 = Line(start= np.array([-1.3,-1,0]), end= np.array([1.3,-1,0]))
        l2 = Line(start= l1.get_start(), end= np.array([0,1,0]))
        l3 = Line(start= l1.get_end(), end= l2.get_end())
        triangle = VGroup(l1,l2,l3)
        self.become(triangle)

        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def set_base_color(self, c):
        self.l1.set_color(color= c)
        return self
    def set_left_color(self, c):
        self.l2.set_color(color= c)
        return self
    def set_right_color(self, c):
        self.l3.set_color(color= c)
        return self

class RTriangle(VMobject):
    """
    This is a right angled triangle
    """
    def __init__(self):
        super().__init__()
        l1 = Line(start= np.array([0,-1,0]), end= np.array([1.3,-1,0]))
        l2 = Line(start= l1.get_start(), end= np.array([0,1,0]))
        l3 = Line(start= l1.get_end(), end= l2.get_end())
        rtriangle = VGroup(l1, l2, l3)
        self.become(rtriangle)

        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    # Getters
    def get_base(self):
        return self.l1
    def get_height(self):
        return self.l2
    def get_hypo(self):
        return self.l3

class CustomTriangle(Scene):
    def construct(self):
        # Making Hexagon using Triangles
        a = CTriangle()
        a.set_base_color(BLACK)
        a.set_right_color(BLACK)
        b = CTriangle().rotate(PI).next_to(a, RIGHT, buff= -1.3)
        b.set_left_color(BLACK)
        b.set_right_color(BLACK)
        c = CTriangle().next_to(b, RIGHT, buff= -1.3)
        c.set_base_color(BLACK)
        c.set_left_color(BLACK)
        d = CTriangle().rotate(PI).next_to(a, DOWN, buff= -0)
        d.set_base_color(BLACK)
        d.set_left_color(BLACK)
        e = CTriangle().next_to(d, RIGHT, buff= -1.3)
        e.set_left_color(BLACK)
        e.set_right_color(BLACK)
        f = CTriangle().rotate(PI).next_to(e, RIGHT, buff= -1.3)
        f.set_base_color(BLACK)
        f.set_right_color(BLACK)

        hexagon = VGroup(a,c,b,d,e,f)
        hexagon.move_to(ORIGIN)

        self.play(Create(hexagon), run_time= 2)
        self.wait(2)

        # Starting to unhide triangles
        self.play(AnimationGroup(
            a.animate.set_right_color(WHITE),
            f.animate.set_right_color(WHITE)
        ))

        self.play(AnimationGroup(
            c.animate.set_left_color(WHITE),
            d.animate.set_left_color(WHITE)
        ))

        # self.play(AnimationGroup(
        #     d.animate.set_base_color(WHITE),
        #     f.animate.set_base_color(WHITE)
        # ))
        self.play(AnimationGroup(
            d[0].animate.set_color(WHITE),
            f[0].animate.set_color(WHITE)
        ))

        for i in [a,b,c,d,e,f]:
            i.set_color(WHITE)

        self.play(AnimationGroup(
            a.animate.shift(a.get_center() * 1.5),
            b.animate.shift(b.get_center() * 1.5),
            c.animate.shift(c.get_center() * 1.5),
            d.animate.shift(d.get_center() * 1.5),
            e.animate.shift(e.get_center() * 1.5),
            f.animate.shift(f.get_center() * 1.5),
        ), run_time= 2)
        self.play(e.animate.set_right_color(RED))
        self.wait(2)

        self.play(AnimationGroup(
            Rotate(b, angle= PI, about_point= b.get_center()),
            Rotate(d, angle= PI, about_point= d.get_center()),
            Rotate(f, angle= PI, about_point= f.get_center())
        ), run_time= 2)
        self.wait(2)

        self.play(FadeOut(
            VGroup(a,c,d,e,f)
        ), run_time= 1.5)
        self.play(b.animate.move_to(ORIGIN))
    
        # Making Right Angle Triangles
        rt_r = RTriangle()
        rt_l = RTriangle().rotate(angle= PI, axis= UP, about_point= rt_r[1].get_center())
        angle_r = RightAngle(line1= rt_r.get_base(), line2= rt_r.get_height(), length= 0.2)
        angle = Angle(line1= rt_r.get_hypo(), line2= rt_r.get_base().reverse_direction())

        self.play(Create(VGroup(rt_r, rt_l)), run_time= 2)
        self.wait(2)
        self.play(Create(VGroup(angle_r, angle)))
        rt_r.add(angle_r, angle)
        self.wait(2)
        self.remove(b)
        self.wait(2)

        self.play(AnimationGroup(
            rt_r.animate.shift(rt_r.get_center() * 3),
            rt_l.animate.shift(rt_l.get_center() * 3)
        ))
        self.wait(2)
        self.play(FadeOut(rt_l),
            rt_r.animate.move_to(ORIGIN).scale(1.5), run_time= 1.5
        )
        self.wait(2)

        Tex.set_default(font_size= 30)
        hypotenuse = Tex("Hypotenuse").next_to(rt_r.get_hypo(), RIGHT, buff= -1.8).rotate(-angle.get_value())
        oppose = Tex("Oppose").next_to(rt_r.get_base(), DOWN, buff= 0.6).shift(LEFT * 0.6)
        adjacent = Tex("Adjacent").rotate(PI/2).next_to(rt_r.get_height(), LEFT, buff= 1.1)

        self.play(Write(hypotenuse), run_time= 1.5)
        self.wait(2)
        self.play(Write(oppose), run_time= 1.5)
        self.wait(2)
        self.play(Write(adjacent), run_time= 1.5)
        self.wait(2)
