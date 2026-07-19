from config import (
    SYSTEM_COLOR,
    RESET
)

from core.clients import (
    clients,
    lock
)

from utils.timeutils import (
    timestamp
)


def send_to(conn, message):

    try:

        conn.sendall(
            (message + "\n").encode()
        )

    except:

        pass


def broadcast(
    message,
    exclude=None
):

    dead = []

    with lock:

        for conn in clients:

            if conn == exclude:
                continue

            try:

                conn.sendall(
                    (
                        message + "\n"
                    ).encode()
                )

            except:

                dead.append(
                    conn
                )

        for conn in dead:

            clients.pop(
                conn,
                None
            )


def system_message(text):

    return (
        f"[{timestamp()}] "
        f"{SYSTEM_COLOR}"
        f"[SISTEMA]"
        f"{RESET} "
        f"{text}"
    )