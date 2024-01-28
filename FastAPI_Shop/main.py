import databases
import sqlalchemy
from sqlalchemy.orm import relationship, backref
from fastapi import FastAPI
from datetime import datetime
from typing import List
from models import UserIn, User, ProductIn, Product, OrderIn, Order
import random
from datetime import datetime
from sqlalchemy import func

DATABASE_URL = "sqlite:///shop.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

Users = sqlalchemy.Table(
    # Таблица пользователи
    "Users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, nullable=False),
    sqlalchemy.Column("first_name", sqlalchemy.String(15), nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String(15), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False),
   
 
    
)

Products = sqlalchemy.Table(
    # Таблица товары
    "Products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("descriptions", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False),
  
    

   
)


Orders = sqlalchemy.Table(
    # Таблица заказы
    "Orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, nullable=False),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("Users.id")),
    sqlalchemy.Column("product_id", sqlalchemy.ForeignKey("Products.id")),
    sqlalchemy.Column(
        "create_at", sqlalchemy.DateTime, nullable=False, default = func.now(),
    ),
    sqlalchemy.Column("status", sqlalchemy.String, nullable=False)
   
    
)


enginie = sqlalchemy.create_engine(DATABASE_URL, connect_args = {"check_same_thread":False})
metadata.create_all(enginie)

app = FastAPI()


# Функции подключкния и отключения от БД


@app.on_event("startup")
async def startup():
    """
    Создание соединения с базой
    данных при запуске приложения
    """
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """
    Закрытие соединения с базой данных
    при остановке прилодежения
    """
    await database.disconnect()


# Заполнение таблиц фейковыми данными
#=====================================

@app.get("/fake_users/{count}")
async def make_fake_users(count: int):
    """
    Заполение таблицы пользователи
    """
    for i in range(count):
        query = Users.insert().values(
            first_name=f"user{i}",
            last_name=f"surname{i}",
            email=f"mail{i}@mail.ru",
            password=f"Fake_pass{i}@#$",
        )
        await database.execute(query)
    return {"message": f"{count} фейковых пользователей создано"}



@app.get("/fake_products/{count}")
async def make_fake_products(count: int):
    """
    Заполнение таблицы товаров
    """
    for i in range(count):
        query = Products.insert().values(
            title = f"product title       {i}",
            descriptions = f"descriptions text    {i}",
            price = i + 10,
        )
        await database.execute(query)
    return {"message": f"{count} фейковых товаров создано"}




@app.get("/fake_orders/{count}")
async def make_fake_orders(count:int):
    """
    Заполнение таблицы заказы
    """
    for i in range(count):
        query = Orders.insert().values(
            user_id = random.randint(0,count),
            product_id = random.randint(0,count),
            create_at =  datetime.now(),
            status = f"example_satus    {i}"
        )
        await database.execute(query)
    return {"message": f"{count} фейковых заказов создано"}


# Вывод всех значений из таблиц (select all)
#(Пользователи, Товары, Заказы )
#=================================== 

@app.get("/all_users/", response_model = List[User])
async def get_all_users():
    """
    Получение всex пользователей 
    """
    query = Users.select()
    
    return await database.fetch_all(query)


@app.get("/all_product/",response_model=List[Product])
async def get_all_products():
    """
    Получение всех товаров
    """
    query = Products.select()
    
    return await database.fetch_all(query)



@app.get("/all_orders/", response_model = List[Order])
async def get_all_orders():
    """
    Получение всех заказов 
    """
    query = Orders.select()
    
    return await database.fetch_all(query)



# Получение одного экземпляра из модели
#========================================


# Cоздание одного экземпляра модели
#=====================================

@app.post("/users/", response_model=Users)
async def create_user(user: UserIn):
    """
    Создание пользователя
    """
    query = Users.insert().values(**user.model_dump())
    record_id = await database.execute(query)
    return{**user.model_dump(), "id": record_id}


@app.post("/products/", response_model=Products)
async def create_product(product: ProductIn):
    """
    Создание товара
    """
    query = Products.insert().values(**product.model_dump())
    record_id = await database.execute(query)
    return{**product.model_dump(), "id": record_id}


@app.post("/orders/", response_model=Orders)
async def create_order(order: OrderIn):
    """
    Создание заказа
    """
    query = Orders.insert().values(**order.model_dump())
    record_id = await database.execute(query)
    return{**order.model_dump(), "id": record_id}