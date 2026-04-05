# py-fim: File Integrity Monitoring using Python

A local File Integrity Monitoring (FIM) tool.

Features:
* Multi-Directory Support: Track multiple unrelated folders in a single baseline.json library.
* SHA-256 Integrity: High-collision-resistance hashing to ensure even a single-bit change is detected.
* Set-Theory Diffing: Efficiently identifies Added, Removed, and Modified files using Python sets.

1. Prerequisites

This project uses uv for lightning-fast dependency management and execution. If you don't have it yet:
```
Bash

curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Installation

Clone the repository and enter the project directory:
```
Bash

git clone https://github.com/HCMacaneiro/py-fim
cd py-fim
```
3. Usage

Run the monitor using uv run. The tool requires a flag and a target directory path.

Create or Update a Baseline (-c)
This scans the directory and saves (or overwrites) the current state in the baseline.json.
```
Bash

uv run main.py -c /path/to/monitor
```

Generate an Integrity Report (-r)
Compares the current files against the saved baseline and reports any drift.
```
Bash

uv run main.py -r /path/to/monitor
```

🛠️ Project Structure

    main.py: The CLI entry point and execution logic.

    engine.py: Contains the Scanner class responsible for file discovery.

    data.py: Handles JSON persistence (Baseline) and change analysis (Diff).

    models.py: Defines the FileState object and SHA-256 hashing logic.