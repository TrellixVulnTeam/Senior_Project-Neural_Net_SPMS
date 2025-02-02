import math
import pandas as pd


def oldOutputWeightUpdate(originalWeight, learningRate, actualOutput, expectedOutput, valuePassed): #outdated See new one below
    return originalWeight - (learningRate * (actualOutput - expectedOutput) * valuePassed) #w(ij) = w(ij) - n * (y(j) - t(j)) * x(i)


def NeuronPassFail(listOfWeights, listOfInputs):
    i = listOfWeights[-1]
    for index in range(len(listOfWeights) - 1):
        i += listOfInputs[index] * listOfWeights[index] #This should be weights * inputs
    return 1 / (1 + math.exp(-i))


def weightUpdate(originalWeight, learningRate, errorOutput, input): #Requires Error function first
    return originalWeight - (learningRate * errorOutput * input)


def getOutputError(actualOutput, targetOutput):
    return (actualOutput - targetOutput) * actualOutput * (1 - actualOutput)


def transfer_derivative(output):
    return output * (1.0 - output)


def getHiddenError(layer, index, layers):
    error = 0
    output = layers[layer][index].output
    for neuron in layers[layer + 1]:
        error += (neuron.weights[index] * neuron.Error)
    return output * (1 - output) * error
