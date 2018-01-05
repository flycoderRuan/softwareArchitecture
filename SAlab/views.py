from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from svmutil import *
import datetime
import time


# text = """<form method="post" action="/add/">
# 	<input type="text" name="a" value="%d"> + <input type="text" name="b" value="%d">
# 	<input type="submit" value="="> <input type="text" value="%d">
# 	</form>"""


# model = 
#     Parameters: [5x1 double]
#       nr_class: 2
#        totalSV: 259
#            rho: 0.0514
#          Label: [2x1 double]
#          ProbA: []
#          ProbB: []
#            nSV: [2x1 double]
#        sv_coef: [259x1 double]
#            SVs: [259x13 double]


@csrf_exempt
def index(request):
	# if 'a' in request.POST:
	# 	a = int(request.POST['a'])
	# 	b = int(request.POST['b'])
	# else:
	# 	a = 0
	# 	b = 0
	# return HttpResponse(text % (a,b,a+b))

	# y, x = svm_read_problem('./heart_scale')
	# m = svm_train(y[:], x[:], '-c 4')
	start = time.time()
	if 'name' in request.POST:
		name = request.POST['name']
		arrStr = name.split('#')

		with open('./data.txt', 'w') as f:
			for term in arrStr:
				if term :
					f.writelines(term+'\n')
		
		y, x = svm_read_problem('./data.txt')
		m = svm_train(y[:], x[:], '-c 4')
		end = time.time()
		print end-start
		return HttpResponse("success")

	return HttpResponse("fail")
		