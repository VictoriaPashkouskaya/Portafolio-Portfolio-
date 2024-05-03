def lazy_or_work(words):
    for word in words:
        try:
            if word.lower() == "work":
                raise ValueError("Error: Work? I'd rather relax!")
            elif word.lower() == "slack off":
                print("Well done, lazybones!")
            else:
                raise ValueError(f"Unknown word: {word}")
        except ValueError as e:
            print(e)

# Пример использования:
lazy_or_work(["work", "slack off", "study", "rest"])
