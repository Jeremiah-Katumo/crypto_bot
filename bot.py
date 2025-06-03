import random
import pyttsx3
from data import crypto_db, fun_facts  # Import data from data.py

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    speak("Hey there! I'm Crypto_bot, your AI-powered crypto sidekick!")
    speak("Ask me about trending coins, sustainable picks, or trusted investments.")
    speak("Say 'exit' to end the chat anytime.")
    print("-" * 50)

def respond_to_query(query):
    if "trending" in query or "rising" in query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        speak(f"These coins are trending up: {', '.join(trending)}!")
    elif "sustainable" in query or "eco" in query:
        sustainable = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        speak(f"{sustainable} is your green hero with a sustainability score of {crypto_db[sustainable]['sustainability_score']} out of 10!")
    elif "trusted" in query or "safe" in query:
        trusted = max(crypto_db, key=lambda x: crypto_db[x]["community_trust"])
        speak(f"{trusted} has the highest community trust score! Solid pick.")
    elif "long-term" in query or "hold" in query:
        candidates = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["sustainability_score"] > 6]
        if candidates:
            speak(f"For long-term growth, consider: {', '.join(candidates)}.")
        else:
            speak("Hmm... nothing screams long-term champion right now. Try again later!")
    elif "fact" in query or "tell me something" in query:
        speak(random.choice(fun_facts))
    else:
        speak("I'm not sure how to help with that. Try asking about trending, sustainable, or trusted coins.")

def disclaimer():
    speak("Crypto investments are risky. Always do your own research before investing!")
    