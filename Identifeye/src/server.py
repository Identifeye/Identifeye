from rpc_server import IdentifeyeService
import grpc
import messages_pb2
import messages_pb2_grpc
from concurrent import futures
import time

if __name__ == '__main__':
    print('Starting Identifeye server...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_IdentifeyeServiceServicer_to_server(IdentifeyeService(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started')
    try:
        while True:
            time.sleep(9999);
    except KeyboardInterrupt:
        server.stop(0)