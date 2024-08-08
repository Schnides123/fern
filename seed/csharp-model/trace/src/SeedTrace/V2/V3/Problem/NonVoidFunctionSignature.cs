using System.Text.Json.Serialization;

#nullable enable

namespace SeedTrace.V2.V3;

public record NonVoidFunctionSignature
{
    [JsonPropertyName("parameters")]
    public IEnumerable<Parameter> Parameters { get; set; } = new List<Parameter>();

    [JsonPropertyName("returnType")]
    public required object ReturnType { get; set; }
}
