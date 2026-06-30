#!/usr/bin/env python3
import sys
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <name>")
        sys.exit(1)

    name = sys.argv[1]
    current_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

    print(f"Hello {name}, right now the time is {current_time}")

if __name__ == "__main__":
    main()
