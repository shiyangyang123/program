#nvidia-msi
import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
print(f"当前设备: {torch.device('cuda' if torch.cuda.is_available() else 'cpu')}")
