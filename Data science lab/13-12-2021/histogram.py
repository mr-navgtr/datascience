import pandas as pd
import matplotlib.pyplot as plt
data = [
['India', 2019, 'Medium', 1368737.513],
['India', 2019, 'High', 1378419.072],
['India', 2019, 'Low', 1359043.965],
['India', 2019, 'Constant fertility', 1373707.838],
['India', 2019,'Instant replacement', 1366687.871],
['India', 2019, 'Zero migration', 1370868.782],
['India', 2019,'Constant mortality', 1366282.778],
['India', 2019, 'No change', 1371221.64],
['India', 2019, 'Momentum', 1367400.614],]
df = pd.DataFrame(data, columns = ([ 'Country or Area', 'Year(s)', 'Variant', 'Value']))
df.hist()
plt.show()