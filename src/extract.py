""" Extract file to transform in dataframe"""

# import library pandas
import pandas as pd 
from pathlib import Path
from .logger import logger

# Create an function to extract file into the folder data/raw
def extract(file: Path) -> pd.DataFrame:
    logger.info(f"{'#'* 20} Debut Extraction")
    
    try:
        df = pd.read_csv(file)

        if df.empty:
            logger.info(f"{file.name} est vide")

        logger.info(f"{file.name} charge avec succes.")
        logger.info(f"Nombre de lignes : {df.shape[0]}")
        logger.info(f"Nombre de colonnes : {df.shape[1]}")

        logger.info(f"{'#'* 20} FIN Extraction")

        return df
    
    
    except FileNotFoundError:
            logger.error(f"fichier introuvable : {file}")
            return None
    except Exception as e:
            logger.error(f"Erreur Extraction : {e}")
            return None

    

    