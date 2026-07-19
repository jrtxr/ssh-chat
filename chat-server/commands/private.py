from core.clients import clients, lock
from utils.messages import send_to
from config import PRIVATE_COLOR, RESET
from utils.timeutils import timestamp


def get_conn_by_nickname(target):

    with lock:

        for conn, nick in clients.items():

            if nick.lower() == target.lower():

                return conn

    return None


def handle_private_message(
    sender_conn,
    sender_nick,
    msg
):

    parts = msg.split(
        " ",
        1
    )

    target = parts[0][1:]

    if len(parts) < 2:

        send_to(
            sender_conn,
            "[SISTEMA] Uso: !usuario mensagem"
        )

        return

    text = parts[1]

    target_conn = get_conn_by_nickname(
        target
    )

    if not target_conn:

        send_to(
            sender_conn,
            f"[SISTEMA]: Usuário '{target}' não está online."
        )

        return

    send_to(
        target_conn,
        (
            f"[{timestamp()}] "
            f"{PRIVATE_COLOR}[PRIVADO]{RESET} "
            f"{sender_nick} → você: "
            f"{text}"
        )
    )

    send_to(
        sender_conn,
        (
            f"[{timestamp()}] "
            f"{PRIVATE_COLOR}[PRIVADO]{RESET} "
            f"você → {target}: "
            f"{text}"
        )
    )