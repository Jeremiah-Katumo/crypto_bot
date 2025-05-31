import string
import random

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

def clean_input(text):
    # Normalize user input by removing punctuation
    return text.lower().translate(str.maketrans("", "", string.punctuation))

def chatbot():
    print("Hey! I'm CryptoBuddy—your AI-powered financial sidekick!")
    print("Always remember crypto is risky business. Do your own research before investing!\n")
    print("Ask me about trending cryptos, sustainability, or what to invest in. Type 'help' if you're lost!")
   

    last_coin_mentioned = None

    while True:
        user_query = input("\nYou: ")
        cleaned_query = clean_input(user_query)

        if "exit" in cleaned_query or "bye" in cleaned_query:
            print("CryptoBuddy: Catch you later! Remember, don’t put all your eggs in one blockchain!")
            break

        elif "help" in cleaned_query:
            print("CryptoBuddy: Here's what I got for you:\n"
                  "- Trending coins (e.g., 'What’s hot right now?')\n"
                  "- Sustainable cryptos (because the planet matters!)\n"
                  "- Long-term investment suggestions\n"
                  "- Coin stats like 'Tell me about Ethereum'\n"
                  "- Type 'exit' to peace out anytime.")

        elif "trending" in cleaned_query or "rising" in cleaned_query:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            if trending:
                phrases = [
                    f"Right now, these coins are riding the rocket: {', '.join(trending)}.",
                    f"Hot off the press! Trending coins you might wanna peek at: {', '.join(trending)}.",
                    f"The crypto market’s buzzing about these rising stars: {', '.join(trending)}."
                ]
                print(f"CryptoBuddy: {random.choice(phrases)}")
            else:
                print("CryptoBuddy: Hmm, no coins are really on fire at the moment. Maybe time to chill?")

        elif "sustainable" in cleaned_query or "eco" in cleaned_query:
            best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            score = crypto_db[best]['sustainability_score']
            print(f"CryptoBuddy: If you care about Mother Earth, {best} is your champ with a green score of {score}/10. Invest smart, save the planet!")

        elif "long term" in cleaned_query or "longterm" in cleaned_query or "long-term" in cleaned_query:
            candidates = [coin for coin in crypto_db
                          if crypto_db[coin]["price_trend"] == "rising"
                          and crypto_db[coin]["market_cap"] in ["high", "medium"]
                          and crypto_db[coin]["sustainability_score"] >= 6]
            if candidates:
                print("CryptoBuddy: Just a quick reminder—crypto is risky. Always do your own research before investing!\n")
                print(f"CryptoBuddy: For long-term growth, consider: {', '.join(candidates)}.")
            else:
                print("CryptoBuddy: Nothing meets all long-term growth criteria right now.")

        elif "short term" in cleaned_query or "shortterm" in cleaned_query or "short-term" in cleaned_query:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            stable = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "stable"]
            suggestions = trending + stable
            if suggestions:
                print(f"CryptoBuddy: For short-term moves, check these out: {', '.join(suggestions)}.")
            else:
                print("CryptoBuddy: No good short-term picks right now. Maybe hold tight.")

        elif any(coin.lower() in cleaned_query for coin in crypto_db):
            for coin in crypto_db:
                if coin.lower() in cleaned_query:
                    last_coin_mentioned = coin
                    info = crypto_db[coin]
                    print(f"CryptoBuddy: Here's the lowdown on {coin}:\n"
                          f"- Price Trend: {info['price_trend'].capitalize()}\n"
                          f"- Market Cap: {info['market_cap'].capitalize()}\n"
                          f"- Energy Use: {info['energy_use'].capitalize()}\n"
                          f"- Sustainability Score: {info['sustainability_score']}/10\n"
                          "Got more questions about it? Just ask!")
                    break

        elif ("sustainability" in cleaned_query or "energy" in cleaned_query or "market cap" in cleaned_query) and last_coin_mentioned:
            info = crypto_db[last_coin_mentioned]
            if "sustainability" in cleaned_query:
                print(f"CryptoBuddy: {last_coin_mentioned} scores {info['sustainability_score']}/10 on sustainability.")
            elif "energy" in cleaned_query:
                print(f"CryptoBuddy: {last_coin_mentioned} consumes {info['energy_use']} energy. Keep that in mind!")
            elif "market cap" in cleaned_query:
                print(f"CryptoBuddy: {last_coin_mentioned} has a {info['market_cap']} market cap. That’s pretty solid!")

        elif ("sustainability" in cleaned_query or "energy" in cleaned_query or "market cap" in cleaned_query) and not last_coin_mentioned:
            print("CryptoBuddy: Which coin? You gotta name-drop it first, or I’m lost!")

        else:
            print("CryptoBuddy: Hmm... I’m not sure what you mean. Try asking about trends, sustainability, or name a coin! Type 'help' for tips.")

if __name__ == "__main__":
    chatbot()
