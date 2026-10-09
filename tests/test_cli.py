from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from harness_creator.cli import main


class MainTests(TestCase):
    def test_blank_request_reprompts_and_accepts_non_empty_request(self) -> None:
        output = StringIO()
        with (
            patch(
                "builtins.input",
                side_effect=["  ", "Create a coding assistant"],
            ) as prompt,
            redirect_stdout(output),
        ):
            result = main()

        self.assertEqual(0, result)
        self.assertEqual(2, prompt.call_count)
        self.assertIn("Enter a description to continue.", output.getvalue())
        self.assertIn("Request received.", output.getvalue())
        self.assertIn("does not create harness files.", output.getvalue())
        self.assertIn("does not save or send your request.", output.getvalue())

    def test_eof_exits_without_saving_or_sending_request(self) -> None:
        output = StringIO()
        with patch("builtins.input", side_effect=EOFError), redirect_stdout(output):
            result = main()

        self.assertEqual(0, result)
        self.assertIn("Your request was not saved or sent.", output.getvalue())
        self.assertNotIn("Request received.", output.getvalue())

    def test_interrupt_exits_without_saving_or_sending_request(self) -> None:
        output = StringIO()
        with (
            patch("builtins.input", side_effect=KeyboardInterrupt),
            redirect_stdout(output),
        ):
            result = main()

        self.assertEqual(0, result)
        self.assertIn("Session cancelled.", output.getvalue())
        self.assertIn("Your request was not saved or sent.", output.getvalue())
