import re

from config import (
    COLORS,
    BOLD,
    RESET
)


user_colors = {}


def get_user_color(nickname):

    if nickname in user_colors:

        return user_colors[
            nickname
        ]

    used = set(
        user_colors.values()
    )

    available = [

        color

        for color in COLORS

        if color not in used

    ]

    if available:

        color = available[0]

    else:

        index = (

            abs(
                hash(
                    nickname.lower()
                )
            )

            % len(COLORS)

        )

        color = COLORS[index]

    user_colors[
        nickname
    ] = color

    return color


def color_mentions(text):

    for nick in user_colors:

        pattern = (
            rf"@{re.escape(nick)}\b"
        )

        replacement = (
            f"{BOLD}"
            f"{get_user_color(nick)}"
            f"@{nick}"
            f"{RESET}"
        )

        text = re.sub(
            pattern,
            replacement,
            text,
            flags=re.IGNORECASE
        )

    return text