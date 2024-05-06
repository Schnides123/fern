/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const Response: core.serialization.Schema<
    serializers.sysprop.getNumWarmInstances.Response.Raw,
    Record<SeedTrace.Language, number | undefined>
> = core.serialization.record(
    core.serialization.lazy(async () => (await import("../../..")).Language),
    core.serialization.number().optional()
);

export declare namespace Response {
    type Raw = Record<serializers.Language.Raw, number | null | undefined>;
}