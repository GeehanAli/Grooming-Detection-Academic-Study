# Milestone 1 — Problem Identification

## 1. Overview

Online grooming remains one of the most complex and difficult online safety problems to detect, especially in *gaming chats*, where conversations are fast, informal, and often appear harmless at first. Predators frequently use gradual psychological manipulation rather than explicit language, making early detection extremely challenging for automated systems.

This project explores whether **machine learning can detect early-stage grooming cues** — particularly the stages of friendship-forming, trust-building, and early isolation — using **synthetic gaming chat data**.

This direction aligns with an academic research focus and incorporates mentor feedback emphasizing:
- clarity about dataset limitations,
- the importance of cultural/linguistic variability,
- and the practical barriers preventing real-world deployment.

---

## 2. Research Questions

1. **Can ML models detect early-stage grooming signals in synthetic chat data more effectively than keyword filters?**
2. **What patterns do ML models learn**, and how do these patterns compare to known behavioral cues in grooming literature?
3. **How do dataset design choices** (e.g., balance, stage labels, conversational structure) impact model performance?
4. **What are the strengths and weaknesses** of keyword-based vs ML-based detection methods?
5. **What are the academic and practical limitations** of using synthetic data for grooming detection research?

---

## 3. Background & Context

Existing grooming research identifies four universal psychological stages:
- **Friendship forming**
- **Trust building**
- **Isolation**
- **Escalation**

These stages appear across cultures, but the *language* used to express them varies greatly.  
Because of this:

- **Keyword-only detection fails** in early stages.
- **ML models show promise** for pattern-level detection.
- **Access to real chat logs** is nearly impossible due to:
  - privacy laws (e.g., COPPA),
  - platform restrictions,
  - ethical considerations,
  - and massive infrastructure costs.

Most academic studies:
- use **small, outdated, or fragmentary datasets**,  
- focus on **late-phase grooming**,  
- or rely entirely on **forensic logs** rather than real-time detection.

*This project addresses the academic gap by centering the earliest grooming stages* — the stages where real-world prevention matters most.

---

## 4. Constraints & Assumptions

- **Synthetic-only dataset:** No real chats used; dataset is handcrafted/generated.
- **English-only:** Cultural and linguistic diversity is not represented.
- **Balanced training set:** Useful for experimentation, but unrealistic compared to real data.
- **No API access:** Cannot validate models against commercial tools (e.g., Bark, Qustodio).
- **Academic scope:** This is a modeling study, not a deployable tool.

---

## 5. Milestone 1 Summary

By completing this milestone:
- The project problem is clearly defined.
- Research questions are established.
- Context and constraints are documented.
- The academic direction is justified.

This provides a foundation for dataset design in **Milestone 2**.
