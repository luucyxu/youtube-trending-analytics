import os
import pandas as pd

# 当前脚本所在的文件夹
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 项目根目录,也就是 Data_Warehousing_Final_Project
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# 原始 csv 所在目录,就是项目根目录
RAW_DATA_DIR = PROJECT_ROOT

# 输出目录
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data_processed")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 你现在有的国家和文件对应关系
country_files = {
    "CA": "CAvideos.csv",
    "DE": "DEvideos.csv",
    "FR": "FRvideos.csv",
    "GB": "GBvideos.csv",
    "IN": "INvideos.csv",
    "JP": "JPvideos.csv",
    "KR": "KRvideos.csv",
    "MX": "MXvideos.csv",
    "RU": "RUvideos.csv",
    "US": "USvideos.csv"
}

df_list = []

for country_code, file_name in country_files.items():
    file_path = os.path.join(RAW_DATA_DIR, file_name)
    print(f"Reading {file_path} for country {country_code}")

    # 有的文件编码是 latin1 比较安全
    df = pd.read_csv(file_path, encoding="latin1")

    # 加上国家字段
    df["country"] = country_code

    df_list.append(df)

# 合并所有国家
combined_df = pd.concat(df_list, ignore_index=True)

print("Total rows after combine:", len(combined_df))

# 列名统一成小写加下划线格式
combined_df.columns = (
    combined_df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

output_path = os.path.join(OUTPUT_DIR, "youtube_trending_combined.csv")
combined_df.to_csv(output_path, index=False)

print(f"Combined file saved to {output_path}")

