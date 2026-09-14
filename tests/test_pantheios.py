
import unittest

import pantheios


class Test_pantheios(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.0', pantheios.__version__)
