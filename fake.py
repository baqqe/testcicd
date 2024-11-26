import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Generate fake data
n_samples = 500

data = {
    "Mold_ID": [f"M{str(i).zfill(3)}" for i in range(1, n_samples + 1)],
    "Cycle_Time": np.round(np.random.normal(loc=45, scale=5, size=n_samples), 2),  # Mean: 45s, Std: 5s
    "Part_Weight": np.round(np.random.uniform(2.0, 10.0, size=n_samples), 2),  # Random between 2g and 10g
    "Material_Used": np.random.choice(["ABS", "Polycarbonate", "Nylon", "Polyethylene"], size=n_samples),
    "Defect_Rate": np.round(np.random.uniform(0, 5, size=n_samples), 2),  # Random between 0% and 5%
    "Temperature": np.round(np.random.normal(loc=220, scale=10, size=n_samples), 2),  # Mean: 220°C, Std: 10°C
    "Pressure": np.round(np.random.uniform(80, 120, size=n_samples), 2),  # Random between 80 and 120 bar
    "Shift": np.random.choice(["Morning", "Afternoon", "Night"], size=n_samples),
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("lego_injection_molding_data.csv", index=False)

print("Fake LEGO injection molding dataset generated and saved to 'lego_injection_molding_data.csv'.")
