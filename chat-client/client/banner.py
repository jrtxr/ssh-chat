def show_banner(nickname):

    CYAN = "\033[96m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print()

    print(
        f"{CYAN}"
        "╔══════════════════════════════════════════════════════════════════════╗"
        f"{RESET}"
    )

    print(
        f"{CYAN}║                                                                      ║{RESET}"
    )

    print(
        f"{BLUE}║   ██████╗██╗  ██╗ █████╗ ████████╗    ██╗███╗   ███╗██████╗ ██████╗  ║{RESET}"
    )

    print(
        f"{BLUE}║  ██╔════╝██║  ██║██╔══██╗╚══██╔══╝    ██║████╗ ████║██╔══██╗██╔══██╗ ║{RESET}"
    )

    print(
        f"{BLUE}║  ██║     ███████║███████║   ██║       ██║██╔████╔██║██████╔╝██████╔╝ ║{RESET}"
    )

    print(
        f"{BLUE}║  ██║     ██╔══██║██╔══██║   ██║       ██║██║╚██╔╝██║██╔═══╝ ██╔══██╗ ║{RESET}"
    )

    print(
        f"{BLUE}║  ╚██████╗██║  ██║██║  ██║   ██║       ██║██║ ╚═╝ ██║██║     ██║  ██║ ║{RESET}"
    )

    print(
        f"{BLUE}║   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝ ║{RESET}"
    )

    print(
        f"{CYAN}║                                                                      ║{RESET}"
    )

    print(
        f"{CYAN}"
        "╚══════════════════════════════════════════════════════════════════════╝"
        f"{RESET}"
    )

    print()

    print(
        f"{GREEN}●{RESET} Conectado como: "
        f"{BOLD}{WHITE}{nickname}{RESET}"
    )

    print()

    print(
        f"{YELLOW}Comandos:{RESET}"
    )

    print("  /on ----------> Ver usuários online")
    print("  /help --------> Ver comandos")
    print("  /s -----------> Sair do chat")
    print()
    print("  /setstt ------> adicionar um status")
    print("  /cleanstt ----> limpar status")
    print()
    print("  @user --------> Mencionar usuário")
    print("  !user texto --> Mensagem privada")

    print()

    print(
        f"{CYAN}"
        "══════════════════════════════════════════════════════════════════════"
        f"{RESET}"
    )

    print()