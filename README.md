# fplAI

## Developing a Machine Learning Model to Predict Fantasy Premier League Points

### Overview
This project aims to harness machine learning to forecast Fantasy Premier League (FPL) player points accurately. By analyzing various performance metrics, we seek to provide FPL enthusiasts with a powerful tool for making informed decisions. 

### Focus Question
How can machine learning be utilized to accurately predict player points in Fantasy Premier League (FPL) based on various performance metrics?

### Key Terms and Methods
The project revolves around the creation of a machine learning model focusing on key aspects such as:

- **Player Performance Metrics**: Analysis of a player's performance over the last season, the last 10 games, and the past two years.
- **Team Performance**: Consideration of the team's recent performance.
- **Fixture Difficulty**: Evaluation of upcoming game difficulty.
- **Advanced Metrics**: Inclusion of expected Goals Involvement (xGI), expected Goals Conceded (xGC), and expected Clean Sheets (xCS).
- **Individual Player Statistics**: Utilization of statistics like bonus points and opponent strength.
- **Position-Specific Analysis**: Tailored analysis based on player positions.
- **Expected Minutes Per Game**: Forecasting playing time.

The methodology encompasses:
1. **Correlation Analysis**: Determining correlation coefficients for predicting points using a comprehensive dataset, categorized by player positions.
2. **Machine Learning Model**: Training a model with data on predicted points, taking into account various factors including player form, opponents, and other pertinent metrics.

### Data Sources
- **Player Stats Per 90**: Sourced from Fantasy Football Hub.
- **Detailed Gameweek Data**: Obtained from the Fantasy Premier League GitHub Repository.
- **Miscellaneous Data**: Acquired from [FBRef](https://fbref.com/en/).

### Model Training and Validation
- The model will be trained and validated on data from seasons 18-22.
- Testing will be conducted on data from the 22/23 and 23/24 seasons.
- Various models will be experimented with, including decision trees and more advanced algorithms.

### Objective
The ultimate goal of this project is to refine and validate the model's precision in predicting FPL points. The envisioned final product will be capable of taking inputs such as player name, fixture, current season form, among other metrics, and outputting the predicted points per 90 minutes. This endeavor aims to contribute valuable insights and assist FPL players and enthusiasts in their strategic planning.

