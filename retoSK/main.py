import random
import sys

from category import Category

""" 

Create five categories with questions and answers. 

"""


def create_categories():

    def category_1():
        global question_1
        global question_2
        global question_3
        global question_4
        global question_5
        question_1 = Category(1, "How many legs does a giraffe have?", [
                              "4", "3", "2", "1"], "4")
        question_2 = Category(1, "How many Stomach does a cow have?", [
                              "4", "3", "2", "1"], "4")
        question_3 = Category(1, "How many eyes does a cat have?", [
                              "4", "3", "2", "1"], "2")
        question_4 = Category(1, "How many legs does a dog have?", [
                              "4", "3", "2", "1"], "4")
        question_5 = Category(1, "How many legs does a horse have?", [
                              "4", "3", "2", "1"], "4")
    category_1()

    def category_2():
        global question_6
        global question_7
        global question_8
        global question_9
        global question_10

        question_6 = Category(2, "What is the name of the main character in the Titanic?",
                              ["Tom Cruise", "Brad Pitt", "Tom Hanks", "Leonardo DiCaprio"], "Leonardo DiCaprio")
        question_7 = Category(2, "What is the name of the second character in the Eleven O'ceans?",
                              ["Tom Cruise", "Brad Pitt", "Tom Hanks", "Leonardo DiCaprio"], "Brad Pitt")
        question_8 = Category(2, "What is the name of the main character in the Forest Gump?",
                              ["Tom Cruise", "Brad Pitt", "Tom Hanks", "Leonardo DiCaprio"], "Tom Hanks")
        question_9 = Category(2, "What is the name of the main character in the Bear?",
                              ["Tom Cruise", "Brad Pitt", "Tom Hanks", "Leonardo DiCaprio"], "Leonardo DiCaprio")
        question_10 = Category(2, "What is the name of the main character in the fifth element?",
                               ["Bruce Willis", "Brad Pitt", "Tom Hanks", "Leonardo DiCaprio"], "Bruce Willis")
    category_2()

    def category_3():
        global question_11
        global question_12
        global question_13
        global question_14
        global question_15
        question_11 = Category(3, "What means Oath in Spanish?", [
            "Cayo", "Cosa", "Juramento", "Caballo"], "Juramento")
        question_12 = Category(3, "What means faithfull in English?", [
                               "Cayo", "Cosa", "Fiel", "Caballo"], "Fiel")
        question_13 = Category(3, "What means Scissors in Spanish?", [
                               "Cayo", "Cosa", "Tijeras", "Caballo"], "Tijeras")
        question_14 = Category(3, "What means nourishment in English?", [
                               "Cayo", "Alimento", "Tijeras", "Caballo"], "Alimento")
        question_15 = Category(3, "What means the sun in Spanish?", [
                               "Cayo", "Sol", "Tijeras", "Caballo"], "Sol")
    category_3()

    def category_4():
        global question_16
        global question_17
        global question_18
        global question_19
        global question_20
        question_16 = Category(4, "What means CSS", [
                               "Cosas", "Cascadas sins", "Cascade-Style-Sheets", "Count seats"], "Cascade-Style-Sheets")
        question_17 = Category(4, "What means HTML", [
                               "Cosas", "Html", "Hyper-Text-Markup-Language", "Count seats"], "Html")
        question_18 = Category(4, "What means JavaScript", [
                               "Cosas", "JavaScript", "Java-Script", "Count seats"], "JavaScript")
        question_19 = Category(4, "What means BEM", [
                               "Cosas", "Python", "Pythons", "Block-Element-Modifier"], "Block-Element-Modifier")
        question_20 = Category(4, "What means CI", [
                               "Cool-images", "Codeigniter", "Continuos-integration", "Count seats"], "Continuos-integration")
    category_4()

    def category_5():
        global question_21
        global question_22
        global question_23
        global question_24
        global question_25
        question_21 = Category(5, "who created the Java language", [
                               "Jhon Doe", "James Gosling", "Jaime Diaz", "Ignacio Cositas"], "James Gosling")
        question_22 = Category(5, "who created the C language", [
                               "Jhon Doe", "Dennis Ritchie", "Jaime Diaz", "Ignacio Cositas"], "Dennis Ritchie")
        question_23 = Category(5, "who created the C++ language", [
                               "Bjarne Stroustrup", "James Gosling", "Jaime Diaz", "Ignacio Cositas"], "Bjarne Stroustrup")
        question_24 = Category(5, "who created the Python language", [
                               "Guido van Rossum", "James Gosling", "Jaime Diaz", "Ignacio Cositas"], "Guido van Rossum")
        question_25 = Category(5, "who created the Ruby language", [
                               "Yukihiro Matsumoto", "James Gosling", "Jaime Diaz", "Ignacio Cositas"], "Yukihiro Matsumoto")
    category_5()


""" 

Game loop  

@param prize = prize for the player
@param life = life of the player

"""


prize = 0
life = 5


