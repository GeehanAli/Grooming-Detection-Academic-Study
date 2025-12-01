# Synthetic Dataset Documentation

## Overview

Because real gaming chat logs are protected by strict privacy rules, platform policies, and ethical considerations, this project relies on a **synthetic dataset** to study grooming detection in online gaming environments. Synthetic data allows controlled experimentation without exposing real users or violating platform restrictions. It also enables us to model specific psychological grooming stages that may be rare or subtle in real-world chat streams.

The purpose of this dataset is **not** to replicate real online chats perfectly. Instead, it is designed to:
- simulate the conversational patterns described in existing grooming literature,
- create structured examples across different grooming stages,
- allow machine-learning models to be tested under controlled conditions,
- compare simple keyword filters with flexible ML models,
- analyze common failure modes and limitations.

This dataset supports the academic direction of the project and is intended for exploration, learning, and insight—not deployment or commercial use.

---

## Data Format and Structure

Each row in the dataset represents a **single chat message** in a synthetic gaming conversation. The planned columns are:

- **conversation_id**  
  A unique identifier grouping all messages that belong to the same conversation.

- **turn_id**  
  The order of each message within its conversation (0, 1, 2, ...).

- **speaker_role**  
  Indicates whether the speaker is synthetically assigned as `adult` or `child`.  
  *(This helps model role-driven behavioral patterns.)*

- **text**  
  The raw chat message written synthetically to resemble gaming-style interaction.

- **label**  
  Either `grooming` or `non_grooming`.  
  Grooming indicates that the message contributes to a grooming attempt.

- **stage** *(optional for exploration)*  
  Grooming messages may be tagged with one of the stages described in the literature:
  - `friendship_forming`
  - `trust_building`
  - `isolation`
  - `escalation`
  For non-grooming messages, the stage is `none`.

This design allows both **message-level** and **conversation-level** experiments.

---

## Class Design and Balance

The dataset will be created in **two versions**:

### **1. Balanced Version (for model training clarity)**
- Approximately 50/50 grooming vs non-grooming conversations.
- Allows models to learn patterns without extreme class imbalance.
- Useful for academic comparison of algorithms.

### **2. Imbalanced Version (to reflect real-world rarity)**
- Heavily skewed toward non-grooming conversations.
- Shows how models struggle when grooming attempts are very rare.
- Helps analyze false positives and recall degradation.

The literature consistently highlights that real-world grooming attempts are **extremely rare**, so the imbalanced version is crucial for understanding model limitations.

---

## Data Generation Process

The dataset is generated through a combination of the following methods:

### **1. Template-Based Message Construction**
Messages inspired by documented grooming patterns:
- friendly rapport building,
- introduction of secrets,
- emotional manipulation,
- gradual attempts at isolation,
- testing boundaries,
- escalating inappropriate suggestions.

Templates ensure psychological consistency across stages.

### **2. Style Variation and Noise Injection**
To mimic gaming chat style:
- short phrases,
- casual tone,
- slang,
- emojis,
- team-based game references,
- typos,
- rapid back-and-forth messages.

This noise helps models learn robustness instead of memorizing rigid templates.

### **3. Role Play Simulation**
Adults and children are assigned synthetically, enabling modeling of:
- power dynamics,
- tone shifts,
- adult-initiated topics,
- child-like responses.

### **4. Literature-Grounded Stage Modeling**
Stages follow widely cited research:
- friendship forming,
- trust building,
- isolation,
- escalation.

Each stage influences message tone, word choice, and conversational direction.

---

## Data Files and Outputs

The following files will be produced:

### **1. `data/raw/synthetic_chats_raw.csv`**
Contains the unprocessed full dataset with:
- conversation_id  
- turn_id  
- speaker_role  
- text  
- label  
- stage  

### **2. `data/processed/synthetic_chats_model_ready.csv`**
A cleaned and tokenized version suitable for model training.

### **Additional exploratory files may include:**
- Stage-specific subsets  
- Conversation-level aggregated labels  
- Visualizations for distribution checks  

---

## Design Principles and Assumptions

The dataset is designed with these assumptions:

- Grooming behavior is structured and progresses through psychological stages, even if language appears friendly.
- Normal chats are noisy, game-focused, and lack directional manipulation.
- Synthetic conversations can meaningfully represent theoretical patterns for academic experimentation.
- Many aspects of human conversation (sarcasm, cultural slang, emotional nuance) cannot be perfectly replicated synthetically.

---

## Known Limitations

This dataset has significant limitations that must be acknowledged:

### **1. Restricted Linguistic Realism**
Synthetic text cannot fully capture:
- sarcasm,
- slang evolution,
- inside jokes,
- cultural context,
- multi-language dynamics.

### **2. English-Only**
Most real platforms host multilingual interactions, limiting model generalizability.

### **3. Clear Labels**
In reality, grooming behavior is ambiguous and emerges gradually.  
Synthetic data is cleaner and more distinct.

### **4. No real-time irregularities**
Real chat streams include:
- message dropouts,
- interruptions,
- changing topics,
- multitasking behavior.

### **5. Potential Overfitting to Synthetic Patterns**
Models may learn the “rules” of synthetic generation instead of real grooming cues.

---

## Why This Dataset Still Matters

Despite limitations, synthetic datasets are widely used in early-stage safety research because they allow:

- **safe experimentation** without ethical concerns,  
- **transparent modeling** of psychological stages,  
- **analysis of ML behavior** in controlled settings,  
- **comparison of baselines** (keywords vs ML),  
- **exploration of failure cases**,  
- **testing of ideas before real-world application**.

This dataset provides a practical foundation for academic exploration, allowing this project to investigate early detection signals, model performance barriers, and gaps in existing approaches.

---
