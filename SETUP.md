# SETUP.md

# SSH Chat - Instalação Completa

Este guia mostra como instalar, configurar e executar o SSH Chat em uma VPS Linux utilizando OpenSSH e systemd.

---

# Visão Geral

O projeto funciona da seguinte forma:

1. O usuário conecta via SSH.
2. O OpenSSH valida a chave pública.
3. O `authorized_keys` executa automaticamente o cliente do chat.
4. O cliente conecta ao servidor local.
5. O usuário entra diretamente na sala.

Fluxo:

```text
Usuário
   │
   ▼
SSH
   │
   ▼
authorized_keys
   │
   ▼
chat-client
   │
   ▼
chat-server
```

---

# Requisitos

Sistema operacional:

* Debian 12+
* Ubuntu 22.04+
* Kali Linux
* Outras distribuições compatíveis

Pacotes necessários:

```bash
apt update

apt install -y \
    python3 \
    python3-pip \
    openssh-server
```

Instalar dependência Python:

```bash
pip3 install prompt_toolkit
```

---

# Estrutura Esperada

```text
/opt/chat
├── chat-client
└── chat-server
```

Exemplo:

```bash
mkdir -p /opt/chat
```

Copie o projeto para:

```text
/opt/chat
```

---

# Criar Usuário Dedicado

Criar usuário exclusivo para o chat:

```bash
useradd -m chat
```

Criar diretório SSH:

```bash
mkdir -p /home/chat/.ssh
```

Permissões:

```bash
chown -R chat:chat /home/chat/.ssh

chmod 700 /home/chat
chmod 700 /home/chat/.ssh
```

---

# Configurar authorized_keys

Arquivo:

```text
/home/chat/.ssh/authorized_keys
```

Exemplo:

```text
# user1
command="/opt/chat/chat-client/chat-client.py user1",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 SUA_CHAVE_PUBLICA

# ark
command="/opt/chat/chat-client/chat-client.py ark",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 SUA_CHAVE_PUBLICA

# anti
command="/opt/chat/chat-client/chat-client.py anti",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 SUA_CHAVE_PUBLICA
```

Permissões:

```bash
chown chat:chat /home/chat/.ssh/authorized_keys

chmod 600 /home/chat/.ssh/authorized_keys
```

---

# Configurar SSH

Editar:

```text
/etc/ssh/sshd_config
```

Recomendações:

```text
PubkeyAuthentication yes

PasswordAuthentication no

ChallengeResponseAuthentication no

PermitRootLogin no
```

Validar:

```bash
sshd -t
```

Reiniciar:

```bash
systemctl restart ssh
```

---

# Configurar Servidor

Editar:

```text
/opt/chat/chat-server/config.py
```

Exemplo:

```python
HOST = "127.0.0.1"
PORT = 9000

MAX_CLIENTS = 10

MAX_MESSAGE_LENGTH = 1000
```

O servidor deve escutar apenas em:

```python
HOST = "127.0.0.1"
```

---

# Configurar Cliente

Editar:

```text
/opt/chat/chat-client/config.py
```

Exemplo:

```python
HOST = "127.0.0.1"
PORT = 9000
```

---

# Tornar Cliente Executável

```bash
chmod +x /opt/chat/chat-client/chat-client.py
```

---

# Criar Serviço systemd

Arquivo:

```text
/etc/systemd/system/chat-server.service
```

Conteúdo:

```ini
[Unit]
Description=SSH Chat Server
After=network.target

[Service]
Type=simple

User=chat
Group=chat

WorkingDirectory=/opt/chat/chat-server

ExecStart=/usr/bin/python3 /opt/chat/chat-server/chat-server.py

Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

---

# Registrar Serviço

```bash
systemctl daemon-reload
```

---

# Habilitar Inicialização Automática

```bash
systemctl enable chat-server
```

---

# Iniciar Servidor

```bash
systemctl start chat-server
```

---

# Verificar Status

```bash
systemctl status chat-server
```

Saída esperada:

```text
active (running)
```

---

# Ver Logs

Logs em tempo real:

```bash
journalctl -u chat-server -f
```

Últimos logs:

```bash
journalctl -u chat-server -n 100
```

---

# Reiniciar Após Alterações

```bash
systemctl restart chat-server
```

---

# Parar Servidor

```bash
systemctl stop chat-server
```

---

# Confirmar Porta

```bash
ss -tlnp | grep 9000
```

Resultado esperado:

```text
127.0.0.1:9000
```

---

# Testar Conexão

Do computador do usuário:

```bash
ssh chat@IP_DA_VPS
```

Após autenticar:

```text
● Conectado como: user1
```

O banner do chat deverá aparecer automaticamente.

---

# Adicionar Novo Usuário

1. Solicite a chave pública.
2. Abra:

```text
/home/chat/.ssh/authorized_keys
```

3. Adicione:

```text
# nickname
command="/opt/chat/chat-client/chat-client.py nickname",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 CHAVE_PUBLICA
```

4. Salve.

Pronto. O usuário já poderá conectar.

---

# Remover Usuário

Remova a linha correspondente do:

```text
/home/chat/.ssh/authorized_keys
```

A alteração terá efeito na próxima conexão.

---

# Comandos Disponíveis

```text
/help
```

Exibe ajuda.

```text
/online
```

Lista usuários online.

```text
/setstatus estudando
```

Define um status.

```text
/cleanstatus
```

Remove o status.

```text
/getstatus usuario
```

Consulta o status de outro usuário.

```text
!usuario mensagem
```

Mensagem privada.

```text
@usuario
```

Menção.

---

# Segurança

O projeto utiliza:

* Autenticação por chave pública.
* Nickname definido pelo administrador.
* Comando SSH forçado.
* Limite de mensagens por segundo.
* Limite de tamanho de mensagem.
* Restrição de port forwarding.
* Restrição de X11 forwarding.
* Restrição de agent forwarding.
* Restrição de PTY.

Recomenda-se manter:

```text
PasswordAuthentication no
PermitRootLogin no
```

em produção.

---

# Atualização

Atualize os arquivos em:

```text
/opt/chat
```

e reinicie:

```bash
systemctl restart chat-server
```

Pronto.
