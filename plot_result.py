import re
from matplotlib import pyplot as plt

fname = "REresult_duel.txt"
f = open(fname, "r")
mae_list = []
mse_list = []
while True:
    line = f.readline().strip()
    cont = line.split(",")
    for i, str in enumerate(cont):
        num = re.findall("\d+\.\d+", str)
        if len(num) == 0:
            continue
        if i == 1:
            mae = float(num[0])
            mae_list.append(mae)
        elif i == 2:
            mse = float(num[0])
            mse_list.append(mse)
            
        print(num)
    print(cont)
    # print(line)
    if not line:
        break
f.close()


plt.plot(mae_list, label = 'MAE')
plt.plot(mse_list, label = 'MSE')
# plt.savefig("mae.png")
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('MAE/MSE')
plt.savefig("{}.png".format(fname))