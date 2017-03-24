"""
WangQL
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#interactive mode
###plt.ion()
n_observations = 100
xs = np.linspace(-3, 3, n_observations)
ys = np.sin(xs) + np.random.uniform(-0.5, 0.5, n_observations)
###ys = np.sin(xs)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([1]), name='weight')
W2 = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
# Y = W * X + b
Y_pred = tf.add(tf.add(tf.multiply(tf.pow(X, 2.0), W1), tf.multiply(X, W2)), b)
#Y_pred = tf.add(tf.add(tf.multiply(tf.pow(X, 3.0), W1), tf.multiply(X, W2)), b)
#use 3.0, we get linear_regiression3.png which shows better result

"""
reduce_sum

'x' is [[1, 1, 1]
        [1, 1, 1]]
tf.reduce_sum(x) ==> 6
tf.reduce_sum(x, 0) ==> [2, 2, 2]
tf.reduce_sum(x, 1) ==> [3, 3]
tf.reduce_sum(x, 1, keep_dims=True) ==> [[3], [3]]
tf.reduce_sum(x, [0, 1]) ==> 6
"""
# sum (Y_pred - Y)^2 / (n_observations - 1)
cost = tf.reduce_sum(tf.pow(Y_pred - Y, 2)) / (n_observations - 1)

# %% Use gradient descent to optimize W,b
# Performs a single step in the negative gradient
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# %% We create a session to use the graph
n_epochs = 1000
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    #Fit all training data
    prev_training_cost = 0.0
    for epoch_i in range(n_epochs):
        for(x, y) in zip(xs, ys):
            sess.run(optimizer, feed_dict = {X: x, Y: y})
        
        training_cost = sess.run(cost, feed_dict = {X: x, Y: y})
        print(training_cost)
        if np.abs(prev_training_cost - training_cost) < 0.000001:
                break
        prev_training_cost = training_cost

    yp = Y_pred.eval(feed_dict={X: xs}, session=sess)
    plt.plot(xs, yp)

plt.plot(xs, ys, 'ro')

plt.show()
plt.waitforbuttonpress()