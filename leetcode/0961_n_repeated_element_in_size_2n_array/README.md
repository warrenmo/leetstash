# Approach

We can solve the problem by keeping track of elements using a hash-set.
This necessitates `O(n)` memory.
Can we do better?

The particular constraints of the problem--namely that the element of interest is repeated exactly `n` times--suggests that we can do something interesting.

Given an array where element `x` makes up exactly half of the elements,
I think of the situation where every other element is `x`.

If this pattern is NOT upheld,
then there will necessarily be at least one situation where two neighboring elements are equal,
by the [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).

So, we first check the base case (`n=2` and so the total number of elements is 4)
where `x` is every other element:
`nums[0] == nums[2]` or `nums[1] == nums[3]`.

In the inductive step, we compare every pair of neighboring elements,
and if they're equal, we have our result.

One subtlety to notice is that, in our base case, we could have `nums[0] == nums[3]`.
So, we'll need to check this manually.
When `n > 2`, this situation would necessitate that some two neighboring elements be equal,
again by the [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).
