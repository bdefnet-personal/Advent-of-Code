from functools import cache

g_device_mappings = {}

def count_paths(start, end):
    if start == end:
        return 1
    if start not in g_device_mappings:
        return 0
    return sum(count_paths(mapping, end) for mapping in g_device_mappings[start])

@cache
def find_paths(from_device, to_device, seen_fft, seen_dac):    
    
    if from_device == "fft":
        seen_fft = True
    elif from_device == "dac":
        seen_dac = True
        
    if from_device == to_device:
        if seen_fft and seen_dac:
            return 1
        else:
            return 0
    
    if from_device not in g_device_mappings:
        return 0
    
    num_paths = 0
    for mapping in g_device_mappings[from_device]:
        num_paths += find_paths(mapping, to_device, seen_fft, seen_dac)
    
    return num_paths

with open('input.txt', 'r') as f:
    content = f.read()
    lines = content.strip().split('\n')

    for device_mapping in lines:
        device, mappings = device_mapping.split(":")
        g_device_mappings[device] = mappings.split()

print(f"Part 1: {count_paths("you", "out")}")

num_paths = find_paths("svr", "out", False, False)
print(f"Part 2: {num_paths}")