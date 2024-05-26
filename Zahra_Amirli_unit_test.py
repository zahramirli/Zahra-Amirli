import unittest
from unittest.mock import patch
from io import StringIO

# Assuming the classes are in a module named 'stack_module'
from stack_module import Logger, Stack, LimitedStack, StackDecorator

class TestLogger(unittest.TestCase):

    def test_singleton(self):
        logger1 = Logger.get_instance()
        logger2 = Logger.get_instance()
        self.assertIs(logger1, logger2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_log(self, mock_stdout):
        logger = Logger.get_instance()
        logger.log("Test message")
        self.assertEqual(mock_stdout.getvalue().strip(), "LOG: Test message")

class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

class TestLimitedStack(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_push_within_limit(self, mock_stdout):
        stack = LimitedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_push_beyond_limit(self, mock_stdout):
        stack = LimitedStack(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertIn("Stack overflow: Cannot push to a full stack", mock_stdout.getvalue().strip())

class TestStackDecorator(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_push_logging(self, mock_stdout):
        stack = LimitedStack(3)
        decorated_stack = StackDecorator(stack)
        decorated_stack.push(1)
        self.assertIn("LOG: Pushing 1", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_pop_logging(self, mock_stdout):
        stack = LimitedStack(3)
        decorated_stack = StackDecorator(stack)
        decorated_stack.push(1)
        decorated_stack.pop()
        self.assertIn("LOG: Popping 1", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_peek_logging(self, mock_stdout):
        stack = LimitedStack(3)
        decorated_stack = StackDecorator(stack)
        decorated_stack.push(1)
        decorated_stack.peek()
        self.assertIn("LOG: Peeking 1", mock_stdout.getvalue().strip())

    def test_is_empty(self):
        stack = LimitedStack(3)
        decorated_stack = StackDecorator(stack)
        self.assertTrue(decorated_stack.is_empty())
        decorated_stack.push(1)
        self.assertFalse(decorated_stack.is_empty())

    def test_size(self):
        stack = LimitedStack(3)
        decorated_stack = StackDecorator(stack)
        self.assertEqual(decorated_stack.size(), 0)
        decorated_stack.push(1)
        self.assertEqual(decorated_stack.size(), 1)

if __name__ == '__main__':
    unittest.main()

