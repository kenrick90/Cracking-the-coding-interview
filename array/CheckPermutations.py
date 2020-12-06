# given two string write a method to decide if one is a permutation of the other
import unittest


def checkpermutation(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) != len(s2):
        return False
    s1.sort()
    s2.sort()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return(False)

    return(True)


class Test(unittest.TestCase):
    dataT = [['abc', 'cba']]
    dataF = [['abc', 'bacd'], ['abc', 'gba']]

    def test_checkpermutation(self):

        for item in self.dataT:
            result = checkpermutation(*item)
            self.assertTrue(result)

        for item in self.dataF:
            result = checkpermutation(*item)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
