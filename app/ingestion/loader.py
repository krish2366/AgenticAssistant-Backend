# file loader

import os

ALLOWED_EXTENTIONS = (".js",".ts",".py",".tsx",".jsx")

IGNORE_DIRS = {
    "node_modules",
    ".git",
    "dist",
    "build",
    "__pycache__"
}

def load_files(repo_path: str):
    files = []

    try:
        if not isinstance(repo_path, str):
            raise TypeError("repo_path must be a string")

        if not os.path.isdir(repo_path):
            raise ValueError("repo_path must be a valid directory")

        repo_path = os.path.abspath(repo_path)

        for root, dirs, filenames in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for filename in filenames:
                if filename.endswith(ALLOWED_EXTENTIONS):
                    full_path = os.path.join(root, filename)

                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            files.append({
                                "file_path": os.path.relpath(full_path, repo_path),
                                "content": f.read()
                            })
                    except Exception:
                        continue

    except Exception as e:
        print(f"[load_files error] {e}")

    return files
