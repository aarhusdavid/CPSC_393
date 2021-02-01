# https://towardsdatascience.com/markov-models-and-trump-tweets-91b0d3f0f1eb

rhymes = open("nursery.txt", "r") #opens file
rhymetxt = rhymes.read() # reads file
rhymetxt = rhymetxt.lower() # turns all text to lowercase


words = rhymetxt.split() #grabs all the words from the text and removes extra white space
words = [word.strip('.,`!";_=+:(){}''~[]\?') for word in words] #removes excess punctuations
words = [word.replace("'s","") for word in words] # words that end in 's are changed to singular
words = [word.replace("-"," ") for word in words] # words that have '-' in between themselves have the '-' removed


unique_words = [] #state space
for word in words: # iterates through the words and grabs each unique word and adds it to an array
    if word not in unique_words: # checks to see if word is already in unique array
        unique_words.append(word) # adds word to array

word_dict = {} #trajectory / path, decided to create a dictionary of words like in the DNA assignment
i = 0 # variable for starting at index 0 of the array
for i in range(len(unique_words)): # loops through and indexes each word
    word_dict[unique_words[i]] = i

#3d array
# wordMatrix = [[[0 for x in range(len(unique_words))]
#                 for y in range(len(unique_words))]
#                 for z in range(len(unique_words))]

wordMatrix = {}
# for i in range(0, len(words)):
#     for n in range(0, len(i) - 1):
#         for p in range(0, len(n) - 2):
#             if words[p] in word_dict.keys():
#                 wordMatrix[word_dict[words[p-2]]][word_dict[words[p-1]]][word_dict[words[p]]] += 1
#             else:
#                 wordMatrix[word_dict[words[p-2]]][word_dict[words[p-1]]][word_dict[words[p]]] = 1
#
for i in range(len(words)):
    for p in range(i - 2):
        if words[p] in word_dict.keys():
            wordMatrix[word_dict[words[p-2]]][word_dict[words[p-1]]][word_dict[words[p]]] += 1
        else:
            wordMatrix[word_dict[words[p-2]]][word_dict[words[p-1]]][word_dict[words[p]]] = 1

# if words[p] in word_dict.keys():
#     wordMatrix[word_dict[words[p-2]]][word_dict[words[p-1]]][word_dict[words[p]]] += 1
# else:
#     wordMatrix[word_dict[words[p-2]]][word_dict[words[p-1]]][word_dict[words[p]]] = 1

# print(wordMatrix)

# probabilities
probMatrix = []
for l in wordMatrix:
    for m in l:
        sum_row = sum(m)
        if sum_row == 0:
            pass
        else:
            prob = [t/sum_row for t in m]
            probMatrix.append(prob)

# print(probMatrix)
print(len(probMatrix)) #107

# This was my attempt to write a new rhyme below.

new_rhyme = []
for i in range(20):
    for j in range(30):
        if i == 0 and j == 0:
            new_rhyme.append("the")
        elif i ==0 and j == 1:
            new_rhyme.append("dog")
        else:
            new_rhyme.append(probMatrix[word_dict[words[i-2]]][word_dict[words[i-1]]][word_dict[words[i]]])
print(new_rhyme)
