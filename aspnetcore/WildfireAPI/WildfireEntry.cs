using MySqlConnector;

namespace WildfireAPI;
public class WildfireEntry
{
    public required int Id { get; set; }
    public float? X { get; set; }
    public float? Y { get; set; }
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
    public float? Totalacres { get; set; }
    public string? Statcause { get; set; }
    public string? Comments { get; set; }
    public int? Datasource { get; set; }
    public string? Fireoutdatetime { get; set; }
    public string? Owneragency { get; set; }
    public string? Unitdowner { get; set; }
    public string? Protectionagency { get; set; }
    public string? Unitdprotect { get; set; }
    public float? Latdd83 { get; set; }
    public float? Longdd83 { get; set; }
    public string? Firetypecaategory { get; set; }
    public string? Pointtype { get; set; }
    public string? Perimiexists { get; set; }
    public string? Firerptqc { get; set; }
    public int? Dbsourceid { get; set; }
    public string? Dbsourcedate { get; set; }
    public int? Accuracy { get; set; }
    public string? Shape { get; set; }

    public static List<WildfireEntry> ContructEntries(MySqlDataReader reader)
    {
        List<WildfireEntry> entries = [];



        return entries;
    }
}