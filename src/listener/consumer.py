import time
import stomp
import src.listener.config.configListener as fila
import src.db.db as db

class Leitor(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, frame):
        print(frame.body)

    def on_message(self, frame):
        print(frame.body)
        db.save_object_listener(frame.body)

conn = fila.obterConexao()
conn.set_listener('', Leitor(conn))

conn.subscribe(destination=fila.confFila, id=1, ack='auto')

while(True):
    print('Listener running')
    time.sleep(2)

conn.disconnect()
