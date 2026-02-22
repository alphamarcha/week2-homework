# fizzbuzz.py
import sys

def main():
    try:
        N = int(sys.argv[1])
        if N < 1:
            raise ValueError
    except (IndexError, ValueError):
        print("Kļūda: N nav norādīts vai nav skaitlis")
        return

    rules = {3: "Fizz", 5: "Buzz" 7: "Jazz"}  

    print(", ".join(
        "".join(word for div, word in rules.items() if i % div == 0) or str(i)
        for i in range(1, N + 1)
    ))

if __name__ == "__main__":
    main()