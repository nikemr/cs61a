"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string. 
   

    """
    selected =([i for i in paragraphs if select(i)])

    if k<len(selected):
        return selected[k]
    else:
        return ''

    
    
       

    
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'   

    def select(paragraph):
        paragraph= remove_punctuation(paragraph) 
        paragraph= lower(paragraph)   
        paragraph= split(paragraph)                
        for i in topic:
            if i in paragraph:
                return True
        else:
            return False   
        
    return select
    


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3

    all_words_len=len(reference_words)
    typed_words_len=len(typed_words)
    

    correct= 0

    if typed=='':
        return 0.0

    for i in range(min(typed_words_len,all_words_len)):
        if typed_words[i]==reference_words[i]:
            correct+=1

    return (correct/typed_words_len)*100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    num_word= len(typed)/5
    elapsed= elapsed/60
    return num_word/elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word

    distance_map= [(diff_function(user_word,possible,limit),possible) for possible in valid_words]
    print (distance_map)
    dist,closest_word= min(distance_map)
    
    if dist==0 :
        return closest_word

    elif dist>limit:
        return user_word
        
    else:
        return closest_word

        
def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # print(start, goal)
    if not start:
        # print("zero")
        return len(goal)

    elif start[0] == goal[0]:
        # print(" eq called")
        return shifty_shifts(start[1:], goal[1:], limit)
        
    else:
        # print("non-eq-called")
        return (1 + shifty_shifts(start[1:], goal[1:], limit-1)) if limit > 0 else 1
   

def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    # assert False, 'Remove this line'
    start[0] == goal[0]
    if not start:
        # print("start exhausted")
        return len(goal)
    if not goal:
        # print("goal exhousted")
        return len(start)

    if start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
        # print("character matched")
        # print(start, goal)
        # print(f'sonraki {start[1:]} ve {goal[1:]} ')        
        return pawssible_patches(start[1:], goal[1:], limit) 
    if limit < 0: # Feel free to remove or add additional cases
        # BEGIN
        return 1
        # END
    

    else:
        # print("else called")
        # print(start, goal)
        add_diff = 1+pawssible_patches(start, goal[1:], limit-1)
        # print("add_diff")
        # print("remove called")
        remove_diff = 1+pawssible_patches(start[1:], goal, limit-1)
        substitute_diff =1+ pawssible_patches(start[1:], goal[1:], limit-1)
        
        
        
        return min(add_diff, remove_diff, substitute_diff)
     
        


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    correct, i = 0, 0
    prompt_length = len(prompt)
    max_iteration = len(typed)
    condition = True
    while condition:
        if typed[i] == prompt[i]:
            correct += 1
            i += 1
        else:
            condition = False

        if i>=max_iteration:
            condition = False
    progress = correct / prompt_length
    report = {
        'id': user_id,
        'progress': progress,
    }
    send(report)
    return progress



def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    
    times = []
    game_len= len(words)
    repeat=0
    temp=[]
    for player_time in times_per_player:
        while repeat<game_len:
            temp.append(abs(player_time[repeat]-player_time[repeat+1]))           
            repeat+=1
        repeat=0
        times.append(temp[:])
        temp=[]
    return game(words,times)
           
           
        
    
    # return game(words,times)


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
