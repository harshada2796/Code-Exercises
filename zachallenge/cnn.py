from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras import backend as K
import keras
import common
import constants

def get_n_classes(dtype='accent'):
    return 3 if dtype == 'accent' else 2

def get_input_shape():
    feature_size = constants.FEATURE_SIZE
    frame_size = constants.NO_FRAME
    input_shape = None
    if K.image_data_format() == 'channels_first':
        input_shape = (1, feature_size, frame_size)
    else:
        input_shape = (feature_size, frame_size, 1)
    return input_shape

def reshape_input(x_train):
    feature_size = constants.FEATURE_SIZE
    frame_size = constants.NO_FRAME

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, feature_size, frame_size)        
    else:
        x_train = x_train.reshape(x_train.shape[0], feature_size, frame_size, 1)
    return x_train

def create_model(input_shape, n_classes):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
 
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
 
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
 
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(n_classes, activation='softmax'))
     
    return model

def get_validation_data(train_input, train_labels):
    no_recs = train_input.shape[0]
    valid_size = round(0.2 * no_recs)
    valid_input, valid_labels = train_input[:valid_size,:,:], train_labels[:valid_size]
    train_input, train_labels = train_input[valid_size:,:,:], train_labels[valid_size:]
    assert len(valid_labels) == valid_size
    assert len(train_labels) == no_recs - valid_size
    return train_input, train_labels, valid_input, valid_labels

def plot_and_show_history(history):
    # Loss Curves
    plt.figure(figsize=[8,6])
    plt.plot(history.history['loss'],'r',linewidth=3.0)
    plt.plot(history.history['val_loss'],'b',linewidth=3.0)
    plt.legend(['Training loss', 'Validation Loss'],fontsize=18)
    plt.xlabel('Epochs ',fontsize=16)
    plt.ylabel('Loss',fontsize=16)
    plt.title('Loss Curves',fontsize=16)
     
    # Accuracy Curves
    plt.figure(figsize=[8,6])
    plt.plot(history.history['acc'],'r',linewidth=3.0)
    plt.plot(history.history['val_acc'],'b',linewidth=3.0)
    plt.legend(['Training Accuracy', 'Validation Accuracy'],fontsize=18)
    plt.xlabel('Epochs ',fontsize=16)
    plt.ylabel('Accuracy',fontsize=16)
    plt.title('Accuracy Curves',fontsize=16)
    plt.show()

def train_and_predict(train_input, train_labels, test_input, test_labels):
    train_input, train_labels, valid_input, valid_labels = get_validation_data(train_input, train_labels)
    train_input  = reshape_input(train_input)
    test_input  = reshape_input(test_input)
    valid_input  = reshape_input(valid_input)
    n_classes = get_n_classes()
    train_labels = keras.utils.to_categorical(train_labels, n_classes)
    test_labels = keras.utils.to_categorical(test_labels, n_classes)
    valid_labels = keras.utils.to_categorical(valid_labels, n_classes)

    m = create_model(get_input_shape(), n_classes)
    batch_size = 32
    epochs = 2
    m.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = m.fit(train_input, train_labels, batch_size=batch_size, epochs=epochs, verbose=1, 
                   validation_data=(valid_input, valid_labels))    
    # write model to file
    m.evaluate(test_input, test_labels)    
    plot_and_show_history(history)

if __name__ == '__main__':
    train_input, train_labels, test_input, test_labels = common.get_accent_data()
    train_and_predict(train_input, train_labels, test_input, test_labels)