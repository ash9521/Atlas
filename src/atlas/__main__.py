import sys

from atlas.application import Application


def main() -> int:
    return Application().run(
        sys.argv[1:],
    )


if __name__ == "__main__":
    raise SystemExit(main())
