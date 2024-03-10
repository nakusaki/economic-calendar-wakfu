import matplotlib.pyplot as plt
import numpy as np

from pandas import DataFrame

def plot_bar_graph(x, y, xlabel='', ylabel='', title='', save_path=None):
    """
    Plot a bar graph with given data.

    Parameters:
        x (list or array-like): Data points for the x-axis.
        y (list or array-like): Data points for the y-axis.
        xlabel (str): Label for the x-axis (default '').
        ylabel (str): Label for the y-axis (default '').
        title (str): Title for the plot (default '').
        save_path (str or None): If provided, save the plot to the specified path (default None).

    Returns:
        None
    """
    # Set the color based on sales value
    colors = ['red' if value < 0 else 'blue' for value in y]
    
    plt.bar(x, y, color=colors)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # Set limits for x and y axes
    plt.ylim(-10, 10)
    
    # Add horizontal line at y=0
    plt.axhline(0, color='black', linewidth=0.5)
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# Example usage:
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
sales = [8, -10, 0, 9, -1, 1, 0]

# plot_bar_graph(days_of_week, sales, xlabel='Day of the Week', ylabel='Sales', title='Weekly Sales')# , save_path='weekly_sales_bar_plot.png')

def plot_table(header, data, save_path=None):
    """
    Plot a table with given header and data.

    Parameters:
        header (list): List representing the header row.
        data (list of lists): 2D list representing the table data.
        save_path (str or None): If provided, save the plot to the specified path (default None).

    Returns:
        None
    """
    df = DataFrame(data)
    plt.figure(figsize=(8, 6))
    ax = plt.subplot(111, frame_on=False) 
    ax.xaxis.set_visible(False) 
    ax.yaxis.set_visible(False) 
    
    # Define colors for cell text
    cell_colors = [['#f2f2f2']*len(df.columns) for _ in range(len(df.index))]
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            if df.iloc[i, j] == 'Male':
                cell_colors[i][j] = 'lightblue'
    
    ax.table(cellText=df.values, colLabels=header, loc='center', 
             cellColours=cell_colors, fontsize=12)
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.axis('off')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()

# Example usage:
header = ["Name", "Age", "Gender"]
data = [
    ["Johndsadsad s", 30, "Male"],
    ["Alicedsadsadsa dsadsa", 25, "Female"],
    ["Bob", 35, "Male"]
]

import matplotlib.pyplot as plt
import numpy as np

# Data
x = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y = [(0, 0), (0, 0), (-20, 15), (0, 0), (0, 5), (-7, 2), (0, 0)]

# Extracting lower and upper bounds from tuples
y_lower = [item[0] for item in y]
y_upper = [item[1] for item in y]

# Creating index for each day
x_index = np.arange(len(x))

# Plotting
plt.bar(x_index - 0.2, y_lower, width=0.4, label='Lower Bound', color='red')
plt.bar(x_index + 0.2, y_upper, width=0.4, label='Upper Bound', color='green')

# Adding labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Values')
plt.title('Bar Graph with Two Bars for Each Day')
plt.xticks(x_index, x)
plt.legend()

# Adding middle line between Mon and Tue
plt.axvline(x_index[0] + 0.5, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x_index[1] + 0.5, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x_index[2] + 0.5, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x_index[3] + 0.5, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x_index[4] + 0.5, color='black', linestyle='--', linewidth=0.5)
plt.axvline(x_index[5] + 0.5, color='black', linestyle='--', linewidth=0.5)
# Adding middle line at y=0
plt.axhline(0, color='black', linewidth=0.5)

# Adding grid
# plt.grid(True)

# Displaying the plot
plt.show()
