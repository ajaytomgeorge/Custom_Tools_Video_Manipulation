import os
import numpy as np
import tensorflow as tf



model = tf.keras.models.load_model('macro.h5')



path2=['data/My Data/macro/c1.jpg','data/My Data/macro/c2.jpg','data/My Data/macro/m1.jpg']
cwd = os.getcwd()

for i,imagepath in enumerate(path2):
    #print('image path is ',os.path.join(cwd,imagepath))
    img = image.load_img(imagepath, target_size=(150, 150))
    x = image.img_to_array(img)
    #print('x before expand _dim', x)
    x = np.expand_dims(x, axis=0)
    #print('x after expand _dim', x)
    images = np.vstack([x])
    #print('images after vstack', images)
    classes = model.predict(images, batch_size=10)
    print(imagepath)
    print(classes)