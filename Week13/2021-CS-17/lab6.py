# MIT 6.034 Lab 6: Neural Nets
# Written by 6.034 Staff

from nn_problems import *
from math import e
INF = float('inf')


#### Part 1: Wiring a Neural Net ###############################################

nn_half = []

nn_angle = []

nn_cross = []

nn_stripe = []

nn_hexagon = []

nn_grid = []


#### Part 2: Coding Warmup #####################################################

# Threshold functions
def stairstep(x, threshold=0):
    if x >= threshold:
        return 1
    else:
        return 0

def sigmoid(x, steepness=1, midpoint=0):
    return 1/(1+e**(-steepness*(x-midpoint)))

def ReLU(x):
    return max(0, x)

# Accuracy function
def accuracy(desired_output, actual_output):
    return -0.5*(desired_output-actual_output)**2


#### Part 3: Forward Propagation ###############################################

def node_value(node, input_values, neuron_outputs):  # PROVIDED BY THE STAFF
    """
    Given 
     * a node (as an input or as a neuron),
     * a dictionary mapping input names to their values, and
     * a dictionary mapping neuron names to their outputs
    returns the output value of the node.
    This function does NOT do any computation; it simply looks up
    values in the provided dictionaries.
    """
    if isinstance(node, str):
        # A string node (either an input or a neuron)
        if node in input_values:
            return input_values[node]
        if node in neuron_outputs:
            return neuron_outputs[node]
        raise KeyError("Node '{}' not found in either the input values or neuron outputs dictionary.".format(node))
    
    if isinstance(node, (int, float)):
        # A constant input, such as -1
        return node
    
    raise TypeError("Node argument is {}; should be either a string or a number.".format(node))

def forward_prop(net, input_values, threshold_fn=stairstep):
    """Given a neural net and dictionary of input values, performs forward
    propagation with the given threshold function to compute binary output.
    This function should not modify the input net.  Returns a tuple containing:
    (1) the final output of the neural net
    (2) a dictionary mapping neurons to their immediate outputs"""

    neuron_outputs = {}  # Dictionary to store the outputs of neurons
    
    # Iterate over each neuron in the neural net
    for neuron in net:
        # Get the inputs for the current neuron
        inputs = [node_value(input_node, input_values, neuron_outputs) for input_node in neuron.inputs]
        
        # Calculate the weighted sum of inputs
        weighted_sum = sum(weight * input_value for weight, input_value in zip(neuron.weights, inputs))
        
        # Apply the threshold function to compute the output of the neuron
        output = threshold_fn(weighted_sum)
        
        # Store the output of the neuron in the dictionary
        neuron_outputs[neuron.name] = output
    
    # Return the final output of the neural net and the dictionary of neuron outputs
    return neuron_outputs[net[-1].name], neuron_outputs


#### Part 4: Backward Propagation ##############################################

def gradient_ascent_step(func, inputs, step_size):
    """Given an unknown function of three variables and a list of three values
    representing the current inputs into the function, increments each variable
    by +/- step_size or 0, with the goal of maximizing the function output.
    After trying all possible variable assignments, returns a tuple containing:
    (1) the maximum function output found, and
    (2) the list of inputs that yielded the highest function output."""
    
    max_output = float('-inf')
    best_inputs = None

    for i in range(3):
        for sign in [-1, 1]:
            new_inputs = inputs.copy()
            new_inputs[i] += sign * step_size

            output = func(*new_inputs)
            if output > max_output:
                max_output = output
                best_inputs = new_inputs

    return max_output, best_inputs

def get_back_prop_dependencies(net, wire):
    """Given a wire in a neural network, returns a set of inputs, neurons, and
    Wires whose outputs/values are required to update this wire's weight."""
    
    dependencies = set()
    
    # Check if the wire is connected to an input
    if wire in net['inputs']:
        dependencies.add(wire)
    
    # Check if the wire is connected to a neuron
    for neuron in net['neurons']:
        if wire in neuron['inputs']:
            dependencies.add(neuron['name'])
            dependencies.update(neuron['inputs'])
    
    # Check if the wire is connected to another wire
    for other_wire in net['wires']:
        if wire in other_wire['inputs']:
            dependencies.add(other_wire['name'])
            dependencies.update(other_wire['inputs'])
    
    return dependencies

def calculate_deltas(net, desired_output, neuron_outputs):
    """Given a neural net and a dictionary of neuron outputs from forward-
    propagation, computes the update coefficient (delta_B) for each
    neuron in the net. Uses the sigmoid function to compute neuron output.
    Returns a dictionary mapping neuron names to update coefficient (the
    delta_B values). """
    
    deltas = {}
    
    for neuron in net['neurons']:
        neuron_name = neuron['name']
        neuron_output = neuron_outputs[neuron_name]
        delta_B = neuron_output * (1 - neuron_output) * (desired_output - neuron_output)
        deltas[neuron_name] = delta_B
    
    return deltas

def update_weights(net, input_values, desired_output, neuron_outputs, r=1):
    """Performs a single step of back-propagation.  Computes delta_B values and
    weight updates for entire neural net, then updates all weights.  Uses the
    sigmoid function to compute neuron output.  Returns the modified neural net,
    with the updated weights."""

    # Compute delta_B values for each neuron
    deltas = calculate_deltas(net, desired_output, neuron_outputs)
    
    # Update weights for each neuron
    for neuron in net['neurons']:
        neuron_name = neuron['name']
        neuron_output = neuron_outputs[neuron_name]
        delta_B = deltas[neuron_name]
        
        # Update weights for each input of the neuron
        for i, input_value in enumerate(input_values):
            neuron['weights'][i] += r * delta_B * input_value
    
    return net



def back_prop(net, input_values, desired_output, r=1, minimum_accuracy=-0.001):
    """Updates weights until accuracy surpasses minimum_accuracy.  Uses the
    sigmoid function to compute neuron output.  Returns a tuple containing:
    (1) the modified neural net, with trained weights
    (2) the number of iterations (that is, the number of weight updates)"""
    
    iterations = 0
    accuracy = -1
    
    while accuracy < minimum_accuracy:
        neuron_outputs = forward_prop(net, input_values)
        net = update_weights(net, input_values, desired_output, neuron_outputs, r)
        iterations += 1
        accuracy = accuracy(desired_output, neuron_outputs)
    
    return net, iterations



#### Part 5: Training a Neural Net #############################################

ANSWER_1 = None
ANSWER_2 = None
ANSWER_3 = None
ANSWER_4 = None
ANSWER_5 = None

ANSWER_6 = None
ANSWER_7 = None
ANSWER_8 = None
ANSWER_9 = None

ANSWER_10 = None
ANSWER_11 = None
ANSWER_12 = None


#### SURVEY ####################################################################

NAME = None
COLLABORATORS = None
HOW_MANY_HOURS_THIS_LAB_TOOK = None
WHAT_I_FOUND_INTERESTING = None
WHAT_I_FOUND_BORING = None
SUGGESTIONS = None
