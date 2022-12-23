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

** For Training ddqn model command**
```python
python train.py
```

** For Training dueling dqn model command**
```python
python train_duel.py
```



TODO: Change the weights and specify the model

** For evaluation command**
```python
python Test_SHT_A.py
```
