early_stopping = EarlyStopping(patience=5, monitor='val_loss')

reduce_lr = ReduceLROnPlateau(monitor='val_loss', min_lr=0.001,
                        patience=5, mode='min',
                        verbose=1)

model_checkpoint = ModelCheckpoint(monitor='val_loss', 
                             filepath='./model-best-kaggle-tl.h5', 
                             save_best_only=True)

callbacks = [
    early_stopping,
    reduce_lr,
    model_checkpoint
]

history = model.fit(train_iterator,
                    validation_data=validation_iterator,
                    epochs=100,
                    callbacks=callbacks)
