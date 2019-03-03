import os

if __name__ == '__main__':
    print('Building protocol buffers')
    os.system('python -m grpc_tools.protoc --python_out=src --grpc_python_out=src --proto_path=../Protos messages.proto')
    print('Starting Identifeye process')
    os.system('python src/server.py')