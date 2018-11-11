import matplotlib.pyplot as plt


def plot_patterns(patterns, title=''):
    fig = plt.figure(figsize=(8, 8))
    fig.suptitle(title, fontsize=16)
    columns = 4
    rows = 5
    for i in range(1, columns * rows + 1):
        if i > len(patterns):
            break
        fig.add_subplot(rows, columns, i)
        plt.imshow(patterns[i - 1], cmap='seismic', interpolation='none', vmin=0, vmax=3)
    plt.show()


def plot_pattern_offsets(pattern, offsets):
    fig = plt.figure(figsize=(8, 8))
    fig.suptitle(title, fontsize=16)
    columns = 4
    rows = 5
    for i in range(1, columns * rows + 1):
        if i > len(offsets):
            break
        fig.add_subplot(rows, columns, i)
        plt.imshow(offsets[i - 1], cmap='seismic', interpolation='none', vmin=0, vmax=3)
    plt.show()


def plot_sample(sample):
    im = plt.imshow(sample, cmap='seismic', interpolation='none', vmin=0, vmax=3)
    plt.colorbar(im)
    plt.show()
