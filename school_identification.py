import pandas as pd

kolkata_df = pd.read_csv("res/kolkata.csv", sep=",", encoding="utf-8", error_bad_lines=False)

"""
Query:
1. School management and school category - sec. / h. sec
2. School management, location - pvt. unaided
3. Location, school type - urban

"""

kolkata_df.query('(`School category`.str.contains("sec./H.sec") or `School Management`.str.contains("sec./H.sec")) and (`School Management` == "Pvt. Unaided" or Location == "Pvt. Unaided")')["Location"]

mumbai_df = pd.read_csv("res/mumbai.csv", sep=",", encoding="utf-8", error_bad_lines=False)

mumbai_df.query('(`School Management` == "Pvt. Unaided" or Location == "Pvt. Unaided") and `School Management`.str.contains("sec./H.sec")').sort_values('Male teachers')

delhi_df = pd.read_csv("res/delhi.csv", sep=",", encoding="utf-8", error_bad_lines=False)

# delhi_df["School Management"].unique()
# delhi_df["School category"].unique()

delhi_df.query('`School Management` == "Pvt. Unaided" and `School category`.str.contains("sec./H.sec")')

pune_df = pd.read_csv("res/pune.csv", sep=",", encoding="utf-8", error_bad_lines=False)

# pune_df["School Management"].unique()
# pune_df["School category"].unique()
# pune_df["Location"].unique()

pune_df.query('(`School category`.str.contains("sec./H.sec") or `School Management`.str.contains("sec./H.sec")) and (`School Management` == "Pvt. Unaided" or Location == "Pvt. Unaided")').sort_values("Number of students")
