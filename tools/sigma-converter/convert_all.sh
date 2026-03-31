#!/bin/bash
SIGMA_DIR="/rules/sigma"
OUTPUT_DIR="/rules/elastic"
mkdir -p "$OUTPUT_DIR"

failed=0

for rule in "$SIGMA_DIR"/*.yml; do
    name=$(basename "$rule" .yml)
    echo "[*] Converting: $name"

    if ! sigma convert -t lucene -p ecs_zeek_beats "$rule" > "$OUTPUT_DIR/${name}.lucene" 2>&1; then
        echo "[!] FAILED (lucene): $name"
        cat "$OUTPUT_DIR/${name}.lucene"
        failed=1
    else
        echo "[+] lucene OK: $name"
    fi

    if ! sigma convert -t eql -p ecs_zeek_beats "$rule" > "$OUTPUT_DIR/${name}.eql" 2>&1; then
        echo "[!] FAILED (eql): $name"
        cat "$OUTPUT_DIR/${name}.eql"
        failed=1
    else
        echo "[+] eql OK: $name"
    fi

done

exit $failed
