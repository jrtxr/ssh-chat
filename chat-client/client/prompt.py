from prompt_toolkit import (
    PromptSession
)

from prompt_toolkit.patch_stdout import (
    patch_stdout
)


def start_prompt(
    sock,
    nickname
):

    session = PromptSession()

    while True:

        with patch_stdout():

            msg = session.prompt(
                f"{nickname}> "
            )

        msg = msg.strip()

        if not msg:
            continue

        if msg.lower() in (
            "/sair",
            "/quit",
            "/exit"
        ):
            break

        sock.sendall(
            (msg + "\n").encode()
        )