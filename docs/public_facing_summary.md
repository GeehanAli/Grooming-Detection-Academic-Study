# Public Summary — Detecting Early Grooming in Gaming Chats  
*MIT Emerging Talent — ELO2 Capstone (Academic Study)*  
*Author: Geehan Ali*

---

## Overview

This project explores whether machine learning can detect **early signs of online grooming** within **synthetic gaming chat conversations**. Early grooming is subtle, relational, and often appears friendly—making it extremely difficult to identify.

This academic study investigates the feasibility of early-stage detection *in theory*, using carefully constructed synthetic data, while recognizing the ethical and technical challenges of real-world deployment.

---

## Why This Matters

Online gaming is a core part of children's social lives.  
As a mother, keeping those spaces safe is deeply meaningful to me.

Most existing safety tools rely on keyword filtering, which fails to capture:

- trust-building  
- secrecy invitations  
- emotional manipulation  
- changes in conversational tone  

These early cues appear **before** explicit language—and current technology largely misses them.

---

## The Gap

There is **no computational method** today that reliably detects early, universal grooming stages.

This project contributes an academic exploration of whether ML models can begin to learn those patterns under controlled conditions.

---

## Approach

Because real chat logs are inaccessible due to privacy laws and platform restrictions, this project uses **synthetic gaming conversations** to model:

- friendship-forming  
- trust-building  
- isolation  
- escalation  

Three machine-learning models were tested:

- Logistic Regression  
- Support Vector Machine (SVM)  
- Multi-Layer Perceptron (MLP)

Compared against a **keyword detector** inspired by grooming literature.

---

## What I Found

- ML models **outperformed keyword filtering** across all metrics.  
- The **SVM model** performed best in distinguishing subtle conversational cues.  
- The keyword baseline missed most early grooming patterns.  
- The dataset was **realistically imbalanced**, adding difficulty and improving evaluation credibility.

These results apply to synthetic data only—but they show promising academic evidence that early-stage detection may be feasible.

---

## Limitations

- Synthetic dataset, not real chat logs  
- English-only language  
- Dataset is small  
- Grooming stages are idealized  
- No access to commercial tools for benchmarking (no public APIs)  
- ML may learn synthetic artifacts rather than natural behavior  

These limitations are important, and they guide how the results should be interpreted.

---

## Future Directions

- Expand synthetic realism (slang, noise, cultural variety, ambiguous cases)  
- Explore behavioral detection (tone shifts, emotional intimacy, secrecy patterns)  
- Build hybrid systems combining keywords + ML for practical efficiency  

---

## Closing

This project is a foundational step toward understanding what machine learning might contribute to child safety online.  
It does not solve the problem—but it helps map the space between theoretical possibility and real-world protection.

My motivation for this work is deeply personal, and my hope is that it supports future research that makes digital spaces safer for all children.

---
