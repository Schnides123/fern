// This file was auto-generated by Fern from our API Definition.

package literal

import (
	json "encoding/json"
	fmt "fmt"
	core "github.com/literal/fern/core"
)

type ATopLevelLiteral struct {
	NestedLiteral *ANestedLiteral `json:"nestedLiteral,omitempty" url:"nestedLiteral,omitempty"`

	extraProperties map[string]interface{}
}

func (a *ATopLevelLiteral) GetExtraProperties() map[string]interface{} {
	return a.extraProperties
}

func (a *ATopLevelLiteral) UnmarshalJSON(data []byte) error {
	type unmarshaler ATopLevelLiteral
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*a = ATopLevelLiteral(value)

	extraProperties, err := core.ExtractExtraProperties(data, *a)
	if err != nil {
		return err
	}
	a.extraProperties = extraProperties

	return nil
}

func (a *ATopLevelLiteral) String() string {
	if value, err := core.StringifyJSON(a); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", a)
}

type SomeAliasedLiteral = string
