import messages_pb2
import messages_pb2_grpc
from adj_list import Graph

class IdentifeyeService(messages_pb2_grpc.IdentifeyeServiceServicer):
    def __init__(self):
        self.graph = Graph()

    def SendData(self, request, context):
        print('Received SendData request')
        print(request)
        self.graph.add_edges([request])
        return messages_pb2.Response(success = True)

    def SendDataBulk(self, request, context):
        print('Received SendDataBulk request')
        print(request)
        self.graph.add_edges(request.data)
        return messages_pb2.Response(success = True)