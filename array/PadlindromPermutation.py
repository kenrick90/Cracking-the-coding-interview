# palindrom permutation
import unittest


def palindromePermutation(s):
    hashtable = [None for _ in range(128)]
    s = s.lower()
    numberOfOdd=0

    for c in s:
        if c == " ":
            continue
        val = ord(c)
        if hashtable[val] is None:
            hashtable[val] = 'Odd'
            numberOfOdd += 1
            continue
        if hashtable[val] == 'Odd':
            hashtable[val] = 'Even'
            numberOfOdd -= 1
            continue

    return numberOfOdd < 2


class Test(unittest.TestCase):
    dataT = ['Tact Coa', 'a', 'aa', 'lll', 'lolo l', 'no x in nixon', 'Able was I ere I saw Elba']
    dataF = ['abac', 'Animal']

    def testpalindrome(self):
        for s in self.dataT:
            self.assertTrue(palindromePermutation(s))
        for s in self.dataF:
            self.assertFalse(palindromePermutation(s))


if __name__ == "__main__":
    unittest.main()
