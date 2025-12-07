# Final Presentation — Grooming Detection Academic Study  
**MIT Emerging Talent (ELO2 Capstone)**  
**Author: Geehan Ali**

---

## 1. Introduction

Online grooming is one of the most hidden and dangerous risks children face in online games. Early-stage grooming often appears casual, friendly, and harmless — making it extremely difficult for keyword-based tools to detect.

This project explores **whether machine learning can detect the earliest psychological stages of grooming** using a synthetic dataset of gaming chat conversations.

The work adopts an **academic direction**, motivated both by research gaps and by real-world concerns I personally experience as a mother whose children play online games daily.

---

## 2. Research Motivation

- Existing tools rely heavily on **keyword lists**, which fail to detect subtle manipulation.
- Early stages of grooming (friendship-forming, trust-building) are **universal across cultures**, but the *language* used is highly variable.
- Real chat logs are not accessible due to **strict privacy rules**, **platform constraints**, and **extremely high computational cost** of real-time scanning.
- As a parent, I want technology that protects children *before* harm happens — not only when explicit warning signs appear.

This project began from that need:  
to investigate **how machine learning behaves** when detecting these early cues, even under synthetic conditions.

---

## 3. Research Questions

1. Can ML models distinguish grooming vs. non-grooming chats in a synthetic gaming dataset?
2. How do keyword filters compare with ML approaches?
3. What signals do ML models learn — and where do they fail?
4. What limitations arise when using synthetic data?
5. Which gaps in existing research does this study address?

---

## 4. Gap Addressed by This Study

### **Main gap addressed:**
Most existing research focuses on **detecting explicit or late-stage grooming**, because those messages are easier to label.

However, **the earliest psychological stages are the most critical for prevention**, yet the least studied due to:

- Lack of real data  
- Weak performance of keyword tools  
- Difficulty capturing subtle relational patterns  

**This project directly targets this gap** by modeling **universal early-stage grooming behaviors** in a controlled dataset to explore whether ML can help detect them.

---

## 5. Dataset Overview

- 1,800+ synthetic chat messages  
- Two classes: grooming vs. non-grooming  
- Includes optional stage labels:
  - friendship_forming  
  - trust_building  
  - isolation  
  - escalation  
- Structured as message-level rows  
- Balanced dataset for initial learning clarity  

Files generated:
- `data/raw/synthetic_chats_raw.csv`
- `data/processed/synthetic_chats_model_ready.csv`

---

## 6. Methods

### **Models Trained**
- Logistic Regression (TF-IDF pipeline)
- Linear SVM (TF-IDF pipeline)
- Multi-Layer Perceptron (TF-IDF)
- Keyword baseline (10 grooming-related cues)

### **Workflow**
1. Synthetic data generation  
2. Text cleaning & preprocessing  
3. Train/test split  
4. Model training & evaluation  
5. Keyword baseline comparison  

---

## 7. Results Summary

| Model | Accuracy | Precision | Recall | F1 |
|-------|----------|-----------|--------|----|
| Logistic Regression | HIGH | HIGH | HIGH | HIGH |
| Linear SVM | HIGH | HIGH | HIGH | HIGH |
| MLP | HIGH | HIGH | HIGH | HIGH |
| Keyword Filter | LOW–MODERATE | LOW | VERY LOW | LOW |

(Actual numbers appear in modeling_results_summary.csv)

### Key Insight
ML models consistently outperform keyword filters, especially for subtle early-stage cues.

---

## 8. Analysis (Technical Interpretation)

- ML models learn relational and contextual patterns that keyword lists cannot capture.
- Overfitting risk exists because synthetic data contains structured patterns.
- Accuracy is high — but **this reflects the dataset, not real-world performance**.
- Keyword systems fail mainly on:
  - indirect language  
  - friendly groomer behaviors  
  - cultural variation  
  - multi-step manipulation  

---

## 9. Limitations

- **Synthetic data realism limits generalizability.**
- **English-only dataset** — lacks cultural diversity.
- **Cannot test against commercial systems** (no public APIs).
- **No real chat logs** due to privacy & platform restrictions.
- Models may **overperform** due to balanced classes and controlled patterns.
- Early-stage cues in reality are often **messy and ambiguous**, unlike synthetic samples.

---

## 10. Future Directions & Proposed Solutions

### **1. Improve Synthetic Data Realism**
- Add more slang, noise, humor, multi-speaker chaos  
- Introduce ambiguous borderline conversations  
- Increase cultural & linguistic diversity  

### **2. Detect Conversational Shifts**
Move beyond phrase-matching by tracking shifts in:  
- tone  
- emotional intimacy  
- secrecy frequency  
- relational manipulation  

Aligns with psychological models of grooming.

### **3. Develop Hybrid Detection Systems**
Combine strengths of different methods:

- **Keyword filters** for fast, low-cost scanning  
- **ML analysis** triggered *only when context becomes unusual*  
- Reduces computation while improving accuracy  

---

## 11. Conclusion

This study demonstrates that machine-learning models can detect **early-stage grooming signals** in a controlled environment significantly better than keyword filters. While limited by synthetic data and privacy constraints, the findings offer a technical foundation for future safety tools that balance feasibility, accuracy, and child protection.

As a mother and a researcher, my motivation is clear:  
**children deserve safer online spaces, and technology should help protect them — not fail them at the earliest signs of danger.**

This academic work is one small step toward that goal.

---
