using System;
using Identifeye;
using System.Threading;
using IdentifeyeCSharp;

namespace Test
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Starting...");
            var client = new Client("127.0.0.1:50051");
            Console.WriteLine("Started pinging");
            while(true)
            {
                client.SendData(new DataPoint
                {
                    AccountNameHash = "abc",
                    ActivePlaytime = 10,
                    CharacterNameHash = "def",
                    IpHash = "hij",
                    IpLocationHash = "klm",
                    IsBanned = false
                });
                Console.WriteLine("Sent data");
                Thread.Sleep(2000);
            }
        }
    }
}
