import itertools,time


def imright(h1,h2):
    return h1-h2==1


def nextto(h1,h2):
    return abs(h1-h2)==1


def zebra_puzzle():
    houses=first,_,middle,_,_=[1,2,3,4,5]
    orderings=list(itertools.permutations(houses))
    return next((WATER,ZEBRA)
                for (red,green,ivory,yellow,blue) in orderings
                if imright(green,ivory)
                for (Englishman,Spaniard,Ukranian,Japanese,Norweigian) in orderings
                if Englishman is red
                if Norweigian is first
                if nextto(Norweigian,blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog,snails,fox,horse,ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields,fox)
                if nextto(Kools,horse)
                )


def timed_call(fn):
    t0=time.clock()
    result=fn()
    t1=time.clock()
    return t1-t0,result


def average(numbers):
    return sum(numbers)/float(len(numbers))


def timed_calls(n,fn):
    if isinstance(n,int):
        times=[timed_call(fn)[0] for _ in range(n)]
    else:
        times=[]
        while sum(times)<n:
            times.append(timed_call(fn)[0])
    return min(times),average(times),max(times)

print(timed_calls(5,zebra_puzzle))