using System;
using Identifeye;
using Grpc.Core;
using System.Collections.Generic;

namespace IdentifeyeCSharp
{
    public class Client
    {
        private Channel channel;
        private IdentifeyeService.IdentifeyeServiceClient client;

        public Client(string target)
        {
            channel = new Channel(target, ChannelCredentials.Insecure);
            client = new IdentifeyeService.IdentifeyeServiceClient(channel);
        }

        public bool SendData(DataPoint data)
        {
            return client.SendData(data).Success;
        }

        public bool SendDataBulk(IList<DataPoint> data)
        {
            return client.SendDataBulk(new BulkData { Data = { data } }).Success;
        }

        public void Stop()
        {
            channel.ShutdownAsync().Wait();
        }
    }
}
