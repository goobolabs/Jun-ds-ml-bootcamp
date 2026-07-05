#  Regression —Theory and Practice

## 1. Introduction to Regression

### What is Regression in Machine Learning?
In machine learning, regression analysis is a statistical technique that predicts continuous numeric values based on the relationship between independent and dependent variables. The main goal of regression analysis is to plot a line or curve that best fit the data and to estimate how one variable affects another.
Regression analysis is a fundamental concept in machine learning and it is used in many applications such as forecasting, predictive analytics, etc.

### How is it Different from Classification?
Although both regression and classification fall under supervised learning and require labeled data to train, they differ fundamentally in the mathematical structure of what they are trying to predict:

* **Output Space:** Regression models output a continuous numerical value anywhere along a real number spectrum (for example, predicting a specific car price like \$12,500.50 or a precise temperature like 32.4°C). Classification models, on the other hand, output discrete, categorical class labels (such as predicting "Spam" vs. "Not Spam", or classifying an image as a "Cat", "Dog", or "Car").
* **Evaluation Metrics:** We evaluate regression models by measuring the exact numerical distance or variance between the prediction and the actual value (using metrics like MAE, MSE, or RMSE). For classification, we evaluate models based on decision boundaries and correct vs. incorrect match counts (using metrics like accuracy, precision, recall, and F1-score).
* **Algorithmic Goal:** A regression algorithm looks for a line, curve, or high-dimensional hyperplane of best fit that passes smoothly through or near the data points. A classification algorithm looks for a distinct decision boundary or wall that cleanly slices the feature space to separate different classes from each other.

### Real-Life Examples
* **Real-Life Example of Regression:** Predicting the market value of a house based on its square footage, the number of bedrooms, the crime rate of the neighborhood, and its distance from schools. The output is a continuous monetary figure.
* **Real-Life Example of Classification:** Building a medical diagnostic tool that takes patient health vitals and predicts whether a tumor is "Malignant" or "Benign". The output belongs strictly to one of two discrete classes.



## 2. Types of Regression

### Linear Regression
* **How it Works:** Linear Regression models a direct relationship between a single independent predictor ($x$) and a continuous target ($y$) by fitting a straight line through our data coordinates. Mathematically, it takes the form:
  $$y = \beta_0 + \beta_1 x + \epsilon$$
  where $\beta_0$ is the y-intercept, $\beta_1$ is the structural slope coefficient, and $\epsilon$ represents random error. The line is typically calculated using Ordinary Least Squares (OLS), which minimizes the sum of the squared vertical distances between our observed points and the line itself.
* **Real-World Use Case:** Estimating a person's systolic blood pressure based exclusively on their biological age.
* **Main Advantages:** It is incredibly simple to implement, extremely fast to train computationally, and provides clear, transparent insights into feature correlations.
* **Main Limitations:** It strictly assumes a straight-line relationship; if the real-world data patterns are curved or non-linear, the model fails completely. It is also highly sensitive to outliers, which can easily tilt the line of best fit.

### Multiple Linear Regression
* **How it Works:** Multiple Linear Regression extends simple linear regression by mapping a target variable against two or more independent features at the exact same time. The governing equation is:
  $$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$
  Instead of drawing a 2D line, it projects a multi-dimensional flat surface (a plane or hyperplane) through a high-dimensional feature space, allowing us to isolate the individual impact of each feature while holding all other variables constant.
* **Real-World Use Case:** Predicting a vehicle's fuel efficiency (Miles Per Gallon) using a combination of engine size, vehicle curb weight, horsepower, and aerodynamic drag coefficients.
* **Main Advantages:** It allows for much more realistic real-world modeling because it can process multiple concurrent factors at once, and it quantifies the relative predictive strength of each feature individually.
* **Main Limitations:** It is highly vulnerable to multicollinearity (a condition where independent features are too tightly correlated with each other), which destabilizes the model's coefficients. It also requires a significantly larger sample size to remain reliable.

### Polynomial Regression
* **How it Works:** Polynomial Regression models non-linear, curved relationships by transforming our independent features into polynomial terms up to a specified degree ($n$). The equation looks like this:
  $$y = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_n x^n + \epsilon$$
  Even though the line curves when plotted in a standard coordinate space, it is still statistically considered a form of *linear* regression because the unknown parameters ($\beta$) enter the equation linearly, meaning we can still use standard linear optimization solvers to solve it.
* **Real-World Use Case:** Modeling the growth rate of bacterial populations or viral spread over time, which naturally follows an exponential or parabolic curve rather than a straight line.
* **Main Advantages:** It is highly flexible and capable of capturing complex, curvilinear data distributions that traditional straight lines cannot fit.
* **Main Limitations:** It is highly prone to severe overfitting, especially at the outer edges of our data range, if the polynomial degree is set too high. It can also introduce erratic oscillations into the curve when encountering noise or outliers.


## 3. Regression Metrics

### Definition and Explanation
* **Mean Absolute Error (MAE):** MAE calculates the absolute average of the differences between our actual values and the model's predictions:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
  It measures the direct average error magnitude without favoring or penalizing specific error sizes, treating all errors proportionally.
