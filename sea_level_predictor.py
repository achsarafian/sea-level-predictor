import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='royalblue', alpha=0.5)

    # Create first line of best fit
    res_best_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x = pd.Series([y for y in range(df['Year'].sort_values().iloc[0], 2051)])

    plt.plot(x, res_best_fit.intercept + res_best_fit.slope*x, 'lime')

    # Create second line of best fit
    mask = df['Year'] >= 2000
    res_best_fit_over_2000 = linregress(df[mask]['Year'], df[mask]['CSIRO Adjusted Sea Level'])

    x = pd.Series([y for y in range(2000, 2051)])

    plt.plot(x, res_best_fit_over_2000.intercept + res_best_fit_over_2000.slope*x, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()