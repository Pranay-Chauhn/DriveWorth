# Data Description for Playground Series S4E9 – Train Dataset

This document describes the dataset used in the DriveWorth project, which aims to predict the price of used cars. The data originates from the Kaggle competition [Playground Series S4E9](https://www.kaggle.com/competitions/playground-series-s4e9/data?select=train.csv). Below is a detailed explanation of each feature in the `train.csv` file.

---

## Overview

The dataset consists of records for used cars and includes various features related to the car's specifications, condition, and market information. These features are used to build machine learning models that estimate the current market price of a second-hand car.

---

## Column Descriptions

- **id**:  
  *Description:* A unique identifier for each car record.  
  *Example:* 1, 2, 3, …  

- **brand**:  
  *Description:* The manufacturer or brand of the car.  
  *Example:* Toyota, Honda, Ford, etc.

- **model**:  
  *Description:* The specific model name of the car.  
  *Example:* Corolla, Civic, Figo, etc.

- **model_year**:  
  *Description:* The year in which the car model was manufactured.  
  *Example:* 2015, 2018, 2020, etc.

- **milage**:  
  *Description:* The total distance (in kilometers or miles) that the car has been driven.  
  *Example:* 45000, 75000, etc.

- **fuel_type**:  
  *Description:* The type of fuel the car uses.  
  *Example:* Petrol, Diesel, Electric, Hybrid, etc.

- **engine**:  
  *Description:* Details related to the engine such as engine configuration or capacity (if provided).  
  *Example:* 2.0L, 1.6L, etc.

- **transmission**:  
  *Description:* The mode of transmission used by the car.  
  *Example:* Automatic, Manual, etc.

- **ext_col** (Exterior Color):  
  *Description:* The exterior color of the vehicle.  
  *Example:* Red, Blue, Black, etc.

- **int_col** (Interior Color):  
  *Description:* The interior color of the car.  
  *Example:* Grey, Black, Beige, etc.

- **accident**:  
  *Description:* Indicates whether the car has been involved in any accidents or has reported damage.  
  *Example:* 'None_reported', 'At least 1 accident or damage reported', etc.

- **clean_title**:  
  *Description:* Denotes whether the car has a clean title (i.e., no major issues with ownership or damage history).  
  *Example:* Yes, No.

- **price**:  
  *Description:* The listed price of the car. Note that for modeling purposes, this target variable is often transformed (e.g., using `log1p`) to stabilize variance.  
  *Example:* 250000, 350000, etc.

- **trans_type**:  
  *Description:* Additional transmission details or classification, if available.  
  *Example:* Could be used to further categorize transmission types.

- **gear**:  
  *Description:* The number of gears in the vehicle.  
  *Example:* 5, 6, 8, etc.

- **horsepower**:  
  *Description:* The power output of the car’s engine, typically measured in horsepower (HP).  
  *Example:* 130, 150, etc.

- **engine_size**:  
  *Description:* The size or displacement of the engine, usually measured in liters (L).  
  *Example:* 1.8, 2.0, etc.

- **cylinders**:  
  *Description:* The number of cylinders the car’s engine has.  
  *Example:* 3, 4, 6, 8, etc.

- **test_train**:  
  *Description:* A flag indicating whether a record belongs to the training set or test set (if applicable). This is useful for experiments and ensuring proper splits during modeling.  
  *Example:* 'train' or 'test'

---

## Additional Notes

- **Target Transformation**:  
  For modeling, the `price` field is often transformed using `log1p` to handle skewness, and predictions are later inverse-transformed using `expm1` for interpretability.

- **Feature Engineering & Scaling**:  
  Many features (e.g., `milage`, `horsepower`) have been processed and scaled to improve model performance. Please refer to the project documentation for details on the preprocessing steps.

- **Usage in Models**:  
  The selected features, along with the engineered features, are used to train various regression models (e.g., Random Forest, XGBoost, CatBoost) to predict the price of a used car.

---

## Conclusion

This data forms the foundation for our DriveWorth project. By understanding these features, their transformations, and their roles in the predictive modeling process, we can derive meaningful insights that help both buyers and sellers make well-informed decisions.

For more details and the complete project code, please visit the [DriveWorth GitHub repository](https://github.com/Pranay-Chauhn/DriveWorth).

---

*Feel free to update or expand upon this data description as the project evolves!*
