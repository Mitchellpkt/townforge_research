from pathlib import Path
from typing import List, Tuple

import pandas as pd


def read_transactions_to_dataframe(
    top_data_directory: Path = Path.cwd() / ".." / "data" / "unpacked",
) -> pd.DataFrame:
    # Get the file paths
    all_paths: List[Path] = list(top_data_directory.glob("**/*"))
    file_paths: List[Path] = [f for f in all_paths if f.is_file()]

    # Read in the files
    transactions: List[Tuple[str, str]] = []
    for file_path in file_paths:
        with open(file_path, "r") as f:
            txn_text: str = f.read().replace("\n", "")  # remove newline
            transactions.append((txn_text, str(file_path)))

    return pd.DataFrame(
        {
            "transaction": list(zip(*transactions))[0],
            "file": list(zip(*transactions))[1],
        }
    )
