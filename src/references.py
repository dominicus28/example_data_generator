reference_dict = {}

def add_reference(ref, value):
    if reference_dict.get(ref):
        reference_dict.get(ref).append(*value)
    else:
        reference_dict.update({ref: value})