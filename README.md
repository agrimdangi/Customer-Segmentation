# Customer-Segmentation
Project on Customer Segmentation

# 🧠 Customer Segmentation using Machine Learning

## 📌 Overview

Customer Segmentation is a machine learning project that groups customers based on their behavior and characteristics.
This project uses clustering techniques to identify distinct customer segments, helping businesses make data-driven decisions.

The model analyzes customer data such as income and spending habits to form meaningful clusters.

---

## 🎯 Objectives

* To segment customers into different groups
* To understand customer behavior patterns
* To apply unsupervised machine learning (clustering)
* To visualize customer groups effectively

---

## 🚀 Features

* 📥 Load and preprocess customer dataset
* 🤖 Apply K-Means Clustering
* 📊 Visualize clusters using graphs
* 🧠 Identify patterns in customer behavior
* 📈 Improve business decision-making

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – data handling
* **Matplotlib** – visualization
* **Scikit-learn** – machine learning
* **NumPy** – numerical operations

---

## 📁 Project Structure

```
customer-segmentation/
│
├── data/
│   └── customers.csv
│
├── output/
│   └── cluster_plot.png
│
├── src/
│   └── main.py
│
├── requirements.txt
├── README.md
```

---

## 📊 Dataset Description

The dataset contains customer details such as:

| CustomerID | Gender | Age | Annual Income | Spending Score |
| ---------- | ------ | --- | ------------- | -------------- |
| 1          | Male   | 19  | 15            | 39             |

* **Annual Income** → Customer earning
* **Spending Score** → Spending behavior (1–100)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Project

```
python src/main.py
```

---

## 🤖 Machine Learning Model

### K-Means Clustering

K-Means is an unsupervised learning algorithm used to group similar data points into clusters.

Steps:

* Choose number of clusters (K)
* Assign points to nearest centroid
* Update centroids
* Repeat until convergence

---

## 📈 Output

* Cluster visualization (scatter plot)
* Customer groups based on spending behavior
* Clear segmentation for analysis

---

## 📌 Example Insights

* High income, high spending customers (premium)
* Low income, low spending customers
* Potential target customers

---

## 🔮 Future Enhancements

* Add real-time dashboard (Streamlit)
* Use advanced clustering (DBSCAN, Hierarchical)
* Deploy as web application
* Add recommendation system

---

## 👨‍💻 Author

**Agrim Dangi**
Student | Developer | Data Enthusiast

---

## ⭐ Conclusion

This project demonstrates how machine learning can be used to analyze customer behavior and help businesses make smarter decisions.

---

## 📎 License

This project is for educational purposes only.
