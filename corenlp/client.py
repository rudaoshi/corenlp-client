

import zmq
import ujson as json

class CoreNLPClient(object):

    def __init__(self, host, port):

        self.host = host
        self.port = port

        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)

        try:
            self.socket.connect ("tcp://{host}:{port}".format(
                host=self.host, port = self.port))
        except:
            raise

    def analysis(self, text):

        self.socket.send("process " + text)
        result = self.socket.recv()

        return json.loads(result)




