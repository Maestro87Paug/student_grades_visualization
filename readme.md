# Student Scores Bar Chart

This script generates a horizontal bar chart displaying the scores of students grouped by their respective groups. The chart is created using Matplotlib and provides a visual representation of the data, including labels for each bar and a legend indicating the groups.

## Data

The data for the students is provided in a dictionary format where each student's name is associated with a tuple containing their score and group.

## Prerequisites

- Python 3
- Matplotlib

You can install Matplotlib using pip:

```bash
pip install matplotlib
```

## Data The data for the students is provided in a dictionary format where each student's name is associated with a tuple containing their score and group.

```python
data = { "Ana": (10, "A"), "Bernardo": (8, "A"), ....}

```

## Data Preparation and Visualization

```python
students = list(data.keys())
scores = []
groups = []
for student in students:
    scores.append(data[student][0])
    groups.append(data[student][1])
```

## Visualization

```python
colors = {'A': 'blue', 'B': 'red', "C": "purple"}
bar_colors = []
for group in groups:
    bar_colors.append(colors[group])
```

## Bar Chart

```python
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
purple_patch = mpatches.Patch(color="purple", label="Group C")
plt.legend(handles=[blue_patch, red_patch, purple_patch], loc='lower right')

```

## Show values next to bars

```python
for bar in bars:
    score = bar.get_width()
    plt.text(score + 0.1, bar.get_y() + bar.get_height() / 2, str(score), ha='left', va='center')

```

## Add gridlines and adjust the figure size

```python
#Add grid
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)
# Adjust x-axis ticks
plt.xticks(range(0, 12, 1))
# Adjust space for student
names plt.subplots_adjust(left=0.2)
# Show the plot plt.show()
plt.show()
```
