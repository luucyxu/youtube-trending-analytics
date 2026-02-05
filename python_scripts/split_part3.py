import os
import math
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

input_path = os.path.join(PROJECT_ROOT, "data_processed", "chunks", "youtube_trending_part3.csv")
output_dir = os.path.join(PROJECT_ROOT, "data_processed", "chunks")
os.makedirs(output_dir, exist_ok=True)

print(f"Input file: {input_path}")

print("Counting total rows in part3...")
with open(input_path, "r", encoding="latin1") as f:
    total_rows = sum(1 for _ in f) - 1

print(f"Total data rows in part3: {total_rows}")

num_parts = 3

rows_per_part = math.ceil(total_rows / num_parts)
print(f"Rows per sub part: {rows_per_part}")

part_idx = 1
rows_written_in_current_part = 0
current_output_path = os.path.join(output_dir, f"youtube_trending_part3_{part_idx}.csv")
current_df_list = []

chunksize = 50_000

print("Start splitting part3...")
for chunk in pd.read_csv(
    input_path,
    encoding="latin1",
    chunksize=chunksize,
    engine="python",
    on_bad_lines="warn"
):
    for i in range(len(chunk)):
        row = chunk.iloc[[i]]
        current_df_list.append(row)
        rows_written_in_current_part += 1

        if rows_written_in_current_part >= rows_per_part and part_idx < num_parts:
            part_df = pd.concat(current_df_list, ignore_index=True)
            part_df.to_csv(current_output_path, index=False)
            print(f"Saved {current_output_path} with {len(part_df)} rows")

            part_idx += 1
            rows_written_in_current_part = 0
            current_df_list = []
            current_output_path = os.path.join(output_dir, f"youtube_trending_part3_{part_idx}.csv")

if current_df_list:
    part_df = pd.concat(current_df_list, ignore_index=True)
    part_df.to_csv(current_output_path, index=False)
    print(f"Saved {current_output_path} with {len(part_df)} rows")

print("Done splitting part3.")

