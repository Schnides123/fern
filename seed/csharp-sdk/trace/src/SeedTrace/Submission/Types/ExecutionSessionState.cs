using System.Text.Json.Serialization;

#nullable enable

namespace SeedTrace;

public record ExecutionSessionState
{
    [JsonPropertyName("lastTimeContacted")]
    public string? LastTimeContacted { get; set; }

    /// <summary>
    /// The auto-generated session id. Formatted as a uuid.
    /// </summary>
    [JsonPropertyName("sessionId")]
    public required string SessionId { get; set; }

    [JsonPropertyName("isWarmInstance")]
    public required bool IsWarmInstance { get; set; }

    [JsonPropertyName("awsTaskId")]
    public string? AwsTaskId { get; set; }

    [JsonPropertyName("language")]
    public required Language Language { get; set; }

    [JsonPropertyName("status")]
    public required ExecutionSessionStatus Status { get; set; }
}
