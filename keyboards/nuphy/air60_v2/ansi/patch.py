import json
import sys


def macro(data, *keys: str) -> str:
    m = data["macro"]
    idx = len(m)
    m.append([["down", k] for k in keys] + [["up", k] for k in reversed(keys)])
    return f"QK_MACRO_{idx}"


def main(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    l0, l1, l2, l3, l4, l5, *_ = data["layout"]

    # System Selection (macOS and Linux)
    for l in l1, l4:
        l[3][1] = "DF(0)"  # Fn + A → macOS
        l[3][2] = "DF(3)"  # Fn + S → Linux

    # RGB_TEST
    for a, b in [(l1, l2), (l4, l5)]:
        a[4][4], b[4][4] = b[4][4], a[4][4]

    # macOS
    l0[5][1] = "LM(2,MOD_LALT)"  # Opt
    l0[5][2] = "LM(2,MOD_LGUI)"  # Cmd

    l1[3][9] = macro(data, "KC_LCTL", "KC_LGUI", "KC_Q")  # Fn + L → Lock Screen

    for i in range(1, 13):
        l2[1][i] = "KC_TRANSPARENT"

    # Linux
    l3[5][2] = "LM(5,MOD_LALT)"  # Alt

    for i in range(1, 13):
        l4[1][i], l5[1][i] = l5[1][i], l4[1][i]

    l4[2][10] = "KC_PRINT_SCREEN"  # P
    l4[3][9] = macro(data, "KC_LGUI", "KC_L")  # Fn + L → Lock Screen

    l5[2][1] = "KC_F4"  # Q
    l5[3][13] = "LCTL(KC_ENTER)"  # Enter

    l5[4][3] = "KC_CUT"  # X
    l5[4][4] = "KC_COPY"  # C
    l5[4][5] = "KC_PASTE"  # V

    json.dump(data, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 patch.py <file.vil>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
