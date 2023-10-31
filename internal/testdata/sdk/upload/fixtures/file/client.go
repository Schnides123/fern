// This file was auto-generated by Fern from our API Definition.

package file

import (
	bytes "bytes"
	context "context"
	fmt "fmt"
	fixtures "github.com/fern-api/fern-go/internal/testdata/sdk/upload/fixtures"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/upload/fixtures/core"
	io "io"
	multipart "mime/multipart"
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

func (c *Client) Upload(ctx context.Context, file io.Reader, request *fixtures.UploadRequest) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := baseURL + "/" + "file/upload"

	var response string
	requestBuffer := bytes.NewBuffer(nil)
	writer := multipart.NewWriter(requestBuffer)
	fileFilename := "file_filename"
	if named, ok := file.(interface{ Name() string }); ok {
		fileFilename = named.Name()
	}
	filePart, err := writer.CreateFormFile("file", fileFilename)
	if err != nil {
		return "", err
	}
	if _, err := io.Copy(filePart, file); err != nil {
		return "", err
	}
	if err := writer.WriteField("fern", fmt.Sprintf("%v", "fern")); err != nil {
		return "", err
	}
	if err := writer.WriteField("status", fmt.Sprintf("%v", request.Status)); err != nil {
		return "", err
	}
	if err := writer.Close(); err != nil {
		return "", err
	}
	c.header.Set("Content-Type", writer.FormDataContentType())

	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  c.header,
			Request:  requestBuffer,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) UploadSimple(ctx context.Context, file io.Reader) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := baseURL + "/" + "file/upload-simple"

	var response string
	requestBuffer := bytes.NewBuffer(nil)
	writer := multipart.NewWriter(requestBuffer)
	fileFilename := "file_filename"
	if named, ok := file.(interface{ Name() string }); ok {
		fileFilename = named.Name()
	}
	filePart, err := writer.CreateFormFile("file", fileFilename)
	if err != nil {
		return "", err
	}
	if _, err := io.Copy(filePart, file); err != nil {
		return "", err
	}
	if err := writer.Close(); err != nil {
		return "", err
	}
	c.header.Set("Content-Type", writer.FormDataContentType())

	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  c.header,
			Request:  requestBuffer,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}

func (c *Client) UploadMultiple(ctx context.Context, file io.Reader, optionalFile io.Reader, request *fixtures.UploadMultiRequest) (string, error) {
	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	endpointURL := baseURL + "/" + "file/upload-multi"

	var response string
	requestBuffer := bytes.NewBuffer(nil)
	writer := multipart.NewWriter(requestBuffer)
	fileFilename := "file_filename"
	if named, ok := file.(interface{ Name() string }); ok {
		fileFilename = named.Name()
	}
	filePart, err := writer.CreateFormFile("file", fileFilename)
	if err != nil {
		return "", err
	}
	if _, err := io.Copy(filePart, file); err != nil {
		return "", err
	}
	if optionalFile != nil {
		optionalFileFilename := "optionalFile_filename"
		if named, ok := optionalFile.(interface{ Name() string }); ok {
			optionalFileFilename = named.Name()
		}
		optionalFilePart, err := writer.CreateFormFile("optionalFile", optionalFileFilename)
		if err != nil {
			return "", err
		}
		if _, err := io.Copy(optionalFilePart, optionalFile); err != nil {
			return "", err
		}
	}
	if err := writer.WriteField("status", fmt.Sprintf("%v", request.Status)); err != nil {
		return "", err
	}
	if err := writer.Close(); err != nil {
		return "", err
	}
	c.header.Set("Content-Type", writer.FormDataContentType())

	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodPost,
			Headers:  c.header,
			Request:  requestBuffer,
			Response: &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}
