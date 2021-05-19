directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'kill', 'eat', 'stop']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
errors = ['ASDFADFASDF', 'IAS']

class Lexicon(object):

    def __init__(self, directions, verbs, stop_words, nouns, numbers, errors):
       # self.sentence = sentence
        self.directions = directions
        self.verbs = verbs
        self.stop_words = stop_words
        self.nouns = nouns
        self.numbers = numbers
        self.errors = errors

    def scan(self, sentence2):
        count = 0
        words = sentence2.split()
        raw_feed = []
        for word in words:
            fixed_text = ["direction", "verb", "stop_word", "noun", \
                "number", "error"]
            [directions, verbs, stop_words, nouns, numbers, errors]
            
            print(directions)
            print()(directions)
            a_list = directions
            #a_list = the_lists[count]
            print[0]
            if len(words) == 1:
                #raw_feed.append((fixed_text[count], the_lists[count].index(count)))
                return raw_feed
                print(directions)
            else:
                raw_feed = []
                #if count == 4:
                 #   newlist[0] = convert_number(a_list[0])
                  #  newlist[1] = convert_number(a_list[1])

                raw_feed.append(fixed_text[count], a_list[0])
                raw_feed.append(fixed_text[count], a_list[1])
                if  ount <3 or count == 5:
                    raw_feed.append(fixed_text[count], a_list[2])
                    #return raw_feed
                    count += 1
                else:
                    count += 1
                    #return raw_feed
                    
    def convert_number(x):
        try:
            return int(x)
        except ValueError:
            return None

    
    # def BuildData(sentence):
    #     words = sentence.split()
    #     for word in words:
    #         char = str(word)
    #         char = char[-1]
    #         for i in range(0,10):
    #             if not i > (len(numbers) - 1) and char == str(numbers[i]):
    #                 raw_feed = ("numbers", word)
    #             elif not i > (len(direction) - 1) and word == direction[i]:
    #                 raw_feed = ("direction", word)
    #             elif not i > (len(verb) - 1) and word == verb[i]:
    #                 raw_feed = ("verb", word)
    #             elif not i > (len(stop_words) - 1) and word == stop_words[i]:
    #                 raw_feed = ("stop_words", word)
    #             elif not i > (len(nouns) - 1) and word == nouns[i]:
    #                 raw_feed = ("nouns", word)
    #             else:
    #                 print(" ")


MyLexicon = Lexicon(directions, verbs, stop_words, nouns, numbers, errors)
MyLexicon.scan("north south east")
# MyLexicon.builddata(direction)
# MyLexicon.builddata(verb)
# MyLexicon.builddata(stop_words)
# MyLexicon.builddata(nouns)
# MyLexicon.builddata(numbers)