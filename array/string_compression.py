import unittest


def string_compression(s):
    newS = []
    count = 0
    for i in range(len(s)):

        if i == 0:
            count += 1
            newS.append(s[i])
            continue
        if s[i] == s[i-1]:
            count += 1
            continue

        if s[i] != s[i-1]:
            newS.append(str(count))
            count = 1
            newS.append(s[i])

    newS.append(str(count))

    if len(newS) < len(s):
        return ''.join(newS)
    else:
        return s


class Test(unittest.TestCase):
    dataT = [
        ['aabcccccaaa', 'a2b1c5a3'],
        ['abcdef', 'abcdef']]

    def test_string_compression(self):
        for testdata, expected in self.dataT:
            self.assertEqual(string_compression(testdata), expected)


if __name__ == '__main__':
    unittest.main()
