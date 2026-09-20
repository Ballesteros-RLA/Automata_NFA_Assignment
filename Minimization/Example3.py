"""
===============================================================================
 MINIMIZATION OF DFA  --  EXAMPLE #3  ( Own Example )
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

ACCEPTED_EXAMPLES = ["001", "100100", "01", "110", "0000001"]
REJECTED_EXAMPLES = ["1011", "100110", "0", "000", "011"]


def simulate(input_string):
    """Run the minimized DFA on input_string.
    Returns (accepted, path_as_string)."""
    current = START_STATE
    path = [current]

    for symbol in input_string:
        if symbol not in ("0", "1"):
            return None, " -> ".join(path)
        current = TRANSITIONS[current][symbol]
        path.append(current)

    return current in FINAL_STATES, " -> ".join(path)


def show_result(string, indent="  "):
    accepted, path = simulate(string)
    print(f"{indent}String '{string}':")
    if accepted is None:
        print(f"{indent}  Invalid input (use 0s and 1s only)")
        return
    if accepted:
        print(f"{indent}  Accepted (\u2713)")
    else:
        print(f"{indent}  Rejected (X)")
    print(f"{indent}  Path: {path}")


def main():
    print("Testing built-in ACCEPTED examples...")
    for s in ACCEPTED_EXAMPLES:
        show_result(s)

    print()
    print("Testing built-in REJECTED examples...")
    for s in REJECTED_EXAMPLES:
        show_result(s)

    print("-" * 32)
    print()
    user_input = input("Now it's your turn! Enter a binary string (0s and 1s): ").strip()

    accepted, path = simulate(user_input)
    print()
    print(f"Result for your string '{user_input}':")
    if accepted is None:
        print("    Invalid input (use 0s and 1s only)")
    else:
        if accepted:
            print("    Accepted (\u2713)")
        else:
            print("    Rejected (X)")
        print(f"    Path: {path}")


if __name__ == "__main__":
    main()