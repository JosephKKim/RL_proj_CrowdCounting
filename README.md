# RL_proj_CrowdCounting

This is RL project repository for Reinforcement Learning class 2022.

This repository is based on [Paper Official Github](https://github.com/poppinace/libranet)

For preparing data please refer the Paper Official Github.

Pretrained weights for reproducing the result I mentioned in the report will be released very soon.

Move the pretrained weights into the folder, and the path structure should be like this: 

````
$./trained_model/
├──── LibraNet_SHT_A.pth.tar
├──── <pretrained_file_name>.pth.tar
````

For reproducing the result, 

## If you want to change hyperparameters,

change the numbers below in the code train.py or train_duel.py

```python
parameters = {'TRAIN_SKIP':100,
             'BUFFER_LENGTH':10000,
             'ERROR_RANGE':0.5,
             'GAMMA':0.9,
             'batch_size':128,
             'Interval_N':57,
             'step_log':0.1,
             'start_log':-2,
             'HV_NUMBER':8,
             'ACTION_NUMBER':9,
             'ERROR_SYSTEM':0,
             'means':[[108.25673428], [ 97.02240046], [ 93.37483706]]}
```


for the learning rate, change the 0.00001 part below,

```python
learning_rate = 0.00001 * np.ones(200)
```

## For Training ddqn model command
```python
python train.py
```

## For Training dueling dqn model command
```python
python train_duel.py
```

Pretrained Weights are in [WEIGHTS](https://drive.google.com/drive/folders/1nCZoNiOPITRM6nV7ZdW1o3bblG-eeN_M?usp=sharing)

##  For evaluation command

```python
python Test_SHT_A.py
```

in Test_SHT_A.py, you can choose between LibraNet (DDQN) or LibraNet_duel(Duel DQN) in line 33/34.
change the file name of the pretrained weigths in line 35.

(Sorry most of the codes are hard coded)
