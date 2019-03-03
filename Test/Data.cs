using Identifeye;

namespace Test
{
    /// <summary>
    /// Data loaded from the CSV file
    /// </summary>
    class Data
    {
        public string AccountName { get; set; }
        public string CharacterName { get; set; }
        public string IP { get; set; }
        public string UUID { get; set; }
        public string IPGeolocation { get; set; }
        public bool IsBanned { get; set; }
        public int ActivePlaytime { get; set; }

        public DataPoint ToDataPoint()
        {
            return new DataPoint
            {
                AccountNameHash = AccountName,
                CharacterNameHash = CharacterName,
                IpHash = IP,
                UuidHash = UUID,
                IpLocationHash = IPGeolocation,
                IsBanned = IsBanned,
                ActivePlaytime = ActivePlaytime
            };
        }
    }
}