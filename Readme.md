# 🏦 Bank Customer Churn Analysis — EDA

## Overview

This project performs an Exploratory Data Analysis (EDA) on a bank customer dataset to identify key factors that contribute to customer churn. The goal is to uncover patterns and attributes that distinguish churners from non-churners, which can inform customer retention strategies.

---

## Dataset

File: `Bank_Churn.csv`
- Shape: 1,000 rows × 13 columns
- Missing Values: None
- Data Types: Clean — no preprocessing required

### Key Features

| Feature | Description |
|---|---|
| `Age` | Customer age |
| `Balance` | Account balance |
| `CreditScore` | Credit score |
| `Geography` | Country (France, Germany, Spain) |
| `Gender` | Male / Female |
| `EstimatedSalary` | Annual salary estimate |
| `Tenure` | Number of years with the bank |
| `NumOfProducts` | Number of bank products used |
| `IsActiveMember` | Whether the customer is active (1/0) |
| `HasCrCard` | Whether the customer has a credit card (1/0) |
| `Exited` | Target variable — 1 = Churned, 0 = Stayed |

---

## Tools & Libraries

Pyth
Pand — data loading and aggregation
Matplotl — basic plotting
Seabo — advanced visualizations (histplots, boxplots, barplots, countplots)



## Analysis Summary

### 1. Age
- Most customers fall between the ages of 35–45.
- Customers aged 50–67 are significantly more likely to churn.
- The average age of churners is higher than that of non-churners.

### 2. Balance
- Churners tend to have a higher account balance than non-churners.
- In every age group, churners consistently show higher average balances.

### 3. Credit Score
- Churners have a slightly lower average credit score compared to retained customers.

### 4. Geography
- Germany has the highest churn rate among all countries, for both males and females.
- German customers also have the highest average balance, which correlates with the balance-churn finding.

### 5. Gender
-Females are more likely to churn than males across all age groups.
- Female churn rate peaks in the 50–65 age bracket (~61%).

### 6. Estimated Salary
- Estimated salary shows no strong predictive signal for churn — distributions are roughly uniform across churners and non-churners.
- Skewness analysis confirms near-symmetrical distributions for both groups.

### 7. Tenure
- Churn rate is not strongly influenced by tenure — customers with both short and long tenure churn at similar rates.

### 8. Number of Products
- Customers with 1 or 2 products show varying churn patterns.
- The relationship between product count and churn is non-linear.

### 9. Active Membership
- Inactive members are more likely to churn than active members.

### 10. Credit Card Ownership
- Having a credit card does not significantly reduce churn — both groups show similar churn behavior.


## Key Findings

| Attribute | Finding |

Age - Older customers (50+) churn more 

Balance - Higher balance → higher churn risk 

Credit Score - Lower credit score slightly associated with churn 

Geography - Germany has the highest churn rate 

Gender - Females churn more than males across all age groups 

Salary - No strong relationship with churn  Tenure - Not a significant churn predictor 

Active Membership - Inactive members churn more 