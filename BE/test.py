import json
from fastapi import FastAPI, Response
from pydantic import BaseModel

import uvicorn
from pyArango.connection import *

app = FastAPI()

username1 = 'root'
password1 = ""

class Req_body01(BaseModel):
    数据库名称: str
    集合名称: str
    文档名称: str
    文档键: str
    文档值: str

@app.post('/api/Databases/create')
def evaluation_data(item: Req_body01):
    conn = Connection(username=username1, password=password1)
    db = conn.createDatabase(name=item.数据库名称)

    tempCollection = db.createCollection(name=item.集合名称)
    doc1 = tempCollection.createDocument()
    doc1[item.文档键] = item.文档值
    doc1.save()
    output2 = {'结果':'成功!'}
    
    resp1 = json.dumps(output2, ensure_ascii=False)
    return Response(resp1, media_type="application/json")


if __name__ == "__main__":
    uvicorn.run('test:app', host="0.0.0.0", port=9999, reload=True)