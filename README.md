# Nonsense
Small scripts that only really waste clock cycles 

## increasingSnakeEyes
"Rolls" two dice until both come up as 1 and then increases "amount of sides" of the dice.
Takes number of sides as parameter, default to 10.
'''python increasingSnakeEyes.py 100'''

Prints in a format that allows for plotting with [katef's plot.awk](https://gist.github.com/katef/fb4cb6d47decd8052bd0e8d88c03a102)
![Two plots of increasingSnakeEyes.py. The first one using dice up to 10 and the second up to 100. The plots have dots for the index and number of rolls needed to get snake eyes. There are large fluctuations from index to index for how many rolls were needed. Almost as if it was random. Because it should be indistinguishable from truly random.](/images/plot.png)

## randomHex
Generates two random hex values of size 32 and 5 until the shorter exists in the longer one.

## randomPrinting
Generate two random base64 values of size 58 and 2 until the shorter exists in the longer one.

## randomMd5
Tries to randomly guess a md5 hash.
