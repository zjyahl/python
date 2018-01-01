# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def draw():
    plt.figure(1)
    plt.style.use('ggplot')

    plt.subplot(211)

    lines = plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(1, 5, r'hhh')
    plt.setp(lines, label="Example one",color='r', linewidth=2.0, linestyle='--')
    print(plt.setp(lines))
    ax = plt.gca()
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ax.set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f'])
    ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    with plt.style.context(('dark_background')):
        pass
   # plt.style.use(['dark_background', 'ggplot'])
    plt.style.use('fivethirtyeight')
    plt.subplot(212)
    plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    plt.axis([1,7, 1, 6])
    #plt.ylim(1, 6)

    plt.grid(True)
    plt.annotate('local max', xy=(2, 2), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )

    plt.show()

draw()