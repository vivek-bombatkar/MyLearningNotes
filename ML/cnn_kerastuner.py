import tensorflow as tf
from tensorflow import keras
import kerastuner as kt
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def model_builder(hp):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        # 512 neuron hidden layer
        tf.keras.layers.Dense(512, activation='relu',input_shape=(300, 300, 3)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    # Tune the learning rate for the optimizer
    # Choose an optimal value from 0.01, 0.001, or 0.0001

    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

    # model.compile(loss='binary_crossentropy',
    #               optimizer=RMSprop(lr=1e-4),
    #               metrics=['accuracy'])

    model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

    return model

if __name__ == '__main__':
    # (img_train, label_train), (img_test, label_test) = keras.datasets.fashion_mnist.load_data()
    # # Normalize pixel values between 0 and 1
    # img_train = img_train.astype('float32') / 255.0
    # img_test = img_test.astype('float32') / 255.0

    train_horse_dir = os.path.join('horse-or-human/horses')
    train_human_dir = os.path.join('horse-or-human/humans')
    validation_horse_dir = os.path.join('validation-horse-or-human/horses')
    validation_human_dir = os.path.join('validation-horse-or-human/humans')

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        fill_mode='nearest')

    validation_datagen = ImageDataGenerator(rescale=1/255)

    # Flow training images in batches of 128 using train_datagen generator
    train_generator = train_datagen.flow_from_directory(
        'horse-or-human/',  # This is the source directory for training images
        target_size=(300, 300),  # All images will be resized to 150x150
        batch_size=128,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

    # Flow training images in batches of 128 using train_datagen generator
    validation_generator = validation_datagen.flow_from_directory(
        'validation-horse-or-human/',  # This is the source directory for training images
        target_size=(300, 300),  # All images will be resized to 150x150
        batch_size=32,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

    tuner = kt.Hyperband(model_builder,
                         objective='val_accuracy',
                         max_epochs=10,
                         factor=3,
                         directory='my_dir',
                         project_name='intro_to_kt')
    stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
    tuner.search(train_generator, epochs=50, validation_split=0.2, callbacks=[stop_early])

    # Get the optimal hyperparameters
    best_hps=tuner.get_best_hyperparameters(num_trials=1)[0]

    print(f"""
    The hyperparameter search is complete. The optimal number of units in the first densely-connected
    layer is {best_hps.get('units')} and the optimal learning rate for the optimizer
    is {best_hps.get('learning_rate')}.
    """)
    # Build the model with the optimal hyperparameters and train it on the data for 50 epochs
    model = tuner.hypermodel.build(best_hps)
    history = model.fit(train_generator, epochs=5)

    val_acc_per_epoch = history.history['accuracy']
    best_epoch = val_acc_per_epoch.index(max(val_acc_per_epoch)) + 1
    print('Best epoch: %d' % (best_epoch,))
    hypermodel = tuner.hypermodel.build(best_hps)

    # Retrain the model
    hypermodel.fit(train_generator, epochs=best_epoch) #, validation_split=0.2

    eval_result = hypermodel.evaluate(validation_generator)
    print("[test loss, test accuracy]:", eval_result)
