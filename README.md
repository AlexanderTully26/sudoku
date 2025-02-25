Runtime efficiency: how fast are our algorithms? Figure out how to do timing in your language. This usually involves getting the system time before running the code you are timing, then getting the time after, then subtracting the two values:

runTime = endTime - startTime

It will be difficult to get accurate values here, so perhaps give some thought about how to time multiple puzzles. I am attaching a file that has a bunch of puzzles, albiet in a different format. sudoku10k.txtDownload sudoku10k.txt

Where do you think your code is slow? That is, what is the algorithm that probably takes the most time and why?

Space efficiency: how much memory are we using? Think about the size of your data structures and how many there are. For instance, if you are storing a value and a possible list for each cell, and those are all integers, then you will be storing anywhere between 64bits + the overhead of an empty integer array, and 9 * 64 bits. Is there a way to make this more efficient without adding too much complexity to your code? Is there a way to make this more efficient regardless of the complexity? One way to think about this would be: what is the minimum number of bits I need to do the things I am doing?

What is the point of a Sudoku Solver? There's some evidence to suggest that overall, we (as a species) are better at chess than we were 20 years ago. There are more players who are also better players, and that is likely attributable to the increased sophistication of computer-based chess enginesLinks to an external site.. There's even evidence to suggest that the best players are humans combined with enginesLinks to an external site.. So what does this mean in terms of Sudoku? Beyond that, what does it mean in terms of humans working with computers, especially in the context of AI?

So, create a file ("reflection.md", for instance) in your github and type up your thoughts on these things! 





Runtime = 0.015583 seconds
