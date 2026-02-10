import argparse
from organizer import organize_folder

def main():
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

    args = parser.parse_args()

    try:
        organize_folder(args.folder_path, dry_run=args.dry_run)
        if args.dry_run:
            print("Dry run completed. No files were moved.")
        else:
            print("Folder organized successfully.")
    except FileNotFoundError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
