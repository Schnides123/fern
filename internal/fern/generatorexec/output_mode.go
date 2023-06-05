// Generated by Fern. Do not edit.

package generatorexec

import (
	json "encoding/json"
	fmt "fmt"
)

type OutputMode struct {
	Type          string
	Publish       *GeneratorPublishConfig
	DownloadFiles any
	Github        *GithubOutputMode
}

func (o *OutputMode) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	o.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "publish":
		value := new(GeneratorPublishConfig)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		o.Publish = value
	case "downloadFiles":
		value := make(map[string]any)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		o.DownloadFiles = value
	case "github":
		value := new(GithubOutputMode)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		o.Github = value
	}
	return nil
}

func (o OutputMode) MarshalJSON() ([]byte, error) {
	switch o.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", o.Type, o)
	case "publish":
		var marshaler = struct {
			Type string `json:"type"`
			*GeneratorPublishConfig
		}{
			Type:                   o.Type,
			GeneratorPublishConfig: o.Publish,
		}
		return json.Marshal(marshaler)
	case "downloadFiles":
		var marshaler = struct {
			Type          string `json:"type"`
			DownloadFiles any    `json:"downloadFiles"`
		}{
			Type:          o.Type,
			DownloadFiles: o.DownloadFiles,
		}
		return json.Marshal(marshaler)
	case "github":
		var marshaler = struct {
			Type string `json:"type"`
			*GithubOutputMode
		}{
			Type:             o.Type,
			GithubOutputMode: o.Github,
		}
		return json.Marshal(marshaler)
	}
}

type OutputModeVisitor interface {
	VisitPublish(*GeneratorPublishConfig) error
	VisitDownloadFiles(any) error
	VisitGithub(*GithubOutputMode) error
}

func (o *OutputMode) Accept(v OutputModeVisitor) error {
	switch o.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", o.Type, o)
	case "publish":
		return v.VisitPublish(o.Publish)
	case "downloadFiles":
		return v.VisitDownloadFiles(o.DownloadFiles)
	case "github":
		return v.VisitGithub(o.Github)
	}
}
