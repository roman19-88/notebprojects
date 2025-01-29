def filter_by_state(list_dictionary):
    dict_state = []
    for i in list_dictionary:
         if i['state']=='EXECUTED':
             dict_state.append(i)

    return dict_state

