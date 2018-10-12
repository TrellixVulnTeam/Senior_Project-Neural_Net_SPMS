import math


def oldOutputWeightUpdate(originalWeight, learningRate, actualOutput, expectedOutput, valuePassed): #outdated See new one below
    return originalWeight - (learningRate * (actualOutput - expectedOutput) * valuePassed) #w(ij) = w(ij) - n * (y(j) - t(j)) * x(i)


def NeuronPassFail(listOfWeights, listOfInputs):
    i = 0
    for index in range(len(listOfWeights)):
        if (index+1) - len(listOfInputs) <= 0:
            i += listOfInputs[index] * listOfWeights[index] #This should be weights * inputs
        else:
            i += -1 * listOfWeights[index]
    return 1 / (1 + math.exp(-i))


def weightUpdate(originalWeight, learningRate, errorOutput, input): #Requires Error function first
    return originalWeight - (learningRate * errorOutput * input)


def getOutputError(actualOutput, targetOutput):
    return (actualOutput - targetOutput) * actualOutput * (1 - actualOutput)


def getHiddenError(neuronPassFailValue, index, layers):
    error = 0
    for neuron in layers[index + 1]:
        error += (neuron.weights[index] * neuron.error)
    return neuronPassFailValue * (1 - neuronPassFailValue) * error
