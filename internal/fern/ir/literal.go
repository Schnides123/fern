// Generated by Fern. Do not edit.

package ir

import (
	json "encoding/json"
	fmt "fmt"
)

type Literal struct {
	Type   string
	String string
}

func (l *Literal) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	l.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "string":
		var valueUnmarshaler struct {
			String string `json:"string"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		l.String = valueUnmarshaler.String
	}
	return nil
}

func (l Literal) MarshalJSON() ([]byte, error) {
	switch l.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", l.Type, l)
	case "string":
		var marshaler = struct {
			Type   string `json:"type"`
			String string `json:"string"`
		}{
			Type:   l.Type,
			String: l.String,
		}
		return json.Marshal(marshaler)
	}
}

type LiteralVisitor interface {
	VisitString(string) error
}

func (l *Literal) Accept(v LiteralVisitor) error {
	switch l.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", l.Type, l)
	case "string":
		return v.VisitString(l.String)
	}
}
