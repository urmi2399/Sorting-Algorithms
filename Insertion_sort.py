import create_data_files
import time
import os

def insertionSort(arr):
    for present_index in range(len(arr)):
        previous_index = present_index - 1
        while(previous_index >= 0):
            if arr[present_index] < arr[previous_index]:
                arr[present_index], arr[previous_index] = arr[previous_index], arr[present_index]
                present_index = present_index-1
            previous_index = previous_index-1
    #print(arr)
    return arr

def main():
    data = [20,100,1000,4000]
    for i in data:
        # create_data_files.content_generate(i)
        if not os.path.isfile(f"arr{i}.txt"):
            create_data_files.content_generate(i)
        data_dict, sum_list = create_data_files.readFile(f"arr{i}.txt")
        start = time.time()
        sorted_sum_list = insertionSort(sum_list)
        end = time.time()
        print(f"Time taken to sort array of {i} is : ",end-start)
        time_taken = str(end-start)
        create_data_files.writeFile(f"arrIS_O_{i}.txt",sorted_sum_list,data_dict, time_taken)



if __name__ == "__main__":
    main()