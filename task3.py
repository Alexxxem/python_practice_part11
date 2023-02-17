# 3. Рефакторинг.
# Дано: неоптимальный код.
#
# Задание: оптимизировать следующий код.

# def responses_creator(item_ids):
#     item_ids = [None] if item_ids is None else item_ids
#
#     responses = []
#     for item_id in item_ids:
#         new_response = dict(item_id=item_id)
#         responses.append(new_response)
#     return responses


def create_response(item_ids):
    item_ids = [None] if item_ids is None else item_ids

    responses = [dict(item_id=_) for _ in item_ids]
    return responses


print(create_response([1, 2, 3]))
print(create_response("hello"))
print(create_response(5))

