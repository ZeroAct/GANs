import matplotlib.pyplot as plt

def imshow(images, labels=None, classes=None, cols=6, cmap='gray'):
    
    if cmap == 'gray':
        if len(images.shape) == 2:
            images = [images]
    
    if labels is None:
        labels = ['' for _ in range(len(images))]
    elif classes is not None:
        labels = [classes[idx] for idx in labels]
    else:
        labels = [str(idx) for idx in labels]
            
    rows = len(images) // cols + 1
    
    plt.figure()
    f, axes = plt.subplots(rows, cols)
    [ax.set_visible(False) for ax in axes.ravel()]
    for i, (image, label) in enumerate(zip(images, labels)):
        r, c = i//cols, i%cols
        axes[r, c].set_title(label)
        axes[r, c].imshow(image, cmap=cmap)
        axes[r, c].set_visible(True)
        axes[r, c].axis('off')
    plt.show()

def get_mean(xs: list):
    return sum(xs) / len(xs)