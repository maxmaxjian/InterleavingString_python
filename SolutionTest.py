import unittest
from parameterized import parameterized
from solution import Solution1


class SolutionTest(unittest.TestCase):
    # soln = Solution1()

    @parameterized.expand([
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "a", False)
    ])
    def test_function(self, s1, s2, s3, expected):
        soln = Solution1()
        self.assertEqual(expected, soln.isInterleave(s1, s2, s3))


if __name__ == '__main__':
    unittest.main()
