import xmpp
import sys


def send_message(username, password, to, message_text):
    client = xmpp.Client('172.16.10.121', debug=[])
    client.connect(server=('172.16.10.121', 5222), secure=False)
    client.auth(username, password, 'Test Reporter')
    client.sendInitPresence()
    message = xmpp.Message(to, message_text)
    client.send(message)

if __name__ == "__main__":
    send_message(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
