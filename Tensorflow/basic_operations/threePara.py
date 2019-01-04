import tensorflow as tf

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output1 = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    output2 = sess.run(y, feed_dict={x: 'Test String', y: 123, z: 45.67})
    output3 = sess.run(z, feed_dict={x: 'Test String', y: 123, z: 45.67})

    print(output1)
    print(output2)
    print(output3)
