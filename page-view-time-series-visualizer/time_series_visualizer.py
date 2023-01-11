import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col=0)

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025))
            & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(8, 4), dpi=150)
    sns.lineplot(data=df, x=df.index, y=df.value)

    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = pd.DatetimeIndex(df_bar.index).year
    df_bar["month"] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(["year", "month"],
                            as_index=False).agg({"value": pd.Series.mean})

    # Draw bar plot
    fig, axes = plt.subplots(figsize=(8, 8))
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]

    sns.barplot(data=df_bar,
                x=df_bar.year,
                y=df_bar.value,
                hue=df_bar.month,
                palette=sns.color_palette("tab10"))

    axes.set_xlabel("Years")
    axes.set_ylabel("Average Page Views")
    axes.legend(loc="upper left", title="Months", labels=month_names)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months_sorted = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    df_box.month = pd.Categorical(
        df_box.month, categories=months_sorted, ordered=True)

    df_box = df_box.sort_values("month")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))
    sns.boxplot(data=df_box,
                x=df_box.year,
                y=df_box.value,
                orient="v",
                ax=ax1)

    # Draw box plots (using Seaborn)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    sns.boxplot(data=df_box,
                x=df_box.month,
                y=df_box.value,
                orient="v",
                ax=ax2)

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
