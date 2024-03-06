from fastapi import FastAPI
import file
myapp=FastAPI()
maman=file.Maman
@myapp.get("/{maman_id}")
def index(maman_id:int):
    return maman[maman_id]
@myapp.post("/add_mamn")
def add(name:str,age:int):
    new_id=len(maman)+1
    
    new_maman={new_id :{"name":name,
                         "age":age
                 }
               }
    maman.update(new_maman)
    return maman
