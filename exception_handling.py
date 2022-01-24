# pylint: disable=missing-module-docstring, missing-function-docstring
import random


def possibly_successful_API_call():
    rint = random.randint(0, 1)
    if rint == 0:
        return {"status": "error"}
    return {"status": "success", "data": "an important piece of data!"}


# TODO: use try/except to make this function handle the "error" output
# without crashing
def safe_API_call():
    response = possibly_successful_API_call()
    return response["data"]


if __name__ == "__main__":
    safe_API_call()
