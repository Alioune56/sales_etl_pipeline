import pandas as pd
from sqlalchemy import create_engine
from .logger import logger
from config.config import DB_URL

def load(data: pd.DataFrame, table_name: str):
    
    logger.info("Debut du chargement des donnees")

    try:

        engine = create_engine(DB_URL)

        data.to_sql(
            con=engine,
            name=table_name,
            if_exists="replace",
            index=False
        )

        logger.info(
            f"Chargement reussi dans la table {table_name}"
        )

    except Exception as e:
        logger.error(
            f"Erreur lors du chargement : {e}"
        )

