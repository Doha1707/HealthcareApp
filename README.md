# 🩺 Healthcare Quality Prediction App

A Machine Learning web application built with **Streamlit** to predict healthcare quality risk using clinical data.

This project uses a **Logistic Regression model** to predict whether a patient is at risk of **PoorCare** based on healthcare usage and treatment variables.

---

# 🚀 Features

* Interactive Streamlit interface
* Real-time prediction
* Probability score output
* Risk classification (High / Low)
* Clean and user-friendly dashboard

---

# 🧠 Machine Learning Model

Model Used:

* Logistic Regression

Pipeline:

* StandardScaler
* Logistic Regression

Prediction Target:

* **PoorCare** (0 = Low Risk, 1 = High Risk)

---

# 📊 Input Variables

The model uses the following features:

* ERVisits
* OfficeVisits
* Narcotics
* ProviderCount
* NumberClaims
* StartedOnCombination

---

# 📂 Project Structure

```
├── healthcareapp.py     # Streamlit application
├── Logreg.py            # Model training script
├── model_A.pkl          # Saved trained model
├── Quality.csv          # Dataset
├── README.md            # Project documentation
```

---

# ⚙️ Installation

Clone repository:

```
git clone https://github.com/Doha1707/HealthcareApp.git
cd HealthcareApp
```

Install dependencies:

```
pip install streamlit pandas scikit-learn
```

---

# ▶️ Run the App

Run Streamlit application:

```
streamlit run healthcareapp.py
```

The application will open automatically in your browser.

---

# 📈 Example Output

The application displays:

* Probability of PoorCare
* Risk classification:

  * 0 → Low Risk
  * 1 → High Risk

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* Pickle

---

# 🎯 Project Purpose

This project demonstrates:

* Machine Learning model deployment
* Healthcare data analysis
* Interactive AI applications
* End-to-end AI pipeline

---

# 📌 Skills Demonstrated

* Machine Learning
* Data Preprocessing
* Model Deployment
* Streamlit App Development
* Data Analysis
