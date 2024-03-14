import pandas as pd

url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-v2-tertiaire-2/lines?size=10000&format=csv&after=10000%2C965634&header=true"

data = pd.read_csv(url)
data.to_csv("data_ademe.csv", index=False)
print(data.shape)
