"""Stage the entry image into the output directory.

Copies the entry.png that lives next to this script into the
directory given by MAKEFUN_OUTPUT_DIR (defaulting to /output),
verifying the source exists before any work is done. Standard
library only; prints one confirmation line and exits 0 on success.
"""

import os
import shutil
import sys


def main() -> int:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    if not os.path.isfile(src):
        print(f"error: source file not found: {src}", file=sys.stderr)
        return 1
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    print(f"copied entry.png to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
