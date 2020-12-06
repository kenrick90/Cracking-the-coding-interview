import unittest


def URLify(s, length):
    newIndex = len(s)-1
    for originalIndex in range(int(length)-1, -1, -1):
        if s[originalIndex] != ' ':
            s[newIndex] = s[originalIndex]
            newIndex -= 1

        if s[originalIndex] == ' ':
            s[newIndex-2:newIndex+1] = '%20'
            newIndex -= 3
    return(s)


class Test(unittest.TestCase):
    dataT = [[list('a b  '), '3', list('a%20b')], [list('Mr John Smith    '),
     13, list('Mr%20John%20Smith')]
    ]

    def test_checkpermutation(self):

        for test_string, length, expected in self.dataT:
            result = URLify(test_string, length)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
