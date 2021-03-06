from keras.callbacks import ModelCheckpoint
from keras.models import load_model
import matplotlib.pyplot as plt
from classifier import architecture as arch
import os
import numpy as np
from sklearn.utils import compute_class_weight


mask_opt = 'masked'
color_opt = 'full'
balance_opt = 'unbalanced'

parent_dir = 'model_data'
opt_str = "_".join([mask_opt, color_opt, balance_opt])
train_dir = "_".join(['train', 'numpy', opt_str])
train_path = os.path.join(parent_dir, train_dir)
model_file = "_".join(['model', opt_str]) + '_simple_fm.hdf5'
model_cache_path = os.path.join(parent_dir, model_file)

test_dir = "_".join(['test', 'numpy', opt_str])
test_path = os.path.join(parent_dir, test_dir)

train_x = np.load(os.path.join(train_path, 'extra.npy'))
train_y = np.load(os.path.join(train_path, 'ohelabels.npy'))

val_x = np.load(os.path.join(test_path, 'extra.npy'))
val_y = np.load(os.path.join(test_path, 'ohelabels.npy'))

y_ints = [y.argmax() for y in train_y]

class_weights = compute_class_weight(
    'balanced',
    np.unique(y_ints),
    y_ints
)

checkpoint = ModelCheckpoint(
    model_cache_path,
    monitor='loss',
    verbose=1,
    save_best_only=True,
    save_weights_only=False,
    mode='auto',
    period=1
)

if os.path.exists(model_cache_path):
    model = load_model(model_cache_path)
    print('Loading model from cache...')
else:
    model = arch.build_simple_fm_model(5, train_x.shape[1])

h = model.fit(
    train_x,
    train_y,
    epochs=1000,
    callbacks=[checkpoint],
    validation_data=(val_x, val_y),
    class_weight=class_weights
)

print(h.history.keys())

# summarize history for accuracy
plt.plot(h.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(h.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
