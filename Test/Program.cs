using System;
using Identifeye;
using System.Threading;
using IdentifeyeCSharp;
using CsvHelper;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace Test
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Starting...");
            var client = new Client("127.0.0.1:50051");
            Console.Write("Enter a CSV file to import: ");

            List<DataPoint> data;
            using(var reader = new StreamReader(Console.ReadLine()))
            {
                using(var CSVReader = new CsvReader(reader))
                {
                    data = CSVReader.GetRecords<Data>().Select(d => d.ToDataPoint()).ToList();
                }
            }

            client.SendDataBulk(data);

            Console.WriteLine("Sent data");
        }
    }
}
