# Seoul Bike Sharing Demand Analysis - Kilbertus, Leyris, Plaideau

### Project Overview
This project aims to predict hourly bike attendance using historical rental data, considering factors like weather and holidays. The goal is to optimize bike supply and distribution for urban operators.

### Team
Developed by a team composed of :
* [Emma KILBERTUS](www.linkedin.com/in/emma-kilbertus/ "Emma KILBERTUS")
* [Anouk LEYRIS](www.linkedin.com/in/anouk-leyris-25a178251/ "Anouk LEYRIS")
* [Anna PLAIDEAU](https://www.linkedin.com/in/anna-plaideau-609074206/ "Anna PLAIDEA")

### Data
Utilized the [Seoul Bike Sharing](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand "Seoul Bike Sharing")
dataset with hourly bike counts, weather, and holiday info. Key variables include date, rented bike count, hour, temperature, humidity, and more.

### Project Structure
1. Importing libraries and data
2. Data Cleaning
  a. Data Exploration
  b. Data Manipulation
  c. Encoding
3. Data Visualization
4. Machine Learning
  a. Modeling: the attendance is determined based on the percentiles
    1. Clustering
    2. Decision Tree, Naive Bayesian and Random Forest Regression
  b. Modeling: the attendance is determined in a binary way
    1. Clustering
    2. Decision Tree, Naive Bayesian and Random Forest Regression
  c. Modeling: the attendance is determined arbitrarily
    1. Clustering
    2. Decision Tree, Naive Bayesian and Random Forest Regression
  d. Conclusion
5. Conclusion
6. API

### Conclusion
Giving the climate measures of a day, the hour and the date, we can say, using DecisionTree with 90% of accuracy, if the attendance of the rented bike system in Seoul is low or high. With more than 80% of accuracy and the same algorithm, we can even detail the attendance of the rent with 4 degrees based on the stats of rented bike number that we have.

### Tools & Technologies
* Jupyter Notebook/Colab Notebook, Python
* Libraries: Numpy, Pandas, Matplotlib, Seaborn, Sklearn, Spicy, Sklearn Extra, Sys, Pickle, Warnings, Statsmodels
