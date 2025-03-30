# this logic cleans the line in the words; we need to do this for every line in the dict

def clean_words(text):
      res = ""

      for word in text.split(" "):
            w=""
            for char in word:
                  if char.isalpha():
                        w+=char.lower()
            res+=w+" "
            # if word.isalpha():
            #       res+= word.lower()
      
      return res 
# for sorting the dictionery


filename = input()
frequency={}
with open(filename, 'r', encoding='utf-8') as file:
      for line in file:
            line = clean_words(line)

            # now we have standard data;
            for word in line.split(' '):
                  if word in frequency:
                        frequency[word]+=1
                  else:
                        frequency[word]=1
# now sort the frequency table;
# 

data = sorted(frequency.items(), key=lambda x : x[1], reverse=True)

# print(data[1:4])
            
# print the first 3.
answer = ""
for tup in data[1:4]:
      answer+= tup[0]+ " "

# text = input()
# print(clean_words(text))

print(answer)