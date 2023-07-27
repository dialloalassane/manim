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

class RightTriangle(VMobject):
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
    def get_corners(self):
        return [self.l1.get_start(), self.l2.get_end(), self.l1.get_end()]

class CustomRightTriangle(VMobject):
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
        t = VGroup(l1,l2,l3)
        self.become(t)
        
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.t = t

    def add_angles(self):
        self.add(self.alpha, self.beta, self.gamma)
    
    def add_side_lens(self):
        MathTex.set_default(font_size= 35, color= WHITE)
        base_tex = MathTex(f"{round(self.l1.get_length(),2)}").next_to(self.l1, DOWN)
        height_tex = MathTex(f"{round(self.l2.get_length(),2)}").next_to(self.l2, LEFT)
        hypo_tex = MathTex(f"{round(self.l3.get_length(),2)}").rotate(self.l3.get_angle()+PI).next_to(self.l3.get_center(), RIGHT)

        self.add(base_tex, height_tex, hypo_tex)

    def add_angles_tex(self):
        MathTex.set_default(font_size= 30, color= "#34eb37")
        alpha_tex = MathTex(rf"90 ^\circ").next_to(self.alpha, DL)
        beta_tex = MathTex(rf"{round(np.rad2deg(self.beta.get_value()),2)} ^\circ").next_to(self.beta, DR)
        gamma_tex = MathTex(rf"{round(np.rad2deg(self.gamma.get_value()),2)} ^\circ").next_to(self.gamma, UP * 1.5)

        self.add(alpha_tex, beta_tex, gamma_tex)
    
    # Getters
    # Get Any side
    def get_base(self):
        return self.l1
    def get_height(self):
        return self.l2
    def get_hypo(self):
        return self.l3
    def get_side(self):
        return [self.l1, self.l2, self.l3]

    # Get side lengths
    def get_base_length(self):
        return self.l1.get_length()
    def get_height_length(self):
        return self.l2.get_length()
    def get_hypo_length(self):
        return self.l3.get_length()

    # Get Corner
    def get_corners(self):
        return [self.l1.get_start(), self.l2.get_end(), self.l1.get_end()]
    
    # Get angles
    def get_alpha(self):
        return self.alpha
    def get_beta(self):
        return self.beta
    def get_gamma(self):
        return self.gamma
