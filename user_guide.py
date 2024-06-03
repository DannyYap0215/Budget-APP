from customtkinter import *


class UserGuide():
    def userGuide1(self):
        self.guide1_line1 = CTkLabel(self.user_guide_frame, text="Main Interface", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide1_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide1_line2 = CTkLabel(self.user_guide_frame, text="Sidebar: Navigate between different sections like Insights, Budget, Update Expenses, Expenses History and Settings", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide1_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.guide1_line3 = CTkLabel(self.user_guide_frame, text="Dashboard: View functions of sections", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide1_line3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
    def userGuide2(self):
        self.guide2_line1 = CTkLabel(self.user_guide_frame, text="Navigation", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide2_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide2_line2 = CTkLabel(self.user_guide_frame, text="Use the sidebar to switch between different sections and click on the desired section to view or edit its content", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide2_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
    def userGuide3(self):   
        self.guide3_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide3_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide3_line2 = CTkLabel(self.user_guide_frame, text="Allocate Income", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline= True) , text_color="#6965A3", wraplength=380)
        self.guide3_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.guide3_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Edit Budget\" button in the sidebar", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line3.grid(row=2, column=0, padx=10, pady=(0,5), sticky="w")
        
        self.guide3_line4 = CTkLabel(self.user_guide_frame, text="2. Click on the \"Set Income\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.guide3_line5 = CTkLabel(self.user_guide_frame, text="3. Enter the Year and select the Month( Make sure to update both to confirm selection ) ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line5.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.guide3_line6 = CTkLabel(self.user_guide_frame, text="4. Enter allocated income and click on \"Save ALL\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide3_line6.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        
    def userGuide4(self):
        self.guide4_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide4_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide4_line2 = CTkLabel(self.user_guide_frame, text="Creating a Budget for Categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline= True) , text_color="#6965A3", wraplength=380)
        self.guide4_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.guide4_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Edit Budget\" button in the sidebar", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line3.grid(row=2, column=0, padx=10, pady=(0,5), sticky="w")
        
        self.guide4_line4 = CTkLabel(self.user_guide_frame, text="2. Click on the \"Set Categories\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.guide4_line5 = CTkLabel(self.user_guide_frame, text="3. Select the Year, Month ( Make sure to update both to confirm selection ) and category of your choice ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line5.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.guide4_line6 = CTkLabel(self.user_guide_frame, text="4. Enter allocated budget and click on \"Save\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide4_line6.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
    def userGuide5(self):
        self.guide5_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide5_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide5_line2 = CTkLabel(self.user_guide_frame, text="Updating Expenses ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide5_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide5_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Update Expenses\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide5_line4 = CTkLabel(self.user_guide_frame, text="2. Choose date, day and year", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide5_line5 = CTkLabel(self.user_guide_frame, text="3. Fill in the expenses used and select categories", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide5_line6 = CTkLabel(self.user_guide_frame, text="4. Add in a note (not required) and click \"Save Expenses\"", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide5_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
    
    def userGuide6(self):
        self.guide6_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide6_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide6_line2 = CTkLabel(self.user_guide_frame, text="View Expenses History", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide6_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide6_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Expenses History\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide6_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide6_line4 = CTkLabel(self.user_guide_frame, text="2. Select Month and Update OR search for any keywords in the search tab and click on \"search\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide6_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide7(self):
        self.guide7_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide7_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide7_line2 = CTkLabel(self.user_guide_frame, text="Expenses Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide7_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide7_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide7_line4 = CTkLabel(self.user_guide_frame, text="2. Click on the \"Expenses\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide7_line5 = CTkLabel(self.user_guide_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide7_line6 = CTkLabel(self.user_guide_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide7_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide8(self):
        self.guide8_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide8_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide8_line2 = CTkLabel(self.user_guide_frame, text="Income Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide8_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide8_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide8_line4 = CTkLabel(self.user_guide_frame, text="2. Click on the \"Income\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide8_line5 = CTkLabel(self.user_guide_frame, text="3. Select Year click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide8_line6 = CTkLabel(self.user_guide_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide8_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide9(self):
        self.guide9_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide9_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide9_line2 = CTkLabel(self.user_guide_frame, text="Usage of Budget Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide9_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide9_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide9_line4 = CTkLabel(self.user_guide_frame, text="2. Click on the \"Usage of Budget\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide9_line5 = CTkLabel(self.user_guide_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide9_line6 = CTkLabel(self.user_guide_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide9_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
        
    def userGuide10(self):
        self.guide10_line1 = CTkLabel(self.user_guide_frame, text="Key Features and How to Use Them", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",25,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide10_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.guide10_line2 = CTkLabel(self.user_guide_frame, text="Usage of Budget Insights ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide10_line2.grid(row=1, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line3 = CTkLabel(self.user_guide_frame, text="1. Click on the \"Insight\" button in the sidebar ", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line3.grid(row=2, column=0, padx=10,pady=(0,5), sticky="w")
        
        self.guide10_line4 = CTkLabel(self.user_guide_frame, text="2. Click on the \"Usage of Budget\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line4.grid(row=3, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line5 = CTkLabel(self.user_guide_frame, text="3. Select Year and Month and click on the \"Update\" button", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line5.grid(row=4, column=0, padx=10,pady=5, sticky="w")
        
        self.guide10_line6 = CTkLabel(self.user_guide_frame, text="4. You can also view details by clicking on \"Show Details\" after step 3", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",15,"bold") , text_color="#6965A3", wraplength=380)
        self.guide10_line6.grid(row=5, column=0, padx=10,pady=5, sticky="w")
    

        
        
        
        
        
        

# Key Features and How to Use Them
# Creating a Budget
# Click on the Budget tab in the sidebar.
# Click the Add New Budget button.
# Enter the budget details including name, amount, and period.
# Click Save to create the budget.

# Adding Expenses and Income
# Click on the Expenses or Income tab.
# Click the Add New button.
# Fill in the details such as category, amount, and date.
# Click Save to record the transaction.

# Viewing Reports
# Click on the Reports tab.
# Select the type of report (e.g., Monthly Summary, Expense Breakdown).
# View the generated report on the screen.
# Setting Goals
# Click on the Goals tab.
# Click the Add New Goal button.
# Enter the goal details including name, amount, and deadline.
# Click Save to set the goal.
# Alerts and Notifications
# BudgetPro will alert you when you are nearing your budget limits or when other significant financial events occur. Ensure notifications are enabled in the settings.

# Advanced Features
# Custom Categories
# Click on Settings in the menu bar.

# Navigate to the Categories section.
# Click Add New Category and fill in the details.
# Click Save to create the category.
# Importing/Exporting Data
# Click on File in the menu bar.
# Select Import or Export.
# Follow the on-screen instructions to complete the process.
# Integration with Other Tools
# BudgetPro can integrate with external financial tools. Refer to the integration section in the settings for detailed instructions.

# Tips and Best Practices
# Budgeting Tips
# Track every expense diligently.
# Set realistic budget limits.
# Review your budget regularly.
# Common Mistakes
# Forgetting to record small expenses.
# Setting unattainable goals.
# Not reviewing the budget periodically.
# Optimization
# Use categories to organize expenses.
# Regularly update your income and expense records.
# Utilize reports to analyze spending patterns.
# Troubleshooting
# Common Issues
# App Crashes: Ensure all dependencies are installed and up to date.
# Data Not Saving: Check file permissions and storage space.
# FAQs
# Q: How do I backup my data?
# A: Use the export feature under the File menu to save a backup.

# Support
# For further assistance, contact our support team at support@example.com.

# Appendix
# Glossary
# Budget: A plan for income and expenses over a specified period.
# Expense: Money spent on goods or services.
# Income: Money received from various sources.