# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

The challenging part was writing `determine_winner`, the function that
compares the player's move to the computer's move. At first, I was confused
about how to check every possible combination of rock, paper, and scissors
without writing a long list of if statements. I overcame it by looking at
examples and tutorials online, and also by tracing the function by hand with
real moves to see what it returned at each step. I ended up using a `BEATS`
dictionary that maps each move to the move it defeats, so the function only
checks for a tie, then a win, and otherwise returns a loss. Once I understood
that, the function became short and easy to read.

2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

One concept I understand better now is how to store and update data in a
dictionary. A dictionary holds labeled values, called keys and values. In my
project, `game_stats` has three keys: "wins," "losses," and "ties," each
starting at zero. After each round, `play_round` adds 1 to the matching key.
I learned that the dictionary has to be created outside `play_round`. If it
were created inside the function, it would reset to zero every round and the
score would never build up.
