from manim import *

class RightTriangle(VMobject):
    def __init__(self, base, height):
        super().__init__()
        l1 = Line(start= np.array([0,0,0]), end= np.array([base,0,0]))
        l2 = Line(start= np.array([0,0,0]), end= np.array([0,height,0]))
        l3 = Line(start= l1.get_end(), end= l2.get_end())
        Angle.set_default(color= "#34eb37")
        alpha = RightAngle(line1= l1, line2= l2)
        beta = Angle(line1= l3, line2= l1.reverse_direction())
        l1.reverse_direction()
        gamma = Angle(line1= l2.reverse_direction(), line2= l3.reverse_direction())
        l2.reverse_direction()
        l3.reverse_direction()
        t = VGroup(alpha,beta,gamma,l1,l2,l3)
        self.become(t)
        
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.t = t
    
    def add_side_lens(self):
        MathTex.set_default(font_size= 35, color= WHITE)
        base_tex = MathTex(f"{round(self.l1.get_length(),2)}").next_to(self.l1, DOWN)
        height_tex = MathTex(f"{round(self.l2.get_length(),2)}").next_to(self.l2, LEFT)
        hypo_tex = MathTex(f"{round(self.l3.get_length(),2)}").rotate(self.l3.get_angle()+PI).next_to(self.l3.get_center(), RIGHT)

        self.add(base_tex, height_tex, hypo_tex)

    def add_angles(self):
        MathTex.set_default(font_size= 35, color= "#34eb37")
        alpha_tex = MathTex(rf"90 ^\circ").next_to(self.alpha, DL)
        beta_tex = MathTex(rf"{round(np.rad2deg(self.beta.get_value()),2)} ^\circ").next_to(self.beta, DR)
        gamma_tex = MathTex(rf"{round(np.rad2deg(self.gamma.get_value()),2)} ^\circ").next_to(self.gamma, UP * 1.4)


        self.add(alpha_tex, beta_tex, gamma_tex)
    
    def get_base(self):
        return self.l1.get_length()
    def get_height(self):
        return self.l2.get_length()
    def get_hypo(self):
        return self.l3.get_length()


class Determine_Angle_based_on_side_lengths(Scene):
    def construct(self):
        Tex.set_default(font_size= 35)
        statement = Title("Calculating angles based on side lengths of triangle", font_size= 35, match_underline_width_to_text= True)
        self.play(Write(statement))
        self.wait(2)
        self.play(FadeOut(statement))

        a = RightTriangle(base=2, height=2)
        b = RightTriangle(base=2.5, height=1.5)
        c = RightTriangle(base=1, height=3)
        d = RightTriangle(base= 2, height= 2.2)

        for i in [a, b, c, d]:
            i.add_angles()
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
        hypo_tex = always_redraw(lambda : MathTex(f"Hypotenuse= {hypo}").next_to(height_tex, DOWN))

        self.play(Write(VGroup(base_tex, height_tex, hypo_tex)), run_time= 2)

        for i in [a,b,c,d]:
            base = i.get_base()
            height = i.get_height()
            hypo = i.get_hypo()
            self.wait(1)
            self.play(Create(i), run_time= 2.5)
            self.wait(2)
        self.wait(1)

        result = Tex("A right triangle is completely defined knowing the lengths of these sides.\n\nThat is, by fixing the lengths of the sides,\n\nthe angles are completely defined.").shift(DOWN * 1)

        self.play(FadeOut(VGroup(base_tex, height_tex, hypo_tex, c, d)))
        self.play(Write(result), run_time= 2)
        self.wait(4)
