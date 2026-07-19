from core.clients import clients, lock
from utils.messages import send_to


def send_online_list(conn):

    with lock:

        users = sorted(
            clients.values()
        )

    msg = "\nUsuários online:\n"

    for user in users:

        msg += (
            f" \033[92m●\033[0m "
            f"{user}\n"
        )

    send_to(
        conn,
        msg
    )