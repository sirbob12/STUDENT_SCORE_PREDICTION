from pathlib import Path

readme_content = """
# 📊 Study Hours vs. Exam Score Prediction App

This project is a simple machine learning API built with **FastAPI**. It uses a **Linear Regression** model to predict a student’s exam score based on the number of hours they studied.

---

## 🛠 Tech Stack

- **Python**
- **Scikit-Learn**
- **FastAPI**
- **Joblib**
- **Uvicorn**

---

## 💡 Project Structure


---

## 📈 How the Model Works

We generated synthetic data where:
A Linear Regression model was trained on this data and saved as `prediction_model.pkl`.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/price-prediction-app.git
cd price-prediction-app


### 2. Create a virtual environment and activate it
python -m venv venv
# On Windows:
venv\\Scripts\\activate
# On Mac/Linux:
source venv/bin/activate


### 3. Install dependencies
pip install -r requirements.txt

### 4. Start the fastApi server
cd app
uvicorn main:app --reload


