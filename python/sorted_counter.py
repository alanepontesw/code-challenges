from collections import Counter

class SortedCounter():

    # Time Complexity O(n)
    def with_counter_collection(self, string: str):
        if not string:
            return None
        unordered = Counter(string)
        # return values in descending order
        return unordered.most_common()

# SortedCounter().with_counter_collection("aoNHQATeMNLuWC4vMdGgQpqMge7bit")
# [('M', 3), ('N', 2), ('Q', 2), ('e', 2), ('g', 2), ('a', 1), ('o', 1), ('H', 1), ('A', 1), ('T', 1), ('L', 1), \
# ('u', 1), ('W', 1), ('C', 1), ('4', 1), ('v', 1), ('d', 1), ('G', 1), ('p', 1), ('q', 1), ('7', 1), ('b', 1), ('i', 1), ('t', 1)]