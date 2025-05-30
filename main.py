
# main.py - Entry point for chatbot interaction

# Define cryptocurrency data
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# Define chatbot logic
def get_crypto_recommendation(user_query):
    if "sustainable" in user_query.lower():
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"
    
    elif "trending" in user_query.lower():
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"Trending cryptos: {', '.join(trending_coins)} 🚀"

    else:
        return "I can help with crypto trends! Ask about sustainability or trending coins."

# User interaction
def chatbot():
    print("CryptoBuddy: Hey there! Ask me about trending cryptos or sustainability! 🌍🚀")
    
    while True:
        user_query = input("You: ")  # Get user input
        if user_query.lower() == "exit":
            print("CryptoBuddy: Goodbye! Stay crypto-smart. 🛠️")
            break
        response = get_crypto_recommendation(user_query)
        print(f"CryptoBuddy: {response}")

# Run chatbot
chatbot()
