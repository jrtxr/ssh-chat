# SSH Chat

Chat multiusuário via SSH escrito em Python.

Cada usuário se conecta utilizando sua própria chave SSH e entra automaticamente no chat com um nickname previamente definido pelo administrador do servidor.

O projeto é dividido em dois componentes:

* `chat-server/` → servidor responsável por gerenciar conexões, histórico, usuários online, mensagens privadas e status.
* `chat-client/` → cliente executado automaticamente após a autenticação SSH.

---

# Funcionalidades

* Login utilizando chave SSH
* Nickname fixo por usuário
* Lista de usuários online
* Mensagens privadas
* Menções com `@usuario`
* Status personalizados
* Histórico de mensagens
* Limite de tamanho de mensagem
* Rate limit (proteção contra spam)
* Limite máximo de usuários simultâneos
* Limpeza automática do estado quando o último usuário sai

---

# Estrutura do Projeto

```text
chat/
├── chat-client/
│   ├── chat-client.py
│   ├── config.py
│   └── client/
│       ├── banner.py
│       ├── connection.py
│       ├── prompt.py
│       └── receiver.py
│
└── chat-server/
    ├── chat-server.py
    ├── config.py
    ├── commands/
    │   ├── help.py
    │   ├── online.py
    │   ├── private.py
    │   └── status.py
    │
    ├── core/
    │   ├── cleanup.py
    │   ├── clients.py
    │   ├── colors.py
    │   ├── history.py
    │   └── status.py
    │
    └── utils/
        ├── messages.py
        └── timeutils.py
```

---

# Requisitos

Servidor Linux com:

* Python 3.11+
* OpenSSH Server

Instalação das dependências:

```bash
pip install prompt_toolkit
```

---

# Configuração do Servidor

Edite:

```text
chat-server/config.py
```

Exemplo:

```python
HOST = "127.0.0.1"
PORT = 9000

MAX_CLIENTS = 10
MAX_MESSAGE_LENGTH = 1000
```

---

# Executando o Servidor

Entre na pasta:

```bash
cd chat-server
```

Execute:

```bash
python3 chat-server.py
```

Saída esperada:

```text
Chat iniciado em 127.0.0.1:9000
```

---

# Configuração do Cliente

Edite:

```text
chat-client/config.py
```

Exemplo:

```python
HOST = "127.0.0.1"
PORT = 9000
```

---

# Executando o Cliente

Para testes locais:

```bash
python3 chat-client.py user1
```

---

# Integração com SSH

O método recomendado é utilizar um usuário dedicado ao chat.

Exemplo:

```bash
useradd -m chat
```

Crie:

```text
/home/chat/.ssh/authorized_keys
```

Cada chave pública deve possuir um comando forçado.

Exemplo:

```text
command="/opt/chat/chat-client user1" ssh-ed25519 AAAA...
```

Quando o usuário autenticar via SSH, o cliente será iniciado automaticamente.

O nickname não é escolhido pelo usuário. Ele é definido pelo administrador através do `authorized_keys`.

---

# Comandos Disponíveis

### Ver usuários online

```text
/online
```

### Exibir ajuda

```text
/help
```

### Sair

```text
/sair
```

### Definir status

```text
/setstatus estudando
```

### Consultar status

```text
/getstatus user1
```

### Remover status

```text
/cleanstatus
```

### Mensagem privada

```text
!usuario mensagem
```

### Menção

```text
@usuario
```

---

# Segurança

Recomendações:

* Utilizar apenas autenticação por chave pública.
* Desabilitar autenticação por senha no SSH.
* Desabilitar login root.
* Utilizar usuário dedicado ao chat.
* Utilizar comandos forçados no `authorized_keys`.
* Utilizar:

  * no-port-forwarding
  * no-X11-forwarding
  * no-agent-forwarding
  * no-pty

Exemplo:

```text
command="/opt/chat/chat-client user1",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 AAAA...
```

---

# Licença

Projeto distribuído para fins educacionais e experimentais.
