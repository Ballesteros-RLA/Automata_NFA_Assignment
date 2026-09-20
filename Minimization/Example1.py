"""
===============================================================================
 MINIMIZATION OF DFA  --  EXAMPLE #1  (From Lesson)
 Name  : Renzo Luis A. Ballesteros
 Course: 3 / BSCS / A
===============================================================================

 ORIGINAL DFA
 ------------
 Q  = {A, B, C, D, E}      q0 = A      F = {E}      Sigma = {0, 1}

        |   0   |   1
   -----+-------+-----
   ->A  |   B   |   C
     B  |   B   |   D
     C  |   B   |   C
     D  |   B   |   E
    (E) |   B   |   C

 MINIMIZATION (equivalence / partition method)
 ---------------------------------------------
   0-EQUIVALENCE : {A, B, C, D} {E}
   1-EQUIVALENCE : {A, B, C} {D} {E}
   2-EQUIVALENCE : {A, C} {B} {D} {E}
   3-EQUIVALENCE : {A, C} {B} {D} {E}   <-- same as 2-equivalence, STOP

 MINIMIZED DFA
 -------------
        |   0   |   1
   -----+-------+-------
   ->AC |   B   |   AC
     B  |   B   |   D
     D  |   B   |   E
    (E) |   B   |   AC
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
    "AC": {"0": "B",  "1": "AC"},
    "B":  {"0": "B",  "1": "D"},
    "D":  {"0": "B",  "1": "E"},
    "E":  {"0": "B",  "1": "AC"},
}

START_STATE = "AC"
FINAL_STATES = {"E"}


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
    "0110",
    "011011",
    "011",
    "00011",
    "1011",
    "111011",
    "0111011",
    "",
    "1",
    "0",
    "01",
    "01100",
    "00000",
    "11111",
    "011010",
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