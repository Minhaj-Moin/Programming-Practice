def func1(lst):
    maxLength = 0;
    for i in lst:
        if (len(i) > maxLength) : maxLength = len(i)
    print("* " * maxLength);
    for i in lst: print ("*", i + " " * (maxLength - (len(i))), "*")
    print("* " * maxLength);

def func2():
    bot = "bottles"
    for i in range(99, -1, -1):
        if (i >= 1):
            if i == 1:
                bot = bot[:-1]
            print ( i, bot,"of beer on the wall,",
                    i, bot,"of beer.\nTake one down and pass it around,",
                    i-1, bot,"of beer on the wall.\n\n" )
        else:
            print ( "No more bottles of beer on the wall,",
                    "no more bottles of beer.\nGo to the store and buy some more,",
                    "99 bottles of beer on the wall")
