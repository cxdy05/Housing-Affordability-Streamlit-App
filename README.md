# Predictive Housing Affordability Dashboard (Hackathon Project)

## Overview
This project explores Western Australian housing affordability using a prototype Streamlit app. The tool predicts and ranks suburbs by affordability and housing stress based on simplified indicators (median rent, median income, population, etc.). The app allows users to interactively explore which areas may be more affordable given their budget and preferences.

## Features of the Analysis
- **Data Cleaning & Preprocessing**
  - Selected key variables from the housing dataset (median rent, household income, population).
  - Removed missing values and reformatted inconsistent column names.
  - Calculated an affordability score (rent-to-income ratio).

- **Exploratory Data Analysis (EDA)**
  - Summary statistics for rents and incomes across suburbs.
  - Distribution plots for rent-to-income ratios.
  - Ranking suburbs by affordability score.

- **Key Insights**
  - Suburbs with lower rent-in-income ratios are more affordable.
  - Higher income areas do not always correlate with affordability due to high rental costs.
  - Population density patterns highligh trade-offs between affordability and accessibility.

- **Visualizations**
  - Bar charts comparing affordability across suburbs.
  - Histograms of rent-to-income ratios.
  - Interactive tablse of suburb rankings.

## Tech Stack
- **Python 3**
- **Libraries:** pandas, numpy, matplotlib, seaborn
- **Streamlit** for interactive dashboard

## Prototype Demo
The **Streamlit app** lets users:
- Input a budget range.
- View ranked suburbs by affordability.
- Explore housing stress indicators interactively.
