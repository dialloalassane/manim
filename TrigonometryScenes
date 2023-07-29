from manim import *
import numpy as np
from TrigonometryMobjects import CTriangle, RightTriangle, CustomRightTriangle

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

        n = 0
        nums = list()
        for i in [a,b,c,d,e,f]:
            num = MathTex(f"{n}").move_to(i.get_center())
            nums.append(num)
            n = n + 1

        for i in [a,b,c,d,e,f]:
            self.play(Create(i))
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

        for i in hexagon:
            i.set_color(WHITE)

        for i in range(len(nums)):
            self.play(Create(nums[i]))
        self.wait(4)
        self.play(FadeOut(VGroup(*nums)))

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

        # self.play(FadeOut(
        #     VGroup(a,c,d,e,f)
        # ), run_time= 1.5)
        
        for i in hexagon:
            self.play(i.animate.move_to([i.get_center()[0], 0, 0]))
        self.play(FadeOut(VGroup(e,d,f)), run_time= 0.2)
        self.play(AnimationGroup(
            a.animate.move_to(ORIGIN),
            c.animate.move_to(ORIGIN)
        ))
    
        # Making Right Angle Triangles
        rt_r = RightTriangle()
        rt_l = RightTriangle().rotate(angle= PI, axis= UP, about_point= rt_r[1].get_center())
        angle_r = RightAngle(line1= rt_r.get_base(), line2= rt_r.get_height(), length= 0.2)
        angle = Angle(line1= rt_r.get_hypo(), line2= rt_r.get_base().reverse_direction())

        self.play(Create(VGroup(rt_r, rt_l)), run_time= 2)
        self.wait(2)
        self.play(FadeOut(VGroup(a,b,c)))
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
            rt_r.animate.move_to(ORIGIN).scale(1.8), run_time= 1.5
        )
        self.wait(2)

        Tex.set_default(font_size= 30)
        hypotenuse = Tex("Hypotenuse").next_to(rt_r.get_hypo(), RIGHT, buff= -1.8).rotate(-angle.get_value())
        oppose = Tex("Oppose").rotate(PI/2).next_to(rt_r.get_height(), LEFT, buff= 1.3)
        adjacent = Tex("Adjacent").next_to(rt_r.get_base(), DOWN, buff= 1).shift(LEFT * 0.6)

        self.play(Write(hypotenuse), run_time= 1.5)
        self.wait(2)
        self.play(Write(oppose), run_time= 1.5)
        self.wait(2)
        self.play(Write(adjacent), run_time= 1.5)
        self.wait(2)


class Sides(Scene):
    def construct(self):
        triangle = CustomRightTriangle(base= 3, height=3)
        triangle.add_angles()

        # Sides
        Tex.set_default(font_size= 30)
        hypotenuse = Tex("Hypotenuse").rotate((triangle.get_hypo().get_angle()-PI)).next_to(triangle.get_hypo(), RIGHT, buff= -1.2)
        oppose = Tex("Oppose").rotate(PI/2).next_to(triangle.get_height(), LEFT, buff= 0.2)
        adjacent = Tex("Adjacent").next_to(triangle.get_base(), DOWN, buff= 0.1)

        # Arrows
        towards_hypo = ArcBetweenPoints(triangle.get_beta().get_center(), triangle.get_base().get_center(), angle= 2, color= WHITE).add_tip(tip_length= 0.1, tip_width= 0.1)
        towards_oppose = Line(start= triangle.get_corners()[0], end= triangle.get_hypo().get_center()).add_tip(tip_length= 0.1, tip_width= 0.1)
        towards_adjacent = Line(start= triangle.get_corners()[2], end= triangle.get_height().get_center()).add_tip(tip_length= 0.1, tip_width= 0.1)
        triangle.add(adjacent, hypotenuse, oppose, towards_hypo, towards_oppose, towards_adjacent)
        
        triangle.move_to(ORIGIN)
        self.play(Create(triangle[0:6]), run_time= 2)
        for i in range(3):
            self.play(Create(triangle[9+i]), run_time= 2)
            self.play(Create(triangle[6+i]), run_time= 2)
            self.wait(2)
            self.play(FadeOut(triangle[9+i]))


