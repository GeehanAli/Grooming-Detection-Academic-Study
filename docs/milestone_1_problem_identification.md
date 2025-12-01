# Milestone 1: Problem Identification

## 1. Problem Statement

Online grooming is a slow and psychological process where an adult builds trust, emotional connection, and dependence with a child. In gaming environments—where conversations are fast, informal, and often friendly—it becomes especially difficult to detect early risk. Many grooming attempts begin with harmless-looking small talk, and the shift toward manipulation can be subtle and easy to overlook.

Today’s safety tools rely heavily on keyword lists or basic filtering rules. These approaches work only when explicit language appears, which is often **late in the grooming process**. They fail to catch:

- gradual trust-building  
- emotional manipulation  
- coded language  
- grooming tactics that do not use explicit words  

Scientifically studying grooming in real chat environments is extremely challenging. Modern gaming platforms do not release chat logs due to privacy regulations, ethical restrictions, and the massive cost of real-time message scanning. As a result, researchers lack access to representative data and must explore alternative methods.

This project adopts an **academic approach** centered on synthetic data. Synthetic gaming chats allow controlled investigation of how machine-learning models behave when asked to distinguish grooming from normal conversations. Although synthetic data cannot fully mirror real online interactions, it enables honest evaluation of what ML might detect—and what it fundamentally cannot.

As both a researcher and a mother whose own children play online games daily, this problem is deeply personal. I see how much creativity, joy, and social growth these platforms offer, but I also recognize the risks that can hide behind seemingly innocent messages. This project aims to explore whether technology might eventually support safer digital experiences without taking away the excitement and benefits of play.


---

## 2. Research Questions

1. Can machine-learning models distinguish between synthetic grooming and non-grooming chats more effectively than simple keyword-based filters?
2. How do different model types (Logistic Regression, SVM, MLP) perform when trained on synthetic chat data representing various stages of grooming?
3. What patterns do keyword-based methods miss that machine-learning models are able to capture, and what kinds of errors do each method tend to make?
4. How do class distribution choices in the synthetic dataset (balanced vs. imbalanced) influence model performance and the interpretation of results?
5. Given cultural, privacy, and data-access limitations, what are the boundaries of what can be learned from synthetic data in this context?

---

## 3. Context & Background

Online grooming has been studied across psychology, criminology, and computer science for over a decade.  
Although exact definitions vary, most research agrees on four broad psychological stages:

1. **Friendship forming** – initial contact, casual conversation  
2. **Trust building** – emotional connection, sharing personal details  
3. **Isolation** – steering the child away from others, creating secrecy  
4. **Escalation** – introducing inappropriate topics or intentions  

These stages appear across cultures, but the **language** used in grooming conversations is extremely varied and highly context-dependent. This makes traditional keyword-based detection unreliable. Groomers often use indirect, friendly, or coded language that never triggers simple keyword lists.

### What existing tools can (and cannot) do
Most commercial child-safety tools still rely on:

- keyword lists  
- simple phrase matching  
- activity monitoring  
- manual reporting  

They do **not** analyze conversational dynamics or psychological progression.  
Academic research has proposed machine-learning methods, but almost all prior studies face the same major limitations:

- **very small datasets** (often fewer than 300 grooming chats)  
- **outdated platforms** (e.g., old IRC logs or Perverted-Justice transcripts)  
- **lack of diversity** in language, culture, and context  
- **no real access to modern gaming chat data**  

Because of strict privacy laws and ethical concerns, researchers cannot obtain real chat logs from Roblox, Fortnite, Minecraft, Discord, etc.  
This creates a huge barrier to developing realistic detection models.

### Why synthetic data is used in safety research
Recent work in online safety, including by organizations like Thorn, CHAI, and various university labs, has increasingly used **synthetic datasets**. While not perfect, synthetic data enables early experimentation without violating privacy. It allows controlled tests of:

- what ML models *tend* to learn  
- where keyword filters fail  
- which conversational cues may be detectable  
- what the limitations of the approach are  

This project builds on that direction: an exploratory academic study using **synthetic gaming chat** to examine what signals ML models respond to, what they miss, and why current tools struggle.


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

### The Gap This Project Addresses

There is a clear gap between what commercial tools currently do and what academic research suggests might be possible.  
Today’s tools rely on keywords because:

- real chat data is inaccessible  
- real-time analysis at scale is too expensive  
- existing datasets are too small for robust ML models  

This leaves a critical research question unanswered:

**If we had a controlled dataset—even synthetic—could machine-learning models detect grooming-related conversational patterns that keyword filters miss?**

This project explores that specific gap. It does not attempt to build a production-level tool, but instead examines the *theoretical potential* and *known limitations* of ML-based detection under restricted data conditions.


