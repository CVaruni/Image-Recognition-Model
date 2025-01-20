import pandas as pd
import matplotlib.pyplot as plt

# Example function to load customer's water consumption data from CSV
def load_consumption_data(customer_id):
    filename = f'customer_{customer_id}_data.csv'
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Data file '{filename}' not found.")
        return None

# Example function to analyze and visualize consumption data
def analyze_and_visualize_consumption(dataframe):
    if dataframe is not None:
        # Calculate total consumption
        total_consumption = dataframe['Consumption'].sum()

        # Plot monthly consumption
        plt.figure(figsize=(10, 6))
        plt.plot(dataframe['Month'], dataframe['Consumption'], marker='o', linestyle='-')
        plt.xlabel('Month')
        plt.ylabel('Consumption (cubic meters)')
        plt.title('Monthly Water Consumption')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('monthly_consumption.png')  # Save the plot as a PNG file
        plt.show()

        print(f"Total consumption: {total_consumption} cubic meters")
    else:
        print("No data available for visualization.")

# Example main function for the application
def main():
    # Assume customer ID for testing
    customer_id = 12345

    # Sample data for customer 12345 (replace with real data handling)
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Consumption': [15, 18, 22, 20, 16, 19]  # Monthly consumption in cubic meters
    }
    df = pd.DataFrame(data)

    # Save sample data to CSV (replace with actual data saving)
    df.to_csv(f'customer_{customer_id}_data.csv', index=False)

    # Load and analyze data
    customer_data = load_consumption_data(customer_id)
    analyze_and_visualize_consumption(customer_data)

if _name_ == "_main_":
    main()