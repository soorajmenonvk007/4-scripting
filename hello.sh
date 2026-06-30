#! /bin/bash


name="$1"

if [ -z "$name" ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

current_time=$(date "+%Y-%m-%d %H:%M:%S %Z")

echo "Hello $name, right now the time is $current_time"
