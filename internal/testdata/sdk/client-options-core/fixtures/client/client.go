// This file was auto-generated by Fern from our API Definition.

package client

import (
	core "github.com/fern-api/fern-go/internal/testdata/sdk/client-options-core/fixtures/core"
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