class Determine_Angle_based_on_side_lengths(Scene):
    def construct(self):
        Tex.set_default(font_size= 35)
        statement = Title("Calculating angles based on side lengths of triangle", font_size= 35, match_underline_width_to_text= True)
        self.play(Write(statement))
        self.wait(2)
        self.play(FadeOut(statement))

        a = CustomRightTriangle(base=2, height=2)
        b = CustomRightTriangle(base=2.5, height=1.5)
        c = CustomRightTriangle(base=1, height=3)
        d = CustomRightTriangle(base= 2, height= 2.2)

        for i in [a, b, c, d]:
            i.add_angles()
            i.add_angles_tex()
            i.add_side_lens()
        a.to_edge(UL)
        b.to_edge(UR)
        c.to_edge(DL)
        d.to_edge(DR)

        base = 0
        height = 0
        hypo = 0
        base_tex = always_redraw(lambda : MathTex(f"Base= {base}"))
        height_tex = always_redraw(lambda : MathTex(f"Height= {height}").next_to(base_tex, DOWN))
        hypo_tex = always_redraw(lambda : MathTex(f"Hypotenuse= {round(hypo,2)}").next_to(height_tex, DOWN))

        self.play(Write(VGroup(base_tex, height_tex, hypo_tex)), run_time= 2)

        for i in [a,b,c,d]:
            base = i.get_base_length()
            height = i.get_height_length()
            hypo = i.get_hypo_length()
            self.wait(1)
            self.play(Create(i), run_time= 2.5)
            self.wait(2)
        self.wait(1)

        result = Tex("A right triangle is completely defined knowing the lengths of these sides.\n\nThat is, by fixing the lengths of the sides,\n\nthe angles are completely defined.").shift(DOWN * 1)

        self.play(FadeOut(VGroup(base_tex, height_tex, hypo_tex, c, d)))
        self.play(Write(result), run_time= 2)
        self.wait(4)


