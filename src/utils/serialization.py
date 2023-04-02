def serial(obj):
    base_dict = obj.__dict__.copy()
    base_dict.pop('_sa_instance_state')
    return base_dict
