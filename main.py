import glob

# from pprint import pprint

file_list=glob.glob("*.txt")

ovr_read = {}
num_file = 0
for id_files in file_list:
    num_file += 1
    num_line = 0
    with open(id_files, encoding='utf-8') as file:
        data = []
        for line_text in file:
            num_line += 1
            data.append(line_text.strip()+'\n')
        ovr_read[id_files] = data, num_line


save_file = [[0,0,0]]
for id in range(num_file-1):
    save_file.append([0,0,0])

n = 0
for id in ovr_read:
    if n == 0:
        save_file[0][0] = ovr_read[id][1]
        save_file[0][1] = id
        save_file[0][2] = ovr_read[id][0]
    else:
        flag = 0
        for i in range(n):
            if ovr_read[id][1] < save_file[i][0] and flag == 0:
                save_file.insert(i,[ovr_read[id][1], id, ovr_read[id][0]])
                save_file.pop(-1)
                flag = 1
            elif flag == 0 and i+1 == n:
                save_file[i+1][0] = ovr_read[id][1]
                save_file[i+1][1] = id
                save_file[i+1][2] = ovr_read[id][0]
    n += 1

with open('result.tx2','wt', encoding='utf-8') as file:
    for id in save_file:
        file.write(id[1]+'\n')
        file.write(str(id[0])+'\n')
        file.write("".join(id[2]))
