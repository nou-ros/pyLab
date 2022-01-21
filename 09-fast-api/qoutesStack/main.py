from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
def index(published: bool, limit: int = 10):
    # return{
    #     'data' : 'qoute list'
    #     }
    # only get 10 published qoutes.[query params]
    if published:
        return {
            'data' : f'{limit} published qoutes from db.'
            }
    else:
        return {
            'data': 'all blogs',
        }

@app.get('/about')
def about():
    return {'data' :'about page'}

@app.get('/qoute/unpublished')
def unpublished():
    return {'data': 'all unpublished qoutes'}

@app.get('/qoute/{id}')
def details(id: int):
    return {'data': id}


@app.get('/qoute/{id}/comments')
def comments(id:int):
    return {'data': ['1', '2']}