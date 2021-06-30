print("""The lion is chasing from behind!Please choose the way 1 or 2?""")

way = input("> ")

if way == "1":
    print("There is a huge wall.")
    print("what do you do?")
    print("1.Climb the wall.")
    print("2.Make a hole in the wall.")

    lion = input("> ")

    if lion == "1":
        print("There was a snake at the end of the climb. Do not mind.")
    elif lion == "2":
        print("The wall collapsed and it was buried alive. Stupid.")
    else:
        print("It was delicious without leaving any bones.")

elif way =="2":
    print("There is a big lake in front of you")
    print("What do you do?.")
    print("1.Swim")
    print("2.Get on the boat")
    print("3.Give up")

    insanity = input("> ")

    if insanity == "1":
        print("Died after being eaten by a shark")
        print("Idiot")
    elif insanity == "2":
        print("There was a hole in the ship and it sank.")
        print("unlucky!")
    elif insanity == "3":
        print("The lion was tired and went home.")
        print("You are lucky!")
    else:
        print("It was delicious without leaving any bones.")

else:
    print("It was delicious without leaving any bones.")

