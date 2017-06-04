import matplotlib.pyplot as plt
import numpy as np
# plt.figure(1)                # the first figure
# plt.subplot(231)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])

# plt.figure(2)                # a second figure
# plt.plot([1, 2, 3])
# plt.legend(['A simple line'])

# plt.figure(3)
# plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
# plt.plot([1,2,3], [1,4,9], 'rs',  label='line 2')
# plt.plot([1,2,3], [1,5,9], 'c+:',  label='line 3')
# plt.plot([1,2,3], [1,6,9], 'b.-',  label='line 4')
# plt.axis([0, 4, 0, 10])
# plt.legend()

# plt.figure(4)
# a = [201701,'201702','201703','201704']
# b = [1000, 2000, 1500, 2100]
# plt.plot(a, b, 'b.-', label='line 4')
# plt.axis('auto')
# plt.legend()
# 
# plt.show()

n_groups = 5
means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)
means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.15

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 #yerr=std_men,
                 error_kw=error_config,
                 label='Men1',
                 align='edge')

rects2 = plt.bar(index+ bar_width, means_men, bar_width,
                 alpha=opacity,
                 color='g',
                 #yerr=std_men,
                 error_kw=error_config,
                 label='Men2',
                 align='edge')

plt.bar(index + bar_width+ bar_width, means_women, bar_width,
                 alpha=opacity,
                 color='r',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='Women',
                 align='edge')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
plt.legend()
plt.tight_layout()
plt.show()