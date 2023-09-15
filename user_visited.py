import pandas as pd

# Function to calculate metrics and write to a CSV file
def calculate_metrics(input_file_path, output_csv_file_path):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(input_file_path)

    # Calculate the total number of interactions
    total_interactions = len(df)

    # Calculate the total number of unique users
    total_unique_users = df['user_id'].nunique()

    # Calculate the most visited URL
    most_visited_url = df['url'].mode().iloc[0]

    # Calculate the average time spent on each URL
    df['page_view_duration'] = pd.to_numeric(df['page_view_duration'], errors='coerce')
    average_time_spent = df.groupby('url')['page_view_duration'].mean().reset_index()
    average_time_spent.rename(columns={'page_view_duration': 'Average Time Spent on Each URL'}, inplace=True)

    # Create a DataFrame with all the results
    results_df = pd.DataFrame({
        'Total Interactions': [total_interactions],
        'Total Unique Users': [total_unique_users],
        'Most Visited URL': [most_visited_url],
    })

    # Write the results to a CSV file
    results_df.to_csv(output_csv_file_path, index=False)

    # Append the average_time_spent DataFrame to the output CSV
    average_time_spent.to_csv(output_csv_file_path, mode='a', header=True, index=False)

if __name__ == "__main__":
    input_file_path = input("Enter the path to the input CSV file: ")
    output_csv_file_path = input("Enter the path to the output CSV file: ")

    calculate_metrics(input_file_path, output_csv_file_path)

    print("Processing complete. Results written to", output_csv_file_path)



