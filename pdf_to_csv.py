import pandas as pd
import tabula

file_path = "./Delhi/0701.pdf"

tabula.convert_into(file_path, "0701.csv", output_format="csv", pages='all')
