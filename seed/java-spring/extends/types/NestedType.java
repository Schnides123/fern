/**
 * This file was auto-generated by Fern from our API Definition.
 */

package types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(
    builder = NestedType.Builder.class
)
public final class NestedType implements IJson {
  private final String raw;

  private final String docs;

  private final String name;

  private NestedType(String raw, String docs, String name) {
    this.raw = raw;
    this.docs = docs;
    this.name = name;
  }

  @JsonProperty("raw")
  @java.lang.Override
  public String getRaw() {
    return raw;
  }

  @JsonProperty("docs")
  @java.lang.Override
  public String getDocs() {
    return docs;
  }

  @JsonProperty("name")
  public String getName() {
    return name;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof NestedType && equalTo((NestedType) other);
  }

  private boolean equalTo(NestedType other) {
    return raw.equals(other.raw) && docs.equals(other.docs) && name.equals(other.name);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.raw, this.docs, this.name);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static RawStage builder() {
    return new Builder();
  }

  public interface RawStage {
    DocsStage raw(String raw);

    Builder from(NestedType other);
  }

  public interface DocsStage {
    NameStage docs(String docs);
  }

  public interface NameStage {
    _FinalStage name(String name);
  }

  public interface _FinalStage {
    NestedType build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements RawStage, DocsStage, NameStage, _FinalStage {
    private String raw;

    private String docs;

    private String name;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(NestedType other) {
      raw(other.getRaw());
      docs(other.getDocs());
      name(other.getName());
      return this;
    }

    @java.lang.Override
    @JsonSetter("raw")
    public DocsStage raw(String raw) {
      this.raw = raw;
      return this;
    }

    @java.lang.Override
    @JsonSetter("docs")
    public NameStage docs(String docs) {
      this.docs = docs;
      return this;
    }

    @java.lang.Override
    @JsonSetter("name")
    public _FinalStage name(String name) {
      this.name = name;
      return this;
    }

    @java.lang.Override
    public NestedType build() {
      return new NestedType(raw, docs, name);
    }
  }
}