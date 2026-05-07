var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// CORS (important pour Angular)
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAngular",
        policy =>
        {
            policy
                .AllowAnyOrigin()
                .AllowAnyHeader()
                .AllowAnyMethod();
        });
});

var app = builder.Build();

app.UseCors("AllowAngular");

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// Endpoint calculatrice
app.MapPost("/calculate", (CalculationRequest req) =>
{
    double result = req.Operation switch
    {
        "+" => req.A + req.B,
        "-" => req.A - req.B,
        "*" => req.A * req.B,
        "/" => req.B != 0 ? req.A / req.B : 0,
        _ => 0
    };

    return Results.Ok(new { result });
})
.WithName("postCalculateAngular")
.WithOpenApi();

app.MapGet("/test", () =>
{
    return Results.Ok(new { message = "Connexion reussie" });
})
.WithName("getTest")
.WithOpenApi();

app.Run();

// DTO (objet reçu depuis Angular)
public record CalculationRequest(double A, double B, string Operation);