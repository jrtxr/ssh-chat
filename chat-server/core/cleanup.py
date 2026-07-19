from core.clients import clients
from core.colors import user_colors
from core.history import history
from core.status import user_status


def reset_server_state():

    history.clear()

    user_colors.clear()

    user_status.clear()

    clients.clear()