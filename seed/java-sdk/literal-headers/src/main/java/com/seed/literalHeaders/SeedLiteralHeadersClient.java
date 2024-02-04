/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.literalHeaders;

import com.seed.literalHeaders.core.ClientOptions;
import com.seed.literalHeaders.core.Suppliers;
import com.seed.literalHeaders.resources.noheaders.NoHeadersClient;
import com.seed.literalHeaders.resources.onlyliteralheaders.OnlyLiteralHeadersClient;
import com.seed.literalHeaders.resources.withnonliteralheaders.WithNonLiteralHeadersClient;
import java.util.function.Supplier;

public class SeedLiteralHeadersClient {
    protected final ClientOptions clientOptions;

    protected final Supplier<NoHeadersClient> noHeadersClient;

    protected final Supplier<OnlyLiteralHeadersClient> onlyLiteralHeadersClient;

    protected final Supplier<WithNonLiteralHeadersClient> withNonLiteralHeadersClient;

    public SeedLiteralHeadersClient(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.noHeadersClient = Suppliers.memoize(() -> new NoHeadersClient(clientOptions));
        this.onlyLiteralHeadersClient = Suppliers.memoize(() -> new OnlyLiteralHeadersClient(clientOptions));
        this.withNonLiteralHeadersClient = Suppliers.memoize(() -> new WithNonLiteralHeadersClient(clientOptions));
    }

    public NoHeadersClient noHeaders() {
        return this.noHeadersClient.get();
    }

    public OnlyLiteralHeadersClient onlyLiteralHeaders() {
        return this.onlyLiteralHeadersClient.get();
    }

    public WithNonLiteralHeadersClient withNonLiteralHeaders() {
        return this.withNonLiteralHeadersClient.get();
    }

    public static SeedLiteralHeadersClientBuilder builder() {
        return new SeedLiteralHeadersClientBuilder();
    }
}