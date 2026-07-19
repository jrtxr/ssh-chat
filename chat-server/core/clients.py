import threading


clients = {}

lock = threading.Lock()


def get_conn_by_nickname(target):

    with lock:

        for conn, nick in clients.items():

            if nick.lower() == target.lower():

                return conn

    return None