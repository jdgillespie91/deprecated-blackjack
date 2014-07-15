--

TOC
0. How can you contribute?
1. Welcome!
2. Blackjack Overview
3. Plan

-- 

0. How Can You Contribute?

Pay attention to the plan which describes our approach to the problem and the work that you can do to help.

1. Welcome!

We are writing a blackjack game that can be understood and played by a learning algorithm so that we can determine the optimal blackjack strategy. 

In blackjack 2.0, we aim to have a working version of blackjack that can be played by humans or automated. The human version will have a variable number of players (set by the human) and each player can input decisions to play his or her hand based on a visual description of the game. The outcome will be presented.

The automated version will have minimal output (hopefully none) and will receive decisions from an external source. This is eventually where our learning algorithm will play.

2. Blackjack Overview

http://en.wikipedia.org/wiki/Blackjack

I realise now that there are a lot of small variations in the rules that we don't need to worry ourselves about too much at this point. For now (version 2.0), we'll ignore splitting and doubling down. We will use the "H17" version of the dealer strategy (dealer hits soft 17). 

3. Plan

Step one: Write the game following the layout described in game_layout.txt using only function calls (the functions will not exist at this point). For each new function, update the documentation (functions.txt) as per the template in that file.

Step two: Write the functions described in functions.txt.

Step three: Test!

Note that these steps must be followed in order. Only when the game is fully written in terms of function calls (step one) may we move on to step two and so on.

To give an example, suppose we were writing a program that would take a temperature in degrees celsius and output that temperature in degrees fahrenheit. Step one would be

temperature_in_celsius = get_temperature_celsius()
temperature_in_fahrenheit = convert_temperature_celsius_to_fahrenheit(temperature_in_celsius)
print_temperature_fahrenheit()

Step two would then be to write functions get_temperature_celsius, convert_temperature_celsius_to_fahrenheit and print_temperature_fahrenheit according to the documentation and step three would be to test that the program does what you expect.