#The file EXAMPLE.txt is the default example file used to function the program. Please, replace this file with the text file of your choice.
fh = open('EXAMPLE.txt','r')
fhupp = fh.read().upper()
fh.close()

char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
charCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

NewChar = []   #The list in which we append the characters that have been used in the file and then it will be sorted.
NewCharCount = []   #The list in which we append the times that each character in NewChar list is being read.

for i in fhupp:   #In this 'for' loop we find the times each character is being read.
	for characters in i:
		for k in range(len(char)):
			if (characters == char[k]):
				charCount[k] += 1

for i in range(len(char)):   #In this 'for' loop we append in the NewChar and NewCharCount lists the characters that have been seen at least once and how many times each, respectively.
	if (charCount[i] != 0):
		NewChar.append(char[i])
		NewCharCount.append(charCount[i])

D = len(NewChar)
for i in range(D):   #In this 'for' loop takes place the sorting of the two lists (NewChar and NewCharCount) based on the times each character is being used in descending order.
	for j in range(0, D-i-1):
		if NewCharCount[j]<NewCharCount[j+1]:
			NewCharCount[j], NewCharCount[j+1] = NewCharCount[j+1], NewCharCount[j]
			NewChar[j], NewChar[j+1] = NewChar[j+1], NewChar[j]

for i in range(int(D/2)):   #In this 'for' loop takes place the replacement of the most used character with the least used character, then the 2nd most used character with the 2nd least used character and so on.
	if (NewCharCount[i] != NewCharCount[-i-1]):
		fhupp = fhupp.replace(NewChar[i], '&*%#$@')
		fhupp = fhupp.replace(NewChar[-i-1], NewChar[i])
		fhupp = fhupp.replace('&*%#$@', NewChar[-i-1])

#Now we print the final text that has been modified.
print(fhupp)



#python 2.x and 3.x compatible
