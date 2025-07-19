import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('resources/sensor_data.csv', parse_dates=['timestamp'])

# print(df.describe())
# print('Data types:\n', df.dtypes)

df['temp_smooth'] = df['temp'].rolling(window=3).mean()
# print("Correlation matrice:\n", df.corr(numeric_only=True))
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['temp'], label='Temperature (°C)', color='red', linestyle='--')
plt.plot(df['timestamp'], df['temp_smooth'], label='Temperature (Smoothed)', color='darkred')
plt.plot(df['timestamp'], df['distance'], label='Distance (cm)', color='blue')
plt.plot(df['timestamp'], df['speed'], label='Speed (m/s)', color='green')

plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title('Robot Sensor Readings Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Dual Y-axis Plot: Separate axis for speed
fig, ax1 = plt.subplots(figsize=(12, 6))

# Primary Y-axis
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Temperature / Distance', color='black')
ax1.plot(df['timestamp'], df['temp'], label='Temperature (°C)', color='red', linestyle='--')
ax1.plot(df['timestamp'], df['distance'], label='Distance (cm)', color='blue')
ax1.tick_params(axis='y', labelcolor='black')

# Secondary Y-axis for speed
ax2 = ax1.twinx()
ax2.set_ylabel('Speed (m/s)', color='green')
ax2.plot(df['timestamp'], df['speed'], label='Speed (m/s)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Merge legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

plt.title("Robot Sensor Readings (Dual Axis)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Speed vs Distance
plt.figure(figsize=(6, 6))
plt.scatter(df['distance'], df['speed'], c='purple', alpha=0.7)
plt.xlabel('Distance (cm)')
plt.ylabel('Speed (m/s)')
plt.title('Speed vs Distance Scatter Plot')
plt.grid(True)
plt.tight_layout()
plt.show()