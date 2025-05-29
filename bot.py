from data_dict import crypto_db

def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending_cryptos = [k for k, v in crypto_db.items() if v["price_trend"] == "rising"]
        return f"Trending cryptos: {', '.join(trending_cryptos)}"

    elif "long-term" in user_query or "buy" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"{coin} looks great for long-term growth!"
        return "I'm not sure, but consider coins with rising trends and high market caps!"

    else:
        return "Sorry, I didn’t catch that. Try asking about trending or sustainable cryptos!"
