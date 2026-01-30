from fastapi import FastAPI
from pydantic import BaseModel

from server.calc_lib.src.Calculator import Calculator

app = FastAPI(title="Calculator API")
calculator = Calculator()


class AddRequest(BaseModel):
    a: float
    b: float


class AddResponse(BaseModel):
    result: float


@app.post("/add", response_model=AddResponse)
def add_numbers(payload: AddRequest) -> AddResponse:
    return AddResponse(result=calculator.add(payload.a, payload.b))
