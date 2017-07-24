import tensorflow as tf
hello = tf.constant("hello Tensorflow!")
sess = tf.Session()

print(sess.run(hello))

##===========
x = 1
y = x + 9
print(y)

x = tf.constant(1,name='x')
x = tf.Variable(x+9,name='y')
print(y)







