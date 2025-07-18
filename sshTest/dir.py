import os
for index,file in enumerate(os.listdir('C:\\py-projects')):
    print(f"{index+1}.{file}")