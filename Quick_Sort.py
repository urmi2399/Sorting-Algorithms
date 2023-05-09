import create_data_files
import time
import os

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i = i+1
            (array[i],array[j]) = (array[j], array[i])
    (array[i+1],array[high]) = (array[high], array[i+1])
    return i+1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
    end = time.time()
    return array


def main():
    data = [20,100,1000,4000]
    for i in data:
        if not os.path.isfile(f"arr{i}.txt"):
            create_data_files.content_generate(i)
        data_dict, sum_list = create_data_files.readFile(f"arr{i}.txt")
        start = time.time()
        sorted_sum_list = quickSort(sum_list, 0,len(sum_list)-1)
        end = time.time()
        print(f"Time taken to sort array of {i} is : ",end-start)
        Time_taken = str(end-start)
        create_data_files.writeFile(f"arrQS_O_{i}.txt",sorted_sum_list,data_dict, Time_taken)

if __name__ == "__main__":
    main()