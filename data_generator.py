
import random
import numpy as np

with open('dataset_class_1.csv', 'w') as f:
    for _ in range(1280000):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        c = 0 if a <= b else 1
        f.writelines("{},{},{}\n".format(a, b, c))

print('done dataset 1')

#with open('dataset_class_2.csv', 'w') as f:
#    for _ in range(128000):
#        a = random.randint(0, 1000)
#        b = random.randint(0, 1000)
#        c = 0 if (a + b) % 2 == 0 else 1
#        f.writelines("{},{},{}\n".format(a, b, c))
#
#print('done dataset 2')
#
#with open('dataset_reg_1.csv', 'w') as f:
#    for _ in range(128000):
#        a = random.randint(0, 1000)
#        b = random.randint(0, 1000)
#        c = 0.3 * a + 0.7 * b + 42
#        f.writelines("{},{},{}\n".format(a, b, c))
#
#print('done dataset 3')
#
#with open('dataset_reg_1.csv', 'w') as f:
#    for _ in range(128000):
#        a = random.randint(0, 1000)
#        b = random.randint(0, 1000)
#        c = 0.3 * a ** 2 + 0.7 * np.sqrt(b) + 42
#        f.writelines("{},{},{}\n".format(a, b, c))
#
#print('done dataset 4')
#
#