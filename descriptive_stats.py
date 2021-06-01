import matplotlib.pyplot as plt
import numpy as np
age_group2 = [18,23,28,67,45,27,29,20,24,22,36,53]

mean_age = np.mean(age_group2)
print("The mean of is: ",mean_age)

std_deviation = np.std(age_group2)
print("The starndard deviaton is: ", std_deviation)

var_age = np.var(age_group2)
print("The variance is: ", var_age)

arranged_values = np.arange(0,21)
print("The arranged values from 0 to 20: ",arranged_values)
