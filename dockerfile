FROM python:3.12
WORKDIR /app
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY poetry.lock pyproject.toml ./
ENV PATH="/root/.local/bin:$PATH"
RUN poetry install --no-root
COPY . .
EXPOSE 8080
CMD ["poetry", "run", "python", "src/service.py"]