# Milestone 1: Problem Identification

## 1. Problem Statement

Online grooming is a gradual psychological process in which an adult builds trust and emotional connection with a child, often through casual, friendly conversations that appear harmless at first. Gaming chats — because of their fast pace, informal tone, and social nature — can create an environment where grooming behaviors are difficult to detect early. Many safety tools designed to help parents rely heavily on keyword lists or basic filtering, which often fail to capture the subtle, context-dependent signals embedded in grooming attempts.

However, studying grooming detection scientifically is challenging. Real gaming chat logs are protected by strict privacy rules, platform policies, and ethical considerations. The financial and engineering costs required to scan billions of real-time messages at scale create another barrier. Because of these constraints, this project takes an academic approach: it relies on synthetic data to explore how machine-learning models behave when attempting to distinguish between grooming and non-grooming conversations. While synthetic data cannot fully represent the complexity of real online communication, it allows controlled experimentation and honest evaluation of what machine learning might achieve under limited conditions.

As a mother who watches her own children navigate online games every day, this issue is deeply personal. I see firsthand how much joy, creativity, and social connection these digital spaces provide — and I also see the risks hiding behind seemingly innocent messages. This project grew out of a desire to understand whether technology could be used thoughtfully to make online environments safer for children without taking away the benefits and excitement of play.

---

## 2. Research Questions

1. Can machine-learning models distinguish between synthetic grooming and non-grooming chats more effectively than simple keyword-based filters?
2. How do different model types (Logistic Regression, SVM, MLP) perform when trained on synthetic chat data representing various stages of grooming?
3. What patterns do keyword-based methods miss that machine-learning models are able to capture, and what kinds of errors do each method tend to make?
4. How do class distribution choices in the synthetic dataset (balanced vs. imbalanced) influence model performance and the interpretation of results?
5. Given cultural, privacy, and data-access limitations, what are the boundaries of what can be learned from synthetic data in this context?

---

## 3. Context & Background

Studies of online grooming often highlight four broad psychological stages: friendship forming, trust building, isolation, and escalation. These stages tend to be universal across cultures, but the language used to convey them is highly dependent on culture, community, and context. This makes pure keyword detection unreliable, especially when predators intentionally use indirect or friendly language.

Commercial safety tools have not advanced far beyond keyword lists, activity monitoring, and reporting-based systems. Academic research has experimented with machine-learning approaches, but most studies rely on very small datasets, transcripts from outdated platforms, or limited publicly available corpora. Access to real chat logs remains a major obstacle.

Synthetic data generation has become a common method in early-stage safety research because it allows prototyping without violating user privacy. While synthetic datasets cannot replicate real-world complexity, they enable controlled exploration of how models behave, what signals they learn, and where they fail.

This project follows that tradition: an exploratory academic study using synthetic gaming chats to observe how machine-learning models interpret early grooming cues and where simple filtering methods break down.

---

## 4. Constraints & Assumptions

### Privacy
- Real-world chat logs from games and messaging platforms are inaccessible due to strong privacy protections and ethical restrictions.
- The project intentionally uses synthetic data to avoid storing or processing any real user conversations.

### Engineering Practicality
- Real-time scanning of massive chat platforms requires significant computational resources, which is beyond the scope of this study.
- The goal is to study model behavior, not to engineer a production-scale system.

### Cultural & Linguistic Scope
- All synthetic data is generated in English.
- Psychological stages of grooming may be universal, but linguistic patterns differ across communities.
- Findings should be interpreted as insights into a controlled synthetic environment rather than generalizable to all languages or platforms.

