import os
def get_times(arr, index):
    times_arr = arr[index].split('-')
    start = int(times_arr[0])
    end = int(times_arr[1])
    return start, end

if __name__ == '__main__':
    x = {'id': '11', 'ids': '116'}
    print(x)
    for key, values in x.items():
        
    times_list = []
    times_int = []
    for key, values in x.items():
        times_list += values
    for times in times_list:
        start_time = int(times.split('-')[0])
        times_int.append(int(start_time))
    merged_videos = [x for _,x in sorted(zip(times_int, times_list))]
    print("Finished !")
