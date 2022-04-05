import { RelativeFilePath } from "@usebirch/compiler-commons";
import { FernSchema } from "./schemas/FernSchema";
import { SyntaxAnalysis } from "./types";

export declare namespace Validator {
    export type Result = SuccessfulResult | FailedResult;

    export interface SuccessfulResult {
        didSucceed: true;
        validatedFiles: Record<RelativeFilePath, FernSchema>;
    }

    export interface FailedResult {
        didSucceed: false;
        failures: Record<RelativeFilePath, SyntaxAnalysis.StructureValidationFailure>;
    }
}

export function validate(files: Record<RelativeFilePath, unknown>): Validator.Result {
    const validatedFiles: Record<RelativeFilePath, FernSchema> = {};
    const failures: Record<RelativeFilePath, SyntaxAnalysis.StructureValidationFailure> = {};

    for (const [relativeFilePath, parsedFileContents] of Object.entries(files)) {
        const parsed = FernSchema.safeParse(parsedFileContents);
        if (parsed.success) {
            validatedFiles[relativeFilePath] = parsed.data;
        } else {
            failures[relativeFilePath] = {
                type: SyntaxAnalysis.FailureType.STRUCTURE_VALIDATION,
                error: parsed.error,
            };
        }
    }

    if (Object.keys(failures).length > 0) {
        return {
            didSucceed: false,
            failures,
        };
    } else {
        return {
            didSucceed: true,
            validatedFiles,
        };
    }
}
