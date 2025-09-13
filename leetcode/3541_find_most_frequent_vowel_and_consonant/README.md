# Lead up to the solution

As we go through the input string,
we should be able to keep track of the highest consonant and vowel frequencies
(note that we don't need to know what the consonant and vowel are;
we just need the frequency of each).

So, a single-pass solution should be feasible.

We should also look at the problem description
to see what are the possible characters we could find in our input string.
In this problem, that's just English, lowercase characters,
which means we can avoid using a hash-map / dictionary.

We do this by taking advantage of subtracting the character `'a'` from the
current character we're on, to get an int that ranges from `[0, 26)`.

So, we can just use a fixed-size array / list to keep track of the counts.


# Solution

Initialize two int variables,
one to keep track of the max vowel frequency count we've seen thus far
and the other to keep track of the max consonant frequency.

As we iterate through the string, we:
  1. increment the count for the character we're on
  2. check if the character is a vowel or a consonant
  3. set the corresponding "max" variable to the this count if this count is
     greater than the "max" variable

Finally, we return the sum of the two "max" variables.


# Complexity

## Time

`O(n)`

We iterate through the entirety of the input string exactly once.
At each step, we perform a constant number of operations.
So, our time complexity is `O(n)`.

## Space

`O(1)`

We take advantage of the fact that we'll only ever encounter English, lowercase
letters, so our array / list will always be of fixed size (26).

We also define a constant number of integer variables.

Note that if our input ever expanded to some undefined-size vocabulary where
keeping fixed-size array / list for all possible values is not feasible,
then we would most likely resort to a hash-map / dictionary.
This would grow with the number of unique characters / tokens,
and so our space complexity would be `O(k)`, where `k` is the number of unique
characters in the input.

## Can we do any better?

In terms of time, no.
We MUST iterate through the entire input string at least once.

In terms of space complexity, also no, since we're at constant space.
An argument could be made that we could use less constant memory if we only
kept track of the characters we've seen, rather than the whole vocabulary,
but the whole vocabulary in this case is just 26, so this isn't worth worrying
about in 99% of scenarios, imo.
