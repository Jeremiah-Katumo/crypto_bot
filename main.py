from bot import greet_user, get_user_input, respond_to_query, disclaimer, speak


def get_user_input():
    return input("You: ").lower()


def main():
    greet_user()
    while True:
        query = get_user_input()
        if query == "exit":
            disclaimer()
            speak("Bye for now! Catch you on the blockchain.")
            break
        respond_to_query(query)


if __name__ == "__main__":
    main()
