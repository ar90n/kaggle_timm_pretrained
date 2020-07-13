import json
from pathlib import Path
from typing import Union

def patch(input_dir: Union[Path, str]) -> None:
    import timm

    input_dir = Path(input_dir)
    for p in input_dir.glob("*"):
        p = Path(p).resolve()
        if not p.name.startswith("timm-pretrained"):
            continue

        index_path = p / "index.json"
        try:
            index = json.loads(index_path.read_text())
        except:
            continue

        for model_type, pretrains in index.items():
            for name, file_name in pretrains.items():
                getattr(timm.models, model_type).default_cfgs[name][
                    "url"
                ] = f"file://{str(p)}/{model_type}/{file_name}"
