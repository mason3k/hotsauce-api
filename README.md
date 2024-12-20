[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)](https://github.com/pre-commit/precommit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?&style=for-the-badge)](https://pycqa.github.io/isort/)
![GitHub last commit](https://img.shields.io/github/last-commit/mason3k/scripts?style=for-the-badge)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg?style=for-the-badge)](https://github.com/PyCQA/bandit)

# Hot Sauce API

A test project to learn FastAPI by creating a hot sauce API!

## Usage 

GET, DELETE, POST, and PUT supported

Example calls:

*Get all sauces*: `hotsauce-sujones.pythonanywhere.com/sauces/`

*Get sauce by id*: `hotsauce-sujones.pythonanywhere.com/sauces/1`

Example response:
```json
{
    "name": "Frank's RedHot",
    "brand": "Frank's",
    "scoville_scale": 450,
    "ingredients": [
        "Aged Cayenne Red Peppers",
        "Distilled Vinegar"
    ],
    "flavor_notes": [
        "Tangy",
        "Spicy"
    ],
    "bottle_size": 12.0,
    "price": "3.99"
}
```

## Developing

```shell
uvicorn fastapi_demo.main:app --reload
```
