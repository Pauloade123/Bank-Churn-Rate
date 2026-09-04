# Bank Customer Churn Prediction

Predicting which bank customers are likely to leave, and digging into *why* — using
demographic, account, and engagement data for 10,000 customers.

## Why this project

Retention is usually far cheaper than acquisition, but only if you know who's actually at
risk. This project treats churn as both a prediction problem (who's leaving) and an
explanation problem (what's driving it) — the second part is arguably more useful to a
business than the prediction alone, since it points to what to actually fix.

## Data

[Kaggle Bank Customer Churn dataset](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)
— 10,000 customers with credit score, geography, gender, age, tenure, balance, product
count, credit card status, activity status, and estimated salary.

## Approach

1. Cleaned the data (dropped identifiers, checked nulls/duplicates, renamed target to `Churn`)
2. Ran EDA across every feature against churn — not just univariate, but a few interaction
   cuts too (age × gender, gender × geography) once single features looked promising
3. Built a class-weighted logistic regression, since churn is imbalanced (~20% positive class)

## Results

| Metric | Stayed | Churned |
|---|---|---|
| Precision | 0.91 | 0.38 |
| Recall | 0.72 | **0.71** |
| F1 | 0.81 | 0.50 |

**71.95% overall accuracy** — but that's the wrong headline number given the class
imbalance. **71% recall on churners** is what `class_weight='balanced'` was actually
optimizing for: catching customers who are about to leave, even at the cost of some false
positives (0.38 precision). For a retention use case, missing an at-risk customer is more
costly than flagging a few who were never going to leave.

## What drives churn

- **Geography** — churn is highest in Germany, for both genders
- **Activity status** — inactive members churn at a much higher rate
- **Product count** — customers with 3–4 products churn far more than those with 1–2
  (worth investigating — possibly over-sold or poorly-fitting product bundles)
- **Age** — churn concentrates in the 40–65 range, and among women specifically in 50–65
- **Balance** — zero-balance customers churn more, but so do those with unusually high
  balances ($100k–150k) — likely two different churn mechanisms worth separating rather
  than treating balance as one linear effect

## What I'd do differently next time

- Try SMOTE or other resampling alongside class weighting to see if it improves precision
  without sacrificing recall
- Add a tree-based model for comparison — logistic regression is interpretable but may be
  leaving accuracy on the table
- Segment the "high product count" churners specifically — that finding deserves its own
  follow-up rather than being one bullet among many

## Tech

Python · pandas · scikit-learn (LogisticRegression, class_weight='balanced') ·
category_encoders (OneHotEncoder) · seaborn/matplotlib · Streamlit (deployment)

## Notebook

See [`churn_analysis.ipynb`](./churn_analysis.ipynb) — narrated section by section.
