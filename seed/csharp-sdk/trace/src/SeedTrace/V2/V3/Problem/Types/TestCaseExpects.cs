using System.Text.Json.Serialization;
using SeedTrace.Core;

#nullable enable

namespace SeedTrace.V2.V3;

public record TestCaseExpects
{
    [JsonPropertyName("expectedStdout")]
    public string? ExpectedStdout { get; set; }

    public override string ToString()
    {
        return JsonUtils.Serialize(this);
    }
}
