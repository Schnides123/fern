"use strict";
/**
 * This file was auto-generated by Fern from our API Definition.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.SeedExtendsError = void 0;
class SeedExtendsError extends Error {
    constructor(errorName) {
        super();
        this.errorName = errorName;
        Object.setPrototypeOf(this, SeedExtendsError.prototype);
    }
}
exports.SeedExtendsError = SeedExtendsError;