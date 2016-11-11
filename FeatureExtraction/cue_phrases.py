
cue_phrases = ["in conclusion", "this letter", "this report", "summary", "argue", "purpose", "develop", "attempt", "conclude", "Finally", "result", "is proved", "idea of", "this approach", "this corresponds", "should", "this method"]

newfile = input("Enter the file name: ")
#newfile = "abc.txt"
file = open(newfile, "r")
string = file.read()
#print(string)
file.close()

line = string.split(".")
no_of_lines = len(line)
print("no of lines", no_of_lines - 1)
count = 0
max = 0
weight = ["" for x in range(no_of_lines)]
for each_line in line:
    weight[count] = 0
    #print(each_line)
    words = each_line.split()
    no_of_words = len(words)
    temp = 0
    str = ''
    while(temp < no_of_words - 1):
        str = ''
        str += words[temp]
        str += " "
        str += words[temp + 1]
        for cue in cue_phrases:
            if str == cue:
                weight[count] += 1
                break
        temp += 1
    for word in words:
    #    print(word)
        for cue in cue_phrases:
            if word == cue:
                weight[count] += 1
                break
    if(weight[count] >= max):
        max = weight[count]
    count += 1

sum_weights = 0.0
for i in weight:
    sum_weights += i
    #print(i)

probs = ["" for z in range(no_of_lines)]
count = 0
req = ''
for each_line in line:
    if count == (no_of_lines-1):
        break
    if weight[count] >= 0:
        req += each_line
        req += '.'
        req += ' with probability: '
        probs[count] = weight[count]/sum_weights
        req += repr(probs[count])
        count += 1
print(req)
file = open('summary.txt', 'w')
file.write(req)
file.close()
