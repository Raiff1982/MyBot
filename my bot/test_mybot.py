
import unittest
from mybot import MyBot
from botbuilder.core import TurnContext, MessageFactory
from botbuilder.schema import Activity, ActivityTypes

class TestMyBot(unittest.TestCase):
    def setUp(self):
        self.bot = MyBot()

    def test_generate_response(self):
        user_id = "test_user"
        text = "What is the meaning of life?"
        response = self.bot.generate_response(text, user_id)
        self.assertIn("Newton's Perspective", response)
        self.assertIn("Da Vinci's Perspective", response)

    def test_end_conversation(self):
        turn_context = TurnContext(Activity(type=ActivityTypes.message, text="end"))
        response = self.bot.on_message_activity(turn_context)
        self.assertIn("Ending conversation from the skill...", response)

if __name__ == "__main__":
    unittest.main()
