4-scripting
Two simple scripts — one in Bash, one in Python — that each take a name as a
command-line argument and print:
```
Hello <name>, right now the time is <current date and time based on timezone>
```
Files
`hello.sh` — Bash version
`hello.py` — Python version
---
Bash script (`hello.sh`)
Bash is an interpreted language. There is no compilation step — the
`bash` interpreter reads and executes the script's commands directly, line
by line, at the moment you run it.
How to run it
Make the script executable (only needed once):
```bash
   chmod +x hello.sh
   ```
Run it, passing a name:
```bash
   ./hello.sh Sooraj
   ```
Or, without making it executable, run it directly with the interpreter:
```bash
   bash hello.sh Sooraj
   ```
Example output
```
Hello Sooraj, right now the time is 2026-07-01 14:32:10 IST (+0530)
```
The time shown uses the local timezone configured on the machine running
the script (via the `date` command).
---
Python script (`hello.py`)
Python is an interpreted language. The CPython interpreter reads and
runs the source file directly at runtime — there's no separate compile
step the user has to perform (CPython compiles to bytecode internally and
automatically, but that's an implementation detail, not a manual build
step like with C or Java).
How to run it
Ensure Python 3 is installed:
```bash
   python3 --version
   ```
Run the script, passing a name:
```bash
   python3 hello.py Sooraj
   ```
Example output
```
Hello Sooraj, right now the time is 2026-07-01 14:32:11 IST (+0530)
```
The script uses Python's `datetime.now().astimezone()` to get a
timezone-aware timestamp based on the system's local timezone.
