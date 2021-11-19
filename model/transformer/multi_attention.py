#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from tensorflow.keras.layers import *
import tensorflow as tf

from model.transformer.single_attention import SingleAttention


class MultiAttention(Layer):
    def __init__(self, d_k, d_v, n_heads,**kwargs):
        super(MultiAttention, self).__init__()
        self.d_k = d_k
        self.d_v = d_v
        self.n_heads = n_heads
        self.attention_heads = list()

    def build(self, input_shape):
        for i in range(self.n_heads):
            self.attention_heads.append(SingleAttention(self.d_k, self.d_v))
        self.linear = Dense(input_shape[0][-1], input_shape=input_shape, kernel_initializer='glorot_uniform',
                            bias_initializer='glorot_uniform')

    def call(self, inputs):
        attention = [self.attention_heads[i](inputs) for i in range(self.n_heads)]
        concat = tf.concat(attention, axis=-1)
        multi_linear = self.linear(concat)
        return multi_linear
