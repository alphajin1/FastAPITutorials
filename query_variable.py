from fastapi import FastAPI
import uvicorn
from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# # skip, limit은 생략 가능 (default 값이 있으므로)
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
#
# # q는 선택적이며 기본값으로 None값이 됨
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# short=1, True, true, on, yes 모두 허용
# 또한 None이면 선택적 매개변수이고, 없다면 필수 매개변수임
# 필수 매개변수, 기본값 매개변수, 선택적 매개변수 3가지임
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
