import playsound
import gtts
import time
import random
import os

version = "1.0.0"

# Functions Area ==========

def fetch_line(filename: str) :
    with open(filename, "r") as file :
        for line in file :
            yield line

def line_break_remover(string: str) :
    string = string.replace("\n","")
    return string

# =========================

def title_screen() :
    while True :
        print("\nWhat is this word               07 Apr 2024")
        print("===========================================")
        print("(s) - Start")
        print("(a) - About")
        print("(x) - Exit")
        print(f"\nV.{version}")
        print("===========================================")
        title_input = input(">> ")
        if title_input == "s" :
            main()
        elif title_input == "a" :
            print("\nAbout")
            print("===========================================")
            print("What is this word               07 Apr 2024")
            print("Create by Ronnapat Phawaphootanon")
            print("\nThe Simple word guessing game")
            print("You have to listen to the meaning of")
            print("the word, and then you have to answer")
            print("the word, if you can't answer you ")
            print("can give up on this word and see the answer.")
            print("\nHere the link go to original inspiration.")
            print("Link : https://www.youtube.com/playlist?list=PL2_38T-JBaYXz6gjG6eobxiMlP5t7zQan")
            print("===========================================")
            input("Press enter key to exit. ")
        elif title_input == "x" :
            print("Bye!!\n")
            exit()
        else :
            print("[Error] Invaild Input")

def main() :
    # Gather word data 
    noround = 5

    word = []
    type_word = []
    meaning = []

    box = ""

    correct = 0
    wrong = 0

    already_random = []

    data = fetch_line("wordlist.txt")
    while True :
        line = next(data)
        line = line_break_remover(line)
        word.append(line)

        line = next(data)
        line = line_break_remover(line)
        type_word.append(line)

        line = next(data)
        line = line_break_remover(line)
        meaning.append(line)

        line = next(data)
        if line == "End" :
            break

    print("Get Ready")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!!")

    for i in range(noround) :
        while True :
            key = 0
            random_word = random.randint(0, len(word) - 1)
            for j in range(len(already_random)) :
                if j == random_word :
                    continue
                else :
                    already_random.append(random_word)
                    key += 1
                    break
            if key == 1 or len(already_random) == 0 :
                break

        # Genarate Google TTS Voice
        tts = gtts.gTTS(meaning[random_word])
        tts.save("sound.mp3")
        
        while True :
            box = ""
            print(f"\nRound {i + 1}")
            print(type_word[random_word])
            for j in range(len(word[random_word])) :
                box = box + "_"
            print(box)
    
            print("\n(/l) - Listen | (/g) - Give Up")
            print("You must answer in capital letter")
            ans = input(">> ")
            if ans == "/l" :
                print(f"\nListen Carefully.")
                playsound.playsound("sound.mp3")
            elif ans == "/g" :
                wrong += 1
                print("\nYou Gave Up")
                print(f"\n{word[random_word]} ({type_word[random_word]})")
                print(meaning[random_word])
                input("\nPress enter to continue.")
                os.remove("/sound.mp3")
                break
            else :
                if ans == word[random_word] :
                    correct += 1
                    print("\nCorrect!!")
                    print(f"\n{word[random_word]} ({type_word[random_word]})")
                    print(meaning[random_word])
                    input("\nPress enter to continue.")
                    break
                else :
                    print("\nWrong!!")
                    print("Please Try again.")
    
    # Remove Sound File
    os.remove("sound.mp3")

    while True :
        print("\nYour Result")
        print("===========================================")
        print(f"Correct Guess : {noround}")
        print(f"Gave Up Guess : {wrong}")
        print("\n(n) - Next Game")
        print("(x) - Back")
        print("===========================================")
        end_input = input(">> ")
        if end_input == "n" :
            break
        elif end_input == "x" :
            title_screen()

title_screen()