import tempfile
from pathlib import Path
from organizer import organize_folder


def test_organize_creates_category_folder():
    with tempfile.TemporaryDirectory() as tmpdir:
        base_path = Path(tmpdir)

 # Crear archivo de prueba
        file = base_path / "test.jpg"
        file.write_text("dummy")

        stats = organize_folder(str(base_path))

        images_folder = base_path / "Images"

        assert images_folder.exists()
        assert (images_folder / "test.jpg").exists()
        assert stats["moved"] == 1
