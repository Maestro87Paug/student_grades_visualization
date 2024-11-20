import matplotlib.pyplot as plt

# Sample data
data = {
    "Ana": (10, "A"),
    "Bernardo": (8, "A"),
    "Carlos": (9, "A"),
    "Daniel": (7, "A"),
    "Eduardo": (6, "A"),
    "Francisco": (5, "A"),
    "Gabriel": (4, "A"),
    "Gustavo": (3, "A"),
    "Helena": (2, "A"),
    "Isabel": (1, "A"),
    "Jose": (8, "B"),
    "Juan": (7, "B"),
    "Luis": (6, "B"),
    "Maria": (5, "B"),
    "Miguel": (4, "B"),
    "Pablo": (3, "B"),
    "Pedro": (2, "B"),
    "Rafael": (1, "B"),
}

# Lists for the data
students = list(data.keys())
scores = []
groups = []
for student in students:
    scores.append(data[student][0])
    groups.append(data[student][1])

# Colors for the groups
colors = {'A': 'blue', 'B': 'red'}
bar_colors = []
for group in groups:
    bar_colors.append(colors[group])

# Create the horizontal bar chart
plt.figure(figsize=(12, 8))  # Figure size
bars = plt.barh(students, scores, color=bar_colors, edgecolor='grey')  # Create horizontal bars

# Titles and labels
plt.title('Student Scores')
plt.xlabel('Score')
plt.ylabel('Student')

# Add the legend
import matplotlib.patches as mpatches
blue_patch = mpatches.Patch(color='blue', label='Group A')
red_patch = mpatches.Patch(color='red', label='Group B')
plt.legend(handles=[blue_patch, red_patch], loc='lower right')

# Show the values next to the bars
for bar in bars:
    score = bar.get_width()
    plt.text(score + 0.1, bar.get_y() + bar.get_height() / 2, str(score), ha='left', va='center')

# Add grid
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust x-axis ticks
plt.xticks(range(0, 12, 1))

# Adjust space for student names
plt.subplots_adjust(left=0.2)

# Show the plot
plt.show()
