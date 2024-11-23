# Quantitative Methods In Finance

This project uses Python 3.11 and includes a virtual environment for package management.

It includes my notes from Carol Alexander's Market Risk Analysis book series.

I've included them in a markdown file with examples created using python.

Any errors or mistakes are my own.

**Source Citation**  

Alexander, C. (2009–2012). *Market risk analysis* (Vols. 1–4). John Wiley & Sons.

## Example Code

```python
# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample data
data = np.random.randn(100)

# Plot data
plt.hist(data, bins=20)
plt.title("Random Data Distribution")
plt.show()

