import { Writer } from "./Writer";

type Namespace = string;

export abstract class AstNode {
    /**
     * Every AST node knows how to write itself to a string.
     */
    public abstract write(writer: Writer): void;

    /**
     * Writes the node to a string.
     */
    public toString(namespace: string, allBaseNamespaces: Set<string>, rootNamespace: string): string {
        const writer = new Writer({ namespace, allBaseNamespaces, rootNamespace });
        this.write(writer);
        return writer.toString();
    }
}
