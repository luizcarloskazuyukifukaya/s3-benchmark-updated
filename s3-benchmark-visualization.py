# Need to install the followings:
# pip install pandas
# pip install matplotlib
# pip install matplotlib
# OR
# pip install -r requirements.txt

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import io

from datetime import datetime

csv_file = "./combined.csv"

# Read the CSV data
# df = pd.read_csv(io.StringIO(csv_data), parse_dates=['DateTime'])
df = pd.read_csv(csv_file, parse_dates=["DateTime"])

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

# Show the plot
plt.tight_layout()

# plt.show()

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time as a string
filename = current_datetime.strftime("s3-benchmark-results_%Y%m%d_%H%M%S.png")

# Save the plot as an image file
# visual_file = './sample_data/s3-benchmark-results.png'
visual_file = "./{}".format(filename)

plt.savefig(visual_file, dpi=300, bbox_inches="tight")

print(f"Graph has been saved as {visual_file}")
