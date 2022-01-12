# Mở file
file = open('data.txt','r')
# Đọc 1 dòng
data = file.readline()
data = data.split('\\n')
# Đọc nhiều dòng
# data = file.readlines()

# Xử lý dữ liệu, loại bỏ các ký tự không cần thiết \r & \t
for i in range(len(data)):
	data[i] = data[i].replace('\\r','')
	data[i] = data[i].replace('\\t','')

# Xóa các tag (các chữ nằm trong <>)
# Regex: <.+?>  <[^>]*>
import re
for i in range(len(data)):
	data[i] = re.sub(r'<.+?>','',data[i])

# another way: longer method

# for i in range(len(data)):
# 	tags = []
# 	for j in range(len(data[i])):
# 		if data[i][j] == '<':
# 			begin = j
# 		if data[i][j] == '>':
# 			end = j
# 			tags.append(data[i][begin:end+1])
# 	for tag in tags:
# 		data[i] = data[i].replace(tag,'')

# Xóa khoảng trắng
for i in range(len(data)):
	data[i] = data[i].strip()

# Xóa các dòng không có dữ liệu
data_unempy = []
for i in range(len(data)):
	if data[i] != '':
		data_unempy.append(data[i])
data = data_unempy		

# Xử lý định dạng tên & điểm số
name = data[7]
dob = data[8]
scores = data[9]

chars = [] # các ký tự đặc biệt (cột 1)
codes = [] # Code của ký tự đặc biệt (cột 2)

file_code = open('unicode.txt', encoding='utf8')
unicode_table = file_code.read().split('\n')

for code in unicode_table:
	x = code.split(' ')
	chars.append(x[0])
	codes.append(x[1])

# thay ký tự đặc biệt trong tên + môn học	
for i in range(len(chars)):
	name = name.replace(codes[i],chars[i])
	scores = scores.replace(codes[i],chars[i])

# Thay ký tự đặc biệt có số (vd &#192)
for i in range(len(name)):
	if name[i:i+2] == '&#':
		name = name.replace(name[i:i+6],chr(int(name[i+2:i+5])))

for i in range(len(scores)):
	if scores[i:i+2] == '&#':
		scores = scores.replace(scores[i:i+6],chr(int(scores[i+2:i+5])))		

# Change to lowercase
name = name.lower()
scores = scores.lower()

# split DOB
dob_list = dob.split('/')
dd = int(dob_list[0])
mm = int(dob_list[1])
yy = int(dob_list[2])

# xu ly diem
# remove ':'
scores = scores.replace('khxh: ','khxh   ')
scores = scores.replace('khtn: ','khtn   ')
scores = scores.replace(':','')
scores_list = scores.split('   ')

data = [name, str(dd), str(mm), str(yy)] # chỉ lấy các thông tin liên quan

# add row subject to data
subject_list = ['toán','ngữ văn','khxh','khtn','lịch sử','địa lí','gdcd','sinh học','vật lí','hóa học','tiếng anh']

for i in subject_list:
	if i in scores_list:
		data.append(str(float(scores_list[scores_list.index(i)+1])))
	else:
		data.append('-1')		


# Lưu dữ liệu vừa đọc sang 1 file sau xử lý
file_2  = open('cuong_test.txt',encoding='utf8',mode='w')
for i in range(len(data)):
	file_2.write(data[i]+',')

## Test xử lý chuỗi trong tag
# s = '<title>Show - S\xe1\xbb\x9f Gi\xc3\xa1o d\xe1\xbb\xa5c v\xc3\xa0 \xc4\x90\xc3\xa0o t\xe1\xba\xa1o TP HCM</title>'
# begin =[] # Vị trí của các dấu <
# end = [] # Vị trí của các dấu >
# for i in range(len(s)):
# 	if s[i] == '<':
# 		begin.append(i)
# 	if s[i] == '>':
# 		end.append(i)

# print(data)


