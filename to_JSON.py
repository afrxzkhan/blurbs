import pandas as pd

# 1. Load the Excel file (setting sheet_name=None reads ALL sheets)
excel_file = "chats.xlsx"
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# 2. Create a dictionary to hold the cleaned data from each sheet
combined_data = {}

# 3. Loop through each sheet name and its data
for sheet_name, df in all_sheets.items():
    # Clean up empty cells (NaN) for this specific sheet
    df_cleaned = df.fillna("")
    
    # Convert this sheet's rows into a list of dictionaries
    combined_data[sheet_name] = df_cleaned.to_dict(orient="records")

# 4. Save the combined master dictionary directly to a JSON file
import json
output_json = "chats.json"

with open(output_json, "w", encoding="utf-8") as json_file:
    json.dump(combined_data, json_file, indent=4, ensure_ascii=False)

print(f"✅ Successfully converted ALL sheets from {excel_file} to {output_json}!")
