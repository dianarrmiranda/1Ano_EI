
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    commoninterests = {(x,y):(name&inte) for x,name in interests.items() for y,inte in interests.items() if  x<y}
    print(commoninterests)

    print("b) Maximum number of common interests:")
    maxCI = max(len(inte) for x, inte in commoninterests.items())
    
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [x for x, y in commoninterests.items() if len(y) == maxCI]
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = [(x,y) for x,name in interests.items() for y,inte in interests.items() if x<y and (len(name & inte)/len(name.union(inte)))<0.25]
    print(lowJaccard)


# Start program:
main()
