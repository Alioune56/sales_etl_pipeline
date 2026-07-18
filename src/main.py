from pathlib import Path
from .extract import extract
from .transform import transform
from config.config import RAW_FILE
from .load import load


if __name__ == '__main__':

   # Extraction
   df_extract = extract(RAW_FILE)

   # Transformation
   df_transform = transform(df_extract)

   # Load
   load(df_transform,"ventes") 