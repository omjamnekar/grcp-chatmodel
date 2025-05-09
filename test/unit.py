import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

import unittest
from src.context_manager import ContextManager



class TestContextManager(unittest.TestCase):

    def setUp(self):
        self.cm = ContextManager()
        self.session_id = "test-session"
        self.user_input = "Hello!"
        self.model_response = "Hi there!"

    def test_initial_context_empty(self):
        self.assertEqual(self.cm.get_context(self.session_id), [])

    def test_update_context(self):
        self.cm.update_context(self.session_id, self.user_input, self.model_response)
        context = self.cm.get_context(self.session_id)

        self.assertEqual(len(context), 2)
        self.assertEqual(context[0]["role"], "user")
        self.assertEqual(context[0]["content"], self.user_input)
        self.assertEqual(context[1]["role"], "assistant")
        self.assertEqual(context[1]["content"], self.model_response)

    def test_multiple_updates(self):
        self.cm.update_context(self.session_id, "Hi", "Hello!")
        self.cm.update_context(self.session_id, "How are you?", "I'm fine!")

        context = self.cm.get_context(self.session_id)
        self.assertEqual(len(context), 4)  

if __name__ == '__main__':
    unittest.main()
