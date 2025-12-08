# Analysis Summary — Grooming Detection in Synthetic Gaming Chats  
*MIT Emerging Talent — ELO2 Capstone (Academic Direction)*  
*Author: Geehan Ali*

---

## 1. Introduction

This study examines whether machine-learning methods can detect **early psychological stages** of online grooming within **synthetic gaming chat conversations**. Early grooming behavior is subtle, relational, and rarely involves explicit language. This makes detection extremely challenging for current tools, which rely primarily on keyword filtering.

The project adopts an **academic direction**, focusing on model behavior, dataset construction, and methodological limitations—rather than real-time deployment—due to strict privacy, cost, and data-access barriers.  
This aligns with mentor guidance and established *translational research* concepts where foundational studies precede applied engineering.

---

## 2. Data Overview & Distribution

The synthetic dataset contains **1,826 messages** generated to simulate gaming chat dynamics.  
Columns include:

- `conversation_id`  
- `turn_id`  
- `speaker_role`  
- `text`  
- `clean_text`  
- `label` (1 = grooming, 0 = non-grooming)  
- `stage` (friendship_forming, trust_building, isolation, escalation, none)

### **Class Distribution**

A key update from earlier drafts:  
**The dataset is NOT 50/50.**  
Non-grooming messages significantly outnumber grooming messages, reflecting more realistic proportions and making the classification task more challenging.

This correction strengthens the validity of the evaluation.

---

## 3. Motivation & Gap

Existing literature shows that grooming typically follows four universal psychological stages:

1. **Friendship forming**  
2. **Trust building**  
3. **Isolation**  
4. **Escalation**

Most tools and ML studies focus on **late-stage** cues—typically explicit or suspicious language.  

However, the **primary gap** addressed in this project is:

> *There is currently no reliable computational approach for detecting early, psychological grooming stages before explicit language appears.*

Early stages rely on:
- tone shifts  
- emotional intimacy  
- personal boundary testing  
- secrecy invitations  

These are **behavioral patterns**, not keywords.

This project explores whether ML can detect such patterns *in theory*, using controlled synthetic data.

---

## 4. Why Synthetic Data?

Real gaming chat logs cannot be accessed due to:

- **privacy laws** (e.g., COPPA)  
- **platform policies**  
- **ethical constraints**  
- **lack of API access to safety tools**  
- **the enormous cost of real-time processing**

Synthetic data allows:

- controlled evaluation of model behavior  
- exploration of early-stage cues  
- understanding failure modes  
- ethical experimentation without real minors’ data

This remains a *sandbox environment*—not a basis for real-world deployment.

---

## 5. Modeling Approach

Three machine-learning models were trained:

1. **Logistic Regression (TF-IDF)**
2. **Linear SVM (best performer)**
3. **Multi-Layer Perceptron (MLP)**

Baseline comparison:

- **Keyword detector** derived from grooming literature  
- Keywords included “secret,” “private,” “don’t tell,” etc.

Evaluation metrics:

- accuracy  
- precision  
- recall  
- F1 score  
- confusion matrices  

Train/test split ensured fair comparison across methods.

---

## 6. Results Summary

### **Keyword Baseline**
- Fast and computationally lightweight  
- Performs poorly on early, indirect grooming  
- High false negatives: misses subtle relational cues  

### **Machine Learning Models**
**Logistic Regression**  
- Strong balanced performance
- Learns TF-IDF signal distributions reliably

**SVM (LinearSVC)**  
- **Best overall performance**
- Most robust to subtle pattern differences  
- Handles imbalanced data surprisingly well  

**MLP**  
- Good performance but more sensitive to dataset size  
- Less stable for small synthetic corpora  

### **Key Insight**
ML models **can detect early-stage behavioral patterns** in synthetic conversations.

Keywords cannot.

However, performance reflects the *structure of synthetic data* and does not generalize to real-world environments.

---

## 7. Interpretation

ML models appear to learn signals such as:

- shifts from game-related talk → personal talk  
- accumulation of trust-building phrases  
- repeated invitations to private communication  
- emotional dependency patterns  

These support psychological models of grooming, which emphasize *progression*, not isolated words.

This provides academic evidence that early-stage detection may be theoretically possible.

---

## 8. Limitations (Formal List)

1. **Synthetic Data Only**  
   Does not fully replicate spontaneity, noise, or complexity of real gaming chats.

2. **English-Only Linguistic Scope**  
   Grooming language varies across cultures; results cannot generalize globally.

3. **Imbalanced but Small Dataset**  
   Although class imbalance was corrected, the total dataset remains small for ML research.

4. **Idealized Stage Labels**  
   Real grooming stages overlap and are difficult to annotate cleanly.

5. **No Access to Commercial Safety Tools**  
   Existing systems like Bark or Qustodio have **no public APIs**, preventing external benchmarking.

6. **Potential Overfitting to Synthetic Patterns**  
   ML models may exploit artifacts unique to synthetic text.

---

## 9. Conclusions

This academic study shows that:

- Early-stage grooming detection **may** be possible in theory with ML.
- Behavioral, conversational signals outperform keyword detection.
- Synthetic data is a useful starting point for methodological exploration.

This work does **not** claim real-world detection performance.  
Instead, it contributes to the foundational understanding needed before translational research can advance toward applied systems.

---

## 10. Future Research Directions

Based on findings and constraints, future work should explore:

1. **Improved Synthetic Realism**  
   - More slang, humor, noise  
   - Multi-speaker dynamics  
   - Cultural and linguistic diversity  
   - Ambiguous, borderline conversations  

2. **Behavioral Detection Systems**  
   - Detect shifts in tone or emotional intimacy  
   - Monitor secrecy patterns  
   - Model progression over time  

3. **Hybrid Safety Approaches**  
   - Fast lightweight keyword filters  
   - ML analysis triggered only when context becomes suspicious  
   - Reduced cost + higher accuracy  

These steps could bring research one phase closer to practical child-safety tools.

---

