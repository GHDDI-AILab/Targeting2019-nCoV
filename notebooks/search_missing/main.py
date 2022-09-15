from re import S
import os
import fnmatch
from datetime import datetime
import pandas as pd


def find_all(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def find_first(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return os.path.join(root, name)
    return ''


df = pd.read_csv("missing_files.csv", header=None)
target_dir = "/data01/ghddi_public"

save_dir = '.'
now_ts = datetime.now().strftime("%Y%m%d_%H%M%S")

# save_fn = os.path.join(save_dir, "searching-result_"+now_ts+".log")
# with open(save_fn, "w") as fout:
#     for i, fname in enumerate(df[1]):
#         print(f'{i} ... '+fname)
#         result = find_all(fname, target_dir)
#         print(result)
#         fout.write(f'{i} ... ')
#         fout.write(fname+"\n")
#         for find_name in result:
#             fout.write(find_name+"\n")
        
results = []
for i, fname in enumerate(df[1]):
    print(f'{i} ... '+fname)
    result = find_first(fname, target_dir)
    results.append(result)

df['find_path'] = results
print(df['find_path'].value_counts())
save_fn = os.path.join(save_dir, "searching-result_"+now_ts+".csv")
df.to_csv(save_fn, index=False)
