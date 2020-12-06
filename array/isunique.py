
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# O(N)


import unittest


def isUnique(s):
    letters = [False for _ in range(128)]
    # print(s)
    for char in s:
        val = ord(char)
        if letters[val] is False:
            letters[val] = True
            continue
        else:
            return False
    return True


class abc(unittest.TestCase):
    dataT = [('abcda'), ('sjaqi'), ('')]
    dataF = [('abcda'), ('ahsnca == ')]

    def test_isUnique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF :
            actual = isUnique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()





