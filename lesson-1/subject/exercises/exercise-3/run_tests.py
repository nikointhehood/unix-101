#! /usr/bin/python3

if __name__ == "__main__":
    # This is utterly ugly, but I don't care
    import sys
    sys.path.append("..")
    from tests_framework import launch_tests #pylint: disable=import-error

    FILENAME = "./my_range.py"
    USAGE_TEXT = b"Usage: " + FILENAME.encode() + b" start end [increment]\n"

    def my_range(a, b , c = 1):
        return b" ".join(str(i).encode() for i in list(range(int(a), int(b), int(c)))) + b"\n"

    TEST_CASES = [
        # Ok tests
        (["0", "10", "1"], my_range(0, 10, 1)),
        (["0", "10", "2"], my_range(0, 10, 2)),
        (["0", "10", "9"], my_range(0, 10, 9)),
        (["0", "10", "15"], my_range(0, 10, 15)),
        (["0", "10", "-15"], my_range(0, 10, -15)),
        (["10", "5", "-1"], my_range(10, 5, -1)),
        (["0", "10", "-1"], my_range(0, 10, -1)),
        (["10", "0", "-1"], my_range(10, 0, -1)),
        (["222", "999", "33"], my_range(222, 999, 33)),

        # Fail cases
        ([], USAGE_TEXT),
        (["1"], USAGE_TEXT),
        (["1", "a"], USAGE_TEXT),
        (["1", "0.3"], USAGE_TEXT),
        (["1", "5", "10", "3"], USAGE_TEXT),
    ]

    launch_tests(FILENAME, TEST_CASES)
