import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from update_expenses import expenses_data
from set_categories import categories, allocated

def open_usage_barchart_window(budget_data, expenses_data):
    # Initialize dictionaries to store budget and expenses for each category
    budget_dict = defaultdict(float)
    expenses_dict = defaultdict(float)

    # Populate budget dictionary
    for category, budget_amount in zip(categories, allocated):
        budget_dict[category] = float(budget_amount)

    # Populate expenses dictionary
    for expense in expenses_data:
        category, amount = expense[2], expense[1]
        expenses_dict[category] += float(amount)

    # Extract categories and corresponding budget and expenses
    categories_list = list(budget_dict.keys())
    budget_values = [budget_dict[category] for category in categories_list]
    expenses_values = [expenses_dict.get(category, 0) for category in categories_list]

    # Bar chart settings
    bar_width = 0.35
    index = np.arange(len(categories_list))

    # Plotting
    plt.bar(index, budget_values, bar_width, label='Budget')
    plt.bar(index + bar_width, expenses_values, bar_width, label='Expenses')

    plt.xlabel('Categories')
    plt.ylabel('Amount (RM)')
    plt.title('Usage of Budget')
    plt.xticks(index, categories_list, rotation=45, ha='right')
    plt.legend()

    plt.tight_layout()
    plt.show()