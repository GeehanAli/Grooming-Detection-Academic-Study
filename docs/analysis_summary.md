# Analysis Summary

This analysis explores how different machine-learning models behave when trained on a synthetic dataset of gaming chat conversations. My goal in this capstone was not to build a real-world detection system, but to academically explore what machine learning *can* and *cannot* learn from controlled data — especially given the strong privacy, engineering, and practicality constraints surrounding real chat logs.

Throughout this work, I continually balanced two forces: the desire to understand grooming detection from a technical perspective, and the reality that true real-time systems face challenges that researchers often cannot overcome without access to private platform data. This academic exploration helped me clarify where machine learning shows promise, where it breaks down, and why the gap still exists in industry-grade tools today.

---

## Logistic Regression (LR)

Logistic Regression served as my baseline ML model.  
When trained on TF-IDF representations of the synthetic messages:

- It captured many of the clearer lexical signals in grooming attempts.
- It performed reasonably well when conversations followed patterns represented in the synthetic dataset.
- However, its reliance on word-level frequency meant it struggled with more subtle, indirect, or context-dependent grooming cues.

LR helped me understand the boundary between *simple statistical signals* and the *complex psychological patterns* described in grooming literature.

---

## Support Vector Machine (SVM)

SVM achieved the strongest performance among the classical models I tested.

Key observations:

- It excelled at separating grooming vs. non-grooming messages when lexical differences were consistent.
- It handled high-dimensional TF-IDF features effectively.
- But, similar to LR, its strength still depended heavily on the limitations of synthetic data — meaning it may not generalize well to real platforms.

SVM showed me what “best-case scenario classical ML” looks like under clean, controlled data conditions.

---

## Multi-Layer Perceptron (MLP)

The MLP model provided an interesting middle ground:

- It captured some nonlinear patterns that LR and SVM missed.
- It sometimes overfit because the dataset, while useful, does not represent all the noise and inconsistency of real chat behavior.
- It highlighted the tension between model complexity and dataset realism.

The MLP results reinforced why modern grooming-detection research often requires much larger, more diverse datasets than are publicly available.

---

## Keyword Baseline

I implemented a keyword-based detector inspired by patterns described in grooming literature and used by commercial tools.

My findings:

- The keyword filter missed many early-stage grooming cues.
- If a message did not contain an explicit trigger word, the system simply failed.
- It produced both **false negatives** (missing subtle grooming) and **false positives** (flagging harmless phrases).

This comparison confirmed why commercial keyword systems are insufficient and why some form of ML-assisted reasoning is needed — even if that ML reasoning is still experimental today.

---

## Limitations of the Models (and Why They Matter)

While all three ML models performed well on the synthetic dataset, I learned that high accuracy here does not translate to real-world safety without addressing several important limitations:

### Dataset Limitations
- Synthetic conversations cannot fully mimic real gaming language, slang, and unpredictability.
- Grooming behavior varies significantly across cultures, age groups, and platforms.
- The dataset includes clear “textbook” grooming stages, which may not appear so cleanly in reality.

### Modeling Limitations
- Classical ML models rely solely on linguistic patterns, but grooming is fundamentally a **behavioral progression**, not just a vocabulary pattern.
- Models may overfit to the artificial patterns present in synthetic data.

These limitations helped me better understand why grooming detection is still considered an open research problem.

---

## Privacy and Access Constraints

Through both my literature review and mentor feedback, I’ve realized that one of the largest barriers to advancing grooming-detection technology is simply **lack of data**.

Major constraints identified in existing research *and in the challenges I encountered personally* include:

- Real chat logs from gaming platforms are private and cannot be shared with external researchers.
- Even with permission, scanning real-time conversations requires large-scale infrastructure that is extremely costly.
- Companies avoid deep conversation analysis because of legal risk and the complexity of moderating behavioral cues across billions of messages.

These barriers directly contribute to the gap I am exploring in this project:  
**What can we learn about grooming detection using academic, controlled methods when real-world data is inaccessible?**

---

## The Gap This Project Explores

Based on all my analysis, reading, and experimentation, the main gap I am addressing is:

> There is no accessible, realistic dataset that allows researchers to study grooming detection patterns in early stages, especially within gaming environments, without violating privacy rules.

Because of this, most existing tools remain keyword-based and reactive rather than pattern-based and proactive.

My project does not claim to solve real-time grooming detection.  
Instead, it explores — academically — what machine-learning models *can* detect in a controlled environment and where they fail.

This work helps build intuition for future research and highlights the challenges that must be addressed before real-world systems can move beyond simple keyword filters.

---

## Summary

Through this analysis, I gained a deeper understanding of:

- how different ML models interpret synthetic grooming cues,
- why their performance cannot be directly applied to real-world platforms,
- how keyword filters compare to ML methods,
- and how privacy, cost, and data accessibility shape what is realistically possible in this domain.

This milestone marks the completion of my modeling stage, and it prepares me for the next phase: clearly communicating these findings and reflecting on the academic pathway I chose.

