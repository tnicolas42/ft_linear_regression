# ft_linear_regression

## Installation
Clone the project
```
git clone https://github.com/tnicolas42/ft_linear_regression
```
Install the required libs
```
pip3 install -r requirements.txt
```

## Test with the notebook
```
jupyter lab
```

## Test with python script
### Train
```
python3 train.py
```
To get usage:
```
python3 train.py --usage
```
Options:
```
--usage  # print the usage
--learning_rate=0.1 [<class 'float'>, <class 'int'>]  # set the learning rate for the linear regression algo
--theta=None [<class 'list'>]  # use a custom theta (instead of import it from a file)
--nb_iter=3500 [<class 'int'>]  # number of iteration to fit the linear regression
--data=data/data.csv [<class 'str'>]  # set the file to read the dataset
--data_km=km [<class 'str'>]  # set the name of km column in dataset
--data_price=price [<class 'str'>]  # set the name of price column in dataset
--theta_filename=data/theta.json [<class 'str'>]  # set the filename to import/export theta
```
Example:
```
python3 train.py --nb_iter=1500 '--theta=[0, 0]'  # to train from empty theta
```
To reset theta:
```
python3 train.py --nb_iter=0 '--theta=[0, 0]'
```

### Predict
```
python3 predict.py
```
To get usage:
```
python3 predict.py --usage
```
Options:
```
--theta=None [<class 'list'>]  # use a custom theta instead of import it from a file
--theta_filename=data/theta.json [<class 'str'>]  # set the filename to import/export theta
--car_km=None [<class 'int'>, <class 'list'>]  # the number of km driven by a car (to predict)
```
Example:
```
python3 predict.py --car_km=130000
python3 predict.py '--car_km=[130000, 350000]'
```
