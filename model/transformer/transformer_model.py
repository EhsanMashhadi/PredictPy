#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from matplotlib import pyplot as plt
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

from model.transformer.multi_attention import MultiAttention
from model.transformer.single_attention import SingleAttention
from model.transformer.time_2_vector import Time2Vector
from model.transformer.transformer_encoder import TransformerEncoder
import tensorflow as tf
import numpy as np


class TransformerModel:
    seq_len = 128
    batch_size = 32
    d_k = 256
    d_v = 256
    n_heads = 12
    ff_dim = 256
    model = None

    def summary(self):
        self.model.summary()

    def create_model(self):
        time_embedding = Time2Vector(seq_len=self.seq_len)
        attention_layer1 = TransformerEncoder(d_k=self.d_k, d_v=self.d_v, n_heads=self.n_heads, ff_dim=self.ff_dim)
        attention_layer2 = TransformerEncoder(d_k=self.d_k, d_v=self.d_v, n_heads=self.n_heads, ff_dim=self.ff_dim)
        attention_layer3 = TransformerEncoder(d_k=self.d_k, d_v=self.d_v, n_heads=self.n_heads, ff_dim=self.ff_dim)

        in_seq = Input(shape=(self.seq_len, 5))
        x = time_embedding(in_seq)
        x = Concatenate(axis=-1)([in_seq, x])
        x = attention_layer1((x, x, x))
        x = attention_layer2((x, x, x))
        x = attention_layer3((x, x, x))
        x = GlobalAveragePooling1D(data_format='channels_first')(x)
        x = Dropout(0.1)(x)
        x = Dense(64, activation='relu')(x)
        x = Dropout(0.1)(x)
        out = Dense(1, activation='linear')(x)

        self.model = Model(inputs=in_seq, outputs=out)
        self.model.compile(loss='mse', optimizer='adam', metrics=['mae', 'mape'])

    def train(self, x_train, y_train, x_val, y_val, batch_size=32):
        callback = tf.keras.callbacks.ModelCheckpoint('Transformer+TimeEmbedding.hdf5',
                                                      monitor='val_loss',
                                                      save_best_only=True, verbose=1)
        history = self.model.fit(x_train, y_train,
                                 batch_size=batch_size,
                                 epochs=10,
                                 callbacks=[callback],
                                 validation_data=(x_val, y_val))
        print(history)

    def load(self):
        self.model = tf.keras.models.load_model('./Transformer+TimeEmbedding.hdf5',
                                                custom_objects={'Time2Vector': Time2Vector,
                                                                'SingleAttention': SingleAttention,
                                                                'MultiAttention': MultiAttention,
                                                                'TransformerEncoder': TransformerEncoder})
        print(self.model.summary)

    def evaluate(self, x_train, y_train, x_val, y_val, x_test, y_test):
        train_eval = self.model.evaluate(x_train, y_train, verbose=0)
        val_eval = self.model.evaluate(x_val, y_val, verbose=0)
        test_eval = self.model.evaluate(x_test, y_test, verbose=0)
        print(' ')
        print('Evaluation metrics')
        print('Training Data - Loss: {:.4f}, MAE: {:.4f}, MAPE: {:.4f}'.format(train_eval[0], train_eval[1],
                                                                               train_eval[2]))
        print('Validation Data - Loss: {:.4f}, MAE: {:.4f}, MAPE: {:.4f}'.format(val_eval[0], val_eval[1], val_eval[2]))
        print('Test Data - Loss: {:.4f}, MAE: {:.4f}, MAPE: {:.4f}'.format(test_eval[0], test_eval[1], test_eval[2]))

    def predict(self, x_test):
        train_pred = self.model.predict(x_test)
        return train_pred

    def plot_results(self, original_data, data_pred, type):
        fig = plt.figure(figsize=(15, 20))
        st = fig.suptitle("Transformer + TimeEmbedding Model", fontsize=10)
        st.set_y(0.92)
        ax11 = fig.add_subplot(311)
        # ax11.plot(np.arange(self.seq_len, data_pred.shape[0] + self.seq_len), data_pred, linewidth=3,
        #           label='Predicted IBM Closing Returns')
        ax11.plot(original_data, label='IBM Closing Returns')
        # ax11.plot(data_pred, label='IBM Predicted Closing Returns')

        ax11.set_title(type, fontsize=18)
        ax11.set_xlabel('Date')
        ax11.set_ylabel('IBM Closing Returns')
        ax11.legend(loc="best", fontsize=12)
        plt.show()
