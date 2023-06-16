// Generated by Fern. Do not edit.

package api

import (
	context "context"
	json "encoding/json"
	errors "errors"
	fmt "fmt"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/error/fixtures/core"
	io "io"
	http "net/http"
)

type UserClient interface{}

type getEndpoint struct {
	url    string
	client core.HTTPClient
}

func newgetEndpoint(url string, client core.HTTPClient) *getEndpoint {
	return &getEndpoint{
		url:    url,
		client: client,
	}
}

func (g *getEndpoint) decodeError(statusCode int, body io.Reader) error {
	decoder := json.NewDecoder(body)
	switch statusCode {
	case 404:
		value := new(UserNotFoundError)
		if err := decoder.Decode(value); err != nil {
			return err
		}
		value.StatusCode = statusCode
		return value
	case 501:
		value := new(NotImplementedError)
		if err := decoder.Decode(value); err != nil {
			return err
		}
		value.StatusCode = statusCode
		return value
	case 418:
		value := new(TeapotError)
		if err := decoder.Decode(value); err != nil {
			return err
		}
		value.StatusCode = statusCode
		return value
	case 426:
		value := new(UpgradeError)
		if err := decoder.Decode(value); err != nil {
			return err
		}
		value.StatusCode = statusCode
		return value
	}
	bytes, err := io.ReadAll(body)
	if err != nil {
		return err
	}
	return errors.New(string(bytes))
}

func (g *getEndpoint) Call(ctx context.Context, id string) (string, error) {
	endpointURL := fmt.Sprintf(g.url, id)
	var response string
	if err := core.DoRequest(
		ctx,
		g.client,
		endpointURL,
		http.MethodGet,
		nil,
		response,
		nil,
		g.decodeError,
	); err != nil {
		return response, err
	}
	return response, nil
}

type updateEndpoint struct {
	url    string
	client core.HTTPClient
}

func newupdateEndpoint(url string, client core.HTTPClient) *updateEndpoint {
	return &updateEndpoint{
		url:    url,
		client: client,
	}
}

func (u *updateEndpoint) decodeError(statusCode int, body io.Reader) error {
	decoder := json.NewDecoder(body)
	switch statusCode {
	case 426:
		value := new(UpgradeError)
		if err := decoder.Decode(value); err != nil {
			return err
		}
		value.StatusCode = statusCode
		return value
	}
	bytes, err := io.ReadAll(body)
	if err != nil {
		return err
	}
	return errors.New(string(bytes))
}

func (u *updateEndpoint) Call(ctx context.Context, id string) (string, error) {
	endpointURL := fmt.Sprintf(u.url, id)
	var response string
	if err := core.DoRequest(
		ctx,
		u.client,
		endpointURL,
		http.MethodPost,
		nil,
		response,
		nil,
		u.decodeError,
	); err != nil {
		return response, err
	}
	return response, nil
}
