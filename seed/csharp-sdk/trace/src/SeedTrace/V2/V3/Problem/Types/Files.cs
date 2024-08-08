using System.Text.Json.Serialization;

#nullable enable

namespace SeedTrace.V2.V3;

public record Files
{
    [JsonPropertyName("files")]
    public IEnumerable<FileInfoV2> Files_ { get; set; } = new List<FileInfoV2>();
}
