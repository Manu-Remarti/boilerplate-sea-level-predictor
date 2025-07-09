import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
            
    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year_extended = pd.Series(range(1880, 2051))
    sea_level_pred = result.slope * year_extended + result.intercept
    plt.plot(year_extended, sea_level_pred, color='red', label='Best Fit Line')

    # Create second line of best fit
    df_recent = df[df['Years']>=2000]]
    result2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = result2.slope * years_recent + result2.intercept
    plt.plot(years_recent, sea_level_pred_recent, color='green', label='Best Fit Line 2000-2051')
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Years')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
