# 🩺 Healthcare Quality Prediction App

AI-powered healthcare quality prediction application built with **Machine Learning** and **Streamlit**.
This app predicts the risk of **PoorCare** using clinical and healthcare-related variables.

## 🚀 Project Overview

This project uses a **Logistic Regression Machine Learning model** to predict whether a patient is at **high risk of poor healthcare quality** based on multiple medical indicators.

The application provides:

* Interactive UI using Streamlit
* Real-time prediction
* Probability score
* Risk classification (High / Low)

---

## 🧠 Machine Learning Model

* Model: Logistic Regression
* Pipeline: StandardScaler → Logistic Regression
* Threshold: 0.5
* Class Weight: Balanced

The model predicts **PoorCare risk** based on:

* ERVisits
* OfficeVisits
* Narcotics
* ProviderCount
* NumberClaims
* StartedOnCombination

---

## 🖥️ App Interface

Features:

* Interactive sliders for input values
* Real-time prediction
* Probability output
* Risk classification
* Technical details section

---

## 📂 Project Structure

```
├── healthcareapp.py
├── model_A.pkl
├── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/Healthcare-Quality-Prediction.git
cd Healthcare-Quality-Prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

Or manually install:

```
pip install streamlit pandas scikit-learn
```

---

## ▶️ Run the Application

Run the Streamlit app:

```
streamlit run healthcareapp.py
```

The app will open in your browser automatically.

---

## 📊 Example Prediction

The model outputs:

* Probability of PoorCare
* Risk classification:

  * 0 → Low Risk
  * 1 → High Risk

---

## 🎯 Use Cases

* Healthcare quality monitoring
* Risk prediction
* Medical decision support
* Data science learning project

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* Pickle





