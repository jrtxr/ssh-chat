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
        "/setstatus "
    ):

        status = msg[
            len("/setstatus "):
        ].strip()

        user_status[
            nickname
        ] = status

        send_to(
            conn,
            system_message(
                f"Status definido para: {status}"
            )
        )

        return True

    if lower == "/cleanstatus":

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

    if lower.startswith(
        "/getstatus "
    ):

        target = msg[
            len("/getstatus "):
        ].strip()

        status = user_status.get(
            target
        )

        if status:

            send_to(
                conn,
                system_message(
                    f"{target} está [{status}]"
                )
            )

        else:

            send_to(
                conn,
                system_message(
                    f"{target} não possui status."
                )
            )

        return True

    return False