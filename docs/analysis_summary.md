# Analysis Summary

This document presents the main findings from my exploratory academic study on detecting grooming-related behaviors in synthetic gaming chat data. The goal of this work was not to build a production-ready safety tool, but to understand how different machine-learning models behave when trained on controlled, ethically generated examples, and to evaluate the strengths and limitations of these approaches against a simple keyword baseline.

---

## 1. Overview of the Modeling Approach

The modeling phase focused on comparing three common machine-learning methods—Logistic Regression, Support Vector Machines (SVM), and a Multi-Layer Perceptron (MLP)—against a lightweight keyword filter similar to what many commercial tools still rely on today. All models were trained on the same synthetic dataset, which I designed to reflect documented psychological stages of grooming while preserving user privacy and avoiding exposure to real harmful content.

The inclusion of a keyword baseline was intentional: it represents the current state of many safety systems, allowing a meaningful comparison between “pattern-based” and “learning-based” approaches.

---

## 2. Key Findings

### **Machine-Learning Models Outperformed the Keyword Baseline**

Across all three ML approaches:

- **Accuracy, precision, and recall were significantly higher** than the keyword-only method.  
- The ML models detected subtle conversational cues that the keyword filter could not.  
- SVM and MLP showed especially strong performance, indicating their ability to capture non-obvious textual signals.

These results confirm that grooming conversations contain patterns that machine-learning methods can learn, even in short, informal gaming-style messages.

### **Keyword Filtering Remains Too Rigid**

The keyword method struggled for two major reasons:

1. Grooming language is often indirect, friendly, or ambiguous.
2. Predators intentionally avoid explicit terms, which means “simple matching” quickly breaks down.

This reinforces what the literature already suggests: keyword filters alone are **insufficient** for early detection
