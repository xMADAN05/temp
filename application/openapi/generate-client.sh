#!/bin/bash

# OpenAPI Client Code Generator Script

# Check if required tools are installed
command -v openapi-generator-cli >/dev/null 2>&1 || { 
    echo "OpenAPI Generator CLI is not installed. Please install it first:"
    echo "npm install @openapitools/openapi-generator-cli -g"
    exit 1
}

# Usage function
usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -f, --file         Path to OpenAPI specification YAML file (required)"
    echo "  -l, --language     Target programming language (default: python)"
    echo "  -o, --output       Output directory for generated code (default: ./generated-client)"
    echo "  -p, --package      Package/group name for the client library"
    echo "  -v, --version      Package version (default: 0.1.0)"
    echo "  -h, --help         Show this help message"
    echo ""
    echo "Example:"
    echo "$0 -f openapi-spec.yaml -l python -o ./my-client -p mycompany.services -v 1.0.0"
}

# Default values
LANGUAGE="python"
OUTPUT_DIR="./generated-client"
VERSION="0.1.0"
PACKAGE=""
SPEC_FILE=""

# Parse command line arguments
ARGS=$(getopt -o f:l:o:p:v:h --long file:,language:,output:,package:,version:,help -n "$0" -- "$@")

if [ $? -ne 0 ]; then
    usage
    exit 1
fi

eval set -- "$ARGS"

while true; do
    case "$1" in
        -f|--file)
            SPEC_FILE="$2"
            shift 2
            ;;
        -l|--language)
            LANGUAGE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -p|--package)
            PACKAGE="$2"
            shift 2
            ;;
        -v|--version)
            VERSION="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Internal error!"
            exit 1
            ;;
    esac
done

# Validate required parameters
if [ -z "$SPEC_FILE" ]; then
    echo "Error: OpenAPI specification file is required"
    usage
    exit 1
fi

# Validate file exists
if [ ! -f "$SPEC_FILE" ]; then
    echo "Error: Specification file '$SPEC_FILE' not found"
    exit 1
fi

# Prepare additional properties
ADDITIONAL_PROPERTIES=""
if [ -n "$PACKAGE" ]; then
    ADDITIONAL_PROPERTIES="--additional-properties=packageName=$PACKAGE"
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Generate client code
echo "Generating $LANGUAGE client from $SPEC_FILE..."
echo "Output Directory: $OUTPUT_DIR"
echo "Package Version: $VERSION"

openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g "$LANGUAGE" \
    -o "$OUTPUT_DIR" \
    --additional-properties=packageVersion="$VERSION" \
    $ADDITIONAL_PROPERTIES

# Check generation result
if [ $? -eq 0 ]; then
    echo "Client code generated successfully in $OUTPUT_DIR"
else
    echo "Error generating client code"
    exit 1
fi