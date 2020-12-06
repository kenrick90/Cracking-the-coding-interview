import unittest
import math


def oneAway(s1, s2):
    edit = 0

    l1 = len(s1)
    l2 = len(s2)

    if abs(l1 - l2) > 1:
        return False

    if l1 == l2:
        for i in range(l1):
            if s1[i] != s2[i]:
                edit += 1
            if edit > 1:
                return False
    else:
        i = 0
        j = 0

        while i < l1 and j < l2:
            if s1[i] != s2[j]:

                if i + 1 < l1 and s1[i+1] == s2[j]:
                        edit += 1
                        i += 1
                elif j + 1 < l2 and s1[i] == s2[j+1]:
                    edit += 1
                    j += 1

                else:
                    return False

            i += 1
            j += 1
            if edit > 1:
                return False
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            print(test_s1, test_s2)
            actual = oneAway(test_s1, test_s2)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
