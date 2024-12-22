def get(sess):
    res = sess.get("breeds/image/random")
    return res
