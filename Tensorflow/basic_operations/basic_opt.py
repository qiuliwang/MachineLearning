import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
with tf.Session() as sess:
    print 'a + b = ', sess.run(a + b)
    print 'a * b = ', sess.run(a * b) 

# place holder
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

# operations
add = tf.add(a, b)
mult = tf.multiply(a, b)
with tf.Session() as sess:
    print 'a + b = ', sess.run(add, feed_dict = {a: 2, b: 4})
    print 'a * b = ', sess.run(mult, feed_dict = {a: 2, b: 4}) 