import subprocess 

result = subprocess.check_output('curl -F "sobaodanh=02000021" diemthi.hcm.edu.vn/Home/Show')

print(result)	 

