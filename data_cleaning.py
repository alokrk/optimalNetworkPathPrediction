import fingerprint
import os


def read_file(filename, directory):
    if filename is None:
        return
    output = []
    with open(os.path.join(directory,filename), 'r') as file_name:
        for line in file_name:
            words = [x.strip() for x in line.split('|')]
            for word in words:
                if word != '1' or word != '0':
                    word = ''.join(e for e in word if e.isalnum())
                    output.append(word)
    return output


def make_path_fingerprint(filename, directory, key_map):
    words = read_file(filename, directory)

    if words is None:
        return
    for word in words:
        f = fingerprint.Fingerprinter(word)
        k = f.get_ngram_fingerprint(n=1)
        if k in key_map:
            v = key_map[k]
            v.append(word)
        else:
            v = []
            v.append(word)
            key_map[k] = v

    return key_map


def assign_numbers(key_map):
    if key_map is None:
        return
    key_assign = 0
    num = {}
    for temp_key in key_map:
        if temp_key not in num:
            num[temp_key] = key_assign
        key_assign += 1
    return num


def change_pathFile_number():
    pass


def change_trainSet():
    pass

if __name__ == '__main__':
    filename = "./data/paths.txt"
    directory = "./data/train/"
    allFiles = tuple(file1 for file1 in os.listdir(directory))
    key_map = {}
    for filename1 in allFiles:
        key_map = make_path_fingerprint(filename1, directory, key_map)
#    count_key = 0
#    count_value = 0
#    for k,v in key_map.iteritems():
#        count_key += 1
#        for val in v:
#            count_value += 1
#    print count_key
#    print count_value

    new_map = assign_numbers(key_map)

    for k,v in new_map.iteritems():
        print k, v