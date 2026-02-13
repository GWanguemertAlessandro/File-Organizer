import argparse
import logging
from organizer import organize_folder


def print_summary(stats: dict, dry_run: bool) -> None:
    logging.info("Summary:")
    logging.info(f"Moved: {stats['moved']}")
    logging.info(f"Skipped (already organized): {stats['skipped']}")
    logging.info(f"Existing (not overwritten): {stats['existing']}")

    if stats["moved"] == 0 and stats["existing"] == 0:
        logging.info("No files needed organization.")

    if dry_run:
        logging.info("Dry run completed. No files were moved.")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    parser = argparse.ArgumentParser(
        description="Organize files in a folder by file type."
    )

    parser.add_argument(
        "folder_path",
        help="Path to the folder you want to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without moving files"
    )

    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Organize files inside subdirectories recursively"
    )

    args = parser.parse_args()

    try:
        stats = organize_folder(
            folder_path=args.folder_path,
            dry_run=args.dry_run,
            recursive=args.recursive
        )

        print_summary(stats, args.dry_run)

    except FileNotFoundError as error:
        logging.error(error)

    except Exception:
        logging.exception("Unexpected error occurred")


if __name__ == "__main__":
    main()
