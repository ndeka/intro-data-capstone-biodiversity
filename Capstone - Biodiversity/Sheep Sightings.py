import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

observations = pd.read_csv('observations.csv')

sheep_observations = observations.merge(sheep_species)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

plt.figure(figsize =(16,4))
plt.bar(range(len(obs_by_park['park_name'])), obs_by_park['observations'])
ax = plt.subplot()
ax.set_xticks(range(len(obs_by_park['park_name'])))
ax.set_xticklabels(obs_by_park['park_name'])

plt.title('Observations of Sheep per Week')
plt.xlabel('Park Name')
plt.ylabel('Number of Observations')
plt.savefig('Observations_by_Parks.png')
plt.show()