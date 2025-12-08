# Milestone 2 — Data Collection & Synthetic Dataset Design

## 1. Overview

Because real gaming chat logs are inaccessible due to privacy, ethical, and platform restrictions, this project uses a **synthetic dataset** of gaming-style chat messages to explore grooming detection academically.

The dataset is structured to reflect:
- early grooming psychology,
- gaming communication patterns,
- and reproducible ML experimentation.

---

## 2. Dataset Structure

Each row represents a single message.

| Column            | Description |
|------------------|-------------|
| **conversation_id** | Groups messages into a conversation |
| **turn_id**         | Order of the message within the conversation |
| **speaker_role**    | “adult” or “child” (synthetic role) |
| **text**            | Original synthetic message |
| **clean_text**      | Preprocessed version |
| **label**           | 1 = grooming, 0 = non-grooming |
| **stage**           | friendship_forming, trust_building, isolation, escalation, none |

Dataset size: **~1,800 messages**.

---

## 3. Generation Strategy

### Grooming messages:
- Inspired by documented grooming tactics.
- Reflect early psychological stages.
- Subtle, indirect, friendly tone.

### Non-grooming messages:
- Game-related chat (commands, jokes, quick replies).
- Noise: slang, emojis, incomplete sentences.

### Goals:
- Capture conversational realism *without* violating privacy.
- Create conditions for controlled ML experimentation.

---

## 4. Limitations (Explicitly Acknowledged)

- Synthetic data cannot replicate real chat complexity.
- English-only; no cultural/linguistic variation.
- Early-stage grooming may appear too clean/consistent.
- Dataset size is small relative to real gaming platforms.
- Unable to test against commercial tools due to **no API access**.

---

## 5. Outputs

Files stored in:
- `data/raw/synthetic_chats_raw.csv`
- `data/processed/synthetic_chats_model_ready.csv`

---

## 6. Milestone 2 Summary

Dataset is complete, documented, and ready for modeling (Milestone 3).