class determine_lengths_based_on_angles(Scene):
    def construct(self):
        statement = Title("Calculating lengths based on angles of triangle", font_size= 35, match_underline_width_to_text= True)
        # self.play(Write(statement), run_time= 1.5)
        # self.wait(2)

        # Angles
        alpha = MathTex(r"\alpha = 90 ^\circ", color= "#4681f0").shift(UP * 3 + LEFT * 5)
        beta = MathTex(r"\beta = 45 ^\circ", color= "#f04646").next_to(alpha, DOWN)
        gamma = MathTex(r"\gamma = 45 ^\circ", color= "#54f046").next_to(beta, DOWN)

        # Triangles
        # Triangle 1
        l11 = Line(start= np.array([0,0,0]), end=([1,0,0]))
        l12 = Line(start= np.array([0,0,0]), end=([0,1,0]))
        l13 = Line(start= l11.get_end(), end= l12.get_end())
        alpha1 = RightAngle(line1= l11, line2= l12, length= 0.2, color= "#4681f0")
        beta1 = Angle(line1 = l12.reverse_direction(), line2= l13.reverse_direction(), color= "#f04646")
        l12.reverse_direction()
        l13.reverse_direction()
        gamma1 = Angle(line1= l13, line2= l11.reverse_direction(), color= "#54f046")
        l11.reverse_direction()

        t1 = VGroup(alpha1, beta1, gamma1, l11,l12,l13).shift(DOWN * 3 + LEFT * 6)
        
        # Triangle 2
        l21 = Line(start= np.array([0,0,0]), end=([3,0,0]))
        l22 = Line(start= np.array([0,0,0]), end=([0,3,0]))
        l23 = Line(start= l21.get_end(), end= l22.get_end())
        alpha2 = RightAngle(line1= l21, line2= l22, color= "#4681f0")
        beta2 = Angle(line1 = l22.reverse_direction(), line2= l23.reverse_direction(), color= "#f04646")
        l22.reverse_direction()
        l23.reverse_direction()
        gamma2 = Angle(line1= l23, line2= l21.reverse_direction(), color= "#54f046")
        l21.reverse_direction()
        t2 = VGroup(alpha2, beta2, gamma2,l21,l22,l23).shift(DOWN * 3 + RIGHT * 4)

        # Triangle with Value Tracker
        t = ValueTracker(2)
        lv1 = always_redraw(lambda : Line(start= np.array([-1,l11.get_y(),0]), end= np.array([-1+t.get_value(),l11.get_y(),0])))
        lv2 = always_redraw(lambda : Line(start= np.array([-1,l11.get_y(),0]), end= np.array([-1,t.get_value()+l11.get_y(),0])))
        lv3 = always_redraw(lambda : Line(start= lv1.get_end(), end= lv2.get_end()))
        alphav = always_redraw(lambda : RightAngle(line1= lv1, line2= lv2, color= "#4681f0"))
        betav = always_redraw(lambda : Angle(line1 = lv2.reverse_direction(), line2= lv3.reverse_direction(), color= "#f04646"))
        gammav = always_redraw(lambda : Angle(line1= lv3.reverse_direction(), line2= lv1.reverse_direction(), color= "#54f046"))
        tv = VGroup(lv1,lv2,lv3)


        self.play(Write(VGroup(alpha, beta, gamma)), run_time= 2)
        self.wait(2)
        self.play(Create(t1), run_time= 1.5)
        self.wait(2)
        self.play(Create(t2), run_time= 1.5)
        self.wait(2)
        self.play(Create(tv), run_time= 1.5)
        self.add(alphav, betav, gammav)
        self.bring_to_front(lv1,lv2,lv3)
        self.wait(2)
        self.play(t1.animate.shift(RIGHT * 5), run_time= 2)
        self.play(t.animate.increment_value(-1), run_time=3)
        self.play(t1.animate.shift(LEFT * 4), t.animate.increment_value(1), run_time= 2)
        self.play(t2.animate.shift(LEFT * 5), run_time= 2)
        self.play(t.animate.increment_value(1), run_time= 4)
        self.wait(2)
        self.play(t2.animate.shift(RIGHT * 5), t.animate.increment_value(-1), run_time= 2)
        self.wait(1)

        result = Tex("A right triangle cannot be fully defined\n\nknowing only its angles but all triangles with the\n\nsame angles have proportional side lengths.", font_size= 25).shift(RIGHT * 3 + UP * 2)
        self.play(Write(result))
        self.wait(4)

from manim import *

