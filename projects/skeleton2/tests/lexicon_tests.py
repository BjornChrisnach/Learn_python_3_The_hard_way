from nose.tools import *
from nose.tools import assert_equal
from ex48.lexicon import Lexicon

'''Don't mess arround with the test file :D !!! '''

def test_directions():
    
    assert_equal(Lexicon.scan('north'), [('direction', 'north')])
    result = Lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])
                          
def test_verbs():
                          
    assert_equal(Lexicon.scan("go"), [('verb', 'go')])
    result = Lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])
                          
def test_stops():
    assert_equal(Lexicon.scan("the"), [('stop', 'the')])
    result = Lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(Lexicon.scan("bear"), [('noun', 'bear')])
    result = Lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])
                    
def test_numbers():
    assert_equal(Lexicon.scan("1234"), [('number', 1234)])
    result = Lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])
           
def test_errors():
    
    assert_equal(Lexicon.scan("ASDFADFASDF"), 
                  [('error', "ASDFADFASDF")])
    result =Lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
