name = input("Please enter your name: ")
mood = input("How are you feeling today? (happy, sad, stressed, excited): ").lower()
energy = int(input("On a scale of 1 to 10, how is your energy level today?: "))

if energy < 3:
    print("Alert : Your energy seems quite low. A Nap or a break might help you recharge.")
if energy >= 5:
    print("Great! Your energy is high. Consider channeling it into productive activities or exercise.")
else:
    print("Take it easy today and do something relaxing.")

if mood == 'happy':
    print('Keep spreading positivity! Maybe share your happiness with someone else.')
elif mood == 'sad':
    print('Talk to someone you trust or do something that makes you feel better.')
elif mood == 'stressed':
    print('Take a deep breath and take a walk to clear your mind.')
elif mood == 'excited':
    print('Use that excitement to start a new project or learn something new.')
else:
    advice = "Every mood is valid, you are human and it's okay to feel different emotions. Take care of yourself and do what feels right for you."

import datetime
today = datetime.datetime.now()


#Summary


print('\nDAILY MOOD ADVISOR SUMMARY')

print(f'Name: {name}')
print(f'Mood: {mood}')
print(f'Energy Level: {energy}')
print(f'Date: {today}')
print(f'Advice: {advice}')