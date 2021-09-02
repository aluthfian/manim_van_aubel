class vanAubel_1(Scene): 
    def construct(self): 
        Line_BA = Line(start=[-4.5,-3,0], end=[0.5,3,0]) 
        m_BA = Line_BA.get_slope() 
        Line_AC = Line(start=Line_BA.get_end(), end=[5.0,-3,0]) 
        m_AC = Line_AC.get_slope() 
        Line_CB = Line(start=Line_AC.get_end(), end=Line_BA.get_start()) 
        m_CB = Line_CB.get_slope() 
         
        Text_A = Text('A').next_to(Line_BA.get_end(), UP) 
        Text_B = Text('B').next_to(Line_CB.get_end(), DOWN) 
        Text_C = Text('C').next_to(Line_AC.get_end(), DOWN) 
         
        self.play(Create(VGroup().add(*[Line_BA, Line_AC, Line_CB, Text_A, Text_B, Text_C]))) 
         
        Point_C1_x = np.random.uniform(low=Line_BA.get_start()[0]+2.5, high=Line_BA.get_end()[0]-2.5, size=(1,)) 
        Point_B1_x = np.random.uniform(low=Line_AC.get_start()[0]+2.5, high=Line_AC.get_end()[0]-2.5, size=(1,)) 
         
         
        Point_C1_y = m_BA*(Point_C1_x - Line_BA.get_start()[0]) + Line_BA.get_start()[1] 
        Point_B1_y = m_AC*(Point_B1_x - Line_AC.get_start()[0]) + Line_AC.get_start()[1] 
         
        Point_C1 = np.array([Point_C1_x[0],Point_C1_y[0],0], dtype='float64') 
        Point_B1 = np.array([Point_B1_x[0],Point_B1_y[0],0], dtype='float64') 
        Point_M = line_intersection([Point_C1, Line_AC.get_end()], 
                                     [Line_CB.get_end(), Point_B1]).flatten() 
        Point_A1 = line_intersection([Line_BA.get_end(), Point_M], 
                                     [Line_CB.get_start(), Line_CB.get_end()]).flatten() 
        
        Line_CC1 = DashedLine(start=Line_AC.get_end(), end=Point_C1) 
        Line_BB1 = DashedLine(start=Line_CB.get_end(), end=Point_B1) 
        Line_AA1 = DashedLine(start=Line_BA.get_end(), end=Point_A1)
        
        Text_A1 = Tex("$A_1$").next_to(Line_AA1.get_end(), DOWN) 
        Text_B1 = Tex("$B_1$").next_to(Line_BB1.get_end(), RIGHT) 
        Text_C1 = Tex("$C_1$").next_to(Line_CC1.get_end(), LEFT)
        Text_M = Tex("$M$", color=PURE_GREEN).next_to(Point_M, UP)
        bg_text_M = BackgroundRectangle(Text_M, color=BLACK, fill_opacity=1.0)
        dot_M = Dot(Point_M, color=PURE_GREEN)
        
        self.play(Create(VGroup().add(*[Line_CC1, Line_BB1, Line_AA1, Text_A1, Text_B1, Text_C1, bg_text_M, dot_M, Text_M])),
                 run_time=1.0)
        self.wait(3)
        
        Text_title = Text("Teorema Van Aubel \n pada segitiga:").to_edge(UP+LEFT).scale(0.75)
        Van_Aubel_text = r'{ {|MA|} \over{ {|MA_1|} } } = { {|AC_1|} \over{ {|BC_1|} } } + { {|AB_1|} \over{ {|CB_1|} } }'
        Van_Aubel_form_1 = MathTex(r'{ {|MA|} \over{ {|MA_1|} } } =').move_to(Text_title.get_corner(DL)+[0.75,-0.75,0]).scale(0.75)
        Van_Aubel_form_1.substrings_to_isolate=[r"MA", r"MA_1"]
        Van_Aubel_form_1.set_color_by_tex(r"MA", BLUE_D)
        Van_Aubel_form_1.set_color_by_tex(r"MA_1", BLUE_B)
        Van_Aubel_form_2 = MathTex(r'{ {|AC_1|} \over{ {|BC_1|} } }').next_to(Van_Aubel_form_1, RIGHT, buff=0).scale(0.75)
        Van_Aubel_form_2.substrings_to_isolate = [r"AC_1", r"BC_1"]
        Van_Aubel_form_2.set_color_by_tex(r"AC_1", RED_D)
        Van_Aubel_form_2.set_color_by_tex(r"BC_1", RED_B)
        Van_Aubel_form_3 = MathTex(r'+ { {|AB_1|} \over{ {|CB_1|} } }').next_to(Van_Aubel_form_2, RIGHT, buff=0).scale(0.75)
        Van_Aubel_form_3.substrings_to_isolate = [r"AB_1", r"CB_1"]
        Van_Aubel_form_3.set_color_by_tex(r"AB_1", GOLD_D)
        Van_Aubel_form_3.set_color_by_tex(r"CB_1", GOLD_B)
        
        Line_MA = Line(start=Point_M, end=Line_BA.get_end(), color=BLUE_D) 
        Line_MA1 = Line(start=Point_A1, end=Point_M, color=BLUE_B) 
        Line_AC1 = Line(start=Line_BA.get_end(), end=Point_C1, color=RED_D) 
        Line_BC1 = Line(start=Line_BA.get_start(), end=Point_C1, color=RED_B)
        Line_AB1 = Line(start=Line_AC.get_start(), end=Point_B1, color=GOLD_D) 
        Line_CB1 = Line(start=Line_AC.get_end(), end=Point_B1, color=GOLD_B)
        
        self.play(Create(Text_title))
        self.wait()
        self.play(FadeIn(Van_Aubel_form_1))
        self.wait()
        self.play(Create(Line_MA))
        self.play(Create(Line_MA1))
        self.wait()
        self.play(FadeIn(Van_Aubel_form_2))
        self.wait()
        self.play(Create(Line_AC1))
        self.play(Create(Line_BC1))
        self.wait()
        self.play(FadeIn(Van_Aubel_form_3))
        self.wait()
        self.play(Create(Line_AB1))
        self.play(Create(Line_CB1))
        self.wait()
