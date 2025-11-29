# Milestone 1: Problem Identification

## 1. Problem Statement

Online grooming is a gradual psychological process where an adult builds trust with a child, often in chat-based environments such as online games. Many safety tools currently used by parents and platforms rely on simple keyword lists or basic filters. These methods can miss subtle or indirect grooming attempts, especially when the language looks friendly and non-threatening.

At the same time, researchers and developers cannot easily access real chat logs because of strict privacy protections, platform policies, and the high cost of scanning large volumes of messages in real time. This makes it difficult to study and improve grooming detection systems using real data.

Because of these constraints, this project takes an **academic approach**. It uses **synthetic gaming chat data** to explore how machine-learning models behave when detecting grooming vs non-grooming chats, and to compare them with simple keyword filters. The main goal is to learn about model behavior, strengths, weaknesses, and limitations in a controlled, research-focused setting — not to deploy a real-world production system.

---

## 2. Research Questions

This project will focus on the following questions:

1. **Detection ability:**  
   Can machine-learning models distinguish between synthetic grooming and non-grooming chats better than a simple keyword-based filter?

2. **Model comparison:**  
   How do different models (e.g., Logistic Regression, Support Vector Machines, Multi-Layer Perceptron) compare in terms of accuracy and other metrics on the synthetic dataset?

3. **Keyword vs ML:**  
   How does a keyword baseline perform relative to ML models on the same synthetic data, and what kinds of errors does each approach tend to make?

4. **Data and imbalance:**  
   How do design choices in the synthetic dataset (such as balanced vs imbalanced classes) affect model performance, and what does this tell us about limitations when moving toward more realistic distributions?

5. **Constraints and generalization:**  
   Given that the data is synthetic, English-only, and not drawn from real platforms, what are the key limitations of this work, and how might future research address them?

---

## 3. Context and Prior Work (High-Level)

Existing work on grooming and online safety highlights several important points:

- Grooming tends to follow recognizable psychological stages (e.g., friendship-forming, trust-building, isolation, and escalation), but the exact words and phrases used can vary across cultures and communities.
- Commercial tools like parental control apps often rely on keyword lists, activity monitoring, and reporting systems, rather than deep modeling of conversational patterns.
- Academic research has shown that ML models can outperform keyword lists in some safety-related tasks, but these studies often depend on limited or specialized datasets and do not always have access to large-scale, real-world chat logs.
- Synthetic data can be useful for prototyping and early research, but it may not fully capture the complexity and variability of real online conversations.

This project positions itself as a small, focused academic contribution: it explores what can be learned from synthetic data while being transparent about what cannot be concluded.

---

## 4. Key Constraints and Assumptions

### 4.1 Privacy and Data Access

- Real chat logs from gaming platforms are not available due to strict privacy rules and platform policies.
- The project does not attempt to collect or process any real user data.
- All training and evaluation will be done on synthetic data that is generated explicitly for this project.

### 4.2 Cost and Engineering Practicality

- Real-time scanning of billions of messages would require heavy engineering and infrastructure, which is beyond the scope of this capstone.
- This project does not attempt to design or implement a production-scale system; it focuses on model behavior and academic insight.

### 4.3 Cultural and Linguistic Scope

- The synthetic data will be in English only.
- Psychological stages of grooming may be universal, but linguistic patterns are culture-specific.
- As a result, any models developed in this project should be considered valid only for the synthetic English-language environment they are trained on.

---

