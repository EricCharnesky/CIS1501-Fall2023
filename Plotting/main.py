# Load matplotlib.pyplot, pandas, and numpy
import matplotlib.pyplot as plt

mpgs = range(10,100)
suvs_gallons_used = []
suvs_gallons_saved = []


sedans_gallons_saved = []
for mpg in mpgs:
    suvs_gallons_used.append(10_000 / mpg)
    suvs_gallons_saved.append(1000 - 10_000 / mpg)
    sedans_gallons_saved.append(500 - 10_000 / mpg)


plt.xlabel("MPGs")
plt.ylabel("Gallons")
plt.axis()
#plt.plot(mpgs, suvs_gallons_used)
plt.plot(mpgs, suvs_gallons_saved)
plt.plot(mpgs, sedans_gallons_saved)
plt.show()
