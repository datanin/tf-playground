import tensorflow as tf

print("Using Tensorflow Version: {}.".format(tf.__version__))

h = tf.constant("Hello")
w = tf.constant(" World!")
hw = h + w

print("hw: {}".format(hw))

with tf.Session() as sess:
    ans = sess.run(hw)

print("ans: {}".format(ans))