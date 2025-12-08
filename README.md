# Detecting Early Online Grooming in Gaming Chats  
### MIT Emerging Talent — ELO2 Capstone Project  
**Author:** Geehan Ali  

---

## 📑 Table of Contents
1. [Overview](#-overview)  
2. [Project Purpose](#-project-purpose)  
3. [Motivation](#-motivation)  
4. [What This Project Addresses](#-what-this-project-addresses)  
5. [Repository Structure](#-repository-structure)  
6. [Dataset Summary](#-dataset-summary)  
7. [Modeling Overview](#-modeling-overview)  
8. [Key Insights](#-key-insights)  
9. [Limitations](#-limitations)  
10. [Future Directions](#-future-directions)  
11. [How to Run](#-how-to-run)  
    
---

## 📌 Overview

This project explores whether early signs of online grooming can be detected in gaming chat conversations using simple machine-learning techniques.  
Because real chat data cannot be accessed for privacy and ethical reasons, the study uses a synthetic dataset to simulate early grooming behaviors.

The intention is not to create a production tool — but to explore patterns, challenges, and possibilities for improving online safety.

---

## 🎯 Project Purpose

- Understand how early grooming behaviors appear in conversation.  
- Explore whether machine learning can identify these patterns.  
- Compare keyword filtering with simple ML approaches.  
- Highlight gaps in current safety tools.  
- Provide ideas for future research and safer digital environments.

---

## 🧠 Motivation

As a mother of children who enjoy online gaming, I often think about the hidden risks that may appear behind friendly messages. Early grooming is subtle, gentle, and easy to miss.

This project was inspired by the question:

**Can technology help detect early warning signs before harm occurs?**

---

## 🧩 What This Project Addresses

Most existing tools:

- rely on keyword lists  
- detect only very explicit or late-stage grooming  
- miss early psychological stages  

This project explores whether a more context-aware approach, even with simple synthetic data, can offer improvements.

---
## 🗂️ Repository Structure

Grooming-Detection-Academic-Study/

│

├── data/

│ ├── raw/ # Synthetic dataset (unprocessed)

│ └── processed/ # Cleaned, tokenized dataset
│
├── notebooks/

│ ├── 02_generate_synthetic_data.ipynb

│ ├── 03_preprocess_data.ipynb

│ └── 04_modeling.ipynb # Main ML evaluation notebook

│

├── docs/

│ ├── milestone_1_problem_identification.md

│ ├── data_documentation.md

│ ├── analysis_summary.md

│ ├── public_summary.md

│ ├── final_reflection.md

│ └── modeling_results_summary.csv

│

├── presentation/

│ └── Grooming_Detection_Presentation.pptx

│
├── models/ # Optional saved models

│

├── README.md # You are here

└── requirements.txt


---

## 🧬 Dataset Summary

- ~1,800 synthetic chat messages  
- Contains message text, speaker roles, and a simple label  
- Includes “stage” categories to simulate early grooming patterns  

The dataset is intentionally small — created strictly for learning and analysis.

---

## 🤖 Modeling Overview

A few simple machine-learning models were compared with a basic keyword list.  
The focus was **not** on building a perfect model, but on understanding:

- how ML reacts to conversational patterns  
- what it can detect vs. what keywords miss  
- how early behaviors appear in synthetic chats  

---

## 📊 Key Insights

- Early grooming looks friendly, supportive, and harmless.  
- Keyword filters miss most early signals.  
- ML models capture more subtle patterns.  
- Better data is needed for any real-world application.  

---

## ⚠️ Limitations

- Synthetic data does not reflect full real-world complexity.  
- English-only dataset.  
- Small dataset size.  
- Not intended for deployment.  

This is a learning-focused, academic exploration only.

---

## 🔮 Future Directions

- More realistic conversation styles (slang, humor, multi-speaker flow)  
- Multilingual datasets  
- Entire-conversation modeling rather than single messages  
- Hybrid systems combining speed (keywords) + depth (ML)  

---

## 🚀 How to Run

Install requirements:

```bash
pip install -r requirements.txt

### ▶️ Run the notebooks in order:

1. `02_generate_synthetic_data.ipynb`  
2. `03_preprocess_data.ipynb`  
3. `04_modeling.ipynb`
