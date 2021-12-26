https://aoc.infi.nl/
Packages of panic

Santa wants his elves to make toys, but he hasn't got his paperwork in order
yet. He has a list of parts that are in every kind of toy. The only problem is
that some parts consist of further parts, which makes counting the number of
parts difficult.

For example, suppose he got this list (ignoring the missing parts for now):

35 parts missing
Zoink: 9 Oink, 5 Dink
Floep: 2 Flap, 4 Dink
Flap: 4 Oink, 3 Dink

In this example, Zoinks are easy: there are a total of 14 (9+5) parts in them. A
Flop is more difficult, because the Flaps that are in it each consist of several
parts. Each Flap consists of 7 parts. A Floep therefore contains 18 (2*7+4)
parts.

Download the toy list ➜

Given the toy list, find the toy with the greatest number of parts. This number
is then the answer to part 1 .


--- Part 2 ---

While you were counting the parts, a few diligent elves had already started!
They have assembled and packed toys, but have already forgotten what was inside.
Strangely enough, they still remember how many parts they used.

The elves have only packed toys, and no parts such as batteries or iron.
Apparently no one has been naughty this year.

In the previous example, there were 35 missing parts. Suppose 3 gifts were
already wrapped. Then there is only 1 way to make exactly 3 toys with those
parts: 2 Zoinks and 1 Flap (14+14+7=35) .

If you know the toys, you can find your answer by putting the first letters of
the toys in alphabetical order. In the above example, that would be FZZ .

20 gifts have already been wrapped. Given the number of missing parts in the toy
list, what are the initial letters (in alphabetical order)?