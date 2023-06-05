// Generated by Fern. Do not edit.

package generatorexec

import (
	json "encoding/json"
	fmt "fmt"
)

type PackageCoordinate struct {
	Type  string
	Npm   *NpmCoordinate
	Maven *MavenCoordinate
}

func (p *PackageCoordinate) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"_type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	p.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "npm":
		value := new(NpmCoordinate)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		p.Npm = value
	case "maven":
		value := new(MavenCoordinate)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		p.Maven = value
	}
	return nil
}

func (p PackageCoordinate) MarshalJSON() ([]byte, error) {
	switch p.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", p.Type, p)
	case "npm":
		var marshaler = struct {
			Type string `json:"_type"`
			*NpmCoordinate
		}{
			Type:          p.Type,
			NpmCoordinate: p.Npm,
		}
		return json.Marshal(marshaler)
	case "maven":
		var marshaler = struct {
			Type string `json:"_type"`
			*MavenCoordinate
		}{
			Type:            p.Type,
			MavenCoordinate: p.Maven,
		}
		return json.Marshal(marshaler)
	}
}

type PackageCoordinateVisitor interface {
	VisitNpm(*NpmCoordinate) error
	VisitMaven(*MavenCoordinate) error
}

func (p *PackageCoordinate) Accept(v PackageCoordinateVisitor) error {
	switch p.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", p.Type, p)
	case "npm":
		return v.VisitNpm(p.Npm)
	case "maven":
		return v.VisitMaven(p.Maven)
	}
}
