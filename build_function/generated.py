def sum_lst(lst):
    try:
        return {'status': 'ok', 'sum': sum(lst)}
    except TypeError:
        return {'status': 'error', 'sum': None}