class VarySides(Scene):
    def construct(self):
        # Defining Triangle
        """
              b
              |\ alpha
              | \
        ab_t  |  \
              |   \
              |____\ beta
              a    c
               ac_t
        """
        ab_T = ValueTracker(5)
        ac_T = ValueTracker(2)
        ab = always_redraw(lambda : Line(start= np.array([2.3,-2,0]), end= np.array([2.3,ab_T.get_value() -2,0])))
        ac = always_redraw(lambda : Line(start= np.array([2.3,-2,0]), end= np.array([2.3+ac_T.get_value(), -2,0])))
        bc = always_redraw(lambda : Line(start= ab.get_end(), end= ac.get_end()))

        # Defining Angles
        beta = always_redraw(lambda : Angle(line1= ab.reverse_direction(), line2= bc.reverse_direction()))
        alpha = always_redraw(lambda : Angle(line1= bc.reverse_direction(), line2= ac.reverse_direction()))

        # Labels on Triangle
        MathTex.set_default(font_size= 35)
        a = always_redraw(lambda : MathTex("A").next_to(ab.get_end(), LEFT+DOWN, buff= 0.1))
        b = always_redraw(lambda : MathTex("B").next_to(ab.get_start(), LEFT+UP, buff= 0.1))
        c = always_redraw(lambda : MathTex("C").next_to(ac.get_start(), RIGHT+DOWN, buff= 0.1))
        alpha_tex = always_redraw(lambda : MathTex(r"\alpha").next_to(alpha.get_center(), UP+RIGHT, buff= 0.2))
        beta_tex = always_redraw(lambda : MathTex(r"\beta").next_to(beta.get_center(), UP+RIGHT, buff= 0.2))

        # VGrouping all
        triangle = VGroup(ab, ac, bc, alpha, beta, a, b, c, alpha_tex, beta_tex)

        # Writings
        MathTex.set_default(font_size= 25)
        sina = always_redraw(lambda : MathTex(
            r"sin(\alpha) = \frac{opposite}{hypotenuse} = \frac{AB}{BC} = ",
            "\\frac{{  {}  }}{{  {}  }} = {{  {}  }}".format( round(ab.get_length(),2), round(bc.get_length(),2), round(ab.get_length()/bc.get_length(),2) ),
            r" = cos(\beta)"
        ).to_corner(LEFT).shift(UP*1))
        cosa = always_redraw(lambda : MathTex(
            r"cos(\alpha) = \frac{adjacent}{hypotenuse} = \frac{AC}{BC} = ",
            "\\frac{{  {}  }}{{  {}  }} = {{  {}  }}".format( round(ac.get_length(),2), round(bc.get_length(),2), round(ac.get_length()/bc.get_length(),2) ),
            r"= sin(\beta)"
        ).next_to(sina, DOWN, buff= 0.3, aligned_edge= LEFT))
        tana = always_redraw(lambda : MathTex(
            r"tan(\alpha) = \frac{opposite}{adjacent} = \frac{AB}{AC} =",
            "{}".format(round(ac.get_length()/ab.get_length(),2))
        ).next_to(cosa, DOWN, buff= 0.3, aligned_edge= LEFT))
        
        self.play(Create(triangle))
        self.wait(1)
        self.play(Write(VGroup(sina, cosa, tana)), run_time= 2)
        self.wait(1)
        self.play(ab_T.animate.increment_value(-4.9999), run_time= 5)
        self.wait(3)
        self.play(ab_T.animate.increment_value(4.9999), run_time= 1)
        self.wait(1.5)
        self.play(ac_T.animate.increment_value(-1.9999), run_time= 5)
        self.wait(3)
        self.play(ac_T.animate.increment_value(1.9999), run_time= 1)
        self.wait(1.5)


