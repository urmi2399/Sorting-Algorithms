import numpy as np
import os

def content_generate(count):
    with open(f"arr{count}.txt","w+") as f:
        for _ in range(count):
            sample = list(np.random.randint(low=0, high=99, size=3))
            sample_sum = sum(sample)
            # f.write(f"{' '.join(map(str,sample))} {sample_sum}\n")
            f.write(f"{' '.join(map(str,sample))} \n")

def readFile(file):
    with open(file,"r") as f:
        content = f.read()
    content_dict={}
    sum_list = []
    for list_ in content.split("\n"):
        if list_:
            numbers = tuple(list_.split()[:3])
            number_sum = sum(tuple((map(int,numbers))))
            if number_sum not in content_dict.keys():
                content_dict[number_sum] = [numbers]
            else:
                content_dict[number_sum].append(numbers)
            content_dict[numbers] = number_sum
            sum_list.append(number_sum)
    return content_dict, sum_list

def writeFile(file,sorted_list,content_dict, time_taken):
    sum_list = []
    with open(file,"w+") as f:
        for number in sorted_list:
            if number not in sum_list:
                sum_list.append(number)
                for list_ in content_dict[number]:
                    f.write(f"{' '.join(list_)} {str(number)} \n")
        f.write(f"Time taken to sort the array is :{time_taken}")