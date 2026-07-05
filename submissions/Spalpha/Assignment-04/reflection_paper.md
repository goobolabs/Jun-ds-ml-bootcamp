# Reflection Paper — Regression Analysis


## 1. What Did You Implement?
In the practical segment of this assignment, I built and executed an end-to-end machine learning pipeline within my Jupyter Notebook (`car_price_prediction.ipynb`) to predict used car prices[cite: 2, 3]. Using the pre-processed dataset `car_l3_clean_ready.csv`, I completed the following core steps:
* **Target and Feature Engineering:** I set `Price` as my target variable ($y$) and isolated the feature matrix ($X$) by explicitly dropping both the `Price` column and its log-transformed version (`LogPrice`) to ensure there was absolutely no data leakage[cite: 2, 3].
* **Data Splitting:** I partitioned the clean dataset into an 80% training set to fit my models and a 20% testing set for validation[cite: 2, 3]. I used `random_state=42` to guarantee strict reproducibility every time the code runs[cite: 2, 3].
* **Model Training:** I initialized and trained two entirely different machine learning architectures: a baseline, parametric `LinearRegression` model and a non-parametric, ensemble-based `RandomForestRegressor` configured with 100 decision trees[cite: 2, 3].
* **Evaluation Framework:** I wrote a custom helper function named `print_metrics` using `scikit-learn` to compute and clean-format the key evaluation diagnostics: Coefficient of Determination ($R^2$), Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE)[cite: 2, 3].


## 2. Comparison of Models & Sanity Check
When I did a quick sanity check by comparing the actual prices against individual predictions on the test partition, I noticed a massive discrepancy in how both models were handling the data[cite: 2].

Looking closely at the dataset, there is a large sequence of vehicles with a fixed floor price of exactly \$1,500.0[cite: 2]. Despite having identical prices, these cars have completely different features—such as heavily varying mileages (`Odometer_km`), different ages (`car_age`), and contrasting accident histories[cite: 2]. 
* My **Linear Regression** model tried to draw a flat hyper-plane right through these points, which forced it to overcorrect heavily and produce highly unrealistic numbers[cite: 2].
* My **Random Forest** model attempted to group these instances into local leaf nodes based on specific feature splits, but because the underlying target values were so heavily distorted and decoupled from the features, its localized averages generated highly erratic predictions on unseen data[cite: 2].

Ultimately, neither model gave realistic or reliable results during my manual sanity check because of these artificial patterns baked into the target column[cite: 2].


## 3. Understanding Random Forest
In my own words, a **Random Forest** is an ensemble learning algorithm that hooks up multiple individual decision trees to create a much more stable and accurate predictor[cite: 3]. Instead of relying on a single tree—which easily overfits and panics when it sees new data—Random Forest injects two layers of randomness to build a diverse "forest" of trees:
1. **Bootstrap Aggregating (Bagging):** Each tree trains on a unique, randomly sampled subset of the training rows, picked with replacement[cite: 3]. 
2. **Feature Randomness:** When a tree splits a node, it doesn't look at all features; it only evaluates a random subset of them[cite: 3].

Once all 100 trees (`n_estimators=100`) are fully grown, they essentially "vote" on the final output[cite: 3]. For a regression task like this one, the Random Forest takes the individual outputs of all 100 trees and calculates their mathematical average[cite: 3]. This cooperative approach smooths out the high variance of individual trees and makes the overall model way more robust[cite: 3].


## 4. Metrics Discussion
The actual evaluation metrics generated in my notebook revealed some very rough, yet highly insightful numbers[cite: 2]:

* **Linear Regression:** $R^2 = -0.0104$ | $\text{MAE} = 7,211.62$ | $\text{RMSE} = 24,705.79$[cite: 2]
* **Random Forest Regressor:** $R^2 = -0.0891$ | $\text{MAE} = 7,084.52$ | $\text{RMSE} = 25,649.99$[cite: 2]

### My Analysis of the Metrics:
* **The Negative $R^2$ Problem:** Seeing a negative $R^2$ score means both of my models performed *worse* than a lazy baseline that simply guesses the global average price of the cars for every single row[cite: 2]. 
* **Overfitting vs. Rigidity:** Interestingly, the Random Forest model actually scored a worse $R^2$ ($-0.0891$) and a higher RMSE than Linear Regression[cite: 2]. This reveals a specific weakness: because Random Forest is highly flexible, it aggressively overfit the heavy noise and conflicting signals within the training features[cite: 2]. Linear Regression, being strictly bound to a rigid linear formula, suffered slightly less from this variance, though its massive MAE proves it’s just as useless here[cite: 2].
* **Data Bottlenecks:** This outcome proves that there is a fundamental structural issue inside `car_l3_clean_ready.csv`[cite: 2]. The mathematical relationships we expect to see (like higher mileage leading to lower prices) are completely broken or heavily masked by the artificial distribution of the target variable[cite: 2].


## 5. My Findings and Personal Preference
Looking at these metrics objectively, **neither model is anywhere near ready for a real-world production environment**[cite: 2]. Relying on them right now would cause worse financial mispricing than simply picking the average car price out of a hat every time[cite: 2].

However, if I can clean up this dataset, fix the target distribution, and re-run this experiment in the future, I fundamentally prefer the **Random Forest Regressor** framework[cite: 2, 3]. The used car market is naturally non-linear[cite: 2]. Factors like geographic location (`Location_Rural`) or accident rates interact with a car's age and mileage in highly complex, non-linear ways[cite: 2]. A simple linear equation cannot capture those multi-dimensional relationships without me manually coding complex interaction terms[cite: 2].

To make Random Forest work up to its true potential next time, my immediate focus must be on fixing the skewed target variable, addressing the artificial \$1,500 floor limit, and applying proper feature scaling to stop the trees from chasing noise[cite: 2].