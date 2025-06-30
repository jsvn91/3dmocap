l = ["cat","dog","god","dgo","tac","net"]
#[("cat","tac"),(dog,god,dgo),(net)]
final = {}
for words in set(["".join(sorted(x)) for x in l]):
    final[words] = []
    for words2 in l:
        if sorted(words2)==sorted(words):
            final[words].append(words2)

print([ (y[0]) if len(y)==1 else tuple(y) for x,y in final.items()])