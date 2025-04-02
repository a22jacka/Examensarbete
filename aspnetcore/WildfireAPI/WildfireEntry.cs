using System.Runtime.CompilerServices;
using System.Text.Json.Serialization;
using MySqlConnector;

namespace WildfireAPI;
public class WildfireEntry
{
    [JsonPropertyName("id")]
    public required string Id { get; set; }
    [JsonPropertyName("x")]
    public double? X { get; set; }
    [JsonPropertyName("y")]
    public double? Y { get; set; }
    [JsonPropertyName("objectid")]
    public int? Objectid { get; set; }
    [JsonPropertyName("globalid")]
    public string? Globalid { get; set; }
    [JsonPropertyName("fireoccurid")]
    public string? Fireoccurid { get; set; }
    [JsonPropertyName("cn")]
    public string? Cn { get; set; }
    [JsonPropertyName("revdate")]
    public string? Revdate { get; set; }
    [JsonPropertyName("firename")]
    public string? Firename { get; set; }
    [JsonPropertyName("complexname")]
    public string? Complexname { get; set; }
    [JsonPropertyName("fireyear")]
    public ushort? Fireyear { get; set; }
    [JsonPropertyName("uniquefireid")]
    public string? Uniquefireid { get; set; }
    [JsonPropertyName("sofirenum")]
    public int? Sofirenum { get; set; }
    [JsonPropertyName("localfirenum")]
    public int? Localfirenum { get; set; }
    [JsonPropertyName("securityid")]
    public int? Securityid { get; set; }
    [JsonPropertyName("discoverydatetime")]
    public string? Discoverydatetime { get; set; }
    [JsonPropertyName("sizeclass")]
    public string? Sizeclass { get; set; }
    [JsonPropertyName("totalacres")]
    public double? Totalacres { get; set; }
    [JsonPropertyName("statcause")]
    public string? Statcause { get; set; }
    [JsonPropertyName("comments")]
    public string? Comments { get; set; }
    [JsonPropertyName("datasource")]
    public int? Datasource { get; set; }
    [JsonPropertyName("fireoutdatetime")]
    public string? Fireoutdatetime { get; set; }
    [JsonPropertyName("owneragency")]
    public string? Owneragency { get; set; }
    [JsonPropertyName("unitdowner")]
    public string? Unitdowner { get; set; }
    [JsonPropertyName("protectionagency")]
    public string? Protectionagency { get; set; }
    [JsonPropertyName("unitdprotect")]
    public string? Unitdprotect { get; set; }
    [JsonPropertyName("latdd83")]
    public double? Latdd83 { get; set; }
    [JsonPropertyName("longdd83")]
    public double? Longdd83 { get; set; }
    [JsonPropertyName("firetypecategory")]
    public string? Firetypecategory { get; set; }
    [JsonPropertyName("pointtype")]
    public string? Pointtype { get; set; }
    [JsonPropertyName("perimiexists")]
    public string? Perimiexists { get; set; }
    [JsonPropertyName("firerptqc")]
    public string? Firerptqc { get; set; }
    [JsonPropertyName("dbsourceid")]
    public int? Dbsourceid { get; set; }
    [JsonPropertyName("dbsourcedate")]
    public string? Dbsourcedate { get; set; }
    [JsonPropertyName("accuracy")]
    public int? Accuracy { get; set; }
    [JsonPropertyName("shape")]
    public string? Shape { get; set; }

