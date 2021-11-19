#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
def check_data(func):
    def func_wrapper(*args, **kwargs):
        if args[0].data is None:
            raise Exception("Data is null")
        res = func(*args, **kwargs)
        return res

    return func_wrapper


def check_model(func):
    def func_wrapper(*args, **kwargs):
        if args[0].model is None:
            raise Exception("Model is null")
        res = func(*args, **kwargs)
        return res

    return func_wrapper
