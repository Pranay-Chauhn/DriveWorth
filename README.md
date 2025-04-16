# DriveWorth: A Used Car Price Predictor

DriveWorth is a comprehensive data science project aimed at predicting the price of second-hand cars. Built by a passionate data scientist, this project leverages machine learning techniques and real-world car features to deliver accurate valuations. Whether you’re a buyer looking for a fair deal or a seller wanting to price your vehicle competitively, DriveWorth helps you make informed decisions.

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Model Evaluation & Results](#model-evaluation--results)
- [Future Roadmap](#future-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

DriveWorth is designed to streamline the process of determining a car’s market value by using advanced ML models. The project focuses on:
- Predicting prices based on key features like **brand, model, mileage, fuel type, engine, transmission, color, accident history, and more**.
- Transforming skewed data (e.g., using `log1p` for price) and scaling features (e.g., using `RobustScaler`) to improve model performance.
- Providing developers and stakeholders with a robust, enterprise-ready solution that can be deployed on-premises or in the cloud.

---

## Problem Statement

The used car market in India is vast and dynamic. Buyers and sellers often struggle with:
- Establishing the true market worth of a vehicle.
- Negotiating fair prices due to inconsistent valuations.
- Dealing with high variability in features and conditions across vehicles.

DriveWorth solves these challenges by predicting car prices using historical data and advanced machine learning algorithms, thereby providing a reliable basis for negotiation and pricing.

---

## Key Features

- **Accurate Price Prediction**: Leverages models like Random Forest, XGBoost, and CatBoost to deliver reliable estimates.
- **Confidence Interval Generation**: Provides a prediction range (price ± RMSE) to indicate the uncertainty in predictions.
- **Data Preprocessing**: Uses techniques like `log1p` for stabilizing variance in price and robust scaling for handling outliers in numerical features.
- **User-Friendly Interface**: Built with FastAPI and a responsive frontend using Tailwind CSS for an intuitive experience.
- **Flexible Deployment**: Offers options for secure on-premises deployment or cloud-based deployment, ensuring compliance and data privacy.

---

## Tech Stack

- **Frontend**:  
  - HTML5, Tailwind CSS  
- **Backend**:  
  - Python, FastAPI, Uvicorn  
- **Machine Learning**:  
  - scikit-learn, XGBoost, CatBoost, RandomForest  
- **Data Processing**:  
  - Pandas, NumPy  
- **DevOps & Deployment**:  
  - Docker (optional), AWS, Render, or local server deployment  
- **Security & Compliance**:  
  - HTTPS, on-premises deployment options for sensitive data

---

## Project Structure

```
DriveWorth/
├── app/
│   ├── main.py         # FastAPI application entry point
│   ├── predict.py      # Prediction logic and integration with the ML model
│   ├── schemas.py      # Pydantic models for data validation
│   ├── models.py       # Database models (if applicable)
│   ├── utils.py        # Utility functions (e.g., evaluation metrics, RMSE calculation)
├── Notebook/           # Jupyter notebooks for EDA and model training
├── requirements.txt    # Project dependencies
├── README.md           # This file
└── .env.example        # Example environment configuration
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- A virtual environment (recommended)
- Git

### Steps to Set Up Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pranay-Chauhn/DriveWorth.git
   cd DriveWorth
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Copy the `.env.example` to `.env` and update if necessary.

5. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Usage

- **Web Interface**:  
  Access the web interface to input car details and obtain price predictions along with a confidence range.
  
- **API Documentation**:  
  Visit `/docs` on your local server (e.g., [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)) for interactive API documentation provided by FastAPI.

- **Prediction Endpoint**:  
  The endpoint `/predict` accepts car features and returns a JSON response with the predicted price (converted back from log scale using `expm1()`) and a confidence interval.

---

## Model Evaluation & Results

*Evaluation on Scaled and Log-Transformed Data:*
- **XGBRegressor**:
  - Training RMSE (log scale): 0.4355 → Test RMSE (log scale): 0.4574
  - After inverse transformation: Test RMSE is significantly improved compared to the raw model.
- Other models are also evaluated, showing that tree-based models performed slightly better without scaling.
  
*Note:* Detailed performance metrics are calculated using an evaluation function that converts predictions back to the original scale using `np.expm1()`. This ensures all metrics are interpretable in actual rupees.

---

## Future Roadmap

- **Enhance Feature Engineering**: Further refine features for even better model performance.
- **Advanced Hyperparameter Tuning**: Explore techniques like RandomizedSearchCV and GridSearchCV for fine-tuning model parameters.
- **Expand Deployment Options**: Integrate options for Dockerized and cloud-based deployments to scale with enterprise needs.
- **User Interface Improvements**: Continue refining the UI for greater interactivity and ease of use.
- **Continuous Learning**: Implement a feedback loop to retrain models periodically with new data.

---

## Contributing

We welcome contributions from the community! If you’d like to help:
- Fork the repository.
- Create a feature branch.
- Submit a pull request detailing your improvements.
- Please follow the coding standards outlined in our contribution guidelines.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Contact

For any inquiries or collaborations, please contact:
- **Email**: [your-email@example.com]
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)

---

*DriveWorth is developed with passion by a dedicated team of data scientists. We aim to empower users in the used car market by providing accurate price predictions and actionable insights. Thank you for checking out our project!*
```

---

Feel free to modify any sections (e.g., contact information, license, roadmap) based on your actual project details. This README is designed to be human-friendly while providing all the necessary technical information for potential collaborators, stakeholders, or hiring managers.
