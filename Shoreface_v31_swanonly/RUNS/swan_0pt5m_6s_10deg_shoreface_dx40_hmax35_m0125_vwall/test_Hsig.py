from subprocess import call

H = ["0.0", "0.5", "1.0", "1.5"]
find_string = "&& change wave height &&"

pre_string = "BOUNDPAR2 SEGMENT IJ 0 0 0 100  CONSTANT PAR "
post_string = " 6. 270. 5."

expt_name1 = "swan_"
expt_name2 = "m_6s_10deg_shoreface_dx40_hmax35_m0125_vwall"

in_filename = "swan_shoreface.in"
base_filename = in_filename + ".base"

for Hstr in H:
	print("Running with ...")
	# Write out new .in file
	fbase = open(base_filename)
	fin = open(in_filename,"w")
	for line in fbase:
		if find_string in line:
			fin.write(pre_string+Hstr+post_string)
			print("H = "+Hstr+"m")
		else:
			fin.write(line)
	fbase.close()
	fin.close()

	run_name = expt_name1+Hstr.replace('.', 'pt')+expt_name2	
	log_name = "log."+run_name
	#print "building..."
	#call("./coawst.bash &> build.log",shell=True)	
	print("running...")
	call("mpirun -np 1 coawstM swan_shoreface.in > " + log_name,shell=True)
	print("copying...")
	call("mkdir RUNS/"+run_name,shell=True)
	call("cp * RUNS/"+run_name,shell=True)
	call("rm "+log_name,shell=True)

print("Done!")
