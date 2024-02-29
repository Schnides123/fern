/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernDocsConfig from "../../../../api";
import * as core from "../../../../core";

export const FontConfig: core.serialization.ObjectSchema<serializers.FontConfig.Raw, FernDocsConfig.FontConfig> =
    core.serialization.object({
        name: core.serialization.string().optional(),
        path: core.serialization.string().optional(),
        weight: core.serialization.string().optional(),
        style: core.serialization.lazy(async () => (await import("../../..")).FontStyle).optional(),
        paths: core.serialization
            .list(core.serialization.lazy(async () => (await import("../../..")).FontConfigPath))
            .optional(),
        display: core.serialization.lazy(async () => (await import("../../..")).FontDisplay).optional(),
        fallback: core.serialization.list(core.serialization.string()).optional(),
        fontVariationSettings: core.serialization.property(
            "font-variation-settings",
            core.serialization.string().optional()
        ),
    });

export declare namespace FontConfig {
    interface Raw {
        name?: string | null;
        path?: string | null;
        weight?: string | null;
        style?: serializers.FontStyle.Raw | null;
        paths?: serializers.FontConfigPath.Raw[] | null;
        display?: serializers.FontDisplay.Raw | null;
        fallback?: string[] | null;
        "font-variation-settings"?: string | null;
    }
}