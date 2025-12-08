# Milestone 3 — Modeling & Analysis

## 1. Overview

This milestone compares:
- **Three ML models:** Logistic Regression, SVM, MLP  
vs.  
- **Keyword baseline** inspired by grooming literature.

Goal: understand model behavior on early-stage grooming cues.

---

## 2. Modeling Setup

### Features:
- TF–IDF vectorization
- Unigram/bigram patterns

### Models Tested:
- Logistic Regression
- Linear SVM (best performer)
- Multi-Layer Perceptron

### Baseline:
- 10-word keyword detector  
- Represents current commercial safety trends

---

## 3. Evaluation Metrics

Measured:
- Accuracy  
- Precision  
- Recall  
- F1 score  
- Confusion matrices

---

## 4. Results Summary

### Keyword Baseline
- Very fast  
- High false negatives  
- Recognizes only explicit cues  

### Logistic Regression
- Strong all-around performance  

### SVM
- Best classifier  
- Most stable and precise  
- Captured subtle conversational shifts  

### MLP
- Good but sensitive to dataset size/noise  

---

## 5. Key Takeaways

- ML significantly outperforms keyword filters.
- Early grooming signals *can* be detected in synthetic chats.
- Conversational-pattern detection > keyword detection.

---

## 6. Limitations

- Synthetic-only dataset.
- Balanced classes inflate performance.
- Inability to test against real tools (no API access).
- Limited linguistic/cultural diversity.

---

## 7. Milestone 3 Summary

Modeling results are complete and ready to communicate in a public-facing artifact (Milestone 4).
