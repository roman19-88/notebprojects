from pydoc import describe


def filter_by_state(list_dictionary):
    dict_state = []
    for i in list_dictionary:
         if i['state']=='EXECUTED':
             dict_state.append(i)

    return dict_state


def sort_by_date(data, descending=True):
    def data_get(item):
        return item['date']

    return sorted(data, key=data_get ,reverse=descending)










