from customtkinter import *


class UserGuide():
    def userGuide1(self):
        # self.clear_frame()
        self.guide1_line1 = CTkLabel(self.user_guide_frame, text="Main Interface", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",30,"bold",underline=True) , text_color="#6965A3", wraplength=380)
        self.guide1_line1.grid(row=0, column=0, padx=10, sticky="nsew")
        self.guide1_line2 = CTkLabel(self.user_guide_frame, text="Overview", justify = LEFT,font=CTkFont("font/Poppins-Bold.ttf",22,"bold") , text_color="#6965A3", wraplength=380)
        self.guide1_line2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
# Main Interface
# Overview
# The main interface of BudgetPro consists of the following components:

# Menu Bar: Access different features and settings.
# Dashboard: View your financial summary.
# Sidebar: Navigate between different sections like Budget, Expenses, Income, and Reports.
# Dashboard
# The dashboard displays a summary of your current financial status, including total income, total expenses, and budget balance.

# Navigation
# Use the sidebar to switch between different sections. Click on the desired section to view or edit its content.

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