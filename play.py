def cave():
    print("You decide to take a break in the cave. After resting for 30 mins, you're about to leave when the cave suddenly starts to shake, causing an avalanche to block the entrance.")
    print("Staying calm, you look for another way out. You see two openings, one on the left and one on the right.")
    print("Which do you choose, left or right?")
    ans1 = input()
    while ans1 != "right" or "left":
        if ans1 == "left":
            print("You walk into the left path. At the end of the path, you're presented with two more openings. One path appears dark and you can feel a cold draft coming through. From the other opening, you hear water dripping.")
            print("Do you choose the 'dark path' or the 'water path'?")
            ans1 = input()
            while ans1 != "dark path" or "water path":
                if ans1 == "dark path":
                    print("You walk through the cold tunnel until you see trees and the moonlight.")
                    print("You've reached the outside! :D")
                    break
                elif ans1== "water path":
                    print("You crawl through the damped and cramped passageway and you feel pebbles falling. All of a sudden, the rocks above you split and water rushes through. You drown.")
                    print("RIP..")
                    break
                else:
                    print("ERROR: Not a possible answer. Please try again.")
                    ans1 = input()
        elif ans1 == "right":
            print("You walk into the entrance and notice it getting darker and darker. In the next moment, you are falling into a deep chasm.")
            print("Rest in peace..")
        else:
            print("ERROR: Not a possible answer. Please try again.")
            ans1 = input()
start = '''
It's a Saturday morning and you have plans to go hiking by yourself. When you arrived, you look up to see a challenging course with a steep incline and a rocky path. Despite feeling overwhelmed, you proceed with the adventure.
'''

print(start)


print("After three long hours, you see a cave. Do you want to take a break?")
ans1 = input()
while ans1 != "no" or "yes":
    if ans1=="no":
        print("You pass by the cave and continue walking for two hours.")
        print("You find another cave up ahead, do you want to take a break?")
        ans1=input()
        if ans1 == "no":
            print("You pass the second cave and you continue hiking further up the mountain as the sun is starting to set.")
            print("It's getting late and you stumble upon another entrance to the cave. Do you want to go in and take a break?")
            ans1= input()
            if ans1 == "yes":
                cave()
            elif ans1 == "no":
                    print("It's midnight now and everyone is tired. You died from fatigue and dehydration. RIP..")
        elif ans1=="yes":
            cave()
    elif ans1=="yes":
        cave()
    else:
        print("ERROR: Not a possible answer. Please try again.")
        ans1 = input() 
