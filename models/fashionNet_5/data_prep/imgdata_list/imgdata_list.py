
g_root = "/local2/home/tong/fashionRecommendation/models/fashionNet_5/data_prep/"

data_type = ['train_', 'val_', 'test_']
item_type = ['top.txt', 'bot.txt', 'sho.txt']

for i in range(0,len(data_type)):
		for k in range(0,len(item_type)):
			imgData_source = open(g_root+"lmdb_list/"+data_type[i]+item_type[k])
			imgData_target = open(g_root+"imgdata_list/"+data_type[i]+item_type[k],'w')

			for line in imgData_source:
				line_temp = line.split('/')
				new_line = "/local/tong/fashionRecommendation/data/images/"+line_temp[9]+"/"+line_temp[12]
				imgData_target.write(new_line)

			imgData_source.close()
			imgData_target.close()
