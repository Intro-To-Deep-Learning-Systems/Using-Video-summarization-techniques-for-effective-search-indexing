from helpers.dsnet import DSNet


def get_anchor_based():
    return DSNet("attention", 1024, 128, [4, 8, 16, 32], 8)


def get_model():
    return get_anchor_based()
