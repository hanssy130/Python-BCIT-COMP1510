filename = 'alice.txt'
alices = ""
with open(filename, 'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    alices += line.rstrip()

q_counter = 0

for i in range(0,len(alices)):
    if alices[i] == "Q" or alices[i] == "q":
        q_counter +=1

print("There are " + str(q_counter) + " q's in the text.")

the_counter = 0
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0,len(alices)):
    if alices[i] == "T" or alices[i] == "t":
        if alices[i+1] == "h":
            if alices[i+2] == "e":
                if alices[i+3] in letters:
                    the_counter += 1
print("There are " + str(the_counter) + " 'the's in the text.")


# nucs = ""
# for line in lines:
#     nucs += line.rstrip()
# print(lines)
# nuc_a = ""
# nuc_g = ""
# nuc_t = ""
# nuc_c = ""
# for i in range(0,len(nucs)):
#     if lines[0][i] == "A":
#         nuc_a += lines[0][i]
#     if lines[0][i] == "G":
#         nuc_g += lines[0][i]
#     if lines[0][i] == "C":
#         nuc_c += lines[0][i]
#     if lines[0][i] == "T":
#         nuc_t += lines[0][i]
# print(len(nucs))
# print("There are this many A nucleotides: " + str(len(nuc_a)))
# print("There are this many C nucleotides: " + str(len(nuc_c)))
# print("There are this many T nucleotides: " + str(len(nuc_t)))
# print("There are this many G nucleotides: " + str(len(nuc_g)))
# gcountlist = []
# gcounter = 0
# for i in range(0, len(nucs)):
#     if lines[0][i] == "G":
#         gcounter += 1
#     else:
#         gcountlist.append(gcounter)
#         gcounter = 0
# gcountlist.sort()
# print("THE LONGEST G STRABD:", gcountlist.pop(-1))