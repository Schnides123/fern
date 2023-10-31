// This file was auto-generated by Fern from our API Definition.

package user

import (
	context "context"
	fmt "fmt"
	fixtures "github.com/fern-api/fern-go/internal/testdata/sdk/optional-response/fixtures"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/optional-response/fixtures/core"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header
}

func NewClient(opts ...core.ClientOption) *Client {
	options := core.NewClientOptions()
	for _, opt := range opts {
		opt(options)
	}
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
	}
}

func (c *Client) GetName(ctx context.Context, userId string) (*string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/name", userId)

	var response *string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:                endpointURL,
			Method:             http.MethodGet,
			Headers:            c.header,
			Response:           &response,
			ResponseIsOptional: true,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}

func (c *Client) GetUser(ctx context.Context, userId string) (*fixtures.User, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v", userId)

	var response *fixtures.User
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:                endpointURL,
			Method:             http.MethodGet,
			Headers:            c.header,
			Response:           &response,
			ResponseIsOptional: true,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}
