/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";
export declare const KeyValuePair: core.serialization.ObjectSchema<serializers.KeyValuePair.Raw, SeedTrace.KeyValuePair>;
export declare namespace KeyValuePair {
    interface Raw {
        key: serializers.VariableValue.Raw;
        value: serializers.VariableValue.Raw;
    }
}