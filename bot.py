
# bot.py - Handles chatbot logic

# Define cryptocurrency data (instead of importing from data.py)
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

# Chatbot logic function
def get_crypto_recommendation(user_query):
    if "sustainable" in user_query.lower():
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"
    
    elif "trending" in user_query.lower():
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"Trending cryptos: {', '.join(trending_coins)} 🚀"

    else:
        return "I can help with crypto trends! Ask about sustainability or trending coins."
