import torch

def neuron_forward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor) -> tuple:
    a = weights @ inputs + bias
    return a, torch.tanh(a)
    
