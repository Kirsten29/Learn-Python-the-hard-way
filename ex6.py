# hier wordt een waarde gegeven voor/aan het aantal soort mensen.
types_of_people = 10
# hier wordt diezelfde waarde in een zin gebruikt en de zin gedefinieerd door x.
x = f"There are {types_of_people} types of people."

#1 hier wordt de waarde 'binary' gedefinieerd om onderscheid te kunnen maken tussen soorten mensen.
binary = "binary"
#1 hier wordt de waarde 'don't' gedefinieerd om onderscheid te kunnen maken tussen soorten mensen.
do_not = "don't"
#1 #2 hier wordt diezelfde waarde in een zin gebruikt en de zin gedefinieerd door y.
y = f"Those who know {binary} and those who {do_not}."

#1 hier wordt 'x' aangeroepen dmv 'print'. x is al eerder gedefinieerd. (#4)
print(x)
#1 hier wordt 'y' aangeroepen dmv 'print'. y is al eerder gedefinieerd. (#11)
print(y)

#1 #2 hier wordt x' opnieuw aangeroepen in een nieuwe zin.
print(f"I said: {x}")
#1 #2 hier wordt 'y' opnieuw aangeroepen in een nieuwe zin.
print(f"I also said: '{y}'")

#1 hier wordt hilarisch als verkeerd/fout gedefinieerd als dit wordt aangeroepen.
hilarious = False
#1 #2 hier wordt een vraag over de grap gedefinieerd waarbij gebruik gemaakt wordt van het 'format' om in code antwoord te geven.
joke_evaluation = "Isn't that joke so funny?! {}"

#1 #2 hier wordt de vraag aangeroepen met de 'format'functie zodat de vraag ook gelijk beantwoord wordt.
print(joke_evaluation.format(hilarious))

#1 'w' wordt gebruikt om een zin te definieren.  
w = "This is the left side of..."
#1 'e' wordt gebruikt om een zin te definieren.
e = "a string with a right side."

#1 #4: w + e plakt heel simpel de door 'w' en 'e' gedefinieerde zinnen achter elkaar. 
print(w + e)

# the drills:
# 1 Go through this program and write a comment above each line explaining it.
# 2 Find all the places where a string is put inside a string.
# 3 Are you sure there are only four places? How do you know? Maybe I like lying.
# 4 Explain why adding the two strings w and e with + makes a longer string.