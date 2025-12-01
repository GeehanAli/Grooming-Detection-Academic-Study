# Synthetic Dataset Documentation

## Overview
Because real gaming chat logs cannot be accessed due to strict privacy rules and platform restrictions, this project uses a synthetic dataset to explore how machine-learning models behave when attempting to distinguish grooming from non-grooming conversations.

This dataset is designed for academic exploration only and cannot represent the full complexity of real online communication. However, it allows controlled experimentation to understand model behavior, error patterns, and limitations.

---

## Dataset Structure

The dataset will contain two classes:

- **grooming** (label = 1)  
- **non-grooming** (label = 0)

Each chat sample will include:
- A short conversation snippet (simulating game chat style)
- A label  
- (Optional later) The grooming stage (friendship-forming, trust-building, isolation, escalation)

---

## Generation Strategy

The dataset will be generated using a combination of:

### 1. **Template-driven messages**
Hand-crafted patterns inspired by documented grooming psychology stages.

### 2. **Language variation**
- Friendly tone for early stages  
- Subtle trust-building language  
- Manipulative or isolating phrasing  
- Slightly more explicit attempts in escalation samples  

### 3. **Noise injection in normal chats**
To simulate real gaming interaction:
- Slang  
- Emojis  
- Short replies  
- Game-focused conversations  

### 4. **Balanced dataset (for training)**
The initial dataset will contain a 50/50 split for model learning clarity.

Later, an *imbalanced version* may be generated to show realistic challenges.

---

## File Outputs

Two CSV files will be created:

### 1. `data/raw/synthetic_chats_raw.csv`
- All raw conversations  
- Columns: `text`, `label`, `stage`

### 2. `data/processed/synthetic_chats_model_ready.csv`
- Cleaned and tokenized version
- Ready for ML model input

---

## Limitations

- Synthetic language cannot fully capture nuance of real chats.
- Cultural diversity is limited (English-only).
- Slang/variation may not match modern platforms exactly.
- Model accuracy may be inflated due to controlled patterns.

These limitations will be openly discussed in Milestone 3 and 4.

---

## Next Steps

- Generate synthetic samples.  
- Save raw version in `/data/raw`.  
- Clean and preprocess → save to `/data/processed`.  
