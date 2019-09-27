"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            'input': (2, 0, 1),
            'answer': 5,
        },
        {
            'input': (2, 1, 3, 0, 4, 5),
            'answer': 271,
        },
        {
            'input': (6, 8, 3, 4, 2, 1, 7, 5, 0),
            'answer': 279780,
        },
        {
            'input': (0, 4, 7, 5, 8, 2, 10, 6, 3, 1, 9, 11),
            'answer': 12843175,
        },
        {
            'input': (9, 0, 6, 2, 5, 7, 12, 10, 3, 8, 11, 4, 13, 1, 14),
            'answer': 787051783737,
        },
        {
            'input': (9, 0, 6, 17, 8, 12, 11, 1, 10, 14, 3, 15, 2, 13, 16, 7, 5, 4),
            'answer': 3208987196401056,
        },
        {
            'input': (9, 5, 4, 12, 13, 17, 7, 0, 23, 16, 11, 8, 15, 21, 2, 3, 22, 1, 10, 19, 6, 20, 14, 18),
            'answer': 238515587608877815254677,
        },
        {
            'input': (16, 17, 10, 23, 4, 22, 7, 18, 2, 21, 13, 6, 9, 8, 19, 3, 25, 12, 26, 24, 14, 1, 0, 20, 15, 5, 11),
            'answer': 6707569694907742966546817183,
        },
    ],
}
