import messages_pb2
import messages_pb2_grpc

class IdentifeyeService(messages_pb2_grpc.IdentifeyeServiceServicer):
    def SendData(self, request, context):
        print('Received SendData request')
        print(request)
        return messages_pb2.Response(success = True)

    def SendDataBulk(self, request, context):
        print('Received SendDataBulk request')
        print(request)
        return messages_pb2.Response(success = True)