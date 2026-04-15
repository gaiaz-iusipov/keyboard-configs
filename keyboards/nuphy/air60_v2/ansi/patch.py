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

    # System Selection (Mac and Win/Linux)
    for l in l1, l4:
        l[3][1] = "DF(0)"  # Fn + A → Mac
        l[3][2] = "DF(3)"  # Fn + S → Win

    # macOS
    l0[5][1] = "LM(2,MOD_LALT)"  # Opt
    l0[5][2] = "LM(2,MOD_LGUI)"  # Cmd

    l1[4][4], l2[4][4] = l2[4][4], l1[4][4]  # RGB_TEST

    for i in range(1, 13):
        l2[1][i] = "KC_TRANSPARENT"

    # Windows
    l3[5][2] = "LM(5,MOD_LALT)"  # Alt
    l3[3][0] = macro(data, "KC_LEFT_ALT", "KC_LEFT_SHIFT")  # Caps Lock

    l4[4][4], l5[4][4] = l5[4][4], l4[4][4]  # RGB_TEST
    for i in range(1, 13):
        l4[1][i], l5[1][i] = l5[1][i], l4[1][i]

    l5[2][1] = "KC_F4"  # Q
    l5[3][13] = macro(data, "KC_LEFT_CTRL", "KC_ENTER")  # Enter

    # Linux
    l5[4][3] = "KC_CUT"  # X
    l5[4][4] = "KC_COPY"  # C
    l5[4][5] = "KC_PASTE"  # V

    json.dump(data, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 patch.py <file.vil>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
