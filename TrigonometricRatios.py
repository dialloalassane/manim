from manim import *

class TrigonometricRatios(Scene):
    def construct(self):
        l1 = Line(start= np.array([0,0,0]), end= np.array([3,0,0]))
        l2 = Line(start= l1.get_start(), end= np.array([0,3,0]))
        l3 = Line(start= l1.get_end(), end= l2.get_end())
        alpha = RightAngle(line1= l1, line2= l2)
        theta = Angle(line1= l3, line2= l1.reverse_direction())
        theta_tex = MathTex(r"\theta", font_size= 35).next_to(theta, LEFT, buff= 0.1).shift(UP * 0.1)
        l1.reverse_direction()
        beta = Angle(line1= l2.reverse_direction(), line2= l3.reverse_direction())
        beta_tex = MathTex(r"\beta", font_size= 35).next_to(beta, DOWN, buff= 0.1).shift(RIGHT * 0.1)
        triangle = VGroup(alpha,beta,theta,theta_tex,beta_tex,l1,l2,l3).shift(RIGHT * 3 + DOWN * 1)

        self.play(Create(triangle), run_time= 1)
        self.wait(1)

        MathTex.set_default(font_size= 30)
        trigRatios = MathTex("Trigonometric Ratios").to_edge(UL)
        sin = MathTex(r"Ratio\ 1:\ sinus(\theta) = \frac{opposite}{hypotenuse}").next_to(trigRatios, DOWN, aligned_edge= LEFT)
        cos = MathTex(r"Ratio\ 2:\ cosin(\theta) = \frac{adjacent}{hypotenuse}").next_to(sin, DOWN, aligned_edge= LEFT)
        tan = MathTex(r"Ratio\ 3:\ tangent(\theta) = \frac{opposite}{adjacent}").next_to(cos, DOWN, aligned_edge= LEFT)
        cosec = MathTex(r"Ratio\ 4:\ cosec(\theta) = \frac{hypotenuse}{opposite}").next_to(tan, DOWN, aligned_edge= LEFT)
        sec = MathTex(r"Ratio\ 5:\ sec(\theta) = \frac{hypotenuse}{adjacent}").next_to(cosec, DOWN, aligned_edge= LEFT)
        cotan = MathTex(r"Ratio\ 6:\ cotan(\theta) = \frac{hypotenuse}{adjacent}").next_to(sec, DOWN, aligned_edge= LEFT)

        sin[0][16:len(sin[0])].set_color(BLACK)
        cos[0][16:len(cos[0])].set_color(BLACK)
        tan[0][18:len(tan[0])].set_color(BLACK)
        cosec[0][16:len(cosec[0])].set_color(BLACK)
        cosec[0][26].set_color(WHITE)
        sec[0][14:len(sec[0])].set_color(BLACK)
        sec[0][-9].set_color(WHITE)
        cotan[0][16:len(cotan[0])].set_color(BLACK)
        cotan[0][-9].set_color(WHITE)

        self.play(Write(sin))
        self.play(ReplacementTransform(l1.copy(), sin[0][16:24].copy().set_color(WHITE)),
            Write(sin[0][24].copy().set_color(WHITE)),
            ReplacementTransform(l3.copy(), sin[0][25:len(sin[0])].copy().set_color(WHITE)),
            run_time= 2
        )
        self.wait(2)
        self.play(Write(cos))
        self.play(ReplacementTransform(l2.copy(), cos[0][16:24].copy().set_color(WHITE)),
            Write(cos[0][24].copy().set_color(WHITE)),
            ReplacementTransform(l3.copy(), cos[0][25:len(sin[0])].copy().set_color(WHITE)),
            run_time= 2
        )
        self.wait(2)
        self.play(Write(tan))
        self.play(ReplacementTransform(l1.copy(), tan[0][18:26].copy().set_color(WHITE)),
            Write(tan[0][26].copy().set_color(WHITE)),
            ReplacementTransform(l2.copy(), tan[0][27:len(sin[0])].copy().set_color(WHITE)),
            run_time= 2
        )
        self.wait(2)
        self.play(Write(cosec))
        self.play(sin[0][25:len(sin[0])].copy().set_color(WHITE).animate.move_to(cosec[0][-18:-9]),
            sin[0][16:24].copy().set_color(WHITE).animate.move_to(cosec[0][-8:-1].get_center())
        )
        self.play(Write(sec))
        self.play(cos[0][25:len(sin[0])].copy().set_color(WHITE).animate.move_to(sec[0][-18:-9]),
            cos[0][16:24].copy().set_color(WHITE).animate.move_to(sec[0][-8:-1].get_center())
        )
        self.play(Write(cotan))
        self.play(tan[0][18:26].copy().set_color(WHITE).animate.move_to(cotan[0][-18:-9]),
            tan[0][27:len(sin[0])].copy().set_color(WHITE).animate.move_to(cotan[0][-8:-1].get_center())
        )
        self.wait(1)

        sinb = MathTex(r"= sin(\beta)").next_to(sin, RIGHT, buff= 0.25)
        cosb = MathTex(r"= cos(\beta)").next_to(cos, RIGHT, buff= 0.25)

        self.play(Write(sinb))
        self.wait(1)
        self.play(Write(cosb))
        self.wait(5)
        self.clear()

        # # 
        self.play(Create(triangle))
        Tex.set_default(font_size= 25)
        notice = Tex("We can completely define a right\n\ntriangle by knowing one of the\n\n angles and the lengthof one side.\n\nFor example, if we know the angle beta\n\nin the figure below, and the length of the\n\nopposite side, we can do the following\n\nto define the lengths of the other\n\nsides of the triangle:").to_edge(UL)
        step1 = MathTex(r"sin(\beta) = \frac{opposite}{hypotenuse}").next_to(notice, DOWN)
        step2 = MathTex(r"hypotenuse = \frac{opposite}{sin(\beta)}").next_to(step1, DOWN)
        step3 = MathTex(r"tan(\beta) =\frac{opposite}{adjacent}").next_to(step2, DOWN)
        step4 = MathTex(r"adjacent =\frac{opposite}{tan(\beta)}").next_to(step3, DOWN)
        
        self.play(Write(notice))
        self.wait(1)
        self.play(Write(step1), run_time= 1.5)
        self.wait(2)
        self.play(Write(step2), run_time= 1.5)
        self.wait(2)
        self.play(Write(step3), run_time= 1.5)
        self.wait(2)
        self.play(Write(step4), run_time= 1.5)
        self.wait(5)
        self.clear()

        # Calculating Values of sin, cos
        data = Tex("Right Triangle whoes two sides are 1, with an angle of 45 \n\nwe can deduce the sines and cosines of this angle.").to_edge(UL).shift(DOWN * 1)
        triangle.shift(LEFT * 1)
        adj = MathTex("1").next_to(l2, LEFT)
        opp = MathTex("1").next_to(l1, DOWN)
        hypo = MathTex(r"\sqrt{1^2 + 1^2}=\sqrt{2}").next_to(l3.get_center(), RIGHT, buff= -0.5).rotate(l3.get_angle())
        beta_val = MathTex(r"30 ^\circ").move_to(beta_tex.get_center())
        triangle.remove(beta_tex)
        triangle.add(beta_val)
        sin = MathTex(r"sine = \frac{opposite}{hypotenuse} = \frac{1}{\sqrt{2}}").next_to(data, DOWN, aligned_edge= LEFT)
        cos = MathTex(r"cosin = \frac{adjacent}{hypotenuse} = \frac{1}{\sqrt{2}}").next_to(sin, DOWN, aligned_edge= LEFT)
        tan = MathTex(r"tan = \frac{opposite}{adjacent} = 1").next_to(cos, DOWN, aligned_edge= LEFT)

        # Equilateral Triangle
        le1 = Line(start= np.array([-2,0,0]), end= np.array([2,0,0]))
        le2 = Line(start= le1.get_start(), end= np.array([0,2,0]))
        le3 = Line(start= le1.get_end(), end= le2.get_end())
        te_s1 = MathTex("1").next_to(le1, DOWN)
        te_s2 = MathTex("1").next_to(le2.get_center(), LEFT, buff= 0.3)
        te_s3 = MathTex("1").next_to(le3.get_center(), RIGHT, buff= 0.3)
        te = VGroup(le1, le2, le3)

        leh1 = Line(start= np.array([0,0,0]), end= np.array([2,0,0]))
        leh2 = Line(start= np.array([0,0,0]), end= np.array([0,2,0]))
        leh3 = Line(start= leh1.get_end(), end= leh2.get_end())
        teh_opp = MathTex(r"\frac{1}{2}").next_to(leh1, DOWN)
        # Calculating adjacent side
        adj_cal = MathTex(r"adjacent = \sqrt{hypotenuse^2 - opposite^2}").to_corner(LEFT)
        adj_cal1 = MathTex(r"= \sqrt{1-\frac{1}{4}}= \sqrt{\frac{3}{4}}").next_to(adj_cal, DOWN, aligned_edge= LEFT)
        teh_adj = MathTex(r"\sqrt{\frac{3}{4}}").next_to(leh2.get_center(), LEFT, buff= 0.3)
        teh_hypo = MathTex("1").next_to(leh3.get_center(), RIGHT, buff= 0.3)
        teh = VGroup(leh1, leh2, leh3, teh_hypo)

        # at 30 degree
        sin30 = MathTex(r"sine(30^\circ) = \frac{opposite}{hypotenuse} = \frac{1}{2}").to_corner(LEFT).shift(UP*1.5)
        cos30 = MathTex(r"cosin(30^\circ) = \frac{adjacent}{hypotenuse} = \frac{3}{4}").next_to(sin30, DOWN, aligned_edge= LEFT)
        tan30 = MathTex(r"tan(30^\circ) = \frac{opposite}{adjacent} = \frac{3}{4}").next_to(cos30, DOWN, aligned_edge= LEFT)

        self.play(Write(data), run_time= 2)
        self.wait(2)
        self.play(Create(triangle), run_time= 1.5)
        self.wait(1)
        self.play(Write(VGroup(adj, opp)))
        self.wait(1)
        self.play(Write(hypo))
        self.wait(1)
        self.play(Write(sin))
        self.wait(1)
        self.play(Write(cos))
        self.wait(1)
        self.play(Write(tan))
        self.wait(4)
        self.clear()
        self.wait(2)
        self.play(Create(te), run_time= 1.5)
        self.play(Write(VGroup(te_s1, te_s2, te_s3)))
        self.wait(2)
        self.play(Create(teh), run_time= 1.5)
        self.bring_to_front(teh)
        self.wait(1)
        self.play(FadeOut(te, te_s2, te_s3), ReplacementTransform(te_s1, teh_opp))
        self.wait(1)
        self.play(Write(adj_cal), run_time= 2)
        self.wait(2)
        self.play(Write(adj_cal1), run_time= 2)
        self.wait(2)
        self.play(Write(teh_adj), run_time= 2)
        self.wait(1.5)
        teh.add(teh_opp, teh_adj, teh_hypo)
        self.play(teh.animate.shift(RIGHT * 3), FadeOut(VGroup(adj_cal, adj_cal1)))
        self.wait(1)
        self.play(Write(sin30), run_time= 2)
        self.wait(1)
        self.play(Write(cos30), run_time= 2)
        self.wait(1)
        self.play(Write(tan30), run_time= 2)
        self.wait(4)
