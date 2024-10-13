🚗 Used Car Price Prediction: Machine Learning Model

This repository contains the code and analysis for a Used Car Price Prediction competition.
The goal of the project is to build a predictive model that estimates the price of a used car based on various features such as brand, model, mileage, and more.

🗂️ Dataset Overview
The dataset includes the following key features about used cars:

brand: The car's manufacturer (e.g., Toyota, Honda, Ford)
model: The specific model of the car
model_year: The year the car was manufactured
milage: The total miles the car has been driven
fuel_type: The type of fuel used by the car (e.g., gasoline, diesel, electric)
engine: Engine size or displacement
transmission: Type of transmission (automatic or manual)
ext_col: The exterior color of the car
int_col: The interior color of the car
accident: Whether the car has been involved in an accident (Yes/No)
clean_title: Whether the car has a clean title (Yes/No)
price: The target variable representing the price of the used car

📊 Project Workflow

1. Data Preprocessing:
Handling Missing Values: Missing data was handled for features such as milage, engine, and model_year to ensure model robustness.
Feature Transformation:
Categorical features such as brand, model, fuel_type, transmission, ext_col, and int_col were encoded using one-hot encoding.
Numeric features like milage and engine were scaled to normalize their distributions.
Outlier Detection and Removal: Outliers in features like price, milage, and engine were detected and handled to improve model accuracy.

2. Exploratory Data Analysis (EDA):
Visualized key relationships between variables, such as how mileage affects price and how different brands have varying average prices.
Analyzed distributions of categorical variables (e.g., fuel types, transmission types) and their impact on the target variable.

3. Feature Engineering:
Created new features such as:
Age of the car based on the model_year.
Interaction terms between fuel_type and engine size to capture complex relationships.
Aggregated accident and clean_title information to form a more comprehensive damage score.
4. Model Building:
Multiple machine learning models were tested, including:
Linear Regression: A baseline model for prediction.
Random Forest Regressor: A tree-based model to capture non-linear relationships.
SVC : 

XGBoost: A boosting algorithm that provided the best performance.
Hyperparameter tuning using GridSearchCV and RandomizedSearchCV to optimize model parameters like n_estimators, max_depth, and learning_rate.

6. Model Evaluation:
The models were evaluated using RMSE (Root Mean Squared Error) as the primary metric for regression.
Cross-validation was performed to ensure that the model generalizes well on unseen data.

📈 Key Insights
Mileage and age of the car are significant factors that influence the price. Older cars with higher mileage typically have lower prices.
The brand of the car plays a crucial role, with premium brands (e.g., BMW, Mercedes) generally having higher prices.
Cars with a clean title and no accidents are valued more highly in the used car market.

🛠️ Tech Stack
Python: Core programming language used for data processing and modeling.
Pandas, NumPy: For data manipulation and analysis.
scikit-learn, XGBoost: For building machine learning models.
Matplotlib, Seaborn: For data visualization.
