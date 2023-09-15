import pandas as pd

# Prompt the user for input and output file paths
input_file_path = input("Enter the path to the input CSV file: ")
output_file_path = input("Enter the path to the output CSV file: ")

# Read the CSV into a Pandas DataFrame
df = pd.read_csv(input_file_path)

# Parse the timestamp column as datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the date from the timestamp
df['date'] = df['timestamp'].dt.date

# Calculate the total spent for each transaction (price * quantity)
df['total_spent'] = df['product_price'] * df['quantity']

# Group by date and customer_id, then sum the total_spent for each group
result_df = df.groupby(['date', 'customer_id'])['total_spent'].sum().reset_index()

# Write the output CSV file
result_df.to_csv(output_file_path, index=False)

print("Processing complete. Results written to", output_file_path)
