from read_files import read_transctions
from pathlib import Path
from typing import List

if __name__ == "__main__":
    top_data_directory: Path = Path.cwd() / ".." / "data" / "unpacked"
    transactions: List[str] = sorted(read_transctions(top_data_directory))

    # Spot check length and content
    assert len(transactions) == 2_048
    assert transactions[0][:30] == "02000202001000639406820207a301"

    print(f"... Tests OK. Read {len(transactions)} txns, first :\n{transactions[0]}")
