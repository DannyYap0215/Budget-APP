from customtkinter import *
from PIL import Image

main_icon = Image.open("icon/home_p.png")
navigate_icon = Image.open("icon/navigate_p.png")
income_icon = Image.open("icon/update_expenses_p.png")
budget_icon = Image.open("icon/budget_p.png")
expenses_icon = Image.open("icon/expenses_p.png")
expenses_history_icon = Image.open("icon/expenses_history_p.png")
expenses_insight_icon = Image.open("icon/expenses_insight_p.png")
income_insight_icon = Image.open("icon/income_p.png")
budget_usage_icon = Image.open("icon/usage_p.png")
category_icon =  Image.open("icon/category_p.png")
colour_label_icon =  Image.open("icon/colour_tag_P.png")
delete_icon = Image.open("icon/delete_p.png")

class UserGuide():
    def userGuide1(self):
        # self.clear_frame()
        main_interface_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(main_icon))
        main_interface_icon.place(relx=0.05, rely=0.08, anchor="w")
        self.guide1_line1 = CTkLabel(self.settings_frame, text="Main Interface", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide1_line1.place(relx=0.08, rely=0.08, anchor="w")
        self.guide1_line2 = CTkLabel(self.settings_frame, text="Overview", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide1_line2.place(relx=0.05, rely=0.14, anchor="w")
        
        self.guide1_line3 = CTkLabel(self.settings_frame, text="Dashboard: View functions of sections", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide1_line3.place(relx=0.05, rely=0.19, anchor="w")
        
        navigation_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(navigate_icon))
        navigation_icon.place(relx=0.05, rely=0.34, anchor="w")
        self.guide2_line1 = CTkLabel(self.settings_frame, text="Navigation", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide2_line1.place(relx=0.08, rely=0.34, anchor="w")
        
        self.guide2_line2 = CTkLabel(self.settings_frame, text="Use the sidebar to switch between different sections and click on the desired section to view or edit its content", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide2_line2.place(relx=0.05, rely=0.42, anchor="w")
        
    def userGuide3(self):   
        self.guide3_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide3_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        allocate_income_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(income_icon))
        allocate_income_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide3_line2 = CTkLabel(self.settings_frame, text="Allocate Income", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline= True) , text_color="#8885B6", wraplength=1020)
        self.guide3_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide3_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Edit Budget\" button in the sidebar", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide3_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide3_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Set Income\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30), text_color="#6965A3", wraplength=1020)
        self.guide3_line4.place(relx=0.05, rely=0.30, anchor="w")

        self.guide3_line5 = CTkLabel(self.settings_frame, text="3. Enter the Year and select the Month( Make sure to update both to confirm selection ) ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide3_line5.place(relx=0.05, rely=0.35, anchor="w")
        
        self.guide3_line6 = CTkLabel(self.settings_frame, text="4. Enter allocated income and click on \"Save ALL\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide3_line6.place(relx=0.05, rely=0.40, anchor="w")
        
        
    def userGuide4(self):
        self.guide4_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide4_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        creating_budget_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(budget_icon))
        creating_budget_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide4_line2 = CTkLabel(self.settings_frame, text="Creating a Budget for Categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline= True) , text_color="#8885B6", wraplength=1020)
        self.guide4_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide4_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Edit Budget\" button in the sidebar", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide4_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide4_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Set Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide4_line4.place(relx=0.05, rely=0.30, anchor="w")
        
        self.guide4_line5 = CTkLabel(self.settings_frame, text="3. Select the Year, Month ( Make sure to update both to confirm selection ) and category of your choice ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide4_line5.place(relx=0.05, rely=0.35, anchor="w")
        
        self.guide4_line6 = CTkLabel(self.settings_frame, text="4. Enter allocated budget and click on \"Save\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide4_line6.place(relx=0.05, rely=0.40, anchor="w")
        
    def userGuide5(self):
        self.guide5_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide5_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        update_expenses_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(expenses_icon))
        update_expenses_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide5_line2 = CTkLabel(self.settings_frame, text="Updating Expenses ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide5_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide5_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Update Expenses\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide5_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide5_line4 = CTkLabel(self.settings_frame, text="2. Choose date, day and year", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide5_line4.place(relx=0.05, rely=0.30, anchor="w")
        
        self.guide5_line5 = CTkLabel(self.settings_frame, text="3. Fill in the expenses used and select categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide5_line5.place(relx=0.05, rely=0.35, anchor="w")
        
        self.guide5_line6 = CTkLabel(self.settings_frame, text="4. Add in a note (not required) and click \"Save Expenses\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide5_line6.place(relx=0.05, rely=0.40, anchor="w")
    
    def userGuide6(self):
        self.guide6_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide6_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        view_expenses_history_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(expenses_history_icon))
        view_expenses_history_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide6_line2 = CTkLabel(self.settings_frame, text="View Expenses History", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide6_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide6_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Expenses History\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide6_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide6_line4 = CTkLabel(self.settings_frame, text="2. Select Month and Update OR search for any keywords in the search tab and click on \"search\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide6_line4.place(relx=0.05, rely=0.30, anchor="w")
        
    def userGuide7(self):
        self.guide7_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide7_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        view_expenses_insight_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(expenses_insight_icon))
        view_expenses_insight_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide7_line2 = CTkLabel(self.settings_frame, text="Expenses Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide7_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide7_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide7_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide7_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Expenses\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide7_line4.place(relx=0.05, rely=0.30, anchor="w")
        
        self.guide7_line5 = CTkLabel(self.settings_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide7_line5.place(relx=0.05, rely=0.35, anchor="w")
        
        self.guide7_line6 = CTkLabel(self.settings_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide7_line6.place(relx=0.05, rely=0.40, anchor="w")
        
    def userGuide8(self):
        self.guide8_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide8_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        view_income_insight_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(income_icon))
        view_income_insight_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide8_line2 = CTkLabel(self.settings_frame, text="Income Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide8_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide8_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide8_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide8_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Income\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide8_line4.place(relx=0.05, rely=0.30, anchor="w")
        
        self.guide8_line5 = CTkLabel(self.settings_frame, text="3. Select Year click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide8_line5.place(relx=0.05, rely=0.35, anchor="w")
        
        self.guide8_line6 = CTkLabel(self.settings_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide8_line6.place(relx=0.05, rely=0.40, anchor="w")
        
    def userGuide9(self):
        self.guide9_line1 = CTkLabel(self.settings_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",50,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide9_line1.place(relx=0.05, rely=0.08, anchor="w")
        
        usage_of_budget_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(budget_usage_icon))
        usage_of_budget_icon.place(relx=0.05, rely=0.18, anchor="w")
        self.guide9_line2 = CTkLabel(self.settings_frame, text="Usage of Budget Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",40,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide9_line2.place(relx=0.08, rely=0.18, anchor="w")
        
        self.guide9_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide9_line3.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide9_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Usage of Budget\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide9_line4.place(relx=0.05, rely=0.30, anchor="w")
        
        self.guide9_line5 = CTkLabel(self.settings_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide9_line5.place(relx=0.05, rely=0.35, anchor="w")
        
        self.guide9_line6 = CTkLabel(self.settings_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30) , text_color="#6965A3", wraplength=1020)
        self.guide9_line6.place(relx=0.05, rely=0.40, anchor="w")
        
    def userGuide10(self):
        self.guide10_line1 = CTkLabel(self.settings_frame, text="Advanced Features", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",45,"bold",underline=True) , text_color="#A7A5C9", wraplength=1020)
        self.guide10_line1.place(relx=0.05, rely=0.08, anchor="w")

        custom_category_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(category_icon))
        custom_category_icon.place(relx=0.05, rely=0.15, anchor="w")
        self.guide10_line2 = CTkLabel(self.settings_frame, text="Custom Categories ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide10_line2.place(relx=0.08, rely=0.15, anchor="w")
        
        self.guide10_line3 = CTkLabel(self.settings_frame, text="1. Click on the \"Edit Budget\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line3.place(relx=0.05, rely=0.20, anchor="w")
        
        self.guide10_line4 = CTkLabel(self.settings_frame, text="2. Click on the \"Set Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line4.place(relx=0.05, rely=0.25, anchor="w")
        
        self.guide10_line5 = CTkLabel(self.settings_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line5.place(relx=0.05, rely=0.30, anchor="w")
        
        self.guide10_line6 = CTkLabel(self.settings_frame, text="4. Enter Custom categories in the entry for \"Add New Categories\" and Click on \"Save\" Button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line6.place(relx=0.05, rely=0.35, anchor="w")
        
        colour_tag_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(colour_label_icon))
        colour_tag_icon.place(relx=0.05, rely=0.42, anchor="w")
        self.guide10_line7 = CTkLabel(self.settings_frame, text="Colour Tag Categories ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide10_line7.place(relx=0.08, rely=0.42, anchor="w")
        
        self.guide10_line8 = CTkLabel(self.settings_frame, text="1. On the same page as the step above select categories in the frame with the words \"Set Colour Here\" ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line8.place(relx=0.05, rely=0.47, anchor="w")

        self.guide10_line9 = CTkLabel(self.settings_frame, text="2. Select colour to be assigned to the selected categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line9.place(relx=0.05, rely=0.52, anchor="w")
        
        self.guide10_line10 = CTkLabel(self.settings_frame, text="3. Click on the \"Set Categories Colours\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line10.place(relx=0.05, rely=0.57, anchor="w")
        
        self.guide10_line11 = CTkLabel(self.settings_frame, text="4. The assigned colours will now be shown in the insights page", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line11.place(relx=0.05, rely=0.62, anchor="w")
        
        delete_category_icon = CTkLabel(self.settings_frame, text="", image= CTkImage(delete_icon))
        delete_category_icon.place(relx=0.05, rely=0.69, anchor="w")
        self.guide10_line12 = CTkLabel(self.settings_frame, text="Delete Categories ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30,underline=True) , text_color="#8885B6", wraplength=1020)
        self.guide10_line12.place(relx=0.08, rely=0.69, anchor="w")
        
        self.guide10_line13 = CTkLabel(self.settings_frame, text="1. On the same page as the step above select categories in the frame with the words \"Delete Categories Here\" ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line13.place(relx=0.05, rely=0.74, anchor="w")
        
        self.guide10_line14 = CTkLabel(self.settings_frame, text="2. Click on the \"Delete Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line14.place(relx=0.05, rely=0.79, anchor="w")
        
        self.guide10_line15 = CTkLabel(self.settings_frame, text="3. The category selected will now be deleted from the database", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",23) , text_color="#6965A3", wraplength=1020)
        self.guide10_line15.place(relx=0.05, rely=0.84, anchor="w")