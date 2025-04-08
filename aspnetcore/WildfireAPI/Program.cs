using System.Text.Json;
using MySqlConnector;
using WildfireAPI;

var builder = WebApplication.CreateBuilder(args);

string? MYSQL_CONNECTION_STRING = builder.Configuration.GetConnectionString("Docker");
if (MYSQL_CONNECTION_STRING is null)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Write("warning: ");
    Console.ForegroundColor = ConsoleColor.White;
    Console.Write("No connection string found\n");
}

builder.Services.AddMySqlDataSource(MYSQL_CONNECTION_STRING!);

var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/wildfires", async (int? limit, int? offset) =>
{
    using var connection = new MySqlConnection(MYSQL_CONNECTION_STRING);
    using var command = connection.CreateCommand();
    command.CommandText = "SELECT * FROM WildfireEntry";
    // adds limit and offset if both are present, ignores otherwise
    if (limit is not null && offset is not null)
    {
        command.CommandText += @" LIMIT @limit OFFSET @offset";
        command.Parameters.AddWithValue("@limit", limit);
        command.Parameters.AddWithValue("@offset", offset);
    }
    command.CommandText += ";";

    await connection.OpenAsync();
    using var reader = await command.ExecuteReaderAsync();
    List<WildfireEntry> entries = await WildfireEntry.ContructEntriesFromReader(reader);
    await connection.CloseAsync();
    return Results.Ok(entries);
});

app.MapPost("/wildfires/addentry", async (Stream requestBody) =>
{
    using var reader = new StreamReader(requestBody, leaveOpen: false);
    var jsonString = await reader.ReadToEndAsync();

    WildfireEntry? entry = JsonSerializer.Deserialize<WildfireEntry>(jsonString);
    if (entry is null)
    {
        return Results.BadRequest("Missing or invalid field");
    }
    try
    {
        await entry.InsertWildfireEntry(MYSQL_CONNECTION_STRING);
        return Results.Created();

    }
    catch (Exception)
    {
        return Results.InternalServerError("Too many connections");
    }
});

app.Run();