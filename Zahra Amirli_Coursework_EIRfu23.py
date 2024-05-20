# Singleton Logger Class
class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def log(self, message):
        print(f"LOG: {message}")

# Base Stack Class
class Stack:
    def __init__(self):
        self._elements = []

    def push(self, item):
        self._elements.append(item)

    def pop(self):
        if not self.is_empty():
            return self._elements.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self._elements[-1]
        return None

    def is_empty(self):
        return len(self._elements) == 0

    def size(self):
        return len(self._elements)

# LimitedStack Class inheriting from Stack
class LimitedStack(Stack):
    def __init__(self, limit):
        super().__init__()
        self._limit = limit

    def push(self, item):
        if self.size() < self._limit:
            super().push(item)
        else:
            print("Stack overflow: Cannot push to a full stack")

# StackDecorator Class using the Decorator Pattern
class StackDecorator:
    def __init__(self, stack):
        self._stack = stack
        self._logger = Logger.get_instance()

    def push(self, item):
        self._logger.log(f"Pushing {item}")
        self._stack.push(item)

    def pop(self):
        item = self._stack.pop()
        self._logger.log(f"Popping {item}")
        return item

    def peek(self):
        item = self._stack.peek()
        self._logger.log(f"Peeking {item}")
        return item

    def is_empty(self):
        return self._stack.is_empty()

    def size(self):
        return self._stack.size()

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    limited_stack = LimitedStack(limit=3)
    decorated_stack = StackDecorator(limited_stack)

    decorated_stack.push(1)
    decorated_stack.push(2)
    decorated_stack.push(3)
    decorated_stack.push(4)  # This should print an overflow message

    print(decorated_stack.pop())
    print(decorated_stack.peek())
    print(decorated_stack.is_empty())
    print(decorated_stack.size())
