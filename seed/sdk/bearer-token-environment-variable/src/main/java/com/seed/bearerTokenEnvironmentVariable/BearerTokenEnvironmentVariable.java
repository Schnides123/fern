/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.bearerTokenEnvironmentVariable;

import com.seed.bearerTokenEnvironmentVariable.core.ClientOptions;
import com.seed.bearerTokenEnvironmentVariable.core.Suppliers;
import com.seed.bearerTokenEnvironmentVariable.service.ServiceClient;
import java.util.function.Supplier;

public class BearerTokenEnvironmentVariable {
    protected final ClientOptions clientOptions;

    protected final Supplier<ServiceClient> serviceClient;

    public BearerTokenEnvironmentVariable(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.serviceClient = Suppliers.memoize(() -> new ServiceClient(clientOptions));
    }

    public ServiceClient service() {
        return this.serviceClient.get();
    }

    public static BearerTokenEnvironmentVariableBuilder builder() {
        return new BearerTokenEnvironmentVariableBuilder();
    }
}