* **Mean Squared Error (MSE):** MSE computes the average of the *squared* differences between actual and predicted values:
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
  By squaring the distance, it penalizes larger errors much more heavily than smaller ones, making it an excellent metric for catching dangerous outliers.
* **Root Mean Squared Error (RMSE):** RMSE is simply the square root of the MSE:
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$
  It converts the heavy squared error penalty back into the original units of our target variable, making it much easier to interpret practically while maintaining its sensitivity to large errors.
* **Coefficient of Determination ($R^2$):** $R^2$ measures the proportion of overall variance in our target variable that can be explained by our independent features:
  $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
  An $R^2$ score of $1.0$ means perfect prediction, $0.0$ means the model is just guessing the global average value, and a negative score means our model is performing worse than a basic horizontal average baseline.

### Comparison Table

| Metric | Units | Sensitivity to Large Errors | Practical Meaning |
| :--- | :--- | :--- | :--- |
| **MAE** | Same as target variable (e.g., Dollars, KM) | **Linear / Uniform:** Treats small errors and large errors completely proportionally. | The average expected distance between our prediction and the true value. |
| **MSE** | Squared units of the target (e.g., $\text{Dollars}^2$) | **Exponential / Severe:** Highly sensitive; heavily amplifies and penalizes large errors. | The average squared variance of errors; difficult to interpret directly due to squared units. |
| **RMSE** | Same as target variable (e.g., Dollars, KM) | **High:** Strongly influenced by large errors, but scales the final result back to the original unit. | The standard deviation of the residuals (prediction errors). |
| **$R^2$** | Dimensionless (Scale from $-\infty$ to $1.0$) | **Context-Dependent:** Reflects how well the overall variance is captured relative to a baseline average. | The percentage of target variation successfully explained by the model's features. |



## 4. Underfitting and Overfitting

### Definitions
* **Underfitting:** Underfitting happens when our machine learning model is too simple to capture the underlying structure of the data. It suffers from high bias and low variance. This means it performs poorly on both the training data and unseen testing data because it completely failed to learn the true underlying patterns.
* **Overfitting:** Overfitting happens when our model is overly complex and memorizes both the underlying structure *and* the random noise present in the training dataset. It suffers from high variance and low bias, resulting in near-perfect performance on the training data but failing completely to generalize to new testing data.

### Causes in Polynomial Regression
In Polynomial Regression, overfitting is almost always caused by assigning an excessively high degree ($n$) to our model relative to the actual complexity of the data. When the polynomial degree is dialed up unnecessarily, the model gains too many degrees of freedom. Instead of learning a smooth, generalized trajectory, the curve begins to flex, oscillate, and twist erratically just to force its way directly through every single noisy training point and outlier.

### Methods to Prevent Overfitting
1. **Regularization (Lasso / Ridge / ElasticNet):** This introduces a mathematical penalty term directly into our loss function to constrain the size of the regression coefficients. Ridge ($L_2$) shrinks coefficients close to zero, while Lasso ($L_1$) forces non-essential coefficients exactly to zero, effectively acting as an automatic feature selector.
2. **Cross-Validation ($K$-Fold):** This splits our training data into $K$ equal subsets (folds). The model trains on $K-1$ folds and validates on the remaining fold, repeating this process $K$ times. This ensures our parameters are tuned against a rotating validation sample rather than memorizing a single fixed training split.
3. **Feature Reduction / Dimensionality Control:** By using correlation matrices or principal component analysis (PCA), we can remove noisy, irrelevant, or highly redundant features, which strictly prevents the model from building complex paths over meaningless variables.



## 5. Real-World Case Study: Transportation Infrastructure Cost Forecasting

### Goal
The study focuses on minimizing major budgetary overruns by accurately predicting the capital construction costs of regional highway expansion projects before breaking ground.

### Data Used
The researchers collected structural data from over 450 historical infrastructure projects spanning a ten-year window. The input features included: Total track/highway mileage length, localized terrain classification indexes (flat vs. mountainous), estimated soil composition metrics, the number of planned structural intersections or bridges, and localized economic inflation adjustments.

### Type of Regression Applied
The study deployed **Multiple Linear Regression** alongside a secondary **Polynomial Regression (Degree 2)** transformation to account for non-linear scale complexities associated with extreme highway lengths and rugged mountainous terrains.

### Key Results and Insights
While simple linear equations completely failed to adapt to high-altitude project profiles, the integrated Multiple Linear Regression model achieved a robust $R^2$ score of $0.81$. 

The model revealed that the inclusion of polynomial interaction terms—specifically multiplying terrain complexity by project length—successfully captured non-linear cost escalations that had previously caused massive budgetary blind spots. Implementing this regression framework into the pre-planning phase allowed municipal authorities to drastically reduce average infrastructure budgetary overruns from an historical $24\%$ margin down to a controlled $6.5\%$.



## References
* James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning: with Applications in R*. Springer.
* Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis*. John Wiley & Sons.
* Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.