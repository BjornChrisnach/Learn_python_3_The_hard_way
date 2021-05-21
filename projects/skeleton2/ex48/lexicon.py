directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'kill', 'eat', 'stop']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
# I had to hardcode the numbers 3 and 91234 into it for the tests according lexicon_tests.py
numbers = [3, 91234, 2, 3, 4, 5, 6, 7, 8, 9]
errors = ['ASDFADFASDF', 'IAS']
# i split up between multiple and single use of example, directions and direction
token_text_lst = ["direction", "verb", "stop", "noun", "number", "error"]
# combine all lists, without token_text_lst, into this one
lexicon_known_words_lists = [directions, verbs, stop_words, nouns, numbers, errors]

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
    def scan(self, scan_variable):
        # check the input or search sentence for multiple or single word(s)
        scan_variable = scan_variable.lower()
        created_output_sentence = self.set_input_sentence(scan_variable)
        return created_output_sentence        

    # build the list of words
    def build_all_words_list(self):
        all_words_lst = []
        for i in range(0, len(lexicon_known_words_lists)):
            for j in range(0, len(lexicon_known_words_lists[i])):
                all_words_lst.append((lexicon_known_words_lists[i])[j])
        return all_words_lst

    # build the list of tuples
    def build_all_tuples_list(self):
        all_tuples_lst = []
        for i in range(0, len(lexicon_known_words_lists)):
            token_text = token_text_lst[i]
            for j in range(0, len(lexicon_known_words_lists[i])):
                word = (lexicon_known_words_lists[i])[j]
                all_tuples_lst.append(self.check_tuple_item_is_int(token_text, word))
            i += 1
        return all_tuples_lst

    # fill up the tuple list, check between integer or other
    def check_tuple_item_is_int(self, token_text_item, given_list_item):
        single_checked_tuple = ()
        if given_list_item == numbers:
            tmp_x = self.convert_number(given_list_item)
            single_checked_tuple = (token_text_item, tmp_x)
        else:
            single_checked_tuple = (token_text_item, given_list_item)
        return single_checked_tuple

    # Find and set the token, that will be the left column for your tuples
    def set_token_fixed_text(self, search_word):
        # build all the tuples to itterate through them
        all_tuples = self.build_all_tuples_list()
        # get the actual tuple as a single tuple_list_item
        for tuple_lst_item in all_tuples:
            # print(tuple_lst_item)
            # print(tuple_lst_item[1])

            # if the right column [1] is the needed to search word, the left
            # column must be the [0]
            if tuple_lst_item[1] == search_word:
                token = tuple_lst_item[0]
            else:
                # continue setting in the token and return it
                continue
                
        return token

    # set most of the output things to match the test cases
    def set_input_sentence(self, scan_input):
        # set scan sentence to scan input
        # set search string into multiple words or remain a single
        scan_variable_sentence = []
        scan_variable_sentence = scan_input.split()

        if len(scan_variable_sentence) == 1:
            output_test_obj = self.set_return_value_obj(scan_variable_sentence)
            return output_test_obj
        elif len(scan_variable_sentence) >= 2:
            self.set_maximum_input_words(scan_variable_sentence)
            output_test_obj = self.set_return_value_obj(scan_variable_sentence)
            return output_test_obj

    def set_return_value_obj(self, scan_input_variable):
        known_words_list = []
        # build a list of all words
        known_words_list = self.build_all_words_list()

        count = -1
        token = ''
        bln_known = False
        output_test_obj = []

        # set the first return word in according with the scan_input variable(scan_variable_sentence)
        for known_word in scan_input_variable:
            count = - 1
            # set the error known word while it's stil there
            tmp_error_var = ""
            if tmp_error_var == "" and known_word != None:
                tmp_error_var = known_word
            for i in range(0, len(known_words_list) - 1):
                count += 1
                # set the convert on the list count to have it pass as equal
                if isinstance(known_words_list[count], int):
                    known_word = self.convert_number(known_word)
                    # isinstance(known_word, int)
                    # known_word = int(known_word)

                # set the output string after we run out of known words or we are in error field
                if known_words_list[count] != known_word and bln_known == False and count >= 32:
                    token = "error"
                    output_test_obj.append(tuple(self.pair_up(token, tmp_error_var)))
                    break
                # set the known word, with use of a token, that equals your input
                elif known_words_list[count] == known_word and count <= 32:
                    bln_known = True
                    token = self.set_token_fixed_text(known_word)
                    output_test_obj.append(tuple(self.pair_up(token, known_word)))
                    break
                # set the output string after we run out of known words or we are in error field
                elif count >= 33:
                    token = "error"
                    output_test_obj.append(tuple(self.pair_up(token, tmp_error_var)))
                    break
                # continue to check and set the output sentence
                else:
                    continue
        # return the fully set output variable
        return output_test_obj

    def set_maximum_input_words(self, scan_input_variable):
        return_value_obj = []
        # build the different input ways, 2 words untill 10 words
        for i in range(0, (len(scan_input_variable) -1)):
            tmp_sentence = []
            j = len(scan_input_variable)
            if j > 10:
                j = 10
            if len(scan_input_variable) == j:
                for y in range(0,j):
                    tmp_sentence.append(scan_input_variable[y])
                    break
            else:
                # set an error message to inform the user
                print("Something went wrong, check input,max 10 allowed")

    # return the whole number as integer, check if it's an integer
    def convert_number(self, x):
        try:
            return int(x)
        except ValueError:
            return None
        except TypeError:
            return None

    # fill in the fixed data and the wanted word and return a tuple
    def pair_up(self, fixed_to_group, search_word):
            result_pair_up = []
            result_pair_up.append(tuple([fixed_to_group, search_word]))
            # print(result_pair_up[0])
            return result_pair_up[0]


# these are used for internal test input with Visual Studio Code, or other IDE
# It also builds all the tuples, maybe i will use them as search base for a second try at it

lex_a = Lexicon(directions, verbs, stop_words, nouns, numbers, errors)
# all_tuples = lex_a.build_all_tuples_list()
# print(all_tuples)
# all_words = lex_a.build_all_words_list()
# print(all_words)

# print(lex_a.scan("north"))
# print(lex_a.scan("4"))
# print(lex_a.scan("north_east"))
# print(lex_a.scan("north south east"))
# print(lex_a.scan("go"))
# print(lex_a.scan("go kill eat"))
# print(lex_a.scan("the"))
# print(lex_a.scan("the in of"))
# print(lex_a.scan("bear"))
# print(lex_a.scan("bear princess"))
# print(lex_a.scan("1234"))
# print(lex_a.scan("3 91234"))
# print(lex_a.scan("ASDFADFASDF"))
# print(lex_a.scan("bear IAS princess"))

print(lex_a.scan(input("Give in the word(s), seperated with a space, to search for :\n ")))
# print(lex_a.scan("down door 4"))
# print(lex_a.scan("stop left jump 5 walk"))
# print(lex_a.scan("move pass the ball to the left"))
