#!/usr/bin/env python3
from ticky_check import *
import unittest

class TestRearrange(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_return(self):
        testcase = "syslog.log"
        expected = (([('Connection to DB failed', 2), ('Connection to DB', 1)], [('test', {'Username': 'test', 'INFO': 1, 'ERROR': 2}), ('username', {'Username': 'username', 'INFO': 1, 'ERROR': 1})]))
        self.assertEqual(parse_log(testcase), expected)

    def tearDown(self) -> None:
        return super().tearDown()

unittest.main()