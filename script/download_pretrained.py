from typing import Dict
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


def main(dst_dir: Path):
    for model_type, urls in get_model_pretraned_urls():
        if model_type not in ["vovnet", "resnest", "sknet"]:
            continue
        typer.echo(f"Start to download {model_type} pretrained files.")
        dataset_dir = dst_dir / model_type
        dataset_dir.mkdir(exist_ok=True)

        pretained_file_dir = dataset_dir / model_type
        pretained_file_dir.mkdir(exist_ok=True)
        pretained_files = {model_type: download_pretrained(pretained_file_dir, urls)}

        index_file = dataset_dir / "index.json"
        with index_file.open("w") as fp:
            json.dump(pretained_files, fp)


if __name__ == "__main__":
    typer.run(main)
