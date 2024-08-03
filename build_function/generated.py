def sum_lst(lst):
    try:
        total = sum(lst)
        return {"status": "ok", "sum": total}
    except TypeError:
        return {"status": "error", "sum": None}