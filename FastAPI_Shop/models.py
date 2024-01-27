from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import List
from datetime import datetime


class UserIn(BaseModel):
    """
    Модель пользователя без ID
    """

    first_name: str = Field(..., title="Имя", min_length=5, max_length=15)
    last_name: str = Field(..., title="Фамилия", min_length=5, max_length=15)
    email: str = Field(..., title="Электронная почта", min_length=5, max_length=15)
    password: str = Field(..., title="Пароль", min_length=5, max_length=15)


class ProductIn(BaseModel):
    """
    Модель товара без ID
    """

    title: str = Field(..., title="Название", min_length=10, max_length=50)
    descriptions: str = Field(..., title="Описание", min_length=10, max_length=2000)
    price: float = Field(..., title="Цена", gt=0, le=10**10)


class OrderIn(BaseModel):
    """
    Модель заказа без ID
    """

    client: UserIn = Field(..., title="Покупатель")
    create_at: datetime = None
    product: ProductIn = Field(..., title="Товар")
    status : str = Field(..., title="Статус", min_length=10, max_length=50)


# =========Mодели с ID==============#


class User(BaseModel):
    """
    Модель пользователя c ID
    """

    id: int
    first_name: str = Field(..., title="Имя", min_length=5, max_length=15)
    last_name: str = Field(..., title="Фамилия", min_length=5, max_length=15)
    email: str = Field(..., title="Электронная почта", min_length=5, max_length=15)
    password: str = Field(..., title="Пароль", min_length=5, max_length=15)


class Product(BaseModel):
    """
    Модель товара c ID
    """

    id: int
    title: str = Field(..., title="Название", min_length=10, max_length=50)
    descriptions: str = Field(..., title="Описание", min_length=10, max_length=2000)
    price: float = Field(..., title="Цена", gt=0, le=10**10)


class Order(BaseModel):
    """
    Модель заказа c ID
    """

    id: int
    client: User = Field(..., title="Покупатель")
    create_at: None
    product: Product = Field(..., title="Товар")
    status : str = Field(..., title="Статус", min_length=10, max_length=50)
