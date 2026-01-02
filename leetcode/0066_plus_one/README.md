# Approach

Given that the digits are ordered from most significant to least,
we'll iterate over the input array from back-to-front.

As with how I learned addition in grade school,
we'll need to maintain the "carry" as we iterate.

The concern that comes to mind, however,
is what happens when our end result requires one more digit than the input?

BUT, when does this "extra digit" case actually occur?
Only when the input is all 9s!

From this, we can implement something clever.

We'll iterate over the input from back-to-front as usual,
but if the digit in the current iteration is NOT a 9, then we can end right there!

If we manage to exit the loop, we know our input was all 9s.
So, we'll just make the first element a 1 and append a 0 to the end!
