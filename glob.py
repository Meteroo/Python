import glob
print (glob.glob(r"/home/mts/Documents/gitTUT/image/*.jpg"),"\n\n")#绝对路径
print(glob.glob(r'./*.py'))   #相对路径
print(glob.glob('*.py'))
print(glob.glob(r'*.py'))
arry = glob.glob('*.py')
brry = glob.glob(r'*.py')
print(arry[0])
c = arry[0]
print(c[0])