class UnitCircle(Scene):
    def construct(self):
        # Unit Circle
        MathTex.set_default(font_size= 13)
        axes = Axes(x_range= [-1,1], y_range= [-1,1], x_length= 6, y_length= 6, tips=False)
        x_points = list(map(MathTex, [r"-\frac{1}{2}", r"-\frac{\sqrt{2}}{2}", r"-\frac{\sqrt{3}}{2}", r"\frac{1}{2}", r"\frac{\sqrt{2}}{2}", r"\frac{\sqrt{3}}{2}"]))
        x_points = VGroup(*x_points)
        y_points = x_points.copy()
        y_points = VGroup(*y_points)
        x_axes_lines = list()
        y_axes_lines = list()
        n=0
        Line.set_default(stroke_width= 1)
        for j in range(1,3): 
            for i in [1/2, np.sqrt(2)/2, np.sqrt(3)/2]:
                i = i * ((-1)**j)
                x_points[n].move_to(axes.c2p(i,-0.1,0))
                y_points[n].move_to(axes.c2p(-0.06,i,0))
                tmp = Line(start= axes.c2p(i,-0.025,0), end= axes.c2p(i,0.025,0))
                x_axes_lines.append(tmp)
                tmp = Line(start= axes.c2p(-0.025,i,0), end= axes.c2p(0.025,i,0))
                y_axes_lines.append(tmp)    
                n = n + 1
        x_points = VGroup(*x_points)
        x_axes_lines = VGroup(*x_axes_lines)
        y_axes_lines = VGroup(*y_axes_lines)
        
        xn = 0
        yn = 0
        for j in range(1,3):
            if j == 1:
                sign = 1
            else:
                sign = -1

            for i in [0.15, 0.2, 0.2]:
                x_points[xn].shift(LEFT * (i*sign))
                xn = xn + 1
            for i in range(3):
                y_points[yn].shift(DOWN * (0.2 * sign))
                yn = yn + 1

        self.play(Create(VGroup(axes, x_points, y_points, x_axes_lines, y_axes_lines)))

        
        TrigCircle = ParametricFunction(lambda t: axes.c2p(np.cos(t), np.sin(t)), t_range= [0,2*PI])
        
        angles = list(map(MathTex, [
            r"0",
            r"\frac{\pi}{6}",
            r"\frac{\pi}{3}",
            r"\frac{\pi}{2}",
            r"\frac{2\pi}{3}",
            r"\frac{5\pi}{6}",
            r"\pi",
            r"-\frac{5\pi}{6}",
            r"\frac{-2\pi}{3}",
            r"\frac{-\pi}{2}",
            r"\frac{-\pi}{3}",
            r"\frac{-\pi}{6}",
        ]))
        angles45 = list(map(MathTex, [
            r"\frac{\pi}{4}",
            r"\frac{3\pi}{4}",
            r"\frac{-3\pi}{4}",
            r"\frac{-\pi}{4}"
        ]))

        self.play(Create(VGroup(axes, TrigCircle)))
        for i in range(0,len(angles)):
            angles[i].move_to(axes.c2p(1.1*np.cos(PI/6 * i),1.1*np.sin(PI/6 * i)))
            self.play(Write(angles[i]), run_time= 0.5)
        for i in range(0, len(angles45)):
            angles45[i].move_to(axes.c2p(1.1*np.cos((PI/2 * i) + PI/4),1.1*np.sin((PI/2 * i) + PI/4)))
            self.play(Write(angles45[i]), run_time= 0.5)
        angles = VGroup(*angles)
        self.add(TrigCircle, angles)

        t = ValueTracker(0)
        Line.set_default(color= "#03fc1c", stroke_width= 2)
        horizontal_line_0 = always_redraw(lambda : Line(start= axes.c2p(0,0,0), end= axes.c2p(np.cos(t.get_value()),0,0)))
        horizontal_line_t = always_redraw(lambda : Line(start= axes.c2p(0,np.sin(t.get_value()),0), end= axes.c2p(np.cos(t.get_value()),np.sin(t.get_value()),0)))
        vertical_line_0 = always_redraw(lambda : Line(start= axes.c2p(0,0,0), end= axes.c2p(0,np.sin(t.get_value()),0)))
        vertical_line_t = always_redraw(lambda : Line(start= axes.c2p(np.cos(t.get_value()),0,0), end= axes.c2p(np.cos(t.get_value()),np.sin(t.get_value()),0)))
        hypo = always_redraw(lambda : Line(start= axes.c2p(0,0,0), end= axes.c2p(np.cos(t.get_value()),np.sin(t.get_value()),0) ))

        self.play(Create(VGroup(horizontal_line_0, horizontal_line_t, vertical_line_0, vertical_line_t, hypo)))

        pre = 0
        colors = ["#fc1c03", "#f0fc03", "#0362fc", "#03fc1c"]
        for j in range(4):
            if j % 2 == 0:
                    n = 0
            else:
                    n = 2
            for i in [PI/6, PI/12, PI/12, PI/6]:
                self.play(t.animate.increment_value(i), run_time= 3, rate_func=rate_functions.linear)
                self.wait(2)

                pre = pre + i
                self.add(
                    Line(start= axes.c2p(0,np.sin(pre),0), end= axes.c2p(np.cos(pre),np.sin(pre),0), color= colors[n]),
                    Line(start= axes.c2p(np.cos(pre),0,0), end= axes.c2p(np.cos(pre),np.sin(pre),0), color= colors[n]),
                    Line(start= axes.c2p(0,0,0), end= axes.c2p(np.cos(t.get_value()),np.sin(t.get_value()),0), color= colors[n])
                )
                if j % 2 == 0:
                    n = n + 1
                else:
                    n = n - 1

        self.wait(5)
