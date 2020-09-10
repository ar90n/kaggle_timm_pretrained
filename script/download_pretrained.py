from typing import Dict, Set
import json

from pathlib import Path
import typer
import timm
import requests
from tqdm import tqdm


def get_model_pretraned_urls():
    for model_type, model_module in timm.models.__dict__.items():
        if not hasattr(model_module, "default_cfgs"):
            continue

        pretrained_urls = {
            n: cfg["url"]
            for n, cfg in model_module.default_cfgs.items()
            if cfg["url"] != ""
        }
        yield (model_type, pretrained_urls)


def download_pretrained(dst_dir: Path, urls: Dict[str, str]) -> Dict[str, str]:
    result = {}
    for n, url in tqdm(urls.items()):
        weight_file_name = url.split("/")[-1]
        weight_file_path = dst_dir / weight_file_name
        with requests.get(url) as r:
            weight_file_path.write_bytes(r.content)
            result[n] = weight_file_name
    return result


def get_folder_name(model_type: str) -> str:
    return model_type.replace("_", "-")


def remove_downloaded_files(
    urls: Dict[str, str], downloaded_files: Set[str]
) -> Dict[str, str]:
    return {n: u for n, u in urls.items() if u.split("/")[-1] not in downloaded_files}


def main(dst_dir: Path):
    has_changed = []
    for model_type, urls in get_model_pretraned_urls():
        typer.echo(f"Start to download {model_type} pretrained files.")
        dataset_dir = dst_dir / get_folder_name(model_type)
        dataset_dir.mkdir(exist_ok=True)

        pretained_file_dir = dataset_dir / model_type
        pretained_file_dir.mkdir(exist_ok=True)

        index_file_path = dataset_dir / "index.json"
        try:
            cur_files = json.loads(index_file_path.read_text())[model_type]
        except FileNotFoundError:
            cur_files = {}

        downloaded_pretrained_files = set(cur_files.values())
        new_urls = remove_downloaded_files(urls, downloaded_pretrained_files)
        if len(new_urls) == 0:
            continue

        diff_files = download_pretrained(pretained_file_dir, new_urls)
        index_file = {model_type: {**cur_files, **diff_files}}
        index_file_path.write_text(json.dumps(index_file))
        has_changed.append(model_type)

    print("following models are changed")
    print("\n".join(has_changed))


if __name__ == "__main__":
    typer.run(main)
