from sys import argv

script, user_name, code = argv
prompt = '>' #SD2 vb '=', 'antwoord:' f'{script}> 'etc.

print(f"Hi {user_name} , I'm the {script} script. How are you liking {code} so far?.") #SD3code
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")
#SD1: http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq
#SD1: https://my.ign.com/atari/adventure
#SD4: Make sure you understand how I combined a """ style multiline string with the {} format activator as the last print.