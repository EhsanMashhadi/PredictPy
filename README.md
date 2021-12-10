# PredictPy

PredictPy can be used for predicting crypto-currency and stock price prediction using different machine learning models.

👍 Your PRs are welcome! 👍

:bangbang: Warning: This is a predictor, but you should not invest your money solely based on the results of this tool!

![price-forecast](https://user-images.githubusercontent.com/6213824/137546144-cb0afe28-bf7e-4d8c-8eb8-94f6faed071e.png)

## Features

* Predicting crypto price using Prophet model
* Predicting crypto price using Transformers

## Dataset

* Different datasets are available using Yahoo finance API
* The `yfinance_data_cathcer` class handles datasets fetching

## Preprocessing

* Different preprocessing steps are required for both Prophet and transformers model
* The `smodel_data_preprocessor` class handles the preprocessing step for Prophet model which contains:
    - Using date column as index
    - Splitting data into training and testing sets
* The `tmodel_data_preprocessor` class handles the preprocessing step for Transformer model which contains:
    - Using date column as index
    - splitting data into training and testing sets
    - Use min-max scaler to normalize data
    - Convert columns values to the percent change value instead of absolute value

## Models

* One model is developed by using [Facebook Prophet](https://github.com/facebook/prophet) library
* Transformer model is developed by using the idea behind the [BERT](https://arxiv.org/abs/1810.04805)
  and [Time2Vec](https://arxiv.org/pdf/1907.05321.pdf)

## Project Structure

This project is developed using [MVP](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) design pattern

* The presenter module contains different presenters like `smodel_presenter` and `transfomer_presenter` class
* The `validator_wrapper` class is a python decorate for handling the nullability of `data` and `model` objects in
  presenter classes to validate these values before calling functions on them


## Setup

**Building on your computer:**

- Clone the repository
- Install Python 3.8+
- Install dependencies

    - Using CPU: ```pip install -r requirements-cpu.txt```
    - Using GPU: ```pip install -r requirements-gpu.txt```

**Using Docker:**
- Installing Docker
- Pulling the Docker image ```docker pull ehsanmashhadi/predictpy:v1.0.0```


## Run

In order to run the project, you have different options:

**Manually:** ```python main.py "method" "currency" "start_date"```

**Docker** ```docker run ehsanmashhadi/predictpy:v1.0.0 "method" "currency" "start_date"```

### Examples:

### Using prophet time series to predict next 10 days analysis:

**Manually:** ``` python main.py "rsm" "btc-usd" "2018-01-04"```

**Docker** ```docker run ehsanmashhadi/predictpy:v1.0.0 "rsm" "btc-usd" "2018-01-04"```

### Using prophet time series to evaluate the model based on last 12 days:

**Manually:** ```python main.py "tes" "btc-usd" "2018-01-04"```

**Docker** ```docker run ehsanmashhadi/predictpy:v1.0.0 "tes" "btc-usd" "2018-01-04"```

### Training transformer model (It may take long time to train the model):

**Manually:** ```python main.py "ttm" "btc-usd" "2018-01-04"```

**Docker** ```docker run ehsanmashhadi/predictpy:v1.0.0 "ttm" "btc-usd" "2018-01-04"```

### Evaluating the model using transformer model (You should train the transformer model first):

**Manually:** ```python main.py "pt" "btc-usd" "2014-01-04"```

**Docker** ```docker run ehsanmashhadi/predictpy:v1.0.0 "pt" "btc-usd" "2014-01-04"```

## Run tests

```python -m pytest tests/```

## Run tests with coverage

``` coverage run -m pytest tests/ && coverage report```

## Contributing

We greatly appreciate any contribution to this project. Before creating a new issue or pull request, please read the
contribution guidelines and policies [CONTRIBUTING](CONTRIBUTING.md) file.

## Licensing

This project is copyright by Ehsan Mashhadi. It is licensed under the MIT license. See the `LICENSE.txt` for the
complete license.