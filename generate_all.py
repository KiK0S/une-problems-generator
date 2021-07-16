from os import system, popen
import json

numbers = ['16', '17', '18', '24', '25', '26', '27.a', '27.b']

tex_template = '''
\\documentclass[12pt]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[russian]{{babel}}
\\usepackage[margin=1.5in,left=1cm,right=1cm, top=2cm,bottom=2cm,bindingoffset=0cm]{{geometry}}
\\usepackage{{graphicx}}
\\usepackage{{color}}
\\usepackage{{amssymb}}
\\usepackage{{hyperref}}
\\usepackage{{amsmath}}
\\usepackage{{fancyhdr}}


\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[LE,RO]{{Автор: Амеличев Константин, \\href{{http://t.me/kik0s}}{{\\textcolor{{blue}}{{telegram}}}}, \\href{{http://github.com/kik0s}}{{\\textcolor{{blue}}{{github}}}}, \\href{{http://vk.com/i_tried_to_name_myself_kikos}}{{\\textcolor{{blue}}{{vk}}}} }}
\\fancyhead[RE,LO]{{Задача номер {0}}}
 
\\begin{{document}}

\\hspace{{\\fill}} \\\\
{1}

\\end{{document}}
'''

for n in numbers:
	for i in range(1, 21):
		values = json.loads(popen("python3 " + str(n) + "/generator.py").read())
		system("mkdir -p output/" + str(n))
		system("touch output/" + str(n) + "/" + str(i).zfill(2) + ".statement.txt")
		system("touch output/" + str(n) + "/" + str(i).zfill(2) + ".statement.tex")
		system("touch output/" + str(n) + "/" + str(i).zfill(2) + ".ans.txt")
		with open("output/" + str(n) + "/" + str(i).zfill(2) + ".statement.txt", "w") as f:
			f.write(str(values[0]))
		with open("output/" + str(n) + "/" + str(i).zfill(2) + ".statement.tex", "w") as f:
			result = tex_template.format(str(n) + "\\_" + str(i), str(values[0]).replace('≤', '$ \\le $').replace('\n', '\\\\').replace('*', '$\\cdot$'))
			f.write(result)
		system('pdflatex -shell-escape -output-directory=output/' + str(n) + " " + 'output' + '/' + str(n) + '/' + str(i).zfill(2) + ".statement.tex")
		with open("output/" + str(n) + "/" + str(i).zfill(2) + ".ans.txt", "w") as f:
			f.write(str(values[1]))
		if values[2] != '':
			system("touch output/" + str(n) + "/" + str(i).zfill(2) + ".in.txt")
			with open("output/" + str(n) + "/" + str(i).zfill(2) + ".in.txt", "w") as f:
				f.write(str(values[2]))
		system('rm output/' + str(n) + '/' + str(i).zfill(2) + '.statement.aux')
		system('rm output/' + str(n) + '/' + str(i).zfill(2) + '.statement.out')
		system('rm output/' + str(n) + '/' + str(i).zfill(2) + '.statement.tex')
		system('rm output/' + str(n) + '/' + str(i).zfill(2) + '.statement.log')