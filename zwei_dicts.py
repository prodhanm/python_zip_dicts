first_dict = {"A": 10, "B": 25, "C": 13}
second_dict = {"A": 12, "B": 45, "C": 89}

def two_dicts():
    for (char1, num1), (char2, num2) in \
        zip(first_dict.items(), second_dict.items()):
        if char1 == char2:
            print(f"{char1}: {num1},{num2}")

def main():
    two_dicts()

if __name__ == "__main__":
    main()