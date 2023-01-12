import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    print(df.head())

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(
        df.Year,
        df["CSIRO Adjusted Sea Level"],
    )

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df.Year, df["CSIRO Adjusted Sea Level"])
    line_x = np.arange(df.Year.min(), 2051, 1)
    line_y = slope * line_x + intercept
    ax.plot(line_x, line_y)

    # Create second line of best fit
    df_start2000 = df.loc[df.Year >= 2000]
    slope_2, intercept_2, r_value_2, p_value_2, str_err_2 = linregress(
        df_start2000.Year, df_start2000["CSIRO Adjusted Sea Level"])
    line_2x = np.arange(2000, 2051, 1)
    line_2y = slope_2 * line_2x + intercept_2
    ax.plot(line_2x, line_2y)

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
