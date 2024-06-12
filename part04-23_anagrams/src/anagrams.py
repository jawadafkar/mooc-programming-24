# Write your solution here
def anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    print(anagrams("jawad", "dawaj"))