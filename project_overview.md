# Project Overview — Grooming Detection (Academic Direction)

## 1. Short Description

This project is an **academic machine-learning study** on detecting online grooming in gaming chats using synthetic data. Because real chat logs are private and not accessible, the goal is not to build a deployed product, but to:

- explore how ML models behave on carefully designed synthetic data,
- compare them to simple keyword filters,
- and clearly document the strengths and limitations of this approach.

The project is part of the MIT Emerging Talent ELO2 Capstone.

---

## 2. Motivation

Online grooming is a serious safety issue for children, especially in game chats where conversations look casual and friendly at the beginning. Most existing tools rely on keyword lists and basic filters, which often miss subtle grooming patterns.

However, researchers and developers cannot easily access real chat logs because of strict privacy protections and the huge cost of scanning messages in real time. This project takes an academic approach: it uses synthetic data to ask “what could ML do in theory?” while being honest about what this cannot tell us about the real world.

---

## 3. Scope and Direction

After discussions with my mentor, I chose to focus on the **academic direction** rather than trying to build a fully practical or real-time system.

That means this project focuses on:

- dataset design (synthetic grooming vs non-grooming chats),
- model selection and evaluation (Logistic Regression, SVM, MLP, keyword baseline),
- analysis of metrics and behavior,
- and a clear discussion of limitations and future work.

I will **not** attempt to solve:

- real-time data collection from platforms,
- legal/privacy integration with real systems,
- or large-scale engineering and deployment.

Those are acknowledged as important, but out of scope for this capstone.

---

## 4. Planned Components

- **Synthetic dataset** of chat samples labeled as grooming / non-grooming.
- **Keyword baseline** that imitates current simple safety tools.
- **Machine learning models** trained and evaluated on the synthetic data.
- **Comparative analysis** of keyword vs ML performance.
- **Public-facing summary** for portfolio use.
- **Final presentation and reflection** for the ELO2 requirements.

---

## 5. Repository Map

- `data/raw/` — initial synthetic dataset(s).
- `data/processed/` — cleaned and model-ready versions of the data.
- `notebooks/` — Jupyter notebooks for exploration, modeling, and evaluation.
- `src/` — Python modules for data generation and modeling.
- `models/` — saved model artifacts (optional).
- `docs/` — milestone writeups, summaries, reflections.
- `presentation/` — slides or other presentation materials.
