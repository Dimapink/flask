from pydantic import BaseModel, Field


class AdvertisementSchema(BaseModel):
    "Схема для запроса"
    
    title: str = Field(
        alias="title",
        description="Заголовок объявления",
        examples="Some titile", max_length=255
)
    description: str = Field(
        alias="description",
        description="Тело объявления",
        examples="Some advertisement text",
        max_length=255
)   
    owner: str | None = Field(
        alias="owner",
        description="Автор объявления",
        default=None,
        examples="John Dow",
        max_length=255,
    )

