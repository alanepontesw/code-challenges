import unittest
from sorted_counter import SortedCounter

class TestSortedCounter(unittest.TestCase):
    def setUp(self):
        self.sorted_counter = SortedCounter()

    def test_order_and_count(self): 
        self.assertEqual(self.sorted_counter.with_counter_collection("alane"), [("a", 2), ("l", 1), ("n", 1), ("e", 1)]) 
        self.assertEqual(self.sorted_counter.with_counter_collection("aaaalannee"), [("a", 5), ("n", 2), ("e", 2), ("l", 1)]) 
        self.assertEqual(self.sorted_counter.with_counter_collection("ane"), [("a", 1), ("n", 1), ("e", 1)])
        self.assertEqual(self.sorted_counter.with_counter_collection("çç"), [("ç", 2)])
        self.assertEqual(self.sorted_counter.with_counter_collection("~[["), [("[", 2), ("~", 1)])
        self.assertEqual(self.sorted_counter.with_counter_collection(None), None)
        self.assertEqual(self.sorted_counter.with_counter_collection(""), None)
        self.assertEqual(self.sorted_counter.with_counter_collection(0), None)

if __name__ == '__main__':
    unittest.main()