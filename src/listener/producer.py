import stomp

conn = stomp.Connection()
conn.connect('admin', 'admin', wait=True)

def send(body):
    conn.send(body=str(body), destination='/queue/produtos')