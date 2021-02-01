# I REFERENCED YOUR CODE ONLINE (https://canvas.chapman.edu/courses/28468/files/1833115?module_item_id=868653).
# PLEASE DO NOT EXPEL ME. CODE IS COMMENTED ACCORDINGLY. APPRECIATE THE ASSIST. WAS VERY HELPFUL
# MY ORIGINAL ATTEMPT IS COMMENTED BELOW MY SOLUTION IF YOU WANTED A QUICK LAUGH.

import math # for log func
seqfile = open("sequences.txt", "r")
test = open("test.txt", "r")

# helps identify new sequence
newseq = ""

start_count = [0,0,0,0] #start counts
nuc_counts = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #nucli counts
indexes = {'a':0,'c':1,'t':2,'g':3} # did not know how this line helped but after
                                        # looking at your code, I saw how it established
                                        # the positions of each letter in the array.
                                        # therefore allowing you to increment each nucleo count
                                        # via index. I origianlly was creating counts for all
                                        # the combininations, which now seems silly.

# iterates through each line of the file
for line in seqfile:
    if line[0] == "R" or line[0] == ">": # disregards these lines
        continue
    elif line[0] == "\n" or line.strip() == "": # did not know what strip() meant after looking at your code, so I
                                                    # learned it here (https://www.w3schools.com/python/ref_string_strip.asp)
                                                    # quite handy actually, wish I knew of it sooner.
        for i in range(len(newseq)): # iterates through sequence letter by letter
            if i == 0: # this means the start of the nucleotide
                start_count[indexes[newseq[i]]] += 1 # I was confused about this line till I made the connection about the indexes
            else: # this means not the start of the nucleotide
                nuc_counts[indexes[newseq[i-1]]][indexes[newseq[i]]] += 1 #still confused about this line, need to ask about it via slack or office hours
        newseq = "" # wipes sequence in order to iterate through new one
    else:
        newseq += line.strip() # if you've gotten this far you now add the whole like to the new sequence that you will be iterating through


# Probabilities (mostly from the solution you sent on Canvas. Code is commented accordingly.
    # Also reached out to you via slack about specific lines I did not understand)
sum_start = sum(start_count)
start_probs = [0,0,0,0]
ind = 0
for i in start_count:
    start_probs[ind] = i / sum_start
    ind+=1
# start_probs = [e/sum_start for e in start_count] # the code you did here
    # was simplier but I didn't want to copy everything so I just re-coded it
    # with a forloop

nuc_prob = [] #arracy for nucleo probabilities
for l in nuc_counts:
    sum_row = sum(l) # takes the sum of the counts for all molecule in the given row
    prob = [j/sum_row for j in l] # calculates for probability for each index of each molecule
    nuc_prob.append(prob) # addes probability to the the molecule_probility array
print(nuc_prob)
# test probability
testseq = ""
for line in test:
    if line[0] == "R" or line[0] == ">": # disregards these lines
        continue
    elif line[0] == "\n" or line.strip() == "":  #disregards these lines
        continue
    else:
        testseq += line.strip()

log_prob = 0

for i in range(len(testseq)):
    if i==0: # indentifies the start of the nucleotide
        log_prob += math.log(start_probs[indexes[testseq[i]]]) # Your code helped alot here, I would not have been able to get this
    else: #base probability on what came before it
        log_prob += math.log(nuc_prob[indexes[testseq[i-1]]][indexes[testseq[i]]]) # Your code helped alot here, I would not have been able to get this

print("The log probability of the test sequence is: " + str(log_prob))
print("The Probability of the test sequence is: " + str(math.exp(log_prob))) #super small number close to zero, program just outputs 0.0

#### ORIGINAL ATTEMPT ####

# # probability count (log)
# aa_count = float(0.0)
# ac_count = float(0.0)
# ag_count = float(0.0)
# at_count = float(0.0)
#
# ca_count = float(0.0)
# cc_count = float(0.0)
# cg_count = float(0.0)
# ct_count = float(0.0)
#
# ga_count = float(0.0)
# gc_count = float(0.0)
# gg_count = float(0.0)
# gt_count = float(0.0)
#
# ta_count = float(0.0)
# tc_count = float(0.0)
# tg_count = float(0.0)
# tt_count = float(0.0)
#
# # helps identify new sequence
# newseq = 0
#
# # length of each strand
# length = 1000000
#
# # Manually count for each sequence starting nucleotide, and count for each 'next nucleotide'
# for line in seq:
#     line_len = len(line)
#     if line[0] == "R":
#         pass
#     elif line[0] == ">":
#         newseq+=1
#         pass
#     else:
#         if newseq == 1:
#             if line[0] == "a":
#                 a_startcount += 1
#             elif line[0] == "c":
#                 c_startcount += 1
#             elif line[0] == "g":
#                 g_startcount += 1
#             elif line[0] == "t":
#                 t_startcount += 1
#             else:
#                 pass
#         for i in line:
#             if i == "a" and line[1] == "a":
#                 aa_count += 1
#             elif i == "a" and line[1] == "c":
#                 ac_count += 1
#             elif i == "a" and line[1] == "g":
#                 ag_count += 1
#             elif i == "a" and line[1] == "t":
#                 at_count += 1
#             elif i == "c" and line[1] == "a":
#                 ca_count += 1
#             elif i == "c" and line[1] == "c":
#                 cc_count += 1
#             elif i == "c" and line[1] == "g":
#                 cg_count += 1
#             elif i == "c" and line[1] == "t":
#                 ct_count += 1
#             elif i == "g" and line[1] == "a":
#                 ga_count += 1
#             elif i == "g" and line[1] == "c":
#                 gc_count += 1
#             elif i == "g" and line[1] == "g":
#                 gg_count += 1
#             elif i == "g" and line[1] == "t":
#                 gt_count += 1
#             elif i == "t" and line[1] == "a":
#                 ta_count += 1
#             elif i == "t" and line[1] == "c":
#                 tc_count += 1
#             elif i == "t" and line[1] == "g":
#                 tg_count += 1
#             elif i == "t" and line[1] == "t":
#                 tt_count += 1

# a_prob = a_count/length
# c_prob = c_count/length
# g_prob = g_count/length
# t_prob = t_count/length
#
# print(a_startcount)
# print(c_startcount)
# print(t_startcount)
# print(g_startcount)
# print("")
# print(aa_count)
# print(ac_count)
# print(ag_count)
# print(at_count)
# print(ca_count)
# print(cc_count)
# print(cg_count)
# print(ct_count)
# print(ga_count)
# print(gc_count)
# print(gg_count)
# print(gt_count)
# print(ta_count)
# print(tc_count)
# print(tg_count)
# print(tt_count)
# print("")
# print(a_prob)
# print(c_prob)
# print(g_prob)
# print(t_prob)
# print(length)
# print("")
# print(line_len)





#
# print(math.log(0.0000005))
# print(math.exp(math.log(0.0000005)))
