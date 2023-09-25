# Data Exploration: Car Break-ins in San Francisco

## Overview

This project focuses on analyzing car break-ins in San Francisco using available data on the day of the week, year, neighborhood, police district, and resolution status. The primary goal is to uncover patterns and insights from the data to inform strategies for reducing car break-ins in the city.

## Table of Contents

- [Project Description](#overview)
- [Data](#data)
- [Analysis](#analysis)
- [Findings](#findings)
- [Contributing](#contributing)
- [License](#license)

## Data

The data used for this analysis was sourced from [[DataSF](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783)]. It includes information about reported car break-in incidents in San Francisco, including:

- **Incident Year**: The year when the incident occurred.
- **Incident Day of Week**: The day of the week when the incident occurred.
- **Analysis Neighborhood**: The neighborhood where the incident took place.
- **Police District**: The police district responsible for the area where the incident occurred.
- **Resolution**: The status of the incident resolution (e.g., "Active" or Not).

## Analysis

### I. Analyzing Day of the Week

We analyzed the data to understand if there are specific days of the week when car break-ins are more likely to occur. This analysis provides insights into temporal patterns of these incidents.

1. **Frequency by Day:**

   - **Friday:** The day with the highest number of car break-ins.
   - **Saturday:** The second-highest day for car break-ins.
   - **Sunday:** The third-highest day for car break-ins.
   - **Monday:** The fourth-highest day for car break-ins.
   - **Wednesday:** The fifth-highest day for car break-ins.
   - **Thursday:** The sixth-highest day for car break-ins.
   - **Tuesday:** The day with the lowest number of car break-ins.
  

![DayOfTheWeek](https://github.com/cmeddata/sf-car-breakins-analysis/assets/124543750/dbaef212-ab68-47d9-9021-136da696fef9)

2. **Overall Trends:**

   Our analysis revealed several noteworthy trends in car break-ins throughout the week:

   - **Weekend Peaks:** Car break-ins are highest on Fridays, Saturdays, and Sundays. This suggests a clear pattern of increased incidents over the weekend, which may be linked to higher levels of social activity during these days.

   - **Midweek Lulls:** Conversely, car break-ins are lowest on Tuesdays, with Wednesdays and Thursdays following suit. These midweek lulls may be attributed to decreased social activity due to work.

   - **Resolution Status:** We observed that while weekends had higher incidents, they also had a lower resolution rate. This might indicate a backlog of unresolved cases due to the surge in incidents over the weekend.

   These trends provide valuable insights for city officials and law enforcement agencies to consider when planning resources and strategies to address car break-ins in San Francisco.


3. **Implications:**

   The findings from our analysis of car break-ins by day of the week carry several implications for addressing this issue in San Francisco:

   - **Resource Allocation:** Law enforcement agencies may consider allocating more resources, such as increased patrolling and surveillance, during weekends (particularly Fridays and Saturdays) when car break-ins are most frequent. This proactive approach could help deter incidents and improve response times.

   - **Community Engagement:** Community organizations and residents can use this information to raise awareness and promote safety measures during high-risk periods. Initiatives like neighborhood watch programs and educational campaigns could be tailored to coincide with the days of the week when car break-ins are most prevalent.

   - **Data Collection and Analysis:** Continuous monitoring and analysis of incident data by day of the week can help adapt strategies over time. Regular updates and refinements to policies and interventions based on changing patterns are essential.

   It's important to note that while our analysis provides valuable insights, it does not account for all factors contributing to car break-ins. Sociodemographic factors, economic conditions, and other external variables may also play a role and warrant further investigation.

   In conclusion, these implications can serve as a starting point for policymakers, law enforcement agencies, and community stakeholders in their efforts to reduce car break-ins and enhance the safety of San Francisco residents.
   

### II. Yearly Trends

In this section, we delve into the trends in car break-ins over the years. Understanding how the frequency of these incidents has evolved can provide valuable insights for addressing the issue and making informed decisions.

#### Data Preparation

To conduct this analysis, we first filtered the dataset to include only car break-ins, ensuring that our focus remained on the relevant incidents. We also extracted the incident year from the "Incident Year" column to enable year-based analysis.

#### Yearly Trends Analysis

- **Increasing Incidents:** Our analysis of car break-ins by year revealed interesting trends:

   - **2018:** The year with the highest number of car break-ins, signaling a significant issue that required attention.
   - **2019:** Following closely, 2019 also had a notable increase in car break-ins.
   - **2022:** A relatively high number of incidents occurred in 2022, indicating a persistent concern.
   - **2021:** While lower than 2018 and 2019, 2021 saw a significant number of car break-ins which may be due to eveything reopening again from COVID-19.
   - **2023:** A noticeable increase compared to previous years, suggesting an emerging trend.
   - **2020:** Car break-ins in 2020 were relatively lower than other years but still require vigilance this may be due to the COVID-19 virus that has plagued the world..

   This data highlights the fluctuation in car break-ins over the years, with some years experiencing surges in incidents.

- **Resolution Rates:** Our analysis also considered the resolution rates for these years. [Discuss any trends or insights related to resolution rates.]

![Years](https://github.com/cmeddata/sf-car-breakins-analysis/assets/124543750/42854a1b-f826-4ed0-abdc-c409acc59457)

#### Implications

- Recognizing the upward trend, city officials and law enforcement agencies should consider allocating additional resources to address the growing issue of car break-ins. Targeting resources this year and the following as the data shows that the number of car break-ins are on track to reach pre-covid numbers.
  
- These implications provide a roadmap for addressing the issue of car break-ins in San Francisco in a manner that is responsive to the evolving trends.


### III. Neighborhood Analysis

We explored the data based on neighborhoods and police districts to provide insights into the geographical distribution of car break-ins. Are certain areas more susceptible to these incidents?

#### Data Source

The car break-in data used in this analysis was sourced from the San Francisco Police Department.

#### Data Preparation

To conduct the Neighborhood Analysis, we extracted and grouped the data by neighborhoods to count the number of car break-ins in each area.


#### Neighborhood Analysis

- **Car Break-ins by Neighborhood:** The bar chart below illustrates the frequency of car break-ins in various San Francisco neighborhoods. It is evident that certain neighborhoods experience higher incidents than others, indicating potential areas of concern.

![Neighbourhood](https://github.com/cmeddata/sf-car-breakins-analysis/assets/124543750/d80faaf2-d34c-46ed-b38b-4d031e465844)

- **Hotspots:** Neighborhoods like North Beach, Financial District/South Beach,Mission, Russian Hill, Hayes Valley,South of Market,Marina,Western Addition,Outer Richmond and the Tenderloin stand out as hotspots for car break-ins, warranting specific attention and preventive measures.


### IV.Police District Analysis

In this section, we delve into the distribution of car break-ins across different police districts within San Francisco. Analyzing incidents by police district provides insights into law enforcement efforts and resource allocation.

#### Data Preparation

Similar to the Neighborhood Analysis, we grouped the data by police districts and counted the number of car break-ins in each district to conduct this analysis.


#### Police District Analysis

- **Car Break-ins by Police District:** The bar chart below illustrates the frequency of car break-ins in different police districts. Notably, certain districts experience higher incident rates than others, reflecting potential areas where law enforcement may need to focus resources.

![Police District](https://github.com/cmeddata/sf-car-breakins-analysis/assets/124543750/d29db4f0-d81c-48d1-bc99-68d52415a70e)

- **Resource Allocation:** Police districts such as Central District,Northern District and Richmond District may require additional resources and attention to address the elevated levels of car break-ins.


### V. Resolution Status

### Resolution Status Analysis

This section explores the resolution status of reported car break-ins in San Francisco. Analyzing the resolution outcomes provides insights into the effectiveness of law enforcement efforts and the current status of these incidents.

#### Data Preparation

To conduct the Resolution Status Analysis, we categorized car break-in cases based on their resolution status, distinguishing between resolved and unresolved incidents.

#### Resolution Status Analysis

- **Car Break-ins by Resolution Status:** The bar chart below illustrates the distribution of car break-ins based on their resolution status. It is essential to note the proportion of resolved cases and those that remain open.

![Status](https://github.com/cmeddata/sf-car-breakins-analysis/assets/124543750/3a7e632f-6123-48be-8d52-351333ff8b56)

- **Implications:** The analysis underscores the challenge of addressing car break-ins effectively, with a substantial number of cases still active. This calls for a concerted effort to enhance resolution rates and investigative processes. This could also mean that the same people doing car break-ins during it's peak at 2018 are the same people doing it today at 2023.

- **Areas of Concern:** Neighborhoods such as North Beach, Financial District/South Beach,Mission, Russian Hill, Hayes Valley,South of Market,Marina,Western Addition,Outer Richmond and the Tenderloin may have a particularly high proportion of unresolved cases, necessitating targeted interventions.

- **Community Confidence:** Effective resolution of cases contributes to community confidence in law enforcement and encourages prompt reporting of incidents.


### Findings

- Based on our analysis of car break-ins in San Francisco, several key findings and insights have emerged:

   - Day of the Week Analysis:
        Car break-ins are most frequent on Fridays and Saturdays, followed by Sundays and Mondays. The weekdays generally exhibit lower incident rates, with Tuesdays having the lowest occurrence.

   - Yearly Trends:
      The analysis of yearly trends shows that car break-ins peaked in 2018, followed by 2019. There was a noticeable decrease in incidents in 2020, followed by fluctuations in 2021, 2022, and 2023.

   - Neighborhood Analysis:
        Certain neighborhoods, such as North Beach, Financial District/South Beach,Mission, Russian Hill, Hayes Valley,South of Market,Marina,Western Addition,Outer Richmond and the Tenderloin, stand out as hotspots for car break-ins, requiring targeted preventive measures and community engagement.

   - Police District Analysis:
        Specific police districts, like Central District,Northern District and Richmond District, experience higher incident rates, indicating the need for resource allocation and strategic law enforcement efforts.

   - Resolution Status:
        A significant majority of reported car break-in cases remain unresolved, underlining the challenges in effectively addressing this issue. Law enforcement efforts should focus on improving resolution rates.

### Implications

These findings have several implications:

   - Enhanced community engagement and awareness campaigns can play a vital role in preventing car break-ins and aiding in investigations.

   - Targeted law enforcement efforts and resource allocation in high-incident neighborhoods and police districts are essential for effective crime reduction.

   - Data-driven strategies, guided by patterns and insights, can contribute to more successful resolutions and crime prevention.




## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.



