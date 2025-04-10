# Customer Clustering

This app has been built using Streamlit and deployed with Streamlit Community Cloud.

🔗 **Visit the app here**: [https://unsupervisedclusteringsolution-lr59w4aqiuswl6pssz3299.streamlit.app/]  
🔐 **Password** (if needed): `streamlit`

---

## 📋 Description

This app segments mall customers using unsupervised clustering based on income and spending habits.

---

## 📁 Dataset

The model is trained on a structured dataset with features such as:
- Age
- Annual Income
- Spending Score

---

## ⚙️ Technologies Used

- **Streamlit** – For building the interactive web application  
- **Scikit-learn** – For model training and evaluation  
- **Pandas & NumPy** – For data preprocessing and manipulation  
- **Matplotlib & Seaborn** – For data visualization and exploration (optional)

---

## 🤖 Model Summary

Applies KMeans clustering with Elbow and Silhouette methods to determine the optimal number of clusters.

---

## 🚀 Future Enhancements

- Add support for additional datasets  
- Incorporate explainability tools like SHAP or LIME  
- Add charts to visualize user inputs and predictions

---

## 🧪 Local Installation

```bash
git clone https://github.com/zoezoe513/Unsupervised_Clustering_Solution
cd customer_clustering_app
python -m venv env
source env/bin/activate  # On Windows use `env\\Scripts\\activate`
pip install -r requirements.txt
streamlit run app.py
```

---

Thanks for using **Customer Clustering**! 🙌  
Feel free to contribute or share your feedback.
