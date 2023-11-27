import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors library

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]  # Values for each section of the pie chart

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 6))  # Set the size of the figure
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
)

# Add interactivity using mplcursors
cursor = mplcursors.cursor(hover=True)
cursor.connect('add', lambda sel: sel.annotation.set_text(
    f'{labels[sel.target.index]}: {sizes[sel.target.index]}%'))

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')
ax.set_title('Interactive Pie Chart')

# Show the plot
plt.show()
