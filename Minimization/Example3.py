"""
===============================================================================
 MINIMIZATION OF DFA  --  EXAMPLE #3  (Own Example)
 Name  : Renzo Luis A. Ballesteros
 Course: 3 / BSCS / A
===============================================================================

 ORIGINAL DFA
 ------------
 Q  = {a, b, c, d, e, f}   q0 = a   F = {d, e}   Sigma = {0, 1}

        |   0   |   1
   -----+-------+-----
   ->a  |   b   |   c
     b  |   c   |   d
     c  |   c   |   e
    (d) |   d   |   f
    (e) |   d   |   f
     f  |   f   |   f

 MINIMIZATION (equivalence / partition method)
 ---------------------------------------------
   0-EQUIVALENCE : {a, b, c, f} {d, e}
   1-EQUIVALENCE : {a, f} {b, c} {d, e}
   2-EQUIVALENCE : {a} {b, c} {f} {d, e}
   3-EQUIVALENCE : {a} {b, c} {f} {d, e}   <-- same as 2-equivalence, STOP

 MINIMIZED DFA
 -------------
         |   0    |   1
   ------+--------+------
   ->a   |   bc   |  bc
     bc  |   bc   |  de
    (de) |   de   |   f
     f   |   f    |   f
===============================================================================
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------------------------------------------------------------------------
# MINIMIZED DFA DEFINITION
# ---------------------------------------------------------------------------
TRANSITIONS = {
    "a":  {"0": "bc", "1": "bc"},
    "bc": {"0": "bc", "1": "de"},
    "de": {"0": "de", "1": "f"},
    "f":  {"0": "f",  "1": "f"},
}

START_STATE = "a"
FINAL_STATES = {"de"}


def simulate(input_string):
    """Run the minimized DFA on input_string.
    Returns (accepted, path_as_string)."""
    current = START_STATE
    path = [current]

    for symbol in input_string:
        if symbol not in ("0", "1"):
            return False, " -> ".join(path) + f"  [INVALID SYMBOL '{symbol}']"
        current = TRANSITIONS[current][symbol]
        path.append(current)

    accepted = current in FINAL_STATES
    return accepted, " -> ".join(path)


# ---------------------------------------------------------------------------
# PART 1 : AUTOMATED EXTENDED TEST SUITE
# ---------------------------------------------------------------------------
TEST_STRINGS = [
    "001",
    "100100",
    "01",
    "110",
    "0000001",
    "1011",
    "100110",
    "",
    "0",
    "1",
    "00",
    "011",
    "000",
    "111",
    "0100",
]


def run_test_suite():
    print("=" * 64)
    print("PART 1: AUTOMATED EXTENDED TEST SUITE".center(64))
    print("=" * 64)
    print()
    print(f"{'Input String':<16}| {'Status':<10}| State Transition Path")
    print("-" * 64)

    for s in TEST_STRINGS:
        accepted, path = simulate(s)
        status = "ACCEPTED" if accepted else "REJECTED"
        label = f"'{s}'" if s else "'' (empty)"
        print(f"{label:<16}| {status:<10}| {path}")

    print()


# ---------------------------------------------------------------------------
# PART 2 : SINGLE CUSTOM INPUT TEST
# ---------------------------------------------------------------------------
def run_custom_test():
    print("=" * 64)
    print("PART 2: SINGLE CUSTOM INPUT TEST".center(64))
    print("=" * 64)
    print()

    user_input = input("Enter binary string to test: ").strip()

    accepted, path = simulate(user_input)
    status = "ACCEPTED" if accepted else "REJECTED"

    print()
    print("-" * 54)
    print(f"Input   : '{user_input}'")
    print(f"Path    : {path}")
    print(f"Result  : {status}")
    print("-" * 54)


def main():
    run_test_suite()
    run_custom_test()
    print()
    print("Program completed.")


if __name__ == "__main__":
    main()