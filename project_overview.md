# Project Overview — Grooming Detection (Academic Study)

## 1. Short Description

This project is an **academic machine-learning study** on detecting online grooming in gaming chats using synthetic data. Because real chat logs are private and not accessible, the goal is not to build a deployed product, but to:

- explore how ML models behave on carefully designed synthetic data,
- compare them to simple keyword filters,
- and clearly document the strengths and limitations of this approach.

The project is part of the MIT Emerging Talent ELO2 Capstone.

---

## 2. Motivation

Online grooming is a serious and often invisible safety risk for children, especially in gaming chats where conversations appear casual, friendly, and harmless in the beginning. Most existing safety tools rely on simple keyword lists and basic filters, which struggle to detect the subtle, psychological patterns that groomers use.

At the same time, researchers and developers face major barriers: real chat logs are protected by strict privacy rules, and monitoring platforms in real time is extremely costly. Because of these challenges, this project adopts an academic approach — using synthetic data to explore what machine learning could do in theory, while being transparent about what synthetic data cannot represent about the real world.

As a mother who watches her own children navigate online games every day, this problem is deeply personal for me. I see how much joy and learning these games bring them, but I also see the risks hidden in the background. This project began from a place of wanting to protect my kids — and every child — by understanding how technology might help create safer digital spaces without taking away the benefits of play.

---

## 3. Scope and Direction

After discussions with my supervisor, I chose to focus on the **academic direction** rather than trying to build a fully practical or real-time system.

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
