def euclid(p, q):
    """Return the euclidean distance.
    Args:
        p (list): p vector
        q (list): q vector

    Returns:
        euclidean distance
    """
    dist = 0
    for p_i, q_i in zip(p, q):
        dist += (q_i - p_i) ** 2
    return dist ** 0.5
