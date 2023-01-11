import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col=0)

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) &
            (df["value"] <= df["value"].quantile(0.985))]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(8, 4), dpi=150)
    plt.plot(df.index, df.value)
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return plt


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = pd.DatetimeIndex(df_bar.index).year
    df_bar["month"] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(["year", "month"], as_index=False).agg(
        {"value": pd.Series.sum})
    print(df_bar.head())
    # Draw bar plot
    plt.figure(figsize=(8, 8))

    fig = sns.barplot(data=df_bar, x=df_bar.year,
                      y=df_bar.value, hue=df_bar.month)

    plt.legend(loc="upper left")

    # Save image and return fig (don't change this part)
    fig.figure.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
