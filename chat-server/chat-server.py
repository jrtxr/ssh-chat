#!/usr/bin/env python3

import socket
import threading
import time
from collections import defaultdict

from config import (
    HOST,
    PORT,
    RESET,
    MAX_CLIENTS,
    MAX_MESSAGE_LENGTH
)
from core.clients import (
    clients,
    lock
)
from core.colors import (
    user_colors,
    get_user_color,
    color_mentions
)
from core.history import (
    history,
    add_history,
    send_history
)
from core.status import (
    user_status,
    get_user_status
)
from utils.messages import (
    broadcast,
    system_message,
    send_to
)
from utils.timeutils import (
    timestamp
)
from utils.messages import (
    system_message
)
from commands.help import (
    show_help
)
from commands.online import (
    send_online_list
)
from commands.private import (
    handle_private_message
)
from commands.status import (
    handle_status_command
)
from core.cleanup import (
    reset_server_state
)

message_rate = defaultdict(list)

def handle_client(conn):

    nickname = None

    try:

        nickname = (
            conn.recv(1024)
            .decode()
            .strip()
        )

        if not nickname:

            return

        get_user_color(
            nickname
        )

        with lock:

            clients[conn] = nickname

        send_history(
            conn
        )

        join_msg = system_message(
            f"{nickname} entrou"
        )

        add_history(
            join_msg
        )

        broadcast(
            join_msg
        )

        while True:

            data = conn.recv(
                4096
            )

            if not data:

                break

            msg = (
                data.decode()
                .strip()
            )

            if len(msg) > MAX_MESSAGE_LENGTH:

                send_to(
                    conn,
                    system_message(
                        f"Mensagem muito grande. Máximo: {MAX_MESSAGE_LENGTH} caracteres."
                    )
                )

                continue

            if not msg:

                continue

            now = time.time()

            message_rate[nickname] = [
                t
                for t in message_rate[nickname]
                if now - t < 1
            ]

            if len(message_rate[nickname]) >= 5:

                send_to(
                    conn,
                    system_message(
                        "Limite: máximo de 5 mensagens por segundo."
                    )
                )

                continue

            message_rate[nickname].append(now)

            if msg.lower() == "/on":

                send_online_list(
                    conn
                )

                continue

            if msg.lower() == "/help":

                show_help(
                    conn
                )

                continue

            if handle_status_command(
                conn,
                nickname,
                msg
            ):

                continue

            if msg.startswith("!"):

                handle_private_message(
                    conn,
                    nickname,
                    msg
                )

                continue

            color = get_user_color(
                nickname
            )

            msg = color_mentions(
                msg
            )

            status = get_user_status(
                nickname
            )

            if status:

                final_msg = (
                    f"[{timestamp()}]"
                    f"({status}){color}[{nickname}]{RESET}: "
                    f"{msg}"
                )

            else:

                final_msg = (
                    f"[{timestamp()}]"
                    f"{color}[{nickname}]:{RESET} "
                    f"{msg}"
                )

            add_history(
                final_msg
            )

            broadcast(
                final_msg,
                exclude=conn
            )

    except Exception:
        import traceback
        traceback.print_exc()

    finally:

        with lock:

            clients.pop(
                conn,
                None
            )

            message_rate.pop(
                nickname,
                None
            )

            if len(clients) == 0:

                reset_server_state()

        if nickname:

            broadcast(
                system_message(
                    f"{nickname} saiu"
                )
            )

        try:

            conn.close()

        except Exception:

            pass


def main():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind(
        (HOST, PORT)
    )

    server.listen(50)

    print(
        f"Chat iniciado em "
        f"{HOST}:{PORT}"
    )

    while True:

        conn, addr = server.accept()

        with lock:

            if len(clients) >= MAX_CLIENTS:

                send_to(
                    conn,
                    system_message(
                        "Servidor cheio."
                    )
                )

                conn.close()
                continue

        threading.Thread(
            target=handle_client,
            args=(conn,),
            daemon=True
        ).start()


if __name__ == "__main__":

    main()