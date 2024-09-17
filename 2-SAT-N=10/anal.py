import numpy as np
import matplotlib.pyplot as plt

# Load data from file.txt
data = np.loadtxt('file_anal.txt')

# Extract columns
x = data[:, 0]  # First column for x-axis (alpha)
y1 = data[:, 1]  # Second column for y-axis (P(SAT))
y1_err = data[:, 2]  # Third column for error bars
y2 = data[:, 3]  # Fourth column for second plot (Output O1-preview)
ypico = data[:, 4]  # pico (P(SAT))
ypico_err = data[:, 5]  # pico error bars
y2_err = data[:, 6]  # pico error bars
# Plot the first data series with error bars
plt.errorbar(x, y1, yerr=y1_err, fmt='o-', label='Output O1-preview  D.C.', capsize=3)
plt.errorbar(x, ypico, yerr=ypico_err, fmt='o-', label='Pycosat', capsize=3)

# Plot the second data series
plt.errorbar(x, y2,  yerr=y2_err, fmt='o-', label='Output O1-preview', capsize=3)
plt.ylim(0, 1.1)
plt.title("Random 2-SAT", fontsize=14)
# Add labels and legend
plt.xlabel(r'$\alpha$', fontsize=14)
plt.ylabel('P(SAT. ASSIG.)', fontsize=14)
plt.legend(fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("2-sat.jpeg")
# Show the plot
plt.show()

plt. close()

data=np.loadtxt("anal_for_hist.txt")
plt.bar(data[:,0], data[:, 1], width=0.1, align='center', edgecolor='black')
plt.ylim(0, 10)
plt.title("Random 2-SAT", fontsize=14)
plt.xlabel(r'$\alpha$', fontsize=14)
plt.ylabel('Number of Occurrences of a SAT SOLVER', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("2-sat-histo.jpeg")
plt.show()
plt. close()


data=np.loadtxt("file_max_sat.txt")
plt.errorbar(data[:,0], data[:,1],  yerr=data[:,2], fmt='o-', label='Output O1-preview  D.C.', capsize=3)
plt.ylim(0, 0.35)
plt.axhline(y=0.25, color='black', linewidth=2, label='Random Guess')
plt.title("Random 2-SAT", fontsize=14)
plt.xlabel(r'$\alpha$', fontsize=14)
plt.ylabel('H', fontsize=14)
plt.legend(fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("2-sat-max.jpeg")
plt.show()
plt. close()
