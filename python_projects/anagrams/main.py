from collections import defaultdict

def group_anagrams(a):
    dfdict=defaultdict(list)
    for i in a:
        sorted_i=" ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()
words=["çay", "yaç", "açy", "kar", "rak", "abow"]
print(group_anagrams(words))