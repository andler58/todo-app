import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=["Bonus1.py", "Bonus2.1.py"], dest_dir="dest")