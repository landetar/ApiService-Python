import unittest
import json
import login

class DevOps_Test(unittest.TestCase):
    def test_get_message(self):
        message = login.LoginUser()
        messageWaited = "Hello Valeria Balseca your message will be send."
        messageResult = message.get_message('Valeria Balseca')
        self.assertEqual(messageResult,messageWaited)

        
if __name__ == "__main__":
    unittest.main()