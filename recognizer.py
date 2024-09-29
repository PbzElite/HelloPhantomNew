#sets up the prompt based on the string (input) which is received from the stt

originalinput = "the weather is great january fourteenth"
string = "what is the the weather like on january fourteenth"
words = string.split(' ')

for i in range(len(words)):
    if words[i] == "weather" or words[i] == "temperature" or words[i] == "calendar" or words[i] == "events" or words[i] == "announcements":
        prompt = words[i]
        break
    else:
        prompt = "not found"
print(prompt)

for i in range(len(words)):
    if words[i] == "yesterday" or words[i] == "today" or words[i] == "tomorrow":
        time = words[i]
        break
    elif words[i] == "january" or words[i] == "february" or words[i] == "march" or words[i] == "april" or words[i] == "may" or words[i] == "june" or words[i] == "july" or words[i] == "august" or words[i] == "september" or words[i] == "october" or words[i] == "november" or words[i] == "december":
        month = words[i]
        if words[i+1] == "first" or words[i+1] == "second" or words[i+1] == "third" or words[i+1] == "fourth" or words[i+1] == "fifth" or words[i+1] == "sixth" or words[i+1] == "seventh" or words[i+1] == "eighth" or words[i+1] == "ninth" or words[i+1] == "tenth" or words[i+1] == "eleventh" or words[i+1] == "twelfth" or words[i+1] == "thirteenth" or words[i+1] == "fourteenth" or words[i+1] == "fifteenth" or words[i+1] == "sixteenth" or words[i+1] == "seventeenth" or words[i+1] == "eighteenth" or words[i+1] == "nineteenth" or words[i+1] == "twentieth" or words[i+1] == "twenty-first" or words[i+1] == "twenty-second" or words[i+1] == "twenty-third" or words[i+1] == "twenty-fourth" or words[i+1] == "twenty-fifth" or words[i+1] == "twenty-sixth" or words[i+1] == "twenty-seventh" or words[i+1] == "twenty-eighth" or words[i+1] == "twenty-ninth" or words[i+1] == "thirtieth" or words[i+1] == "thirty-first":
            day = words[i+1]
            break
    else:
        time = "today"
        month = "-"
        day = "-"
print(day)