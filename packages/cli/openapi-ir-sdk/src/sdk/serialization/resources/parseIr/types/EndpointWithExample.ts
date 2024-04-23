/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const EndpointWithExample: core.serialization.ObjectSchema<
    serializers.EndpointWithExample.Raw,
    FernOpenapiIr.EndpointWithExample
> = core.serialization
    .objectWithoutOptionalProperties({
        authed: core.serialization.boolean(),
        internal: core.serialization.boolean().optional(),
        method: core.serialization.lazy(async () => (await import("../../..")).HttpMethod),
        availability: core.serialization.lazy(async () => (await import("../../..")).EndpointAvailability).optional(),
        audiences: core.serialization.list(core.serialization.string()),
        path: core.serialization.string(),
        summary: core.serialization.string().optional(),
        operationId: core.serialization.string().optional(),
        tags: core.serialization.list(core.serialization.lazy(async () => (await import("../../..")).TagId)),
        pathParameters: core.serialization.list(
            core.serialization.lazyObject(async () => (await import("../../..")).PathParameterWithExample)
        ),
        queryParameters: core.serialization.list(
            core.serialization.lazyObject(async () => (await import("../../..")).QueryParameterWithExample)
        ),
        headers: core.serialization.list(
            core.serialization.lazyObject(async () => (await import("../../..")).HeaderWithExample)
        ),
        sdkName: core.serialization.lazyObject(async () => (await import("../../..")).EndpointSdkName).optional(),
        generatedRequestName: core.serialization.string(),
        requestNameOverride: core.serialization.string().optional(),
        request: core.serialization.lazy(async () => (await import("../../..")).RequestWithExample).optional(),
        response: core.serialization.lazy(async () => (await import("../../..")).ResponseWithExample).optional(),
        errors: core.serialization.record(
            core.serialization.lazy(async () => (await import("../../..")).StatusCode),
            core.serialization.lazyObject(async () => (await import("../../..")).HttpErrorWithExample)
        ),
        server: core.serialization.list(core.serialization.lazyObject(async () => (await import("../../..")).Server)),
        examples: core.serialization.list(
            core.serialization.lazy(async () => (await import("../../..")).EndpointExample)
        ),
    })
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithDescription));

export declare namespace EndpointWithExample {
    interface Raw extends serializers.WithDescription.Raw {
        authed: boolean;
        internal?: boolean | null;
        method: serializers.HttpMethod.Raw;
        availability?: serializers.EndpointAvailability.Raw | null;
        audiences: string[];
        path: string;
        summary?: string | null;
        operationId?: string | null;
        tags: serializers.TagId.Raw[];
        pathParameters: serializers.PathParameterWithExample.Raw[];
        queryParameters: serializers.QueryParameterWithExample.Raw[];
        headers: serializers.HeaderWithExample.Raw[];
        sdkName?: serializers.EndpointSdkName.Raw | null;
        generatedRequestName: string;
        requestNameOverride?: string | null;
        request?: serializers.RequestWithExample.Raw | null;
        response?: serializers.ResponseWithExample.Raw | null;
        errors: Record<serializers.StatusCode.Raw, serializers.HttpErrorWithExample.Raw>;
        server: serializers.Server.Raw[];
        examples: serializers.EndpointExample.Raw[];
    }
}
