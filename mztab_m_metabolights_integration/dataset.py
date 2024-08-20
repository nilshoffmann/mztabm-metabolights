from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from mztab_m_metabolights_integration.config import PROCESSED_DATA_DIR, EXTERNAL_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = EXTERNAL_DATA_DIR / "MTBLS263.mztab.json",
    output_path: Path = PROCESSED_DATA_DIR / "MTBLS263",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
