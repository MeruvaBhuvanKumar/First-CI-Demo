import unittest
from result_logic import predict_result


class TestResultLogic(unittest.TestCase):

    def test_pass_result(self):
        self.assertEqual(predict_result(70, 85), "PASS")

    def test_fail_low_marks(self):
        self.assertEqual(predict_result(30, 85), "FAIL")

    def test_fail_low_attendance(self):
        self.assertEqual(predict_result(70, 60), "FAIL")


if __name__ == "__main__":
    unittest.main()
