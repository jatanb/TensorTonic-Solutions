import torch

def neuron_forward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor) -> tuple:

    ans=0

    for i in range(len(inputs)):
        ans+=(inputs[i]*weights[i])

    y=torch.tanh(ans+bias)

    
        

    return tuple([ans+bias,y])
