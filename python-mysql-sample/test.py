import unittest
from application import calculate_score

class TestSuite(unittest.TestCase):
  def test(self):
    score = calculate_score(29)
    self.failIf(score > 8)

def main():
  unittest.main()

if __name__ == "__main__":
  main()
