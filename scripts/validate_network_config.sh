#!/bin/bash

CONFIG_FILE="config/network.conf"
FAILURES=0

echo "===================================="
echo " Network Configuration Validation"
echo "===================================="

if [ ! -f "$CONFIG_FILE" ]; then
    echo "FAIL: Configuration file missing"
    exit 1
fi

echo "PASS: Configuration file exists"

if grep -Eq '^DNS_PRIMARY=[^[:space:]]+$' "$CONFIG_FILE"; then
    echo "PASS: Primary DNS configured"
else
    echo "FAIL: Primary DNS missing"
    FAILURES=$((FAILURES + 1))
fi

if grep -Eq '^DNS_SECONDARY=[^[:space:]]+$' "$CONFIG_FILE"; then
    echo "PASS: Secondary DNS configured"
else
    echo "FAIL: Secondary DNS missing"
    FAILURES=$((FAILURES + 1))
fi

if grep -Eqi '^MANAGEMENT_PROTOCOL=SSH$' "$CONFIG_FILE"; then
    echo "PASS: SSH management configured"
else
    echo "FAIL: SSH management not configured"
    FAILURES=$((FAILURES + 1))
fi

echo "===================================="

if [ "$FAILURES" -eq 0 ]; then
    echo "VALIDATION SUCCESSFUL"
    exit 0
else
    echo "VALIDATION FAILED: $FAILURES issue(s)"
    exit 1
fi
