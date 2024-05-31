from fastapi import FastAPI

# uvicorn main:app --reload - запуск в терминале
app = FastAPI()


@app.get('/users')
async def all_users():
    # return '1.David, 2.Ruslan, 3.John'
    return {'User': 'Dmitri', 'User2': 'Jora'}


@app.post('/products')
async def all_products(title: str, price: int):
    return {'status': f'Your product name {title} and price {price}'}
