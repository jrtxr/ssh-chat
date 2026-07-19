from utils.messages import send_to


def show_help(conn):

    send_to(
        conn,
        """
Comandos:
  /online ---------------> ver quem está online
  /help -----------------> ver comandos
  /sair -----------------> sair

  /setstatus <text> ----> adicionar status
  /getstatus <user> ----> ver status de um usuário específico
  /cleanstatus ---------> limpar status

  @user mensagem -------> mencionar usuário
  !user mensagem -------> enviar mensagem privada
        """
    )