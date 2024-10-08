/**
 * This file was auto-generated by Fern from our API Definition.
 */

import express from "express";

export abstract class SeedObjectsWithImportsError extends Error {
    constructor(public readonly errorName?: string) {
        super();
        Object.setPrototypeOf(this, SeedObjectsWithImportsError.prototype);
    }

    public abstract send(res: express.Response): Promise<void>;
}
