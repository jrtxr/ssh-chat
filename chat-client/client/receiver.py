import threading

from prompt_toolkit import (
    print_formatted_text
)

from prompt_toolkit.formatted_text import (
    ANSI
)


def receive(sock):

    while True:

        try:

            data = sock.recv(
                4096
            )

            if not data:

                print(
                    "\nConexão encerrada.\n"
                )

                break

            message = (
                data.decode(
                    "utf-8",
                    errors="ignore"
                )
                .rstrip()
            )

            print_formatted_text(
                ANSI(message)
            )

        except Exception:

            break


def start_receiver(sock):

    threading.Thread(
        target=receive,
        args=(sock,),
        daemon=True
    ).start()