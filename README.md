# SSH Chat

Chat multiusuário via SSH escrito em Python.

O projeto permite que usuários entrem em uma sala de conversa utilizando apenas uma conexão SSH autenticada por chave pública.

Cada chave SSH pode ser associada a um nickname fixo definido pelo administrador do servidor.

---

# Características

* Autenticação por chave pública SSH
* Nicknames controlados pelo administrador
* Mensagens privadas
* Menções de usuários
* Status personalizados
* Histórico de mensagens
* Cores automáticas por usuário
* Rate limit anti-spam
* Limite de tamanho de mensagem
* Execução automática via OpenSSH
* Compatível com Linux, VPS e servidores dedicados

---

# Demonstração

```text
[12:30] [SISTEMA] clark entrou

[clark] [studying] Hi guys

[parker] Hi

[bruce] welcome
```

Mensagem privada:

```text
!bruce Hellow
```

Consulta de status:

```text
/getstatus clark

[SISTEMA] clark está [studying]
```

---

# Comandos

| Comando                | Descrição             |
| ---------------------- | --------------------- |
| `/help`                | Exibe ajuda           |
| `/online`              | Lista usuários online |
| `/setstatus <texto>`   | Define status         |
| `/cleanstatus`         | Remove status         |
| `/getstatus <usuario>` | Consulta status       |
| `!usuario mensagem`    | Mensagem privada      |
| `@usuario`             | Menção                |

---

# Estrutura do Projeto

```text
chat/
├── chat-client/
│   ├── chat-client.py
│   └── client/
│       ├── banner.py
│       ├── connection.py
│       ├── prompt.py
│       └── receiver.py
│
└── chat-server/
    ├── chat-server.py
    ├── config.py
│
    ├── commands/
│       ├── help.py
│       ├── online.py
│       ├── private.py
│       └── status.py
│
    ├── core/
│       ├── cleanup.py
│       ├── clients.py
│       ├── colors.py
│       ├── history.py
│       └── status.py
│
    └── utils/
        ├── messages.py
        └── timeutils.py
```

---

# Segurança

O projeto foi desenvolvido para operar atrás do OpenSSH.

Recursos implementados:

* Autenticação por chave pública
* Nickname fixo definido pelo servidor
* Limite de mensagens por segundo
* Limite de tamanho de mensagem
* Restrições de SSH através de `authorized_keys`
* Limite máximo de conexões simultâneas
* Timeout de conexão configurável

---

# Requisitos

* Python 3.10+
* OpenSSH Server
* Linux

---

# Instalação

Consulte:

```text
SETUP.md
```

O arquivo contém o processo completo de instalação, configuração do OpenSSH, systemd e deploy em produção.

---

# Licença

MIT License

```
```

# SSH Chat
PARA REALIZAR A INSTALAÇÃO LEIA O SETUP.md
