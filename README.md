# Connect Four Game 

This is a project I have made that plays Four Connect against a Myopic AI player, this makes use of various Evaluation functions as stated 
below and shows the respective readings given for the same for a simulation of 100 epochs for each function, further some factors were tinkered
such as game tree depth and some optimization strategies such as Alpha-beta pruning and Move-ordering was implemented as well. All the findings
and readings have been shown in a pdf part of this repository, the source code for the same has been provided for running the simulation as well.

Thank You for taking your time in having a look at this project!


## Introduction
This project implements a Game Tree-based player for Connect Four. The goal is to beat a Myopic player by looking ahead in the game tree.

## Table of Contents
- [Game Rules](#game-rules)
- [Implemented Strategies](#implemented-strategies)
- [Evaluation Functions](#evaluation-functions)
- [Alpha-Beta Pruning](#alpha-beta-pruning)
- [Move Ordering](#move-ordering)
- [Results and Comparison](#results-and-comparison)

## Game Rules
The rules of Connect Four can be found [here](https://en.wikipedia.org/wiki/Connect_Four).

## Implemented Strategies
1. Myopic Player (Player 1)
2. Game Tree Player (Player 2)

## Evaluation Functions
### Random Utility
- Assigns a random utility value to evaluate each game state.

### Set Matching Utility
- Assigns utility values based on matching sets of discs. A set of 4 for the max player gets a utility of +10000, and the same for the min player gets -10000.

### Progressive Utility
 A set of two was given a Utility value of +10, a set of 3 was given a Utility value of +100 while a set of 4 was given a utility of +10000 and same 
 for the min player in negative .
 
### Complex Utility
Taking many factors into consideration such as current available sets, proximity to the centre and number of available winning positions for the opponent.

## Alpha-Beta Pruning
Alpha Beta Pruning has been implemented to have get faster results.( For more info please see : https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

## Move Ordering
The move ordering strategy used here was starting from the middle column (Column 3), as the player having the middle of the game board had a higher
probability of winning the game faster. Similarly from there we move onto Column 2 and 4, then Column 1 and 5, and Finally Column 0 and 6. This would 
get us the higher utility functions beforehand hence helping us to prune out the weaker results.

## Results and Comparison
A pdf has been included in the repository highlighting all the results and readings from the simulations
