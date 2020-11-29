"""
1656. Design an Ordered Stream
Difficulty: easy

There is a stream of n (id, value) pairs arriving in an arbitrary order, where id is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int id, String value) Inserts the pair (id, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.


Example:



Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.a = [None] * n
        self.n = n
        self.pointer = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.a[id] = value
        returned = []
        if id == self.pointer:
            while self.pointer < self.n and self.a[self.pointer] is not None:
                returned.append(self.a[self.pointer])
                self.pointer += 1
        return returned


class OrderedStreamTester():

    def __init__(self, l, to_test):
        self.n = l[0][0]
        self.inserts = l[1:]
        self.results = []
        self.to_test = to_test(self.n)

    def run(self):
        for i, s in self.inserts:
            self.results.append(self.to_test.insert(i, s))


if __name__ == "__main__":
    ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
    t = OrderedStreamTester([[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]], OrderedStream)
    t.run()
    assert t.results == [[],["aaaaa"],["bbbbb","ccccc"],[],["ddddd","eeeee"]]