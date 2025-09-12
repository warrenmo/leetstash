# Lead up to the solution

With these 1-vs-1 problems (and other types of problems),
I've realized that there's potentially a LOT of value to be had
when you simply run through the base case and a few simple cases after that.

From there, I tend to get a sense of a solution and a "proof"
(the order these come to me varies depending on the time of day).

# Solution

After running through a few simple cases,
it starts to become clear that, so long as Alice has a valid initial move,
Alice can guarantee a win.

Why is this the case?
Either the number of vowels in the input is odd or even:

 - odd: Alice takes the entire string, leaving no characters for Bob
 - even: Alice takes all vowels except 1, leaving Bob with either no valid move
      or a move that involves only taking a consonant. Alice takes the remaining
      string (and last remaining vowel) in the next move.

The only exception to this rule
occurs when Alice has no valid move from the get-go:
when there are 0 vowels in the input.

So, all we need to do is iterate through the input character-by-character.
If we run into a single vowel, we know immediately that Alice is the winner.
If we didn't find a single vowel, we know that Bob is the winner.
