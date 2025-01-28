import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models import FactorRange

# Sample DataFrame creation
file_path = "Test.csv"
data = pd.read_csv(file_path)

# Create a mapping for month names to numerical values
month_mapping = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

# Map months to their numerical values for sorting
data['Month_Num'] = data['Month'].map(month_mapping)

# Sort data by Month_Num for correct order
data = data.sort_values('Month_Num')

# Convert to ColumnDataSource and ensure proper data types
source = ColumnDataSource(data)

# Create a new Bokeh plot with categorical x-axis
plot = figure(title="Website Leads by Month",
              x_axis_label='Month',
              y_axis_label='Leads',
              width=900,
              height=500,
              x_range=FactorRange(*data['Month']))  # Use month names as categorical x-axis

# Add lines for each year
plot.line(x='Month', y='Leads_2024', source=source, legend_label="Leads 2024", line_width=2, color="blue")
plot.line(x='Month', y='Leads_2025', source=source, legend_label="Leads 2025", line_width=2, color="green")

# Add tooltips using HoverTool
hover = HoverTool(tooltips=[
    ("Month", "@Month"),
    ("Leads 2024", "@Leads_2024"),
    ("Leads 2025", "@Leads_2025")
])
plot.add_tools(hover)

# Customize the legend
plot.legend.title = "Metrics"
plot.legend.location = "top_left"

# Save the output to an HTML file and display it
output_file("sample_with_tooltip.html")
show(plot)
