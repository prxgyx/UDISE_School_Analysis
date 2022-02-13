import pandas as pd

kolkata_df = pd.read_csv("res/kolkata.csv", sep=",", encoding="utf-8", error_bad_lines=False)

kolkata_df.query('(`School Management` == "Pvt. Unaided" or Location == "Pvt. Unaided")').count

"""
Query:
1. School management and school category - sec. / h. sec
2. School management, location - pvt. unaided
3. Location, school type - urban

"""
kolkata_df.query('`School category`.str.contains("sec./H.sec") or `School Management`.str.contains("sec./H.sec")').count
kolkata_df.query('(`School Management` == "Pvt. Unaided" or Location == "Pvt. Unaided")').count
 # and ().count