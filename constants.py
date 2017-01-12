# Constant holding the weak pair hands when we have the same color
WEAK_PAIR_HANDS = [
    (2, 7),
    (2, 8),
    (3, 8),
    (3, 7),
    (2, 6),
    (2, 9),
    (3, 9),
    (4, 9),
    (2, 10),
    (5, 9),
    (4, 7),
    (4, 8),
    (5, 8),
    (3, 6)
]

# constant with strong 5 card hands
STRONG_HANDS = [
    [ #royal flush hearts
        {
            "rank": "A",
            "suit": "hearts"
        },
        {
            "rank": "K",
            "suit": "hearts"
        },
        {
            "rank": "Q",
            "suit": "hearts"
        },
        {
            "rank": "J",
            "suit": "hearts"
        },
        {
            "rank": "10",
            "suit": "hearts"
        }
    ],
    [ #royal flush clubs
        {
            "rank": "A",
            "suit": "clubs"
        },
        {
            "rank": "K",
            "suit": "clubs"
        },
        {
            "rank": "Q",
            "suit": "clubs"
        },
        {
            "rank": "J",
            "suit": "clubs"
        },
        {
            "rank": "10",
            "suit": "clubs"
        }
    ],
    [ #royal flush spades
        {
            "rank": "A",
            "suit": "spades"
        },
        {
            "rank": "K",
            "suit": "spades"
        },
        {
            "rank": "Q",
            "suit": "spades"
        },
        {
            "rank": "J",
            "suit": "spades"
        },
        {
            "rank": "10",
            "suit": "spades"
        }
    ],
    [ #royal flush diamonds
        {
            "rank": "A",
            "suit": "diamonds"
        },
        {
            "rank": "K",
            "suit": "diamonds"
        },
        {
            "rank": "Q",
            "suit": "diamonds"
        },
        {
            "rank": "J",
            "suit": "diamonds"
        },
        {
            "rank": "10",
            "suit": "diamonds"
        }
    ]
]

# Constant holding the face cards one-char symbol and their value
FACE_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}