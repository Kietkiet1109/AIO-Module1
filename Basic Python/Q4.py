import math
import random

def exercise4():
    num_samples = input('Input number of samples (integer number) which are generated: ')

    if not num_samples.isnumeric():
        print('Number of samples must be an integer number')
        return

    num_samples = int(num_samples)
    loss_name = input('Input loss name (MAE, MSE, RMSE): ')

    total = 0
    for sample in range(num_samples):
        pred = random.uniform(0,10)
        target = random.uniform(0,10)

        if loss_name == 'MAE':
            loss = abs(pred - target)
        elif loss_name == 'MSE' or loss_name == 'RMSE':
            loss = (pred - target) ** 2

        total += loss
        print('Loss name: %s, Sample: %i, Pred: %f, Target: %f, Loss: %f'
              %(loss_name, sample, pred, target, loss))

    final = total / num_samples
    if loss_name == 'RMSE':
        final = math.sqrt(final)

    print('Final %s: %f' %(loss_name, final))
    return


exercise4()