    public static async Task<List<WildfireEntry>> ContructEntriesFromReader(MySqlDataReader reader)
    {
        List<WildfireEntry> entries = [];

        // extra variables for null handling
        while (await reader.ReadAsync())
        {
            // I am not proud of this solution but it works and I wanna work on something else
            // All the TryParse is for null handling, other is just fails with "Can't convert DBNull to other types" 
            var entry = new WildfireEntry()
            {
                // never null so doesn't need extra stuff to handle null
                Id = reader.GetString(0),
                X = Double.TryParse(reader.GetValue(1).ToString(), out double dresult) ? dresult : null,
                Y = Double.TryParse(reader.GetValue(2).ToString(), out dresult) ? dresult : null,
                Objectid = Int32.TryParse(reader.GetValue(3).ToString(), out int result) ? result : null,
                Globalid = reader.GetValue(4).ToString(),
                Fireoccurid = reader.GetValue(5).ToString(),
                Cn = reader.GetValue(6).ToString(),
                Revdate = reader.GetValue(7).ToString(),
                Firename = reader.GetValue(8).ToString(),
                Complexname = reader.GetValue(9).ToString(),
                Fireyear = UInt16.TryParse(reader.GetValue(10).ToString(), out ushort uresult) ? uresult : null,
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
                Firetypecategory = reader.GetValue(28).ToString(),
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

    public async Task InsertWildfireEntry(string connectionString)
    {
        using var connection = new MySqlConnection(connectionString);
        using var command = connection.CreateCommand();
        command.CommandText = @"INSERT INTO WildfireEntry
            (Id, X, Y, Objectid, Globalid, Fireoccurid, Cn, Revdate, Firename, Complexname, Fireyear, Uniquefireid, Sofirenum, Localfirenum, Securityid, Discoverydatetime, Sizeclass, Totalacres, Statcause, Comments, Datasource, Fireoutdatetime, Owneragency, Unitdowner, Protectionagency, Unitdprotect, Latdd83, Longdd83, Firetypecategory, Pointtype, Perimiexists, Firerptqc, Dbsourceid, Dbsourcedate, Accuracy, Shape) VALUES
            (@Id, @X, @Y, @Objectid, @Globalid, @Fireoccurid, @Cn, @Revdate, @Firename, @Complexname, @Fireyear, @Uniquefireid, @Sofirenum, @Localfirenum, @Securityid, @Discoverydatetime, @Sizeclass, @Totalacres, @Statcause, @Comments, @Datasource, @Fireoutdatetime, @Owneragency, @Unitdowner, @Protectionagency, @Unitdprotect, @Latdd83, @Longdd83, @Firetypecategory, @Pointtype, @Perimiexists, @Firerptqc, @Dbsourceid, @Dbsourcedate, @Accuracy, @Shape)";

        // likely a nicer way to do this 
        command.Parameters.AddWithValue("@Id", Id);
        command.Parameters.AddWithValue("@X", X);
        command.Parameters.AddWithValue("@Y", Y);
        command.Parameters.AddWithValue("@Objectid", Objectid);
        command.Parameters.AddWithValue("@Globalid", Globalid);
        command.Parameters.AddWithValue("@Fireoccurid", Fireoccurid);
        command.Parameters.AddWithValue("@Cn", Cn);
        command.Parameters.AddWithValue("@Revdate", Revdate);
        command.Parameters.AddWithValue("@Firename", Firename);
        command.Parameters.AddWithValue("@Complexname", Complexname);
        command.Parameters.AddWithValue("@Fireyear", Fireyear);
        command.Parameters.AddWithValue("@Uniquefireid", Uniquefireid);
        command.Parameters.AddWithValue("@Sofirenum", Sofirenum);
        command.Parameters.AddWithValue("@Localfirenum", Localfirenum);
        command.Parameters.AddWithValue("@Securityid", Securityid);
        command.Parameters.AddWithValue("@Discoverydatetime", Discoverydatetime);
        command.Parameters.AddWithValue("@Sizeclass", Sizeclass);
        command.Parameters.AddWithValue("@Totalacres", Totalacres);
        command.Parameters.AddWithValue("@Statcause", Statcause);
        command.Parameters.AddWithValue("@Comments", Comments);
        command.Parameters.AddWithValue("@Datasource", Datasource);
        command.Parameters.AddWithValue("@Fireoutdatetime", Fireoutdatetime);
        command.Parameters.AddWithValue("@Owneragency", Owneragency);
        command.Parameters.AddWithValue("@Unitdowner", Unitdowner);
        command.Parameters.AddWithValue("@Protectionagency", Protectionagency);
        command.Parameters.AddWithValue("@Unitdprotect", Unitdprotect);
        command.Parameters.AddWithValue("@Latdd83", Latdd83);
        command.Parameters.AddWithValue("@Longdd83", Longdd83);
        command.Parameters.AddWithValue("@Firetypecategory", Firetypecategory);
        command.Parameters.AddWithValue("@Pointtype", Pointtype);
        command.Parameters.AddWithValue("@Perimiexists", Perimiexists);
        command.Parameters.AddWithValue("@Firerptqc", Firerptqc);
        command.Parameters.AddWithValue("@Dbsourceid", Dbsourceid);
        command.Parameters.AddWithValue("@Dbsourcedate", Dbsourcedate);
        command.Parameters.AddWithValue("@Accuracy", Accuracy);
        command.Parameters.AddWithValue("@Shape", Shape);

        await connection.OpenAsync();
        await command.ExecuteNonQueryAsync();
        await connection.CloseAsync();
    }
}