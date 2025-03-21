using Microsoft.AspNetCore.Http.HttpResults;
using MySqlConnector;
using WildfireAPI;

var builder = WebApplication.CreateBuilder(args);

string? MYSQL_CONNECTION_STRING = builder.Configuration.GetConnectionString("Custom");
builder.Services.AddMySqlDataSource(MYSQL_CONNECTION_STRING!);

var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/wildfires", async (int? limit, int? offset) =>
{
    using var connection = new MySqlConnection(MYSQL_CONNECTION_STRING);
    await connection.OpenAsync();

    string query = "SELECT * FROM WildfireEntry";
    // adds limit and offset if both are present, ignores otherwise
    if (limit is not null && offset is not null)
        query += $" LIMIT {limit} OFFSET {offset}";
    using var command = new MySqlCommand(query + ";", connection);

    using var reader = await command.ExecuteReaderAsync();
    return await WildfireEntry.ContructEntriesFromReader(reader);
});

app.MapPost("/wildifres/addentry", async () =>
{
    return "post";
});

app.Run();
