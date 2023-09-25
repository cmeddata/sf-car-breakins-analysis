import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reads csv file
Police_Report_df = pd.read_csv("Police_Report.csv")

#filters the csv file to Larceny Theft with Subcategory of Larceny from vehicle. then sets it to Police_Report_df
condition = (Police_Report_df['Incident Category'] == 'Larceny Theft') & (Police_Report_df['Incident Subcategory'] == 'Larceny - From Vehicle')
Police_Report_df = Police_Report_df[condition]

# Set a more appealing style for plots using Seaborn
sns.set(style="whitegrid")

# Analysis of Reported Car Breakins by year
def Analysis_by_year(data):
    # Group and count incidents by year
    IncidentYear = Police_Report_df['Incident Year'].value_counts().sort_index()

    # Create a time series plot
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    plt.plot(IncidentYear.index, IncidentYear.values, marker='o', linestyle='-')
    plt.title('Car Break-ins Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Analysis by day of week
def Analysis_by_Day_of_Week(data):
    # Count the number of incidents for each day of the week
    day_of_week_counts = Police_Report_df['Incident Day of Week'].value_counts()

    # Create a list of days of the week in the correct order
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Reorder the counts based on the list of days
    day_of_week_counts = day_of_week_counts.reindex(days_of_week, fill_value=0)

    # Create a bar plot 
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    day_of_week_counts.plot(kind='bar', color='skyblue')
    plt.title('Car Break-ins by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Analysis by police Districts
def Analysis_by_Police_District(data):
    # Count the number of incidents for each police district
    Police_District = Police_Report_df['Police District'].value_counts()

    # Create a bar plot
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    Police_District.plot(kind='bar', color='skyblue')
    plt.title('Car Break-ins by Police District')
    plt.xlabel('Police District')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


# Status of Reported Car Breakins
def Analysis_by_Status(data):
    # Count the number for each incident status
    Status = Police_Report_df['Resolution'].value_counts()

    # Create a bar plot
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    Status.plot(kind='bar', color='lightcoral')
    plt.title('Status of Car Breakins')
    plt.xlabel('Status')
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

#Analysis by Neighborhood
def Analysis_by_Neighborhood(data):
    # Count the number of incidents for each neighborhood
    neighborhood_counts = Police_Report_df['Analysis Neighborhood'].value_counts()

    # Create a bar plot
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    neighborhood_counts.plot(kind='bar', color='lightcoral')
    plt.title('Car Break-ins by Neighborhood')
    plt.xlabel('Neighborhood')
    plt.ylabel('Frequency')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


#Shows The graph for Category each in Order
Analysis_by_year(Police_Report_df)
Analysis_by_Day_of_Week(Police_Report_df)
Analysis_by_Neighborhood(Police_Report_df)
Analysis_by_Police_District(Police_Report_df)
Analysis_by_Status(Police_Report_df)
plt.show()