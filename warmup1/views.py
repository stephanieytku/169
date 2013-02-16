# Create your views here.
from django.http import HttpResponse
from warmup1.models import userModel
from django.utils import simplejson as json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import StringIO

SUCCESS               =   1  # : a success
ERR_BAD_CREDENTIALS   =  -1  # : (for login only) cannot find the user/password pair in the database
ERR_USER_EXISTS       =  -2  # : (for add only) trying to add a user that already exists
ERR_BAD_USERNAME      =  -3  # : (for add, or login) invalid user name (only empty string is invalid for now)
ERR_BAD_PASSWORD      =  -4

MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

@csrf_exempt
def index(request):
    return render_to_response('client.html', {})
#    obj = userModel.objects.get(name="Stephanie")
#    return HttpResponse("Username: "+obj.name+" Password: "+obj.password+" Count: "+str(obj.count))

@csrf_exempt
def login(request):
    numberResponse = ''
    user = passwd = ''
    result=[]
    print "hi"
    if True:
        print "hi again"
        postrequest = literal_eval(request.body)
        user = postrequest['user']
        passwd = postrequest['password']
        try:
            theUser = userModel.objects.get(name=user, password=passwd)
            theUser.count = theUser.count+1
            theUser.save()
            result.append({'errCode': SUCCESS})
            result.append({'count': theUser.count})
        except:
            result.append({'errCode': ERR_BAD_CREDENTIALS})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

@csrf_exempt
def add(request):
    result=[]
    user = passwd = ''
    user = postrequest['user']
    passwd = postrequest['password']
    #function checks that the user does not exist, the username is not empty (password may be empty
    #On success - function adds a row to the database w/ count initialized to 1
    #on success - result is the count of logins
    #On failure the result is an error code
    if (user=="" or (len(user)>MAX_USERNAME_LENGTH)):
        result.append({'errCode':ERR_BAD_USERNAME})
    elif (len(password)>MAX_PASSWORD_LENGTH):
        result.append({'errCode':ERR_BAD_PASSWORD})
    elif(userModel.objects.filter(name=user)== None):
        newUser = userModel.objects.create(name=user, password=passwd, count=1)
        result.append({'errCode': SUCCESS})
    else:
        result.append({'errCode': ERR_USER_EXISTS})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')


@csrf_exempt
def TESTAPI_resetFixture(request):
    for obj in userModel.objects.all():
        obj.delete()
    result=[]
    result.append({'errCode':SUCCESS})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

@csrf_exempt
def TESTAPI_unitTests(request):
    buffer = StringIO.StringIO()
    suite = unittest.TestLoader().loadTestsFromTestCase(tests.SimpleTest)
    result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(suite)
    result = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')
  