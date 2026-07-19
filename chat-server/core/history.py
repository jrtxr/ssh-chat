from utils.messages import (
    send_to
)


history = []


def add_history(message):

    history.append(
        message
    )

    if len(history) > 50:

        history.pop(0)


def send_history(conn):

    if not history:

        return

    send_to(
        conn,
        "\n========== HISTÓRICO ==========\n"
    )

    for line in history:

        send_to(
            conn,
            line
        )

    send_to(
        conn,
        "\n===============================\n"
    )