import pandas as pd

# === Input & Output ===
input_file = "data_mutations.txt"  
output_file = "filtered_missense_lung.csv"

# === Load the data ===
df = pd.read_csv(input_file, sep='\t', low_memory=False)

# === Filter only Missense Mutations ===
df_filtered = df[df["Variant_Classification"] == "Missense_Mutation"]

# === Select only relevant columns ===
columns_to_keep = [
    "Hugo_Symbol",
    "HGVSp_Short",
    "Tumor_Sample_Barcode"
]
df_filtered = df_filtered[columns_to_keep]

# === Drop rows with missing HGVSp_Short (no protein change info) ===
df_filtered = df_filtered.dropna(subset=["HGVSp_Short"])

# === Save filtered output ===
df_filtered.to_csv(output_file, index=False)

print(f"✅ Done! Saved filtered file to: {output_file}")
