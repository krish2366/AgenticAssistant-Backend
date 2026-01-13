from app.ingestion.loader import load_files

files = load_files("C:/code_playground/trpizy_backend")
print(len(files))
print(files[0]["file_path"])
