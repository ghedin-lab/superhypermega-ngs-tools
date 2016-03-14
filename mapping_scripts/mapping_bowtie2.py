import os

filelist = [('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a1.341000000083f5.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a1.342000000083f2.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a2.3410000000847d.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a2.3420000000847a.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a3.341000000084f4.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a3.342000000084f1.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a4.3410000000857c.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a4.34200000008579.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a5.341000000085f3.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a5.342000000085f0.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a6.3410000000867b.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a6.34200000008678.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a7.341000000086f2.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a7.342000000086ff.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_a8.3410000000877a.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_a8.34200000008777.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b1.34100000008403.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b1.34200000008400.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b2.3410000000848a.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b2.34200000008487.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b3.34100000008502.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b3.3420000000850f.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b4.34100000008589.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b4.34200000008586.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b5.34100000008601.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b5.3420000000860e.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b6.34100000008688.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b6.34200000008685.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_b7.34100000008700.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_b7.3420000000870d.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c1.34100000008410.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c1.3420000000841d.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c2.34100000008497.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c2.34200000008494.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c3.3410000000851f.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c3.3420000000851c.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c4.34100000008596.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c4.34200000008593.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c5.3410000000861e.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c5.3420000000861b.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c6.34100000008695.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c6.34200000008692.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_c7.3410000000871d.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_c7.3420000000871a.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d1.3410000000842d.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d1.3420000000842a.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d2.341000000084a4.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d2.342000000084a1.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d3.3410000000852c.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d3.34200000008529.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d4.341000000085a3.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d4.342000000085a0.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d5.3410000000862b.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d5.34200000008628.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d6.341000000086a2.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d6.342000000086af.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_d7.3410000000872a.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_d7.34200000008727.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e1.3410000000843a.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e1.34200000008437.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e2.341000000084b0.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e2.342000000084bd.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e3.34100000008539.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e3.34200000008536.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e4.341000000085bf.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e4.342000000085bc.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e5.34100000008638.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e5.34200000008635.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e6.341000000086be.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e6.342000000086bb.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_e7.34100000008737.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_e7.34200000008734.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f1.34100000008447.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f1.34200000008444.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f2.341000000084cd.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f2.342000000084ca.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f3.34100000008546.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f3.34200000008543.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f4.341000000085cc.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f4.342000000085c9.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f5.34100000008645.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f5.34200000008642.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f6.341000000086cb.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f6.342000000086c8.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_f7.34100000008744.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_f7.34200000008741.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g1.34100000008454.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g1.34200000008451.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g2.341000000084da.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g2.342000000084d7.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g3.34100000008553.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g3.34200000008550.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g4.341000000085d9.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g4.342000000085d6.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g5.34100000008652.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g5.3420000000865f.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g6.341000000086d8.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g6.342000000086d5.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_g7.34100000008751.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_g7.3420000000875e.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h1.34100000008460.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h1.3420000000846d.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h2.341000000084e7.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h2.342000000084e4.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h3.3410000000856f.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h3.3420000000856c.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h4.341000000085e6.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h4.342000000085e3.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h5.3410000000866e.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h5.3420000000866b.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h6.341000000086e5.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h6.342000000086e2.fastq.gz'),
('000000000-AE52Y_l01n01_flu_mrt-pcr_updated_h7.3410000000876d.fastq.gz','000000000-AE52Y_l01n02_flu_mrt-pcr_updated_h7.3420000000876a.fastq.gz')]


badlist = ['a8','b7','c7','d7','e7','f7','g7','h7']
path = '/data1/share/raw-sequencing-data/MiSeq/2015-03-11_AE52Y/'




for mate1,mate2 in filelist:
	# print mate1,mate2
	newname1 = mate1.split('.')[0].split('_')[5]
	newname2 = mate2.split('.')[0].split('_')[5]

	filepathmate1 = path+mate1
	filepathmate2 = path+mate2

	if newname1 in badlist:
		# print newname1
		pass
	else:
		print 'ANALYZING ' + newname1 + ' BEEP - BOOP'
		os.system("bowtie2 -x calref --un-conc unmapped."+newname1+" --local --no-mixed -p 20 -1 "+filepathmate1+" -2 "+filepathmate2+" -S "+newname1+".sam")
		os.system("samtools view -bS "+newname1+".sam > "+newname1+".bam")
		os.system("samtools sort "+newname1+".bam "+newname1+".sorted")
		os.system("samtools index "+newname1+".sorted.bam")
		os.system("rm "+newname1+".bam")
		os.system("rm "+newname1+".sam")













