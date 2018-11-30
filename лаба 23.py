import numpy as np
import random as rand
import matplotlib.pyplot as plt

arr = np.array([rand.randint(0,1000) for i in range(1000)])
arrnum = [i for i in range(1000)]
print("\nМассив:\n", arr,
      "\nМинимальное значение:\t",np.min(arr),
      "\nМаксимальное значение:\t",np.max(arr),
      "\nМедиана:\t\t",np.median(arr),
      "\nСтандартное отклонение:\t",np.std(arr),
      "\nСреднее значение:\t",np.mean(arr),
      "\nДисперсия:\t\t",np.var(arr))
plt.figure("Nice one",figsize = (12,6))

plt.subplot(111)
plt.bar(arrnum,arr)
plt.xlabel("Numbers")
plt.ylabel("Random values")

plt.show()

 



