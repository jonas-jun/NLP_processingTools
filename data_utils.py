#-*-coding:utf-8-*-

from collections import defaultdict
import os
from typing import Dict

def load_txt(file, split_by = '\t', num_cat=3, num_txt=4) -> Dict:
    '''
    @params
    file: file path to load
    split_by: tsv --> '\t'
    num_cat: category index, line.split('\t')[3] is category?
    num_txt: text index, line.split('\t')[4] is review text?
    '''
    print('Start to load {}'.format(file))
    rst = defaultdict(lambda: list())
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip().split(split_by)
            rst['cat'].append(line[num_cat])
            rst['text'].append(line[num_txt])
    print('Finish loading {:,} samples'.format(len(rst['cat'])))
    return rst

def cut_tsv(in_file, out_dir, cut=1000000):
    '''
    @params
    in_file: \t seperated text file
    out_dir: dir to save
    cut: cut every () samples
    '''
    if not os.path.exists(out_dir): os.mkdir(out_dir)
    
    print('START to load {}'.format(in_file))
    with open(in_file, 'r') as f:
        lines = f.readlines()
    length = len(lines)
    print('FINISHI loading {}'.format(in_file))

    start_idx = [i*cut for i in range((length//cut) + 1)]
    start_idx.append(length) # last idx
    nums = 0
    print('START to write {}'.format(out_dir))
    for i in range(len(start_idx)-1):
        pool = lines[start_idx[i]:start_idx[i+1]]
        fname = in_file.split('.')[0] + '_{:02d}.txt'.format(i) # name of export files
        
        with open(os.path.join(out_dir, fname), 'w', encoding='utf-8') as f:
            for line in pool:
                f.write(line.rstrip()+'\n')
                nums += 1
            print('  {:,}/{:,} exported'.format(nums, length))
    print('FINISH writing {}'.format(in_file))
