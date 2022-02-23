import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x_values = np.random.random(10, 3, 300)  # Generating Data
df = pd.DataFrame(x_values, columns=['var_name'])  # Converting array to pandas DataFrame
df.plot(kind='density)