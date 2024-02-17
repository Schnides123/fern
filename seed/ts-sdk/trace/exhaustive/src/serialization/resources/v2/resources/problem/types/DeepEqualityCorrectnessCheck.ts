/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../..";
import * as SeedTrace from "../../../../../../api";
import * as core from "../../../../../../core";

export const DeepEqualityCorrectnessCheck: core.serialization.ObjectSchema<
    serializers.v2.DeepEqualityCorrectnessCheck.Raw,
    SeedTrace.v2.DeepEqualityCorrectnessCheck
> = core.serialization.object({
    expectedValueParameterId: core.serialization.lazy(async () => (await import("../../../../..")).v2.ParameterId),
});

export declare namespace DeepEqualityCorrectnessCheck {
    interface Raw {
        expectedValueParameterId: serializers.v2.ParameterId.Raw;
    }
}