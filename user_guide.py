from customtkinter import *


class UserGuide():
    def userGuide1(self):
        # self.clear_frame()
        self.guide1_line1 = CTkLabel(self.settings_frame, text="Main Interface", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide1_line1.place(relx=0.05, rely=0.08, anchor="w")
        self.guide1_line2 = CTkLabel(self.settings_frame, text="Overview", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",22,"bold") , text_color="#6965A3", wraplength=380)
        self.guide1_line2.place(relx=0.05, rely=0.16, anchor="w")
        
        self.guide1_line3 = CTkLabel(self.settings_frame, text="Dashboard: View functions of sections", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide1_line3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
    def userGuide2(self):
        self.guide2_line1 = CTkLabel(self.settings_frame, text="Navigation", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide2_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide2_line2 = CTkLabel(self.settings_frame, text="Use the sidebar to switch between different sections and click on the desired section to view or edit its content", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide2_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
    def userGuide3(self):   
        self.guide3_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide3_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide3_line2 = CTkLabel(self.settings_frame, text="Allocate Income", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline= True) , text_color="#6965A3", wraplength=380)
        self.guide3_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.guide3_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Edit Budget\" button in the sidebar", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line3.grid(row=2, column=0, padx=10, pady=(0,5), sticky="w")
        
        self.guide3_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Set Income\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.guide3_line5 = CTkLabel(self.settings_frame, text="3. Enter the Year and select the Month( Make sure to update both to confirm selection ) ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line5.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.guide3_line6 = CTkLabel(self.settings_frame, text="4. Enter allocated income and click on \"Save ALL\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line6.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        
    def userGuide4(self):
        self.guide4_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide4_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide4_line2 = CTkLabel(self.settings_frame, text="Creating a Budget for Categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline= True) , text_color="#6965A3", wraplength=380)
        self.guide4_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.guide4_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Edit Budget\" button in the sidebar", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line3.grid(row=2, column=0, padx=10, pady=(0,5), sticky="w")
        
        self.guide4_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Set Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.guide4_line5 = CTkLabel(self.settings_frame, text="3. Select the Year, Month ( Make sure to update both to confirm selection ) and category of your choice ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line5.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.guide4_line6 = CTkLabel(self.settings_frame, text="4. Enter allocated budget and click on \"Save\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line6.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
    def userGuide5(self):
        self.guide5_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide5_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide5_line2 = CTkLabel(self.settings_frame, text="Updating Expenses ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide5_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide5_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Update Expenses\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide5_line4 = CTkLabel(self.settings_frame, text="2. Choose date, day and year", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide5_line5 = CTkLabel(self.settings_frame, text="3. Fill in the expenses used and select categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide5_line6 = CTkLabel(self.settings_frame, text="4. Add in a note (not required) and click \"Save Expenses\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
    
    def userGuide6(self):
        self.guide6_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide6_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide6_line2 = CTkLabel(self.settings_frame, text="View Expenses History", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide6_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide6_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Expenses History\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide6_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide6_line4 = CTkLabel(self.settings_frame, text="2. Select Month and Update OR search for any keywords in the search tab and click on \"search\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide6_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide7(self):
        self.guide7_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide7_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide7_line2 = CTkLabel(self.settings_frame, text="Expenses Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide7_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide7_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide7_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Expenses\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide7_line5 = CTkLabel(self.settings_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide7_line6 = CTkLabel(self.settings_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide8(self):
        self.guide8_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide8_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide8_line2 = CTkLabel(self.settings_frame, text="Income Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide8_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide8_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide8_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Income\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide8_line5 = CTkLabel(self.settings_frame, text="3. Select Year click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide8_line6 = CTkLabel(self.settings_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide9(self):
        self.guide9_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide9_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide9_line2 = CTkLabel(self.settings_frame, text="Usage of Budget Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide9_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide9_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide9_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Usage of Budget\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide9_line5 = CTkLabel(self.settings_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide9_line6 = CTkLabel(self.settings_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide10(self):
        self.guide10_line1 = CTkLabel(self.settings_frame, text="Advanced Features", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide10_line1.grid(row=0, column=0, padx=10, sticky="nsew")
    
        self.guide10_line2 = CTkLabel(self.settings_frame, text="Custom Categories ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide10_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Edit Budget\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide10_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Set Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line5 = CTkLabel(self.settings_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line6 = CTkLabel(self.settings_frame, text="4. Enter Custom categories in the entry for \"Add New Categories\" and Click on \"Save\" Button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line7 = CTkLabel(self.settings_frame, text="Colour Tag Categories ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide10_line7.grid(row=6, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line8 = CTkLabel(self.settings_frame, text="1. On the same page as the step above select categories in the frame with the words \"Set Colour Here\" ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line8.grid(row=7, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide10_line9 = CTkLabel(self.settings_frame, text="2. Select colour to be assigned to the selected categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line9.grid(row=8, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line10 = CTkLabel(self.settings_frame, text="3. Click on the \"Set Categories Colours\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line10.grid(row=9, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line11 = CTkLabel(self.settings_frame, text="4. The assigned colours will now be shown in the insights page", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line11.grid(row=10, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line12 = CTkLabel(self.settings_frame, text="Delete Categories ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide10_line12.grid(row=11, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line13 = CTkLabel(self.settings_frame, text="1. On the same page as the step above select categories in the frame with the words \"Delete Categories Here\" ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line13.grid(row=12, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide10_line14 = CTkLabel(self.settings_frame, text="2. Click on the \"Delete Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line14.grid(row=13, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line15 = CTkLabel(self.settings_frame, text="3. The category selected will now be deleted from the database", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line15.grid(row=14, column=0, padx=10,pady=5, sticky="w")