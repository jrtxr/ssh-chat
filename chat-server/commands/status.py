from core.status import user_status
from utils.messages import send_to
from utils.messages import system_message


def handle_status_command(
    conn,
    nickname,
    msg
):

    lower = msg.lower()

    if lower.startswith(
        "/setstt "
    ):

        status = msg[
            len("/setstt "):
        ].strip()

        user_status[
            nickname
        ] = status

        send_to(
            conn,
            system_message(
                f"status modificado ({status})"
            )
        )

        return True

    if lower == "/cleanstt":

        user_status.pop(
            nickname,
            None
        )

        send_to(
            conn,
            system_message(
                "Status removido."
            )
        )

        return True

    return False