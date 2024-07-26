def sum_lst(lst):
    try:
        total = sum(lst)
        return {'status': 'ok', 'sum': total}
    except Exception as e:
        return {'status': 'error', 'msg': str(e)}