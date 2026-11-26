import os
import shutil


def main() -> int:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    print(f"copied entry.png to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
