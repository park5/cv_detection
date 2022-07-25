from glob import glob

all_txt = glob("/Users/krc/Desktop/Hanbok_Raw_Data/Image/*.txt")

# txt = 0
# i=0
for txt in range(len(all_txt)):
    with open(all_txt[txt]) as f:
        txt_file = f.readlines()
    label_list = []
    for i in range(len(txt_file)):
        k = txt_file[i]
        # print(k)
        k = "0"+k[1:]
        # print(k)
        label_list.append(k)
        print(label_list)
    with open(all_txt[txt],"w") as f:
        f.write("".join(str(item) for item in label_list))
    print(f"{txt}/{len(all_txt)}")

