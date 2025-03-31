import glob , os
path= "C:\\Users\\benso\\Desktop\\python_練習\\"
os.chdir(path)
for file in glob.glob("*.py"):
    print('檔案',file)