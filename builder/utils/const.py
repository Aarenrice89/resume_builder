from pathlib import Path

L1 = " " * 4
L2 = L1 * 2
L3 = L1 * 3

NUM_TO_WORD = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

STYLING_CLASS_PATH = Path(__file__).parent.parent.parent.joinpath("template", "tex_example", "styling.cls")
