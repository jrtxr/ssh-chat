from core.clients import clients, lock
from utils.messages import send_to
from core.status import get_user_status
from core.colors import get_user_color
from config import (RESET)


def send_online_list(conn):

    with lock:

        users = sorted(
            clients.values()
        )

    msg = "==================================================\n"
    msg += "\nUsuários online:\n"

    for user in users:

        status = get_user_status(user)        
        if status:
            msgStatus = f"({status})"
        else:
            msgStatus = ''

        color = get_user_color(
            user
        )

        msg += (
            f" \033[92m●\033[0m "
            f"{color}[{user}]{RESET}{msgStatus}\n"
        )

    msg += "\n==================================================\n"

    send_to(
        conn,
        msg
    )