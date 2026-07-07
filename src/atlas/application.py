from pathlib import Path


class Application:
    """
    Atlas application entry point.
    """

    def run(
        self,
        argv: list[str],
    ) -> int:
        print("=" * 37)
        print("Atlas Export Intelligence")
        print("Version 0.1")
        print("=" * 37)
        print()

        if not argv:
            print("Usage:")
            print("  python -m atlas <excel-file>")
            return 1

        filename = Path(argv[0])

        if not filename.exists():
            print(f"Error: File not found: {filename}")
            return 1

        print(f"Loading: {filename}")

        return 0
