package secondsem;

import java.util.EnumSet;
import java.util.Set;

/**
 * NFA for L = { w in {a, *, /}* | w is a well-formed C-style comment }
 *
 * States:
 *   START  - no input consumed yet
 *   SLASH  - just consumed the opening '/'
 *   BODY   - inside the comment, no pending '*' (main "loop" state)
 *   STAR   - just consumed a '*' that MIGHT be starting the closing "*\/"
 *   ACCEPT - just consumed the closing "*\/"; this is a dead end (sink),
 *            so anything extra after it kills every remaining thread.
 *
 * Transition function delta: State x symbol -> set of States
 *   START ,'/'      -> {SLASH}
 *   SLASH ,'*'      -> {BODY}
 *   BODY  , other   -> {BODY}     // 'a' placeholder, digits, letters, spaces, or a lone '/'
 *   BODY  ,'*'      -> {STAR}     // could be the start of the closing sequence
 *   STAR  ,'*'      -> {STAR}     // absorbs runs of stars, e.g. "***\/"
 *   STAR  ,'/'      -> {ACCEPT}   // closes the comment
 *   STAR  , other   -> {BODY}     // false alarm: that '*' was just body content
 *   (everything else, including anything read from ACCEPT) -> {}  (trap/dead)
 *
 * A string is accepted iff, after consuming it entirely, ACCEPT is among
 * the currently active states.
 */
public class NFAchecker {

    private enum State { START, SLASH, BODY, STAR, ACCEPT }

    private static Set<State> step(Set<State> current, char c) {
        EnumSet<State> next = EnumSet.noneOf(State.class);
        boolean isStar  = (c == '*');
        boolean isSlash = (c == '/');

        for (State s : current) {
            switch (s) {
                case START:
                    if (isSlash) next.add(State.SLASH);
                    break;
                case SLASH:
                    if (isStar) next.add(State.BODY);
                    break;
                case BODY:
                    if (isStar) next.add(State.STAR);
                    else        next.add(State.BODY); // covers 'a' AND a lone '/'
                    break;
                case STAR:
                    if (isStar)      next.add(State.STAR);
                    else if (isSlash) next.add(State.ACCEPT);
                    else              next.add(State.BODY); // false alarm
                    break;
                case ACCEPT:
                    // sink: nothing may follow a completed comment
                    break;
            }
        }
        return next;
    }

    public static boolean accepts(String w) {
        Set<State> current = EnumSet.of(State.START);
        for (char c : w.toCharArray()) {
            current = step(current, c);
            if (current.isEmpty()) return false; // every thread died
        }
        return current.contains(State.ACCEPT);  
    }

    public static void main(String[] args) {
        String[] tests = {
            "/*a*/", "/**/", "/***/", "/*aaa*aaa*/", "/*a/a*/",         // expect ACCEPTED
            "/**", "/**/a/*aa*/", "aaa/**/aa", "/*/", "/**a/", "//aaaa", // expect REJECTED
            "/*b/b*/", "/*Test1*/", "/* aaa * aa */",          // expect ACCEPTED
            "/**/b/*bb*/", "bbb/**/bb", "/**b/", "//bbbb", "/*b*/b"      // expect REJECTED
        };

        for (String t : tests) {
            System.out.printf("Input: %-25s -> [%s]%n",
                    t, accepts(t) ? "ACCEPTED" : "REJECTED");
        }
    }
}