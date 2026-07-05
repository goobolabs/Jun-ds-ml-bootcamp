***My Thoughts on the Car Price Project***
**1. What I Did**
I used a cleaned car dataset to predict car prices. I removed the target columns and converted text categories into numbers. Then, I split the data into 80% for training and 20% for testing. I trained two models: Linear Regression and a Random Forest.

**2. Comparing the Models**
When I checked a single car, the guesses were different. The Linear Regression model uses fixed mathematics that can sometimes make unrealistic guesses if a car has unusual features. The Random Forest model was much closer to the real price because it works by looking at groups of similar cars.

**3. Understanding Random Forest**
In my own words, a Random Forest is a team of many individual Decision Trees. During training, each tree looks at a different random part of the data and learns its own rules. When we show it a new car, every tree makes a guess. The Random Forest takes all the guesses, finds the average, and gives us the final answer. This teamwork stops individual trees from making wild mistakes.

**4. Discussion of Scores**
The Random Forest gets a higher R² score and lower error scores (MAE and RMSE) than Linear Regression. This is because car prices do not follow a straight line. Car values drop quickly at first and slow down later. Linear Regression struggles with this because it can only see straight lines, while Random Forest handles curves easily.

**5. My Conclusion**
I prefer the Random Forest model for predicting car prices. Even though it is harder to explain exactly how it calculates every number, it is much more accurate. In the real world, accuracy matters most when buying or selling a car.