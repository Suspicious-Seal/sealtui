from testclass import Test, TEST

from ..styles import *
from ..styler import *


TESTS = [
    Test("Styling", StyleString, "[bold]text[/]", "a")
]

TEST(TESTS)
