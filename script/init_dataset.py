from typing import Dict
import json

from pathlib import Path
import typer


def create_meta_data(name: str) -> Dict:
    return {
        "title": f"timm-pretrained-{name}",
        "id": f"ar90ngas/timm-pretrained-{name}",
        "licenses": [{"name": "other"}],
    }


def main(root_dir: Path):
    for dataset_path in root_dir.glob("*"):
        if not dataset_path.is_dir():
            continue

        dataset_name = dataset_path.name
        meta_data = create_meta_data(dataset_name)
        meta_data_path = dataset_path / "dataset-metadata.json"
        with meta_data_path.open("w") as fp:
            json.dump(meta_data, fp)


if __name__ == "__main__":
    typer.run(main)
