from pathlib import Path
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Code": [".py", ".js", ".html", ".css"],
}


def organize_folder(folder_path: str, dry_run: bool = False, recursive: bool = False) -> dict:
    base_path = Path(folder_path)

    if not base_path.exists() or not base_path.is_dir():
        raise FileNotFoundError("The specified folder does not exist or is not a directory.")

    stats = {
        "moved": 0,
        "skipped": 0,
        "existing": 0
    }

    iterator = base_path.rglob("*") if recursive else base_path.iterdir()

    for item in iterator:
        if item.is_file():
            result = move_file(item, base_path, dry_run)
            if result:
                stats[result] += 1

    return stats


def move_file(file_path: Path, base_path: Path, dry_run: bool) -> str | None:
    if file_path.parent.name in FILE_TYPES.keys() or file_path.parent.name == "Other":
        return "skipped"

    for folder_name, extensions in FILE_TYPES.items():
        if file_path.suffix.lower() in extensions:
            return _move(file_path, base_path / folder_name, dry_run)

    return _move(file_path, base_path / "Other", dry_run)


def _move(file_path: Path, target_dir: Path, dry_run: bool) -> str:
    target_path = target_dir / file_path.name

    if target_path.exists():
        print(f"Skipping {file_path.name} (already exists in {target_dir.name})")
        return "existing"

    if dry_run:
        print(f"[DRY RUN] {file_path.name} -> {target_dir.name}/")
        return "moved"

    target_dir.mkdir(exist_ok=True)
    shutil.move(str(file_path), str(target_path))
    return "moved"

