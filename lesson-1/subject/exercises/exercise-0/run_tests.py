#! /usr/bin/python3

from subprocess import run, PIPE, CalledProcessError, TimeoutExpired
from typing import List, Tuple

def launch_command(args: List[str]) -> Tuple[bool, bytes]:
    try:
        done = run(["./biggest.py"] + args,
                   stdin=PIPE, stdout=PIPE,
                   timeout=2, check=True)

        if done.stderr:
            return False, done.stderr
        return True, done.stdout

    except FileNotFoundError:
        return False, b"File not found. Make sure your script is correctly named"
    except CalledProcessError as err:
        return False, b"There was an error(" + err.stderr + b")"
    except TimeoutExpired as err:
        return False, b"Took too long to execute!"

def colored_print(test_name: str, success: bool) -> None:
    if success:
        print("\x1b[7;32;40mTest {} - {}\x1b[0m".format(test_name, "PASSED"))
    else:
        print("\x1b[7;31;40mTest {} - {}\x1b[0m".format(test_name, "FAILED"))

def launch_tests(test_cases: List[Tuple[List, bytes]]) -> None:
    for test_arguments, expected_output in test_cases:
        completed_okay, output = launch_command(test_arguments)
        if completed_okay and output == expected_output:
            colored_print(test_arguments, True)
            continue
        colored_print(test_arguments, False)
        if completed_okay:
            print("--> Got unexpected output, obtained {} when {} was "
                  "expected".format(output.decode(), expected_output.decode()))
        else:
            print("--> Your script encountered an error: {}".format(output.decode()))
        return

    print("\nAll tests passed! Good job :). Make sure you did not forget any not tested case")

if __name__ == "__main__":
    USAGE_TEXT = b"Usage: ./biggest.py integer1 integer2\n"
    TEST_CASES = [
        (["1", "2"], b"2\n"),
        (["1123123", "2"], b"1123123\n"),
        (["-17", "13"], b"13\n"),
        (["0.3", "13"], USAGE_TEXT),
        (["13"], USAGE_TEXT),
        (["0.1"], USAGE_TEXT),
        (["1", "2", "3", "-8"], USAGE_TEXT),
        (["mdr", "3"], USAGE_TEXT),
    ]

    launch_tests(TEST_CASES)