def game_loop_category_1():
    print("Welcome to the game!")
    print("First Category:")
    global prize
    global life
    random_option = random.randint(1, 5)
    while(True):
        if(1 == random_option):
            print(question_1.question)
            print(question_1.options)
            answer = input("Your answer: ")
            if(answer == question_1.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")
                print(life)
                life -= 1

        elif(2 == random_option):
            print(question_2.question)
            print(question_2.options)
            answer = input("Your answer: ")
            if(answer == question_2.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")
                life -= 1

        elif(3 == random_option):
            print(question_3.question)
            print(question_3.options)
            answer = input("Your answer: ")
            if(answer == question_3.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")
                life -= 1

        elif(4 == random_option):
            print(question_4.question)
            print(question_4.options)
            answer = input("Your answer: ")
            if(answer == question_4.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")
                life -= 1

        elif(5 == random_option):
            print(question_5.question)
            print(question_5.options)
            answer = input("Your answer: ")
            if(answer == question_5.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")
                life -= 1

        if(life <= 0):
            sys.exit("You lost")


def game_loop_category_2():
    print("Second Category:")
    global prize
    global life
    random_option = random.randint(6, 10)

    while(True):

        if(6 == random_option):
            print(question_6.question)
            print(question_6.options)
            answer = input("Your answer: ")
            if(answer == question_6.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(7 == random_option):
            print(question_7.question)
            print(question_7.options)
            answer = input("Your answer: ")
            if(answer == question_7.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(8 == random_option):
            print(question_8.question)
            print(question_8.options)
            answer = input("Your answer: ")
            if(answer == question_8.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(9 == random_option):
            print(question_9.question)
            print(question_9.options)
            answer = input("Your answer: ")
            if(answer == question_9.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(10 == random_option):
            print(question_10.question)
            print(question_10.options)
            answer = input("Your answer: ")
            if(answer == question_10.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        if(life <= 0):
            sys.exit("You lost")


def game_loop_category_3():
    print("Third Category:")
    global prize
    global life
    random_option = random.randint(11, 15)

    while(True):
        if(11 == random_option):
            print(question_11.question)
            print(question_11.options)
            answer = input("Your answer: ")
            if(answer == question_11.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(12 == random_option):
            print(question_12.question)
            print(question_12.options)
            answer = input("Your answer: ")
            if(answer == question_12.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(13 == random_option):
            print(question_13.question)
            print(question_13.options)
            answer = input("Your answer: ")
            if(answer == question_13.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(14 == random_option):
            print(question_14.question)
            print(question_14.options)
            answer = input("Your answer: ")
            if(answer == question_14.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(15 == random_option):
            print(question_15.question)
            print(question_15.options)
            answer = input("Your answer: ")
            if(answer == question_15.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        if(life <= 0):
            sys.exit("You lost")


def game_loop_category_4():
    print("Fourth Category:")
    global prize
    global life
    random_option = random.randint(16, 20)

    while(True):
        if(16 == random_option):
            print(question_16.question)
            print(question_16.options)
            answer = input("Your answer: ")
            if(answer == question_16.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(17 == random_option):
            print(question_17.question)
            print(question_17.options)
            answer = input("Your answer: ")
            if(answer == question_17.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(18 == random_option):
            print(question_18.question)
            print(question_18.options)
            answer = input("Your answer: ")
            if(answer == question_18.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(19 == random_option):
            print(question_19.question)
            print(question_19.options)
            answer = input("Your answer: ")
            if(answer == question_19.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(20 == random_option):
            print(question_20.question)
            print(question_20.options)
            answer = input("Your answer: ")
            if(answer == question_20.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        if(life <= 0):
            sys.exit("You lost")


def game_loop_category_5():
    print("Fifth Category:")
    global prize
    global life
    random_option = random.randint(21, 25)

    while(True):
        if(21 == random_option):
            print(question_21.question)
            print(question_21.options)
            answer = input("Your answer: ")
            if(answer == question_21.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(22 == random_option):
            print(question_22.question)
            print(question_22.options)
            answer = input("Your answer: ")
            if(answer == question_22.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(23 == random_option):
            print(question_23.question)
            print(question_23.options)
            answer = input("Your answer: ")
            if(answer == question_23.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(24 == random_option):
            print(question_24.question)
            print(question_24.options)
            answer = input("Your answer: ")
            if(answer == question_24.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        elif(25 == random_option):
            print(question_25.question)
            print(question_25.options)
            answer = input("Your answer: ")
            if(answer == question_25.answer):
                print("Correct!")
                prize += 100
                return False
            else:
                print("Wrong!")

        if(life <= 0):
            sys.exit("You lost")


def print_points():
    print("")
    print("You have:", prize, "points")
    print("")


def save_data():
    data = open("data.txt", "x")
    data.write("Player information")
    data.write(player_name)
    data.write("\n")
    data.write(str(prize))
    data.close()


if __name__ == "__main__":
    print("*** Welcome to the Quiz Game! ***")
    print("*** You will be asked 1 questions about the 5 categories. ***")
    print("*** You will have 1 chances to answer correctly. ***")
    print("*** First We are going to create the questions ***")
    create_categories()
    print("*** Questions created. ***")
    print("*** Now we are going to start the game. ***")
    player_name = input("Enter your name: ")
    print("*** Good Luck!", player_name + " ***")
    print("\n")
    game_loop_category_1()
    print_points()
    game_loop_category_2()
    print_points()
    game_loop_category_3()
    print_points()
    game_loop_category_4()
    print_points()
    game_loop_category_5()
    save_data()
