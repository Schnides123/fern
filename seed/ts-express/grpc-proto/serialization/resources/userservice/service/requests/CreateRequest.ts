/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../index";
import * as SeedApi from "../../../../../api/index";
import * as core from "../../../../../core";

export const CreateRequest: core.serialization.Schema<serializers.CreateRequest.Raw, SeedApi.CreateRequest> =
    core.serialization.object({
        username: core.serialization.string().optional(),
        email: core.serialization.string().optional(),
        age: core.serialization.number().optional(),
        weight: core.serialization.number().optional(),
        metadata: core.serialization.lazy(() => serializers.Metadata).optional(),
    });

export declare namespace CreateRequest {
    interface Raw {
        username?: string | null;
        email?: string | null;
        age?: number | null;
        weight?: number | null;
        metadata?: serializers.Metadata.Raw | null;
    }
}
