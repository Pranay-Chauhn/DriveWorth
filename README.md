# DriveWorth: Used Car Price Prediction

Welcome to **DriveWorth** – A project designed topredict the price of Used-Cars in USA. Aiming to empower buyers and sellers with accurate car valuations. My goal is to help users determine the current worth of a car, facilitating fair negotiations and informed decision-making.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation and Objectives](#motivation-and-objectives)
- [Dataset and Features](#dataset-and-features)
- [Data Preprocessing and Feature Engineering](#data-preprocessing-and-feature-engineering)
- [Modeling Approach](#modeling-approach)
- [Model Evaluation](#model-evaluation)
- [Results and Insights](#results-and-insights)
- [Deployment](#deployment)
- [Future Roadmap](#future-roadmap)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview
DriveWorth is built to answer a very practical question: *What is the current market price of my used car?* By leveraging a rich dataset of vehicle attributes and historical sales data, our machine learning model predicts car prices, providing a confidence interval for its prediction. This assists both buyers and sellers by:
- Eliminating guesswork in pricing.
- Helping negotiate fair prices.
- Offering insights into market trends.

---

## Motivation and Objectives
In a competitive market like India’s used car industry, price uncertainty can hinder transactions. My objectives are to:
- **Provide a data-driven estimate:** Eliminate subjective pricing.
- **Improve transparency:** Give a clear price range to boost buyer and seller confidence.
- **Increase efficiency:** Automate the price prediction process, saving time and effort in negotiations.

---

## Dataset and Features
This project uses a comprehensive dataset containing key features such as:
- **Car Identification:** Brand, Model, Model Year
- **Vehicle Specifications:** Mileage, Engine, Transmission, Horsepower, Engine Size, Cylinders
- **Condition Indicators:** Exterior/Interior Color, Accident History, Clean Title
- **Market Data:** Listed Price, Fuel Type, Additional Technical Attributes

*For more details, please refer to the [data description file](link-to-data-description) included in this repository.*

---

## Data Preprocessing and Feature Engineering
We applied a series of preprocessing steps including:
- **Handling Missing Values:** Imputation techniques (mode-based for categorical and ML-based for numerical features).
- **Feature Engineering:** Extracted the usefull information from engine(172.0HP 1.6L 4 Cylinder Engine Gasoline Fuel), transmission('4-Speed Automatic', '7-Speed M/T').eg : number of gears , engine size , Transmission  type , HorsePower of car , number of cylinders, etc
- **Feature Scaling:** RobustScaler was used for continuous features to handle outliers.
- **Target Transformation:** Since car prices are heavily skewed, we applied a `log1p` transformation on the price variable to stabilize variance and improve model performance.
- **One-Hot Encoding:** Categorical features were transformed using `pd.get_dummies` to prepare the data for our ML models.
- **Feature Selection:** Applied feauter selection using f-regression, mutual info regresision, xgboost feature imnportance and selected top 82 features from 553 features 

These steps were crucial in improving the quality of our features, ultimately enhancing the predictive capability of models.

---

## Modeling Approach
I experimented with various regression models including:
- **Linear Regression, Ridge, Lasso** – For baseline comparisons.
- **Tree-based Models:**
  - **Random Forest Regressor**
  - **XGBoost Regressor**
  - **CatBoost Regressor**
- **Other Ensemble Techniques:** AdaBoost Regressor and K-Neighbors Regressor

After careful evaluation, our top models based on R² scores were:
1. **CatBoost Regressor** – R² ≈ 0.6777
2. **XGBoost Regressor** – R² ≈ 0.6751
3. **Random Forest Regressor** – R² ≈ 0.6451

---

## Model Evaluation
I use standard regression metrics to evaluate model performance:
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**
- **R² Score**

*For models trained on log-transformed prices, we apply the inverse transform using `np.expm1()` before metric calculation to get interpretable values in dollars.*

Evaluation showed that transforming the target and scaling features significantly improved generalization on the test data compared to models trained on raw data.

---

## Results and Insights
- The **tree-based models** (XGBoost, CatBoost) performed better on scaled data.
- **CatBoost** slightly outperformed **XGBoost** in terms of R², indicating its robustness for our dataset.
- **Scaling & Target Transformation:** Our results confirmed that applying a `log1p` transformation to the price and scaling features with RobustScaler helps in reducing error variance.
- **Confidence Intervals:** By computing RMSE on the transformed target and reverting via `np.expm1()`, I can provide a meaningful price range (e.g., ₹[Lower Bound] – ₹[Upper Bound]).

---

## **Hyperparameter Tunning:** 
- Further Refined Model Using Techniques like RandomizedSearchCV .
- Applied RandomizedSearchCV on CatboostRegressoor & Xgboostregressor using wide range of params.
- Results Shows Xgboost Outperformed Catboost
    - Best score for CatBoost: 0.6800732943057692
    - Best params for CatBoost: {'subsample': 0.7, 'learning_rate': 0.1, 'l2_leaf_reg': 9, 'iterations': 1000, 'depth': 6}
    - Best score for XGBoost: 0.6810259882267823
    - Best params for XGBoost: {'subsample': 0.8, 'reg_lambda': 5, 'reg_alpha': 0.5, 'n_estimators': 1000, 'max_depth': 6, 'learning_rate': 0.03, 'colsample_bytree': 1.0}
---

## Deployment
The model is deployed using FastAPI, enabling:
- **Real-time predictions:** Users can send car attributes via an API, and receive price predictions instantly.
- **Enterprise-grade deployment:** Options for on-premise deployment ensure data security and compliance for enterprise customers.

See the [Deployment Guide](link-to-deployment-guide) for more details.

---

## Future Roadmap
- **Hyperparameter Tuning:** Further refine models using techniques like GridSearchCV to narrow range of params .
- **Model Performance:** Increase the model performance by 20%
- **UI Enhancements:** Build interactive dashboards to visualize model performance and data trends.
- **CI/CD Integration:** Automate model retraining and deployment processes.
- **User Feedback:** Integrate feedback mechanisms to continuously improve predictions.

---

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Pranay-Chauhn/DriveWorth.git
   cd DriveWorth
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables:**  
   Create a `.env` file as needed.
5. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Usage
- **API Documentation:**  
  Visit `http://127.0.0.1:8000/docs` to interact with the API via Swagger UI.
- **Prediction:**  
  Use the web interface or API endpoint `/predict` to submit car details and receive a predicted price along with a confidence range.
- **Local Testing:**  
  Test prediction logic using the provided Jupyter notebooks in the `Notebook/` directory.

---

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Open a pull request explaining your changes.

---

## Contact
For questions or collaboration, please contact:
- **Email:** [pranaychauhan663@gmail.com]
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/pranay-chauhan-0ab85a263/
)
---
