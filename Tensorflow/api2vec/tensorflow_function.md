#tf.random_uniform
###function
tf.random_uniform(shape,minval=0,maxval=None,dtype=tf.float32,seed=None,name=None) 
random_uniform:均匀分布随机数，范围为[minval,maxval]
###example 
tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))

#tf.nn.embedding_lookup
###function
tf.nn.embedding_lookup(params, ids, partition_strategy='mod', name=None, validate_indices=True, max_norm=None)
在params中查找与ids对应的表示。 
###example
tf.nn.embedding_lookup(embeddings, train_inputs)

#tf.truncated_normal
###function
tf.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)返回一个tensor其中的元素服从截断正态分布
###example
tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))