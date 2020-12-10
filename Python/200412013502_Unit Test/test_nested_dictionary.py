import unittest
from unittest import mock
import io
from nested_dictionary import name_of_every_process, main


class TestNestedDict(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_name_of_every_process(self, mock_stdout):
        name_of_every_process({"name": "Parent", "children": [{"name": "Process", "children": [],
                                                                    'sig_company': "Company"}], 'sig_company': "Company"},
                              "Company")
        self.assertEqual(mock_stdout.getvalue(), "Process with Parent as parent\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch("nested_dictionary.open", new_callable=mock.mock_open, read_data=
    '{"name": "Parent", "children": [{"name": "Process", "children": [],'
    '"sig_company": "Microsoft Corporation"}], "sig_company": "Company"}')
    def test_main(self, mock_file, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue(), "Process with Parent as parent\n")
