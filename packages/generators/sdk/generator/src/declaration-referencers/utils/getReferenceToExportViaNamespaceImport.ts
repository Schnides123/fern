import { Reference } from "@fern-typescript/sdk-declaration-handler";
import { SourceFile, ts } from "ts-morph";
import {
    convertExportedFilePathToFilePath,
    ExportedDirectory,
    ExportedFilePath,
} from "../../exports-manager/ExportedFilePath";
import { ImportDeclaration } from "../../imports-manager/ImportsManager";
import { getRelativePathAsModuleSpecifierTo } from "../../utils/getRelativePathAsModuleSpecifierTo";
import { ModuleSpecifier } from "../../utils/ModuleSpecifier";
import { getEntityNameOfDirectory } from "./getEntityNameOfDirectory";
import { getExpressionToDirectory } from "./getExpressionToDirectory";

export function getReferenceToExportViaNamespaceImport({
    exportedName,
    filepathToNamespaceImport,
    filepathInsideNamespaceImport,
    namespaceImport,
    addImport: addImportToFile,
    referencedIn,
    subImport = [],
    packageName,
}: {
    exportedName: string;
    filepathToNamespaceImport: ExportedFilePath;
    filepathInsideNamespaceImport: ExportedDirectory[] | ExportedFilePath | undefined;
    namespaceImport: string;
    addImport: (moduleSpecifier: ModuleSpecifier, importDeclaration: ImportDeclaration) => void;
    referencedIn: SourceFile;
    subImport?: string[];
    packageName: string;
}): Reference {
    const addImport = () => {
        addImportToFile(
            getRelativePathAsModuleSpecifierTo({
                from: referencedIn,
                to: convertExportedFilePathToFilePath(filepathToNamespaceImport),
                packageName,
            }),
            { namespaceImport }
        );
    };

    const pathToDirectoryInsideNamespaceImport =
        filepathInsideNamespaceImport != null
            ? Array.isArray(filepathInsideNamespaceImport)
                ? filepathInsideNamespaceImport
                : filepathInsideNamespaceImport.directories
            : [];

    const entityName = [exportedName, ...subImport].reduce<ts.EntityName>(
        (acc, part) => ts.factory.createQualifiedName(acc, part),
        getEntityNameOfDirectory({
            pathToDirectory: pathToDirectoryInsideNamespaceImport,
            prefix: ts.factory.createIdentifier(namespaceImport),
        })
    );

    const expression = [exportedName, ...subImport].reduce<ts.Expression>(
        (acc, part) => ts.factory.createPropertyAccessExpression(acc, part),
        getExpressionToDirectory({
            pathToDirectory: pathToDirectoryInsideNamespaceImport,
            prefix: ts.factory.createIdentifier(namespaceImport),
        })
    );

    return {
        getTypeNode: () => {
            addImport();
            return ts.factory.createTypeReferenceNode(entityName);
        },
        getEntityName: () => {
            addImport();
            return entityName;
        },
        getExpression: () => {
            addImport();
            return expression;
        },
    };
}
