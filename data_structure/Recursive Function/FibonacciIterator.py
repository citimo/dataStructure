# 简单的斐波那契数列生成器
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.previous = 0
        self.next_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.next_value
        self.previous, self.next_value = self.next_value, self.previous + self.next_value
        self.current += 1
        return value

fibonacci_iter = FibonacciIterator(10)

for num in fibonacci_iter:
    print(num)