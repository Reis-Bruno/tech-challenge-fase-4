"""Baixa o Brazilian E-Commerce Public Dataset by Olist do Kaggle para data/raw/.

Requer credenciais do Kaggle (~/.kaggle/kaggle.json ou KAGGLE_USERNAME/KAGGLE_KEY)
— ou faça o download manual em
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce e extraia os CSVs em data/raw/.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from voc_rag.config import RAW_DIR  # noqa: E402
from voc_rag.data_prep import FILES  # noqa: E402


def main() -> None:
    import kagglehub

    path = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))
    print("Dataset baixado em:", path)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for fname in FILES.values():
        src = next(path.rglob(fname), None)
        if src is None:
            raise FileNotFoundError(f"{fname} não encontrado em {path}")
        shutil.copy2(src, RAW_DIR / fname)
        print("  copiado:", fname)
    print(f"CSVs prontos em {RAW_DIR}")


if __name__ == "__main__":
    main()
