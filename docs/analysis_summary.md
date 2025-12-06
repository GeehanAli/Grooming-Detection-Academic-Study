# Analysis Summary  
**Grooming Detection — Academic ML Study Using Synthetic Gaming Chats**

This document summarizes the exploratory modeling work completed for Milestone 3. It outlines how the dataset was prepared, how multiple models performed, and how these results should be interpreted within the context of an academic, synthetic-data–based project. It also integrates key limitations and considerations raised in the literature and by mentor feedback.

---

## 1. Overview of the Modeling Approach

The goal of this milestone was to compare:

- A **simple keyword filter** (similar to commercial parental-control tools), and  
- Three **machine-learning models**:
  - Logistic Regression  
  - Support Vector Machine (LinearSVC)  
  - Multi-Layer Perceptron (MLP)

All models were trained on a **synthetic dataset** of gaming chat snippets, which was cleaned and vectorized using TF-IDF. The objective was not to build a production-grade system, but to explore how ML behaves in a controlled, academic setting where data constraints are openly acknowledged.

---

## 2. Dataset Characteristics and Preparation

The dataset used here contains:

- **1,830 messages**  
- Two labels: `grooming` vs `non_grooming`  
- Optional grooming stages for analysis  
- Cleaned text using lowercasing, punctuation removal, and simple token normalization  

For training clarity, the dataset is **balanced**.  
This is *not* representative of the real world, where grooming cases are extremely rare. This intentional imbalance:

- Helps illustrate how models learn patterns  
- But inflates accuracy and reduces real-world validity  

This limitation is explicitly recognized and discussed.

---

## 3. Model Performance Summary

Below is the performance table generated in the modeling notebook:

| Model | Accuracy | Notes |
|-------|----------|-------|
| Logistic Regression | **1.00** (100%) | High performance due to synthetic patterns and balanced classes. |
| Support Vector Machine (LinearSVC) | **1.00** (100%) | Same behavior as LR — strong separation in the synthetic dataset. |
| Multi-Layer Perceptron | **1.00** (100%) | Also reaches perfect accuracy under controlled conditions. |
| Keyword Filter | Lower accuracy | Misses subtle patterns; only detects obvious surface terms. |

### Interpretation

These perfect ML scores do **not** imply real-world readiness.  
They reflect:

- Clear, structured patterns in synthetic data  
- Strong class separation  
- A balanced dataset  
- Lack of noise, slang, misspellings, and adversarial behavior  

In contrast, the keyword system behaves more like real commercial tools and demonstrates why such systems fail to detect early grooming cues.

---

## 4. Limitations and Key Insights  

### 4.1 Synthetic Data Constraints  
Synthetic chats are not messy, unpredictable, or deceptive in the same way real predators behave. As a result:

- ML models appear much stronger than they would on real data  
- Keyword filters appear much weaker  
- False positives and false negatives cannot be accurately estimated  

This mirrors concerns in the literature, where most grooming datasets are extremely small or artificially constructed.

### 4.2 Imbalance in the Real World  
Real platforms have **millions of normal chats** and very few grooming attempts.  
Training on a balanced dataset:

- Helps early academic exploration  
- But dramatically reduces real-world validity  
- Prevents realistic measurement of precision and recall  

A follow-up study would need to simulate highly imbalanced conditions.

### 4.3 Cultural and Linguistic Limitations  
Grooming psychology may be universal, but language is **culture-specific**.

This model is:

- English-only  
- Synthetic-only  
- Not evaluated across slang communities, dialects, gaming cultures, or age groups  

This reflects a gap identified by mentor feedback and the literature:  
**models trained on one linguistic environment cannot be reliably generalized to others.**

### 4.4 Privacy and Access Barriers  
Major constraints identified in both research and mentor feedback:

- Real chat logs are inaccessible due to privacy regulations  
- Platforms cannot legally share conversations with researchers  
- Real-time scanning at scale is technically expensive  

This explains the biggest gap in the field:

> Many researchers can design academic models, but very few can test them on real, live data.

This project exists entirely within this academic zone — openly acknowledging these constraints.

---

## 5. The Gap This Study Highlights

Across academic papers, commercial tools, and mentor guidance, one gap appears repeatedly:

### **There is no publicly available, large-scale, modern dataset of real gaming chats that includes grooming labels.**

Because of this:

- Researchers cannot evaluate models realistically  
- Real-time pattern detection remains unsolved  
- Industry tools depend on simple keyword lists  
- Advanced ML systems cannot be validated or deployed  

This study does *not* solve that gap — but it **documents and demonstrates why the gap exists**, and explores what ML might do in a controlled academic environment.

The project contributes:

- A transparent synthetic dataset  
- Multiple baseline models  
- A keyword comparison  
- Documentation of limitations  
- A clear explanation of why grooming detection remains an open problem  

---

## 6. Summary of What These Results Mean

- Machine-learning models can learn synthetic grooming cues extremely well.  
- Keyword filters miss subtle psychological patterns.  
- Synthetic data is useful for conceptual exploration, not real deployment.  
- Real-world grooming detection requires:
  - Access to real chat logs (currently impossible)
  - Handling huge class imbalance
  - Deep cultural and linguistic variation
  - Expensive engineering infrastructure

Thus, this project provides an academically meaningful exploration while remaining realistic and honest about what is — and is not — possible today.

---

## 7. Next Steps (For Future Work)

- Create an imbalanced version of the dataset to simulate real conditions  
- Add adversarial or intentionally misleading language  
- Experiment with sequence models (e.g., LSTM or transformers)  
- Explore conversation-level (rather than message-level) predictions  
- Investigate metadata features (timing, frequency, speaker shifts)

These directions build on what has been learned while respecting the constraints of this research environment.
