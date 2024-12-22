def get(sess):
    res = sess.get("breeds/list/all")
    return res
