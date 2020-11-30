def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def minus(x, y):
    return x - y


op_combs = [list(combinations_with_replacement([
    add,
    mult,
    minus
], i)) for i in range(1, 11)]


class Solution:
    def sub_divisions(num):
        for idx in range(1, len(num) + 1):
            for sub_sub in sub_divisions(num[idx:]):
                yield [inst(num[:idx])] + sub_sub

    def addOperators(self, num: str, target: int) -> List[str]:
        for sd in sub_divisions(nums):
            a = [sd[0]]
            for idx in range(1, len(sd)):
                a.append(op_comb[len(sd) - 1][idx - 1])
                a.append(sd[idx])

            i = 1
            found_mul
            while i < len(a):
                if a[i] == mult:
                    a = a[:i - 1] + [a[i - 1] * a[i + 1]] + a[i + 2:]
                    i = 0
                else i += 2

            total = a[0]
            for i in range(1, len(a), 2)
                if a[i] == add:
                    total += a[i + 1]
                else:
                    total -= a[i + 1]

            if total == target:

