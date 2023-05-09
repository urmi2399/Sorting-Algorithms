from tracemalloc import start
import create_data_files
import time
import os

def mergeSort(arr):
    start = time.time()
    if len(arr) > 1:

        # q is the midpoint of the array
        q = len(arr)//2
        L = arr[:q]
        R = arr[q:]

        # Sorting the divided arrays
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    end = time.time()
    # print(arr)
    # print ("Time to sort the array is :", end-start)
    return arr


def main():
    data = [20,100,1000,4000]
    for i in data:
        # create_data_files.content_generate(i)
        if not os.path.isfile(f"arr{i}.txt"):
            create_data_files.content_generate(i)
        data_dict, sum_list = create_data_files.readFile(f"arr{i}.txt")
        start = time.time()
        sorted_sum_list = mergeSort(sum_list)
        end = time.time()
        print(f"Time taken to sort array of {i} is : ",end-start)
        Time_taken = str(end-start)
        create_data_files.writeFile(f"arrMS_O_{i}.txt",sorted_sum_list,data_dict, Time_taken)

if __name__ == "__main__":
    main()
