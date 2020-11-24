# Negating propositions involving or

Now that you understand how to negate a proposition involving and it stands to reason that the next thing we are going to learn in this task is how to negate a proposition involving or.  As we did for the logical conjunction lets start the process of learning to negate the logical disjunction by looking at the truth table for the logical disjunction once more:

![](disjunction.png)

Given that the negation of a proposition is the proposition that is true whenever the original proposition is false.  The truth table for the negation for the logical proposition involving the logical disjunction operator above must be:

![](neg_disjunction.ng

__To complete the exercise you need to use the ideas above to complete the `negationOutside` function in the panel on the left.__  The two functions on the panel in the left take the following arguments:

1. `data` - a numpy array that contains multiple integers
2. `a` - an integer
3. `b` - an integer that is greater than `a`

The function I have written for you `numberOutside` returns the number of elements in `data` that are less than `a` or greater than `b`.  The `negationOutside` function that you will write should return the number of elements in `data` for which the negation of the logical proposition in `numberOutside` is true.

__As with the previous exercise, recognising that you can construct the truth table for the negation of a proposition involving or (which I have provided above) in another way if you start from the negations of the two proposition from which the compound proposition was formed is the key to solving this exercise.__
