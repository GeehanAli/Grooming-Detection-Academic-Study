import random
import pandas as pd

# ---- PATTERNS FOR NORMAL CHATS ----
normal_templates = [
    "gg that was fun lol",
    "come help me in level 3",
    "brb getting water",
    "bro you stole my loot 😂",
    "need healing asap",
    "anyone wanna team up?",
    "nah i gotta sleep soon",
    "watch out behind you!!",
    "nice shot",
    "lag is so bad today"
]

# ---- PATTERNS FOR GROOMING STAGES ----

# 1. friendship forming
friend_templates = [
    "you seem really cool, wanna play again tomorrow?",
    "you're fun to talk to, how old are you btw?",
    "you remind me of my little cousin, we should chat more",
    "you're really good at this game, we make a great team"
]

# 2. trust building
trust_templates = [
    "you can tell me anything, I’m a good listener",
    "don’t worry, I won’t judge you",
    "I feel like we’re becoming close friends",
    "you’re mature for your age"
]

# 3. isolation
isolation_templates = [
    "don’t tell others about our chats, they wouldn’t get it",
    "we should talk privately, people in the game are nosy",
    "you don’t need anyone else, you’ve got me",
    "I always have time for you, even when others don’t"
]

# 4. escalation
escalation_templates = [
    "can you send me a picture of you?",
    "let’s move this conversation somewhere more private",
    "I think I like you more than just a friend",
    "don’t tell your parents about our chats okay?"
]

# ---- GENERATE SAMPLES ----

def generate_samples(n=1000):
    data = []

    for _ in range(n//2):
        text = random.choice(normal_templates)
        data.append([text, 0, "none"])

    for _ in range(n//8):
        data.append([random.choice(friend_templates), 1, "friendship"])

    for _ in range(n//8):
        data.append([random.choice(trust_templates), 1, "trust"])

    for _ in range(n//8):
        data.append([random.choice(isolation_templates), 1, "isolation"])

    for _ in range(n//8):
        data.append([random.choice(escalation_templates), 1, "escalation"])

    random.shuffle(data)

    df = pd.DataFrame(data, columns=["text", "label", "stage"])
    return df


if __name__ == "__main__":
    df = generate_samples(1000)
    df.to_csv("data/raw/synthetic_chats_raw.csv", index=False)
    print("Synthetic dataset created successfully!")
