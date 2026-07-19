#!/usr/bin/env python3

import sys

from client.banner import (
    show_banner
)

from client.connection import (
    create_connection
)

from client.receiver import (
    start_receiver
)

from client.prompt import (
    start_prompt
)


def main():

    if len(sys.argv) < 2:

        print(
            "Uso: chat-client <nickname>"
        )

        sys.exit(1)

    nickname = sys.argv[1]

    try:

        sock = create_connection(
            nickname
        )

    except ConnectionRefusedError:

        print(
            "\nServidor offline.\n"
        )

        sys.exit(1)

    except Exception as e:

        print(
            f"Erro: {e}"
        )

        sys.exit(1)

    show_banner(
        nickname
    )

    start_receiver(
        sock
    )

    try:

        start_prompt(
            sock,
            nickname
        )

    except (
        KeyboardInterrupt,
        EOFError
    ):

        pass

    finally:

        try:

            sock.close()

        except Exception:

            pass

        print()
        print(
            "Desconectado."
        )
        print()


if __name__ == "__main__":

    main()