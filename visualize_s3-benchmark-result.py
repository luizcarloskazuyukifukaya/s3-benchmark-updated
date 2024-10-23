import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime

# Function to generate a default filename with current date and time
def generate_default_filename():
    current_datetime = datetime.now()
    return current_datetime.strftime("s3-benchmark-results_%Y%m%d_%H%M%S.png")

# Check if a command-line argument was provided
if len(sys.argv) > 1:
    csv_filename = sys.argv[1]
else:
    csv_filename = "combined.csv"  # Default CSV filename if no argument is provided

# Generate the output filename for the graph
if len(sys.argv) > 2:
    output_filename = sys.argv[2]
else:
    output_filename = generate_default_filename()

# Read the CSV data
try:
    df = pd.read_csv(csv_filename, parse_dates=["DateTime"])
except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: The file '{csv_filename}' is empty.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df["DateTime"], df["Speed(B/sec)"], marker="o")

# Customize the plot
plt.title("Speed (B/sec) over Time")
plt.xlabel("Date and Time")
plt.ylabel("Speed (B/sec)")
plt.grid(True)

# Rotate and align the tick labels so they look better
plt.gcf().autofmt_xdate()

# Use a more readable date format on the x-axis
date_formatter = DateFormatter("%H:%M")
plt.gca().xaxis.set_major_formatter(date_formatter)

# Add labels to the points
for i, txt in enumerate(df["Speed(B/sec)"]):
    plt.annotate(
        f"{txt:.0f}",
        (df["DateTime"].iloc[i], txt),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=8,
    )

# Adjust layout
plt.tight_layout()

# Save the plot as an image file
plt.savefig(output_filename, dpi=300, bbox_inches="tight")

print(f"Graph has been saved as '{output_filename}'")
