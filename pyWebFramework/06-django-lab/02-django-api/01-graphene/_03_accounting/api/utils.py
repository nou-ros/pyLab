from django.db.models import Q, ForeignKey, ManyToManyField

def prepare_model_data_from_dict(model_data, data):
    copy_data = {} 
    fks = [field.name for field in model_data._meta.get_fields() if isinstance(field, ForeignKey) ]
    m2m = [field.name for field in model_data._meta.get_fields() if isinstance(field, ManyToManyField) ]

    for key, value in data.items():
        if key not in m2m:
            if fks and key in fks: 
                copy_data['{}_id'.format(key)] = value 
            else: 
                copy_data[key] = value
    return copy_data