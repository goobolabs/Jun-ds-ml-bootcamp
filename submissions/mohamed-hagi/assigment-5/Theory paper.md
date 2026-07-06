Haa. Haddii ujeeddadu tahay inaad barato ama diyaariso assignment gaaban, kuwan ayaa ah **qodobada ugu muhiimsan** ee aad diiradda saari karto.

# 1. Introduction to Classification

### What is Classification?

Classification waa hab Machine Learning ah oo lagu saadaaliyo **category (class)** uu xog cusub ka tirsan yahay.

**Examples:**

* Email → Spam / Not Spam
* Loan → Approved / Rejected
* Disease → Positive / Negative

### Classification vs Regression

| Classification      | Regression                |
| ------------------- | ------------------------- |
| Predicts categories | Predicts numerical values |
| Output = Class      | Output = Number           |
| Example: Pass/Fail  | Example: House Price      |

**Real-life Examples**

* **Classification:** Loan approval (Approve or Reject)
* **Regression:** Predicting house prices.

---

# 2. Classification Algorithms

## Logistic Regression

### Basic Idea

Uses probability to classify data into categories.

**Use Case**

* Email spam detection
* Loan approval

**Advantages**

* Simple
* Fast
* Easy to interpret

**Limitations**

* Works best with linear relationships.

---

## Decision Tree

### Basic Idea

Makes decisions using a tree of questions.

Example:

```
Income > $50,000?
      |
     Yes
      |
Credit Score > 700?
      |
   Approve
```

**Use Case**

* Customer segmentation
* Medical diagnosis

**Advantages**

* Easy to understand
* Handles both numerical and categorical data

**Limitations**

* Can overfit the training data.

---

## Random Forest

### Basic Idea

Combines many Decision Trees and chooses the majority vote.

**Use Case**

* Fraud detection
* Credit scoring

**Advantages**

* High accuracy
* Reduces overfitting

**Limitations**

* Slower
* Harder to interpret.

---

# 3. Classification Metrics

| Metric           | What it Measures              | Best Use                         | Sensitive to Class Imbalance? |
| ---------------- | ----------------------------- | -------------------------------- | ----------------------------- |
| Accuracy         | Overall correct predictions   | Balanced datasets                | Yes                           |
| Precision        | Correct positive predictions  | When false positives are costly  | Less sensitive                |
| Recall           | Finds actual positives        | When missing positives is costly | Less sensitive                |
| F1-Score         | Balance of Precision & Recall | Imbalanced datasets              | Good                          |
| Confusion Matrix | Shows TP, TN, FP, FN          | Error analysis                   | No                            |

### Simple Definitions

* **Accuracy:** Percentage of correct predictions.
* **Precision:** Of predicted positives, how many are actually positive?
* **Recall:** Of all actual positives, how many were found?
* **F1-Score:** Balance between Precision and Recall.
* **Confusion Matrix:** Table showing correct and incorrect predictions.

---

# 4. Class Imbalance

### Why Accuracy Can Be Misleading

Imagine:

* 95 good customers
* 5 bad customers

If a model predicts **everyone is good**, Accuracy = **95%**, but it completely fails to detect bad customers.

So Accuracy alone is not enough for imbalanced data.

### Loan Approval Example

**Prioritize Precision**

* When approving risky applicants is very costly.
* Better to approve only applicants who are very likely to repay.

**Prioritize Recall**

* When you want to identify as many eligible applicants as possible.
* Missing qualified applicants would reduce business opportunities.

---

# 5. Real-World Case Study (Example)

### Loan Approval Prediction

**Goal**
Predict whether a loan application should be approved or rejected.

**Data Used**

* Income
* Credit score
* Employment status
* Loan amount
* Previous loan history

**Classifier**

* Random Forest

**Results**

* Improved prediction accuracy.
* Reduced loan defaults.
* Helped banks make faster and more consistent lending decisions.

---

## Key Points to Remember

* **Classification** predicts categories.
* **Regression** predicts numbers.
* **Logistic Regression**: simple and fast.
* **Decision Tree**: easy to understand.
* **Random Forest**: more accurate, combines many trees.
* **Accuracy** is not reliable for imbalanced data.
* **Precision** matters when false positives are costly.
* **Recall** matters when missing positives is costly.
* **F1-Score** balances Precision and Recall.
* **Confusion Matrix** helps analyze prediction errors.
* **Random Forest** is one of the most widely used classifiers in real-world applications such as fraud detection and loan approval.
