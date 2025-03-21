using System.Globalization;
using System.Reflection;
using MySqlConnector;

namespace WildfireAPI;
public class WildfireEntry
{
    public required string Id { get; set; }
    public double? X { get; set; }
    public double? Y { get; set; }
    public int? Objectid { get; set; }
    public string? Globalid { get; set; }
    public string? Fireoccurid { get; set; }
    public string? Cn { get; set; }
    public string? Revdate { get; set; }
    public string? Firename { get; set; }
    public string? Complexname { get; set; }
    public ushort? Fireyear { get; set; }
    public string? Uniquefireid { get; set; }
    public int? Sofirenum { get; set; }
    public int? Localfirenum { get; set; }
    public int? Securityid { get; set; }
    public string? Discoverydatetime { get; set; }
    public string? Sizeclass { get; set; }
    public double? Totalacres { get; set; }
    public string? Statcause { get; set; }
    public string? Comments { get; set; }
    public int? Datasource { get; set; }
    public string? Fireoutdatetime { get; set; }
    public string? Owneragency { get; set; }
    public string? Unitdowner { get; set; }
    public string? Protectionagency { get; set; }
    public string? Unitdprotect { get; set; }
    public double? Latdd83 { get; set; }
    public double? Longdd83 { get; set; }
    public string? Firetypecaategory { get; set; }
    public string? Pointtype { get; set; }
    public string? Perimiexists { get; set; }
    public string? Firerptqc { get; set; }
    public int? Dbsourceid { get; set; }
    public string? Dbsourcedate { get; set; }
    public int? Accuracy { get; set; }
    public string? Shape { get; set; }

    // to format headers from "COLUMNNAME" to "Columnname"
    private static string FormatColumnHeaderName(string str)
        => new String(Char.ToUpper(str[0]) + str[1..str.Length].ToLower());

    public static async Task<List<WildfireEntry>> ContructEntriesFromReader(MySqlDataReader reader)
    {
        List<WildfireEntry> entries = [];

        // extra variables for null handling
        int result;
        ushort uresult;
        double dresult;
        while (await reader.ReadAsync())
        {
            // I am not proud of this solution but it works and I wanna work on something else
            var entry = new WildfireEntry()
            {
                // never null so doesn't need extra stuff to handle null
                Id = reader.GetString(0),
                X = Double.TryParse(reader.GetValue(1).ToString(), out dresult) ? dresult : null,
                Y = Double.TryParse(reader.GetValue(2).ToString(), out dresult) ? dresult : null,
                Objectid = Int32.TryParse(reader.GetValue(3).ToString(), out result) ? result : null,
                Globalid = reader.GetValue(4).ToString(),
                Fireoccurid = reader.GetValue(5).ToString(),
                Cn = reader.GetValue(6).ToString(),
                Revdate = reader.GetValue(7).ToString(),
                Firename = reader.GetValue(8).ToString(),
                Complexname = reader.GetValue(9).ToString(),
                Fireyear = UInt16.TryParse(reader.GetValue(10).ToString(), out uresult) ? uresult : null,
                Uniquefireid = reader.GetValue(11).ToString(),
                Sofirenum = Int32.TryParse(reader.GetValue(12).ToString(), out result) ? result : null,
                Localfirenum = Int32.TryParse(reader.GetValue(13).ToString(), out result) ? result : null,
                Securityid = Int32.TryParse(reader.GetValue(14).ToString(), out result) ? result : null,
                Discoverydatetime = reader.GetValue(15).ToString(),
                Sizeclass = reader.GetValue(16).ToString(),
                Totalacres = Double.TryParse(reader.GetValue(17).ToString(), out dresult) ? dresult : null,
                Statcause = reader.GetValue(18).ToString(),
                Comments = reader.GetValue(19).ToString(),
                Datasource = Int32.TryParse(reader.GetValue(20).ToString(), out result) ? result : null,
                Fireoutdatetime = reader.GetValue(21).ToString(),
                Owneragency = reader.GetValue(22).ToString(),
                Unitdowner = reader.GetValue(23).ToString(),
                Protectionagency = reader.GetValue(24).ToString(),
                Unitdprotect = reader.GetValue(25).ToString(),
                Latdd83 = Double.TryParse(reader.GetValue(26).ToString(), out dresult) ? dresult : null,
                Longdd83 = Double.TryParse(reader.GetValue(27).ToString(), out dresult) ? dresult : null,
                Firetypecaategory = reader.GetValue(28).ToString(),
                Pointtype = reader.GetValue(29).ToString(),
                Perimiexists = reader.GetValue(30).ToString(),
                Firerptqc = reader.GetValue(31).ToString(),
                Dbsourceid = Int32.TryParse(reader.GetValue(32).ToString(), out result) ? result : null,
                Dbsourcedate = reader.GetValue(33).ToString(),
                Accuracy = Int32.TryParse(reader.GetValue(34).ToString(), out result) ? result : null,
                Shape = reader.GetValue(35).ToString(),
            };
            entries.Add(entry);
        }

        return entries;
    }
}