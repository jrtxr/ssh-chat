user_status = {}


def get_user_status(
    nickname
):

    return user_status.get(
        nickname,
        None
    )


def set_user_status(
    nickname,
    status
):

    user_status[
        nickname
    ] = status


def clear_user_status(
    nickname
):

    user_status.pop(
        nickname,
        None
    )