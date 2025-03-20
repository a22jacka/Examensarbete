var builder = WebApplication.CreateBuilder(args);

string? MYSQL_CONNECTION_STRING = builder.Configuration.GetConnectionString("Custom");

var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/wildfires", async () =>
{
    return "wah";
});

app.Run();
