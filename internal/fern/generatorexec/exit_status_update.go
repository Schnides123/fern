// Generated by Fern. Do not edit.

package generatorexec

import (
	json "encoding/json"
	fmt "fmt"
)

type ExitStatusUpdate struct {
	Type       string
	Successful *SuccessfulStatusUpdate
	Error      *ErrorExitStatusUpdate
}

func (e *ExitStatusUpdate) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"_type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	e.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "successful":
		value := new(SuccessfulStatusUpdate)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		e.Successful = value
	case "error":
		value := new(ErrorExitStatusUpdate)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		e.Error = value
	}
	return nil
}

func (e ExitStatusUpdate) MarshalJSON() ([]byte, error) {
	switch e.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", e.Type, e)
	case "successful":
		var marshaler = struct {
			Type string `json:"_type"`
			*SuccessfulStatusUpdate
		}{
			Type:                   e.Type,
			SuccessfulStatusUpdate: e.Successful,
		}
		return json.Marshal(marshaler)
	case "error":
		var marshaler = struct {
			Type string `json:"_type"`
			*ErrorExitStatusUpdate
		}{
			Type:                  e.Type,
			ErrorExitStatusUpdate: e.Error,
		}
		return json.Marshal(marshaler)
	}
}

type ExitStatusUpdateVisitor interface {
	VisitSuccessful(*SuccessfulStatusUpdate) error
	VisitError(*ErrorExitStatusUpdate) error
}

func (e *ExitStatusUpdate) Accept(v ExitStatusUpdateVisitor) error {
	switch e.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", e.Type, e)
	case "successful":
		return v.VisitSuccessful(e.Successful)
	case "error":
		return v.VisitError(e.Error)
	}
}
