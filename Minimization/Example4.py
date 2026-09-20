"""
===============================================================================
 MINIMIZATION OF DFA  --  EXAMPLE #4  ( Own Example )
 Name  : Renzo Luis A. Ballesteros
 Course: 3 / BSCS / A
===============================================================================

 ORIGINAL DFA
 ------------
 Q  = {A, B, C, D, E, F, G}   q0 = A   F = {C, D}   Sigma = {0, 1}

        |   0   |   1
   -----+-------+-----
   ->A  |   B   |   C
     B  |   A   |   D
    (C) |   E   |   F
    (D) |   E   |   F
     E  |   E   |   E
     F  |   G   |   C
     G  |   F   |   D

 MINIMIZATION (equivalence / partition method)
 ---------------------------------------------
   0-EQUIVALENCE : {A, B, E, F, G} {C, D}
   1-EQUIVALENCE : {A, B, F, G} {E} {C, D}
   2-EQUIVALENCE : {A, B, F, G} {E} {C, D}   <-- same as 1-equivalence, STOP

 MINIMIZED DFA
 -------------
          |   0    |    1
   -------+--------+--------
   ->ABFG |  ABFG  |   CD
    (CD)  |   E    |  ABFG
      E   |   E    |   E
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
    "ABFG": {"0": "ABFG", "1": "CD"},
    "CD":   {"0": "E",    "1": "ABFG"},
    "E":    {"0": "E",    "1": "E"},
}

START_STATE = "ABFG"
FINAL_STATES = {"CD"}

ACCEPTED_EXAMPLES = ["1101", "01101", "1", "0001", "111"]
REJECTED_EXAMPLES = ["00110", "0100", "0", "10", "11"]


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