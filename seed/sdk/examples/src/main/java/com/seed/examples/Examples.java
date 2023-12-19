/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.examples;

import com.seed.examples.core.ApiError;
import com.seed.examples.core.ClientOptions;
import com.seed.examples.core.MediaTypes;
import com.seed.examples.core.ObjectMappers;
import com.seed.examples.core.RequestOptions;
import com.seed.examples.core.Suppliers;
import com.seed.examples.file.FileClient;
import com.seed.examples.health.HealthClient;
import com.seed.examples.service.ServiceClient;
import java.io.IOException;
import java.util.function.Supplier;
import okhttp3.Headers;
import okhttp3.HttpUrl;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class Examples {
    protected final ClientOptions clientOptions;

    protected final Supplier<FileClient> fileClient;

    protected final Supplier<HealthClient> healthClient;

    protected final Supplier<ServiceClient> serviceClient;

    public Examples(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.fileClient = Suppliers.memoize(() -> new FileClient(clientOptions));
        this.healthClient = Suppliers.memoize(() -> new HealthClient(clientOptions));
        this.serviceClient = Suppliers.memoize(() -> new ServiceClient(clientOptions));
    }

    public String echo(String request) {
        return echo(request, null);
    }

    public String echo(String request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .build();
        RequestBody body;
        try {
            body = RequestBody.create(
                    ObjectMappers.JSON_MAPPER.writeValueAsBytes(request), MediaTypes.APPLICATION_JSON);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        Request okhttpRequest = new Request.Builder()
                .url(httpUrl)
                .method("POST", body)
                .headers(Headers.of(clientOptions.headers(requestOptions)))
                .addHeader("Content-Type", "application/json")
                .build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return ObjectMappers.JSON_MAPPER.readValue(response.body().string(), String.class);
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public FileClient file() {
        return this.fileClient.get();
    }

    public HealthClient health() {
        return this.healthClient.get();
    }

    public ServiceClient service() {
        return this.serviceClient.get();
    }

    public static ExamplesBuilder builder() {
        return new ExamplesBuilder();
    }
}
