from pathlib import Path
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Code": [".py", ".js", ".html", ".css",],
}

#--------------------DefFunctions---------------------------

def organize_folder(folder_path: str) -> None:
    
    """
    Organizes files in the given folder into subfolders
    based on file extensions.
    """
    base_path = Path(folder_path)

    if not base_path.exists():
        raise FileNotFoundError("The specified folder does not exist.")

    for item in base_path.iterdir():
        if item.is_file():
            move_file(item, base_path)


def move_file(file_path: Path, base_path: Path) -> None:
   
    """
    Moves a file into a subfolder according to its extension.
    """
    for folder_name, extensions in FILE_TYPES.items():
        if file_path.suffix.lower() in extensions:
            target_dir = base_path / folder_name
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(target_dir / file_path.name))
            return