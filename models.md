# 🧠 Scikit-Learn Models — Study Notes

---

## 🌳 1. Tree-Based Models

### Decision Tree (`DecisionTreeClassifier / Regressor`)
**Idea:**  
Splits data using rules (like a flowchart)

**How it works:**
- Chooses best feature to split data
- Repeats until it reaches a decision

**Strengths:**
- Easy to understand
- Works with non-linear data
- No scaling needed

**Weaknesses:**
- Overfits easily (memorizes data)

**Use when:**
- You need interpretability  
- You want simple logic rules  

**Example:**  
Loan approval system:
> If income > 50k and credit score > 700 → approve

---

### Random Forest (`RandomForestClassifier / Regressor`)
**Idea:**  
Many trees → vote (classification) or average (regression)

**How it works:**
- Builds many decision trees
- Each tree sees random data/features
- Combines results

**Strengths:**
- Very strong performance
- Reduces overfitting
- Works on most datasets

**Weaknesses:**
- Harder to interpret
- Slower than a single tree

**Use when:**
- You want a reliable default model  
- Data is messy or complex  

**Example:**  
Fraud detection system using many signals  

---

### Gradient Boosting (`GradientBoosting`)
**Idea:**  
Models learn from previous mistakes

**How it works:**
- Build tree → check errors  
- Next tree focuses on those errors  
- Repeat

**Strengths:**
- Very high accuracy
- Great for structured data

**Weaknesses:**
- Slower to train
- Needs tuning

**Use when:**
- You want best performance  
- You’re okay with complexity  

**Example:**  
Pricing models, competitions  

---

## 📏 2. Linear Models

### Linear Regression
**Idea:**  
Fits a straight line to predict numbers

**Formula idea:**  
y = mx + b

**Strengths:**
- Simple
- Fast
- Interpretable

**Weaknesses:**
- Can’t handle complex relationships

**Use when:**
- Relationship is roughly linear  

**Example:**  
House price vs size  

---

### Logistic Regression
**Idea:**  
Linear model for classification (outputs probability)

**How it works:**
- Uses sigmoid function → outputs 0–1 probability  

**Strengths:**
- Fast
- Good baseline
- Works well with clean data

**Weaknesses:**
- Struggles with complex patterns

**Use when:**
- Binary classification problems  

**Example:**  
Spam vs not spam  

---

## 📍 3. Distance-Based Models

### K-Nearest Neighbors (KNN)
**Idea:**  
Look at closest data points

**How it works:**
- Find K nearest neighbors
- Majority vote (classification)
- Average (regression)

**Strengths:**
- Simple
- No training phase

**Weaknesses:**
- Slow for large data
- Needs scaling
- Sensitive to noise

**Use when:**
- Small datasets  
- Local patterns matter  

**Example:**  
Recommending similar products  

---

## 📈 4. Support Vector Machines (SVM)

### SVC / SVR
**Idea:**  
Find best boundary (maximum margin)

**How it works:**
- Draws line/plane separating classes
- Can use kernels for complex shapes

**Strengths:**
- Works well in high dimensions
- Powerful for complex data

**Weaknesses:**
- Slow for large datasets
- Needs scaling
- Harder to tune

**Use when:**
- Medium-sized datasets  
- Complex boundaries  

**Example:**  
Image classification  

---

## 🧩 5. Clustering Models

### KMeans
**Idea:**  
Group data into K clusters

**How it works:**
- Pick K centers
- Assign points to nearest center
- Update centers

**Strengths:**
- Fast
- Easy to use

**Weaknesses:**
- Must choose K
- Assumes circular clusters

**Use when:**
- You know number of groups  

**Example:**  
Customer segmentation  

---

### DBSCAN
**Idea:**  
Cluster based on density

**How it works:**
- Groups dense regions
- Marks sparse points as noise

**Strengths:**
- Finds weird shapes
- Handles outliers well

**Weaknesses:**
- Hard to tune parameters

**Use when:**
- Data has irregular clusters  

**Example:**  
Anomaly detection  

---

## 📉 6. Dimensionality Reduction

### PCA (Principal Component Analysis)
**Idea:**  
Reduce number of features

**How it works:**
- Combines features into new ones
- Keeps most important variance

**Strengths:**
- Speeds up models
- Helps visualization

**Weaknesses:**
- Hard to interpret
- Loses some information

**Use when:**
- Too many features  
- Need faster training  

**Example:**  
Reducing 100 variables → 10  

---

## 🧠 Final Mental Summary

- Linear models → simple relationships  
- Trees → rule-based decisions  
- Random Forest → strong default  
- Boosting → best performance  
- KNN → similarity-based  
- SVM → boundary optimization  
- Clustering → find hidden groups  
- PCA → compress data  

---

## 🎯 Quick Strategy

- Start with **Logistic / Linear**
- Use **Random Forest** if unsure  
- Use **Gradient Boosting** for best results  
- Use **KMeans** if no labels  