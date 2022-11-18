import stomp

confUsuario = "admin"
confSenha = "admin"

confFila = "/queue/produtos"

def obterConexao():
    conn = stomp.Connection()
    conn.connect(confUsuario, confSenha, wait=True)

    return conn