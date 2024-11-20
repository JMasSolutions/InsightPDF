# env/__init__.py
import torch

def get_device():
    if torch.mps.is_available():
        device = torch.device('mps')
        print("Device being used:", device)
    elif torch.cuda.is_available():
        device = torch.device('cuda')
        print("Device being used:", device)
    else:
        device = torch.device('cpu')
        print("Device being used:", device)
    return device

# Initialize device information
DEVICE_INFO = get_device()