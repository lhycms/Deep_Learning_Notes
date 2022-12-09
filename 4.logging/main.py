'''
Descripttion: 
version: 
Author: sch
Date: 2022-03-09 11:47:31
LastEditors: sch
LastEditTime: 2022-03-14 13:55:38
'''
import json


def save_info(file_path:str, **kwargs):
    with open(file_path, "w") as f:
        json.dump(kwargs, f)


def load_info(file_path:str):
    with open(file_path, "r") as f:
        dict_1 = json.load(f)
    return dict_1["name"]


if __name__ == "__main__":
    file_path = "/Users/mac/我的文件/Notebook/Deep_Learning/PyTorch_TuTorial_youtube/logging/log.log"
    save_info(file_path, name="Liu", age=21)
    print(load_info(file_path))