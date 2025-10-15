# healthcareapp.py
import streamlit as st
import pickle
import pandas as pd
 
st.set_page_config(page_title="Quality Prediction", page_icon="🩺", layout="centered")
 
@st.cache_resource
def load_model():
    with open("model_A.pkl", "rb") as f:
        saved = pickle.load(f)
    return saved["model"], saved["features"]
 
model_A, feature_cols = load_model()
 

 
def main():
    st.title("🩺 Quality Prediction App (Logistic Regression)")
    st.markdown("Prédit *PoorCare* à partir de variables cliniques.")
 
    st.sidebar.header("Entrées")
    ERVisits = st.sidebar.slider("ERVisits", 0, 20, 1)
    OfficeVisits = st.sidebar.slider("OfficeVisits", 0, 60, 13)
    Narcotics = st.sidebar.slider("Narcotics", 0, 100, 4)
    ProviderCount = st.sidebar.slider("ProviderCount", 1, 120, 23)
    NumberClaims = st.sidebar.slider("NumberClaims", 0, 400, 43)
    StartedOnCombination = st.sidebar.selectbox("StartedOnCombination", [0, 1], index=1)
 
    user_input = pd.DataFrame(
        {
            "ERVisits": [ERVisits],
            "OfficeVisits": [OfficeVisits],
            "Narcotics": [Narcotics],
            "ProviderCount": [ProviderCount],
            "NumberClaims": [NumberClaims],
            "StartedOnCombination": [int(StartedOnCombination)],
        }
    )[feature_cols]  # garantit le bon ordre
 
    st.subheader("Tes entrées")
    st.dataframe(user_input, use_container_width=True)
 
    st.divider()
    st.subheader("Prédiction")
 
    if st.button("Predict"):
        proba = float(model_A.predict_proba(user_input)[0, 1])
        y_pred = int(proba >= 0.5)
 
        st.success(f"Probabilité de PoorCare = {proba:.3f} (seuil 0.5)")
        if y_pred == 1:
            st.markdown(
                """
                <div style="background-color:#27AE60;padding:12px;border-radius:12px;">
                  <h4 style="color:white;margin:0;">Prédiction: 1 (risque élevé)</h4>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("Le modèle estime un **risque élevé** de *PoorCare*.")
        else:
            st.markdown(
                """
                <div style="background-color:#2980B9;padding:12px;border-radius:12px;">
                  <h4 style="color:white;margin:0;">Prédiction: 0 (risque faible)</h4>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("Le modèle estime un **risque faible** de *PoorCare*.")
 
        with st.expander("Détails techniqu�es"):
            st.write(
                "- Modèle: LogisticRegression (liblinear, class_weight=balanced)\n"
                "- Pipeline: StandardScaler ➜ LogisticRegression\n"
                "- Seuil de décision: 0.5 (tu peux l’exposer en slider si besoin)"
            )
 
if __name__ == "__main__":
    main()
 