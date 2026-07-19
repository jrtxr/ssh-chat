from utils.messages import send_to


def show_help(conn):

    send_to(
        conn,
        """
        
==========================================================
Comandos:
  /on -------------> ver quem está online
  /help -----------> ver comandos
  /s --------------> sair

  /setstt <text> --> adicionar status
  /cleanstt -------> limpar status

  @user mensagem --> mencionar usuário
  !user mensagem --> enviar mensagem privada
==========================================================

        """
    )