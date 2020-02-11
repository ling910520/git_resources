import unittest
from filecreated import Helper
import os
path = r"C:\Users\ling910520\Desktop\c-sharp"
class TestCheckSize(unittest.TestCase):
    def testgetsize(self):
        folder = os.path.getsize(path)
        self.assertEqual(Helper.checkSize(path),True)