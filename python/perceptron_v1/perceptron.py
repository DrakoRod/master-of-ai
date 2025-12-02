# from data import train_data, train_xor, train_nand, train_or, train_and
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

alpha = 0.5
bias = 1

weights = [0.1, 0.5, 0.7, 0.8, 0.2, 0.4]
weights_interations = []
weights_interations.append(weights)

def train():
    print("Training the Perceptron Multilayer...")

    i = 0

    for row in train_data:
        x1 = row[0] 
        x2 = row[1]
        print(f"For x1 = {x1} and x2 = {x2}")

        wi1 = weights_interations[i][0]
        wi1 = weights_interations[i][0]

        print(f" x1 = {x1} and x2 = {x2}")
        #h1 = calculate_h(x1, x2, )


        break

# Calculate h

def calculate_h(x1, x2, wi, wj):
    h = (x1 * wi) + (x2 * wj) * bias
    return h

# Activation function
def f_de_u(h):
    u = 1 / (1 + math.exp(-h))
    return u

def calculate_yhat(u1, u2, wh1, wh2):
    yhat = (u1 * wh1) + (u2 * wh2)

def error(yhat, y):
    error = yhat * (1 - yhat) * (y - yhat) 
    return error

# Dataset

train_data = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

target_xor = np.array(
    [
        [0],
        [1],
        [1],
        [0]])

target_nand = np.array(
    [
        [1],
        [1],
        [1],
        [0]])

target_or = np.array(
    [
        [0],
        [1],
        [1],
        [1]])

target_and = np.array(
    [
        [0],
        [0],
        [0],
        [1]])