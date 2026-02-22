import random

while True:  
    secret = random.randint(1, 100)                                   #logika, baze
    attempts = 0
    max_attempts = 10

    print("Es iedomājos skaitli no 1 līdz 100.")
    print("Tev ir 10 mēģinājumi to uzminēt.")

    while True:                                                       #minēšana
        if attempts >= max_attempts:
            print("Mēģinājumi beigušies!")
            break

        user_input = input("Tavs minējums: ")

       
        if not user_input.isdigit():                                  #tikai skaitli
            print("Lūdzu, ievadi skaitli!")
            continue

        guess = int(user_input)
        attempts += 1
         
        #mēģinājumi 
        if guess < secret:
            print("Par mazu")
        elif guess > secret:
            print("Par lielu")
        else:
            print("🎉 Uzminēji!")
            break

    print(f"Pareizā atbilde bija: {secret}")
    print(f"Mēģinājumu skaits: {attempts}")

    again = input("Vai vēlies spēlēt vēlreiz? (jā/nē): ").lower()          #spēles atkārtošana
    if again != "jā":
        print("Paldies par spēli! 👋")
        break