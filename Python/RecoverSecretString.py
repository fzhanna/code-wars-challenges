"""There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you."""

def recoverSecret(triplets):
    solution=[]
    for i in triplets:
        x=i[0]
        y=i[1]
        z=i[2]

        if x not in solution: solution.insert(0,x)
        if y not in solution: solution.insert((solution.index(x))+1,y)
        elif y in solution and solution.index(y)<solution.index(x):
            solution.pop(solution.index(y))
            solution.insert((solution.index(x))+1,y)
        if z not in solution:solution.insert((solution.index(y))+1,z)
        elif z in solution and solution.index(z)<solution.index(y):
            solution.pop(solution.index(z))
            solution.insert((solution.index(y))+1,z)

    return "".join(solution)

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))