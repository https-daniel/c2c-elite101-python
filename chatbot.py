# for my good friend sumina
# welcome to zicobot
print("Daniel's therapy bot <3")
print("How are you feeling today?\n")

# mood ask
mood = input("Rate ur mood 1-10: ")
mood = int(mood)
# checks mood if integer
# mood stuff
if mood >= 8:
    mood_msg = "That's great. I'm happy to hear you're feeling good!"
elif mood >= 5:
    mood_msg = "You're doing alright, that's good to know."
elif mood >= 3:
    mood_msg = "If you need someone to talk to, I'm here for you."
else:
    mood_msg = "I'm sorry you're feeling this way. Remember, it's okay to seek help."

print("\n" + mood_msg)
print("\n")

# stress stuff
print("What are you stressed about right now?")
print("options: Home, School, Outside Work (Jobs, Social Life, etc.)\n")

stress = input("Type an option: ")
stress = stress.lower()
# OK BASICALLY .lower() just puts everything in lowercase so it matches the if statements. took too long to figure that out lol
if stress == "home":
    stress_msg = "Doing things at home can be stressful, especially if you have a lot of things on your plate.\n Whether it's babysitting, chores for the entire family, cooking, or other responsibilities, it can be overwhelming. Remember to take breaks and ask for help when you need it. Try to set aside some time for yourself to relax and unwind, and time-management is a big key to balancing everything. You got this."
elif stress == "school":
    stress_msg = "School is another big thing. School can be super stressful, especially with assignments, exams, and social pressures. \n What I like to do is manage my time and take breaks when needed. If I don't get a topic, I ask for help instead of feeling helpless and thinking that I'll never get it. See if your class that you're struggling with has office hours or tutoring available and focus on what topics you are struggling on."
elif stress == "outside work":
    stress_msg = "I hate outside work. Jobs and responsibilities during the weekends cut out the time that I need to do other important things for school and clubs as well. Outside work just gets in the way of everything, but it's okay. There's a simple solution to this as well.\n Two words, time management. Plan out your week and see where you can fit in your outside work without it interfering with other important things. If you're taking up too much time doing one thing, move on and come back to it later when you have more time. Take a breather at the end of every shift. I always love to get boba or do a hobby to get my mind off of work. You got this."
else:
    stress_msg = "That's great! I'm glad you have nothing to stress about. Hopefully it stays that way! :) - zicobot"

print("\n" + stress_msg + "\n")
talk = input("Do you wanna talk more about it? (yes/no): ").lower()

if talk == "yes":
    stress_lvl = input("Okay, how stressed do you feel on a scale of 1-10? ")
    print("Thanks for telling me. I'm here for you, fr.\n")
else:
    print("Alright, that's okay. You don't gotta talk if you don't wanna. :)\n")

print("More options coming soon. :o")
