import torch 


### Case 1. 
gpu_tensor_1 = torch.tensor([
                    [2, 5, 8],
                    [1, 4, 7],
                    [3, 6, 9],
                    ],
                    device=torch.device("cuda:0"))
print(gpu_tensor_1.device)

### Case 2.
gpu_tensor_2 = torch.rand(size=(3, 4), device=torch.device("cuda:0"))
print(gpu_tensor_2.device)

### Case 3.
gpu_tensor_3 = torch.ones(size=(3, 4), device=torch.device("cuda:0"))
print(gpu_tensor_3.device)
