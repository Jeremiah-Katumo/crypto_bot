from bot import respond_to_query

print("Welcome to CryptoBuddy! Ask me anything about crypto!")
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("CryptoBuddy: See you next time! Stay green and savvy!")
        break
    response = respond_to_query(query)
    print("CryptoBuddy:", response)
