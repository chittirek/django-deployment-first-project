from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	ss = "<center><h2 style='color:Blue;'>Hello User, Welcome to Django First-Project First-App</h2><hr /></center>";
	return HttpResponse(ss);

def show(request): 
	ss = '''
	HTML Webpage to display 'Welcome-Message' with different Headings
<html>
	<head>
		<title>***Weclome-Page***</title>
		<style>
			h1{
				color:white;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color='brown' width='95%'/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color='brown' width='85%'/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color='brown' width='75%'/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color='brown' width='65%'/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color='brown' width='55%'/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color='brown' width='45%'/>
		</center>
	</body>
</html>
''';
	return HttpResponse(ss); 
    
def display(request): #view-function (/welcome/)
	print("welcome/ url is requested & display() is executed");

def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
				}
				h2{
					color:Green;
				}
				h3{
					color:Red;
				}
				h1,h2,h3{
					background-color:plum;
					width:60%;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='80%'/>
				<h3>Have a nice day...</h3>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
				}
				h2{
					color:Green;
				}
				h3{
					color:Red;
				}
				h1,h2,h3{
					background-color:plum;
					width:60%;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='80%'/>
				<h3>''',ct,'''</h3>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
	    