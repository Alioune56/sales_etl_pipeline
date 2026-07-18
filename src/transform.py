import pandas as pd
from .logger import logger

def transform(data: pd.DataFrame) -> pd.DataFrame:
    logger.info(f"{'#'* 20} Debut Transformation")

    data.columns = data.columns.str.lower()
    data.columns = data.columns.str.replace(' ','_')

    logger.info(f"Le nombre de doublons est : {data.duplicated().sum()}")
    if data.duplicated().sum() > 0:
        data.drop_duplicates(inplace = True)
        logger.info("Doublons supprimees avec succes")
        logger.info(f"Nombre de doublons apres suppression : {data.duplicated().sum()}")
    else:
        logger.info("Aucun doublon dans le dataframe")

    logger.info(f"Donnees manquantes : {data.isna().sum().sum()}")
    if data.isna().sum().sum() > 0:
        logger.info("Donnees manquantes a transforme")
    else :
        logger.info("Aucun donnee manquante dans le dataframe")

    date_colums = ['order_date','ship_date']
    for col in date_colums:
        if col in data.columns :
            data[col] = pd.to_datetime(data[col],errors='coerce')
        
        else :
            logger.warning(f"{data[col]} est absent de la liste des colonnes du dataset")
    logger.info(f"{'#'*20} Fin Transformation")

    return data

    