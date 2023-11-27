# Interactive Pie Chart with Matplotlib and mplcursors

This Python script generates an interactive pie chart using Matplotlib library to visualize data with interactive tooltips for each section of the pie chart. The mplcursors library is used to enable interactivity, allowing users to hover over sections and view labels and percentages.

## Requirements

- Python (3.x recommended)
- Matplotlib
- mplcursors

## Installation

1. Clone the repository or download the Python script.
2. Install the required libraries by running the following command:

   ```bash
   pip install matplotlib mplcursors
   ```

## Usage

1. Ensure you have the required Python libraries installed (Matplotlib and mplcursors).
2. Run the Python script `piechart.py`.
3. The script will generate a window displaying an interactive pie chart.
4. Hover over each section of the pie chart to see tooltips displaying the label and percentage of that section.

## Code Overview

- `piechart.py`: Python script that creates an interactive pie chart using Matplotlib and mplcursors.
- `labels`: List containing labels for different sections of the pie chart.
- `sizes`: List containing the values for each section of the pie chart.
- `plt.pie()`: Method to create the pie chart with specified labels, sizes, percentages, and interactivity using mplcursors.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
