# recieve a string of text and clean it;
# cleaning means having only english letters;

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


text = input()
print(clean_words(text))

