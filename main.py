import random

quotes = [
    "Believe in yourself.",
    "Small steps lead to big results.",
    "Never stop learning.",
    "Consistency beats motivation.",
    "Every expert was once a beginner.",
    "Your only limit is your mindset.",
    "Progress is better than perfection.",
    "Dream big and work hard."
]


def show_random_quote():
    quote = random.choice(quotes)
    print("\nYour motivational quote:")
    print(f'"{quote}"')


def main():
    print("=" * 35)
    print("     RANDOM QUOTE GENERATOR")
    print("=" * 35)

    while True:
        print("\n1. Get a random quote")
        print("2. Exit")

        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            show_random_quote()
        elif choice == "2":
            print("Keep going. You have got this!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
