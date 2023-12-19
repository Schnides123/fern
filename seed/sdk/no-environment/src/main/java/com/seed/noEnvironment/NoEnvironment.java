/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.noEnvironment;

import com.seed.noEnvironment.core.ClientOptions;
import com.seed.noEnvironment.core.Suppliers;
import com.seed.noEnvironment.dummy.DummyClient;
import java.util.function.Supplier;

public class NoEnvironment {
    protected final ClientOptions clientOptions;

    protected final Supplier<DummyClient> dummyClient;

    public NoEnvironment(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.dummyClient = Suppliers.memoize(() -> new DummyClient(clientOptions));
    }

    public DummyClient dummy() {
        return this.dummyClient.get();
    }

    public static NoEnvironmentBuilder builder() {
        return new NoEnvironmentBuilder();
    }
}
