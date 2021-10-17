from stopwatchmodule import Stopwatch

# define the passage that we want our typing pupil to type
sentence = 's'

# write the prompt
print('Please type the following message: ')
print(sentence)

# create a stopwatch object (named "timer") and use it to time how
timer = Stopwatch()
timer.start()
typed = input()
timer.stop()

# ensure that the passage was typed correctly
if typed == sentence:
    seconds = timer.look_at_time()
    # convert seconds to words per minute
    number_of_words = len(sentence.split())
    minutes = seconds / 60.0
    wpm = number_of_words / minutes
    
    print('Good job! Your spam speed speed was', round(wpm), 'words per minute.')
else:
    print('You made a mistake. ;-(')