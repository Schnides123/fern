using System.Text.Json.Serialization;
using Proto = Data.V1.Grpc;

#nullable enable

namespace SeedApi;

public record UploadResponse
{
    [JsonPropertyName("count")]
    public uint? Count { get; set; }

    /// <summary>
    /// Maps the UploadResponse type into its Protobuf-equivalent representation.
    /// </summary>
    internal Proto.UploadResponse ToProto()
    {
        var result = new Proto.UploadResponse();
        if (Count != null)
        {
            result.Count = Count ?? 0U;
        }
        return result;
    }

    /// <summary>
    /// Returns a new UploadResponse type from its Protobuf-equivalent representation.
    /// </summary>
    internal static UploadResponse FromProto(Proto.UploadResponse value)
    {
        return new UploadResponse { Count = value.Count };
    }
}
