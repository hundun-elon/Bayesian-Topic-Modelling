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

filename = input()
with open(filename, 'r', encoding='utf-8') as file:
      for line in file:
            print(line)




# text = input()
# print(clean_words(text))

