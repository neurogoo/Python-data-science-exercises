import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from src import main
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_oikea(self):
        x = main.testi()
        assert x == 3
