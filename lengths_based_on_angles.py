from manim import *

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
