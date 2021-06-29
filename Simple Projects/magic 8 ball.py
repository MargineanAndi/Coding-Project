import random 

# Variable Declarion -----------------------------------------------------------------------------------------------------------------------------------------------------------
name = input("Please enter your name:")

question = input (name + ", what is your question for Magic 8 Ball?")

answer = ""

random.randint(1,9)

random_number = random.randint(1,9)

print(random_number)

# Core Logic for Magic 8 Ball ---------------------------------------------------------------------------------------------------------------------------------------------------

if random_number == 1 :
    answer = "Yes-defintely"
elif random_number == 2:
    answer = "It is decidely so"
elif random_number == 3 :
    answer = "Without a doubt"
elif random_number == 4 :\
    answer = "Reply hazy, try again"
elif random_number == 5 :
    answer  = "Ask again later"
elif random_number == 6 :
    answer = "Better not tell you now, you are not ready"
elif random_number == 7 :
    answer = "My sources say no"
elif random_number == 8 :
    answer = "Outlook is not good"
elif random_number == 9:
    answer = "Very doubtful, but could happen"
else :
    answer = "Error"
    
if name == "" :
    print("Question:" + name)
else:
    print(name + " asks:" + question)

print("****************************************************************")   
print("Magic 8-ball's answer: " + answer)
print("Created by Andi Marginean © 2021")
    