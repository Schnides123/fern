// Generated by Fern. Do not edit.

package api

import (
	context "context"
	errors "errors"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/bearer/fixtures/core"
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
	bytes, err := io.ReadAll(body)
	if err != nil {
		return err
	}
	return errors.New(string(bytes))
}

func (g *getEndpoint) Call(ctx context.Context) (string, error) {
	endpointURL := g.url
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
