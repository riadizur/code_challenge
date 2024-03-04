import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set start date and number of days
start_date = datetime(2023, 1, 1)
num_days = 10000

# Generate date range
dates = [start_date + timedelta(days=i) for i in range(num_days)]

# Generate random sales data
np.random.seed(42)  # for reproducibility
sales = np.random.randint(50, 500, num_days)

# Create DataFrame
df = pd.DataFrame({'date': dates, 'sales': sales})

# Save to CSV
df.to_csv('sales_data_large.csv', index=False)