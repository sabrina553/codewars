'''starting to just google things more blatantly rather than techniques, i suppose it\'s still learning '''
def reverse_words(text):
    a = []
    text = text.split(' ')
    for i in text: 
        a.append(i[::-1])
    return ' '.join(a)
print(reverse_words("hi my name is sabrina"))

#proud of this one :)
def better(text):
    return ' '.join(i[::-1] for i in text.split(' '))
print(better("hi  my  name  is"))
#nvm it doesn't work for double spaces :)
# had to add (' ') to the split function :) 

