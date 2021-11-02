import glob

def read_file(list_files,data_in_files):
    num_f = 0
    for id_files in list_files:
        num_f += 1
        num_line = 0
        with open(id_files, encoding='utf-8') as file:
            data = []
            for line_text in file:
                num_line += 1
                data.append(line_text.strip() + '\n')
            data_in_files[id_files] = data, num_line
    return num_f

def init_mass(num):
    s_file = [[0, 0, 0]]
    for id in range(num - 1):
        s_file.append([0, 0, 0])
    return s_file

def write_file(name, s_file):
    with open(name, 'wt', encoding='utf-8') as file:
        for id in s_file:
            file.write(id[1] + '\n')
            file.write(str(id[0]) + '\n')
            file.write("".join(id[2]))

def sort_file(ovr_r, s_file):
    n = 0
    for id in ovr_r:
        if n == 0:
            s_file[0][0] = ovr_r[id][1]
            s_file[0][1] = id
            s_file[0][2] = ovr_r[id][0]
        else:
            flag = 0
            for i in range(n):
                if ovr_r[id][1] < s_file[i][0] and flag == 0:
                    s_file.insert(i, [ovr_r[id][1], id, ovr_r[id][0]])
                    s_file.pop(-1)
                    flag = 1
                elif flag == 0 and i + 1 == n:
                    s_file[i + 1][0] = ovr_r[id][1]
                    s_file[i + 1][1] = id
                    s_file[i + 1][2] = ovr_r[id][0]
        n += 1


file_list=glob.glob("*.txt")
ovr_read = {}
num_file = read_file(file_list, ovr_read)
save_file = init_mass(num_file)
sort_file(ovr_read, save_file)
write_file('result.tx2', save_file)
