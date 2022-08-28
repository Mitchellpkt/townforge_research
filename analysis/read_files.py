from pathlib import Path
from typing import List


def read_transctions(
    top_data_directory: Path = Path.cwd() / ".." / "data" / "unpacked",
) -> List[str]:
    # Get the file paths
    all_paths: List[Path] = list(top_data_directory.glob("**/*"))
    file_paths: List[Path] = [f for f in all_paths if f.is_file()]

    # Read in the files
    transactions: List[str] = []
    for file_path in file_paths:
        with open(file_path, "r") as f:
            transactions.append(f.read())

    return transactions
