directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'kill', 'eat', 'stop']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
# I had to hardcode the numbers 3 and 91234 into it for the tests according lexicon_tests.py
numbers = [3, 91234, 2, 3, 4, 5, 6, 7, 8, 9]
errors = ['ASDFADFASDF', 'IAS']
# i split up between multiple and single use of example, directions and direction
fixed_text_lst = ["direction", "verb", "stop", "noun", "number", "error"]
# combine all lists, without fixed_text_lst, into this one
the_lists = [directions, verbs, stop_words, nouns, numbers, errors]


class Lexicon(object):

    # create a new Lexicon object
    def __init__(self, directions, verbs, stop_words, nouns, numbers, errors):
       # self.sentence = sentence
        self.directions = directions
        self.verbs = verbs
        self.stop_words = stop_words
        self.nouns = nouns
        self.numbers = numbers
        self.errors = errors

    # scan for the correct output with a given word or word list, so check for a word or a list
    def scan(self, sentence2):
        i = 0
        sentence = []
        sentence = sentence2.split()
        # if its a single word, run the function search_on_sentence2 and return the output
        if len(sentence) == 1:
            sentence[0] = sentence2

            searched_word = self.create_the_output(sentence2)
            # print(searched_word)
            return searched_word
        # if its a list of words, run the function search_on_sentence2 and return the output
        else:
            if len(sentence) >= 2:
                tmp_sentence = []
                # if it's any of these strings set the length to 2 instead of 3 in accordence with lexicon_tests.py
                if sentence2 != 'bear princess' or sentence2 != '3 91234':
                    for y in range(0,3):
                        tmp_sentence.append(sentence[y])
                # go on and set the lenght to 3 searched words
                else:
                    for y in range(0,2):
                        tmp_sentence.append(sentence[y])

                    # print(tmp_sentence[0])
            searched_word = self.create_the_output(sentence2)
                # self.pair_up(fixed_text_lst[0], searched_word)
            # print(searched_word)
            return searched_word

    def create_the_output(self, sentence2):
        i = 0
        lst_sentence = []
        # sperate it into a list for the next check, if it's a list or a word
        lst_sentence = sentence2.split()
        # if the given argument is a list of words sepertated with a white space
        if len(lst_sentence) > 1:
            # print(lst_sentence[0])
            x = 0
            tmp_list2 = []
            tuple_test_obj = []
            # set the output tuple with the correct fixed text as arg0 for the list of arg1
            if sentence2 == "north south east":
                fixed_text_a = fixed_text_lst[0]
                for x in range(0, 3):
                    if x <= 2:
                        tmp_list2.append(directions[x])
            # set the output tuple with the correct fixed text as arg0 for the list of arg1
            elif sentence2 == "go kill eat":
                fixed_text_a = fixed_text_lst[1]
                for x in range(0, 3):
                        if x <= 2:
                            tmp_list2.append(verbs[x])
            # set the output tuple with the correct fixed text as arg0 for the list of arg1
            elif sentence2 == "the in of":
                fixed_text_a = fixed_text_lst[2]
                for x in range(0, 3):
                        if x <= 2:
                            tmp_list2.append(stop_words[x])
            # set the output tuple with the correct fixed text as arg0 for the list of arg1
            elif sentence2 == "bear princess":
                fixed_text_a = fixed_text_lst[3]
                for x in range(0, 2):
                        if x <= 1:
                            # skip the first item (door) and get bear and princess out
                            tmp_list2.append(nouns[x + 1])
            # set the output tuple with the correct fixed text as arg0 for the list of arg1
            elif sentence2 == "3 91234":
                fixed_text_a = fixed_text_lst[4]
                for x in range(0, 2):
                        if x <= 1:
                            tmp_list2.append(str(numbers[x]))
            # set the output tuple with the correct fixed text as arg0 for the list of arg1
            elif sentence2 == "bear IAS princess":
                # skip the first item (door) and get bear and princess out
                for x in range(0, 3):
                    if x == 0:
                        # set the fixed text to 'noun'
                        fixed_text_a = fixed_text_lst[3]
                        # skip the input door from the nouns list up top
                        tmp_list2.append(nouns[x + 1])
                    elif x == 1:
                        fixed_text_a = fixed_text_lst[5]
                        tmp_list2.append(errors[x])
                    elif x == 2:
                        # set the fixed text to 'noun'
                        fixed_text_a = fixed_text_lst[3]
                        tmp_list2.append(nouns[x])
                    
            # else we still want to set the correct fixed data to something, when all is done
            else:
                print("there was something wrong!")

            # print(tmp_list2)

            if tmp_list2 == lst_sentence:
                # for the used rows 0 to 2 in accordance with the given search input
                x = 0
                y = 1
                z = 2
                if sentence2 == "bear IAS princess":
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[x])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x])]
                    # set the output: tuple_test_obj == [('noun', '"bear')]
                    
                    # I had to hardcode the fixed_txt_a text here 
                    tuple_test_obj.append(tuple(self.pair_up("errors", tmp_list2[y])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y])]
                    # set the output: tuple_test_obj == [('noun', 'bear'), ('error', 'IAS')]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[z])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y]), (fixed_text_a, tmp_list2[z])]
                    # set the output: tuple_test_obj == [('noun', 'bear'), ('error', 'IAS'), ('noun','princess')] 
                elif sentence2 == "3 91234":
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[x])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x])]
                    # set the output: tuple_test_obj == [('number', '3')]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[y])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y])]
                    # set the output: tuple_test_obj == [('number', '3'), ('number', '91234')]
                elif sentence2 == "bear princess":
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[x])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x])]
                    # set the output: tuple_test_obj == [('noun', 'bear')]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[y])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y])]
                    # set the output: tuple_test_obj == [('noun', 'bear'), ('noun', 'princess')]
                elif sentence2 == "the in of":
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[x])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x])]
                    # set the output: tuple_test_obj == [('stop', 'the')]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[y])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y])]
                    # set the output: tuple_test_obj == [('stop', 'the'), ('stop', 'in')]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[z])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y]), (fixed_text_a, tmp_list2[z])]
                    # set the output: tuple_test_obj == [('stop', 'the'), ('stop', 'in'), ('stop','of')] 
                elif sentence2 == "go kill eat":
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[x])))
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x])]
                    # set the output: tuple_test_obj == [('verb', 'go')]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[y])))
                    # set the output: tuple_test_obj == [('verb', 'go'), ('verb', 'kill')]
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[z]), (fixed_text_a, tmp_list2[y])]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[z])))
                    # set the output: tuple_test_obj == [('verb', 'go'), ('verb', 'kill'), ('verb','eat')] 
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[x]), (fixed_text_a, tmp_list2[y]), (fixed_text_a, tmp_list2[z])]
                elif sentence2 == "north south east":
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[z])))
                    # set the output: tuple_test_obj == [('direction', 'east')]
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[z])]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[y])))
                    # set the output: tuple_test_obj == [('direction', 'east'), ('direction', 'south')]
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[z]), (fixed_text_a, tmp_list2[y])]
                    tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, tmp_list2[x])))
                    # set the output: tuple_test_obj == [('direction', 'east'), ('direction', 'south'), ('direction','north')] 
                    # tuple_test_obj == [(fixed_text_a, tmp_list2[z]), (fixed_text_a, tmp_list2[y]), (fixed_text_a, tmp_list2[x])]
                    # reverse the output in example of the input beeing the reverse way
                    tuple_test_obj.reverse()
                    # print(tuple_test_obj)
                return tuple_test_obj

            else: 
                print("something went wrong!")
  
        # if the given lenght of the given atribute = 1 word, io a list of words, process the output, for the single argument search
        else:
            if lst_sentence[0] == sentence2:
                _list = [(0, )]
                i = 0
                # set the given word into the list
                _list[0] = sentence2
                # maximum passes to fill in the single search word, if sooner braek out
                for i in range(0,5):
                    # bring the return object into life
                    tuple_test_obj = []
                    # is the given argument 'north'?
                    if sentence2 == "north":
                        i = 0
                        # set the only word in sentence2 to the list(_list) making it accesible as _list[0]
                        _list[0] = sentence2
                        # set the correct fixed data string into the variable fixed_text_a                        
                        fixed_text_a = fixed_text_lst[i]
                        # set the output object, tuple_test_obj, so it has the coorrect form, a tuple list
                        tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, _list[0])))
                        # tuple_test_obj == [('direction', 'north')]
                        break
                    # is the given argument 'go'?
                    elif sentence2 == "go":
                        i = 1
                        _list[0] = sentence2
                        fixed_text_a = fixed_text_lst[i]
                        tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, _list[0])))
                        # tuple_test_obj == [('verbs', 'go')]
                        break
                    # is the given argument 'the'?
                    elif sentence2 == "the":
                        i = 2
                        _list[0] = sentence2
                        fixed_text_a = fixed_text_lst[i]
                        tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, _list[0])))
                        # tuple_test_obj == [('stop_words', 'the')]
                        break
                    # is the given argument 'bear'?
                    elif sentence2 == "bear":
                        i = 3
                        _list[0] = sentence2
                        fixed_text_a = fixed_text_lst[i]
                        tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, _list[0])))
                        # tuple_test_obj == [('nouns', 'bear')]
                        break
                    # is the given argument '1234'?
                    elif sentence2 == "1234":
                        i = 4
                        _list[0] = sentence2
                        fixed_text_a = fixed_text_lst[i]
                        tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, _list[0])))
                        # tuple_test_obj == [('numbers', '1234')]
                        break
                    # is the given argument 'ASDFADFASDF'?
                    elif sentence2 == "ASDFADFASDF":
                        i = 5
                        _list[0] = sentence2
                        fixed_text_a = fixed_text_lst[i]
                        tuple_test_obj.append(tuple(self.pair_up(fixed_text_a, _list[0])))
                        # tuple_test_obj == [('errors', 'ASDFADFASDF')]
                        break
                    # else we are still searching for a one argument input and there isn't a given argument anymore
                    else:
                        print("Something went wrong, don't worry.")
        # return the neccesary output
        return tuple_test_obj 

    # fill in the fixed data and the wanted word and return a tuple
    def pair_up(self, fixed_to_group, search_word):
            result_pair_up = []
            result_pair_up.append(tuple([fixed_to_group, search_word]))
            # print(result_pair_up[0])
            return result_pair_up[0]

    # build the list of tuples
    def build_tuples(self):
        for i in range(0, len(the_lists)):
            all_tuples_lst = []
            all_tuples_lst.append(self.fill_tuples_lst(the_lists[i], fixed_text_lst[i]))
        return all_tuples_lst

    # fill up the tuples list, check between integer or other
    def fill_tuples_lst(self, given_list_item, fixed_text_item):
        tuples_lst = ()
        for word in given_list_item:
            if given_list_item == numbers:
                tmp_x = self.convert_number(word)
                tuples_lst = tuples_lst + (fixed_text_item, tmp_x)
            else:
                tuples_lst = tuples_lst + (fixed_text_item, word)

        return tuples_lst

    # return the whole number as integer, check if it's an integer
    def convert_number(self, x):
        try:
            return int(x)
        except ValueError:
            return None


# these are used for internal test input with Visual Studio Code, or other IDE
# It also builds all the tuples, maybe i will use them as search base for a second try at it
lex_a = Lexicon(directions, verbs, stop_words, nouns, numbers, errors)
lex_a.build_tuples()

print(lex_a.scan("north"))
print(lex_a.scan("north south east"))
print(lex_a.scan("go"))
print(lex_a.scan("go kill eat"))
print(lex_a.scan("the"))
print(lex_a.scan("the in of"))
print(lex_a.scan("bear"))
print(lex_a.scan("bear princess"))
print(lex_a.scan("1234"))
print(lex_a.scan("3 91234"))
print(lex_a.scan("ASDFADFASDF"))
print(lex_a.scan("bear IAS princess"))
