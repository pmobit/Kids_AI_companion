#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from textblob import TextBlob

class KidCompanion:
    def __init__(self):
        self.stress_level = "medium"  # Default stress level

    def analyze_stress_level(self, text):
        # Placeholder function for stress level analysis (you might use an NLP library for this)
        return "medium"

    def calculate_sentiment_score(self, text):
        analysis = TextBlob(text)
        # The sentiment polarity ranges from -1 to 1 (negative to positive)
        return analysis.sentiment.polarity

    def is_feeling_fine(self, text):
        # Check if the kid's input contains words like "good" or "ok"
        return any(word in text.lower() for word in ["good", "ok"])

    def contains_bye(self, text):
        # Check if the kid's input contains the word "bye"
        return "bye" in text.lower()

    def calm_kid(self):
        high_stress_responses = [
            "I understand it can be challenging, especially in the hospital. How about we focus on something positive to lighten the mood? What activities or topics interest you?",
            "Dealing with hospital stays is tough. Let's talk through it together. What would make you feel a bit better right now?",
            "Your strength in facing challenges is admirable. Share your thoughts, and we'll navigate through them together."
        ]

        medium_stress_responses = [
            "It's normal to feel a bit uneasy, especially in a hospital. What specific things can we discuss to make you more comfortable?",
            "Hospitals can be overwhelming, but we can find ways to make it more manageable. What activities or topics interest you?",
            "Let's create a positive distraction together. What would you enjoy chatting about right now?"
        ]

        low_stress_responses = [
            "I'm glad you're feeling okay! Hospitals aren't the most fun places. Is there anything you'd like to chat about or do to pass the time?",
            "Great to hear that you're doing well! Anything specific on your mind? We can talk about anything you like.",
            "Being in the hospital might not be ideal, but your positive attitude is inspiring. What can we do to make your day a bit brighter?"
        ]

        if self.stress_level == "high":
            return random.choice(high_stress_responses)
        elif self.stress_level == "medium":
            return random.choice(medium_stress_responses)
        else:
            return random.choice(low_stress_responses)

    def respond_to_kid_input(self, kid_input):
        self.stress_level = self.analyze_stress_level(kid_input)

        if self.contains_bye(kid_input):
            return "AI Companion: Goodbye! Wishing you a speedy recovery. Sending you lots of positive vibes for a brighter day!"

        if "exit" in kid_input.lower():
            return "AI Companion: Goodbye! Wishing you a speedy recovery. Sending you lots of positive vibes for a brighter day!"

        # Calculate sentiment score for the first output
        sentiment_score = self.calculate_sentiment_score(kid_input)

        if sentiment_score > 0:
            sentiment_response = "AI Companion: It sounds like you're feeling positive. That's wonderful! "
        elif sentiment_score < 0:
            sentiment_response = "AI Companion: I'm here for you. If you're feeling down, we can work through it together. "
        else:
            sentiment_response = "AI Companion: Your message is neutral. How can I assist you today? "

        if self.is_feeling_fine(kid_input):
            return sentiment_response + "If there's anything specific you'd like to chat about or if you have any questions, feel free to let me know."

        if "video games" in kid_input.lower():
            return sentiment_response + "Video games can be a great way to escape and have fun. What's your favorite game, and why do you enjoy playing it?"

        if "sports" in kid_input.lower():
            return sentiment_response + "Sports are awesome! Whether you're a player or a fan, they bring people together. Do you have a favorite sport or team?"

        if "build" in kid_input.lower():
            return sentiment_response + "Building and creating things is so cool! What inspired you to start building in games? Is there a particular creation you're proud of?"

        if "friends" in kid_input.lower():
            return sentiment_response + "Missing your friends is completely understandable. Let's think about ways to stay connected. What activities do you usually enjoy doing together?"

        return sentiment_response + self.calm_kid()

def chatbot_demo():
    kid_companion = KidCompanion()

    print("AI Companion: Hi there! I'm here to chat and provide support during your time in the hospital. If you need anything specific, feel free to let me know. If you want to end our conversation, just type 'exit'.")

    while True:
        kid_input = input("Kid: ")
        response = kid_companion.respond_to_kid_input(kid_input)
        print(response)

        if kid_companion.contains_bye(kid_input):
            print("AI Companion: Goodbye! Wishing you a speedy recovery. Sending you lots of positive vibes for a brighter day!")
            break

        if "exit" in kid_input.lower():
            print("AI Companion: Goodbye! Wishing you a speedy recovery. Sending you lots of positive vibes for a brighter day!")
            break

if __name__ == "__main__":
    chatbot_demo()


# In[2]:


# Create an instance of KidCompanion
kid_companion = KidCompanion()

# Get the sentiment score for a given input text
input_text = "I love playing video games!"
sentiment_score = kid_companion.calculate_sentiment_score(input_text)

# Print the sentiment score
print(f"Sentiment Score: {sentiment_score}")


# In[ ]:




