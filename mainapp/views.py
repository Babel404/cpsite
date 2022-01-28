from django.shortcuts import render, redirect
from .models import Question
from random import *

def index(request):

	return render(request, 'mainapp/home.html')

def q1(request):

	title = 'NO JUDGMENT'

	if request.method == 'POST' :

		if not 'q1a1' in request.POST and 'q1a2' in request.POST and 'q1a3' in request.POST and 'q1a4' in request.POST and not 'q1a5' in request.POST:

			question = {
				'question':'Why is château perché trying to make you be non judgmental of yourself? (1 answer accepted)<br>Pourquoi est-ce que Château Perché t’invite à être dans le non-jugement envers toi-même? (1 bonne réponse)',
				'answer1':"To help you let go, to free yourself and experiment<br>Afin de t’aider à lâcher prise, te libérer et expérimenter",
				'answer2': "It helps you see clearly<br>Parce que ça t’aide à y voir plus clair",
				'answer3': "To help you cultivate a peaceful mind<br>Afin de t’aider à être en paix avec toi-même",
				'answer4':"All of the above<br>Toutes les réponses ci-dessus",
			}

			context = {
				'title' : title,

				'question' : question['question'],
				'answer1' : question['answer1'],
				'answer2' : question['answer2'],
				'answer3' : question['answer3'],
				'answer4' : question['answer4']
			}

			return render(request, 'mainapp/1q2.html', context)

		if  not 'q2a1' in request.POST and not 'q2a2' in request.POST and not 'q2a3' in request.POST and 'q2a4' in request.POST :

			question = {
				'question':'If you see someone naked on the dancefloor: (select the 3 correct answers)<br>Si tu vois quelqu’un nu sur le dancefloor: (sélectionne 3 bonnes réponses)',
				'answer1':"I'm happy this person accepts their body<br>Ahh, enfin quelqu’un qui accepte son corps",
				'answer2': "You stare?<br>Tu mates?",
				'answer3': "You smile?<br>Tu souris?",
				'answer4':"Why am I the only one naked on the dancefloor?<br>Pourquoi suis-je le/la seul·e nu·e sur le dancefloor?",
			}

			context = {
				'title' : title,

				'question' : question['question'],
				'answer1' : question['answer1'],
				'answer2' : question['answer2'],
				'answer3' : question['answer3'],
				'answer4' : question['answer4']
			}

			return render(request, 'mainapp/1q3.html', context)

		if 'q3a1' in request.POST and not 'qui3a2' in request.POST and 'q3a3' in request.POST and 'q3a4' in request.POST :
			return render(request, 'mainapp/res1.html')

	question = {
		'question':'Why is Château Perché trying to make you be non judgmental of others? (select the 3 correct answers)<br>Pourquoi est-ce que Château Perché t’invite à être dans le non-jugement envers les autres? (sélectionne 3 bonnes réponses)',
		'answer1':"Cuz you watched it on mainstream media?<br>Parce que tu as vu ça à la télé?",
		'answer2': "Non-judgment opens you up to more of life’s beauty<br>Parce que le non-jugement te permet de voir la vie d’une manière encore plus belle",
		'answer3': "To develop an empathic approach to people<br>Afin de développer de l’empathie envers les autres",
		'answer4': "It helps others to let go<br>Parce que ça t’aide à lâcher prise",
		'answer5': "Namaste",
	}

	"""


	question3 = {
		'question':'If you see someone naked on the dancefloor:',
		'answer1':"I'm happy this person accepts their body",
		'answer2': "You stare?",
		'answer3': "You smile?",
		'answer4':"Why am I the only one naked on the dancefloor?",
	}
	"""
	context = {
		'title' : title,

		'question' : question['question'],
		'answer1' : question['answer1'],
		'answer2' : question['answer2'],
		'answer3' : question['answer3'],
		'answer4' : question['answer4'],
		'answer5' : question['answer5'],

	}


	return render(request, 'mainapp/1q1.html', context)


def q2(request):

	title = 'LEAVE NO TRACE'

	if request.method == 'POST' :
		if not 'q1a1' in request.POST and 'q1a2' in request.POST and not 'q3a3' in request.POST :

			question = {
				'question':'Climate change, does that resonate with you? (select 2 correct answers)<br>Le changement climatique, ça te parle? (sélectionne les 2 bonnes réponses)',
				'answer1':"It's too late anyway<br>Foutu pour foutu!",
				'answer2': "I am Pachamama<br>Je suis Pachamama",
				'answer3': "I do and by doing, I am a part of the solution<br>Je fais et en faisant, je fais parti de la solution",
			}

			context = {
				'title' : title,

				'question' : question['question'],
				'answer1' : question['answer1'],
				'answer2' : question['answer2'],
				'answer3' : question['answer3'],
			}

			return render(request, 'mainapp/2q2.html', context)

		if not 'q2a1' in request.POST and 'q2a2' in request.POST and 'q2a3' in request.POST :

			question = {
				'question':"We promote a “ I come with Shuttle Bus Only transport mode”, why ? (Select 4 correct answers)<br>On met en avant le “je viens, mais seulement en navette”, pourquoi? (Sélectionne 4 bonnes réponses)",
				'answer1':"It’s way more ecological<br>C’est indiscutablement plus écologique",
				'answer2': "The budget we would use for parking slots can be reinjected in artistic realisations (the deco budget is the same as for Château Perché 2019 but with half the crowds’ size!!)<br>Le budget qu’on mettrait dans les places de parking pourrait être réinjecté dans les réalisations artistiques (le budget déco est le même que pour le château Perché 2019 mais avec moitié moins de monde!!)",
				'answer3': "I will benefit from a “Queue- cut at arrival”<br>Je bénéficierai d’un coupe-queue en arrivant",
				'answer4': "Because buses are faster than cars<br>Le bus c’est plus rapide",

			}

			context = {
				'title' : title,

				'question' : question['question'],
				'answer1' : question['answer1'],
				'answer2' : question['answer2'],
				'answer3' : question['answer3'],
				'answer4' : question['answer4'],

			}

			return render(request, 'mainapp/2q3.html', context)

		if 'q3a1' in request.POST and 'q3a2' in request.POST and 'q3a3' in request.POST and 'q3a4' in request.POST:
			return render(request, 'mainapp/res2.html')

	

	question = {
		'question':"Do you put your cigarettes butts in your grannys' flower pots? (1 correct answer)<br>Est-ce que tu jettes tes cigarettes dans les pots de fleurs de ta mère-grand? (1 bonne réponse)",
		'answer1':"Oopsy",
		'answer2': "Naaah, I've got my pocket ashtray<br>Naan, j’ai mon cendrier de poche of course!",
		'answer3': "It's okay, I'll throw them tomorrow<br>Ça vaaaa, je les mettrai dans un cendrier demain",
	}


	context = {
		'title' : title,

		'question' : question['question'],
		'answer1' : question['answer1'],
		'answer2' : question['answer2'],
		'answer3' : question['answer3'],
	}

	return render(request, 'mainapp/2q1.html', context)


def q3(request):

	title = 'CONSENT'

	if request.method == 'POST' :
		if 'q1a1' in request.POST and 'q1a2' in request.POST and not 'q1a3' in request.POST:

			question = {
				'question':'If you come to witness a delicate situation, you: (select 2 correct answers)<br>Si tu es témoin d’une situation délicate, tu: (sélectionne 2 bonnes réponses)',
				'answer1':"Look away, you'll forget about it anyway<br>Fais style que t’as rien vu, t’oublieras vite de toute façon",
				'answer2': "Inform one of the Château Perché crew members<br>Informes un des membres du crew Château Perché",
				'answer3': "Go and help whoever is experiencing difficulties<br>Va aider la personne en difficulté",
				'answer4' : "Continue dancing the night/day away<br>Tu continues à danser comme s’il n’y avait pas de lendemain"
			}


			context = {
				'title' : title,

				'question' : question['question'],
				'answer1' : question['answer1'],
				'answer2' : question['answer2'],
				'answer3' : question['answer3'],
				'answer4' : question['answer4'],
			}

			return render(request, 'mainapp/3q2.html', context)


		if not 'q2a1' in request.POST and 'q2a2' in request.POST and 'q2a3' in request.POST and not 'q2a4' in request.POST :
			return render(request, 'mainapp/res3.html')

	

	question = {
		'question':"According to you, which situation is not respecting consent? \[situation which is obviously not welcome at Château Perché\] (select 2 correct answers)<br>Selon toi, quelles sont les situations qui ne respectent pas le consentement?[situations qui ne sont évidemment pas les bienvenues au Château Perché] (sélectionne 2 bonnes réponses)",
		'answer1':"Someone you desire is being vulnerable (drugs, alcohol, other...), you take that opportunity to get closer and fulfill this desire<br>Quelqu’un que tu kiffes se retrouve dans un moment de vulnérabilité (drogues, alcool, autres…), tu saisis cette opportunité pour t’en rapprocher et tenter d’assouvir ton désir",
		'answer2': "Someone you desire is being vulnerable (drugs, alcohol, other...), you try to get closer cuz that’s what you desire, everyone is f****d up anyway<br>Quelqu’un que tu kiffes se retrouve dans un moment de vulnérabilité (drogues, alcool, autres…), tu saisis cette opportunité pour t’en rapprocher parce que c’est ce que tu désires, et de toute façon, tout le monde est éclaté",
		'answer3': "Someone you desire is being vulnerable (drugs, alcohol, other...), you want to get closer but hey, maybe this person just wants to enjoy and not get involved with your desire<br>Quelqu’un que tu kiffes se retrouve dans un moment de vulnérabilité (drogues, alcool, autres…), tu aimerai t’en rapprocher, mais attends, peut-être que cette personne est juste en train de kiffer et n’a pas envie de faire parti de ton désir",
	}

	

	context = {
		'title' : title,

		'question' : question['question'],
		'answer1' : question['answer1'],
		'answer2' : question['answer2'],
		'answer3' : question['answer3'],


	}

	return render(request, 'mainapp/3q1.html', context)



def q4(request):

	title = 'LOVE CAMP'

	if request.method == 'POST' :

		if 'q1a1' in request.POST and not 'q1a2' in request.POST and 'q1a3' in request.POST :

			return render(request, 'mainapp/res4.html')

	

	question = {
		'question':"What could it be? (select the 2 correct answers)<br>Qu’est ce que ça t’évoque? (sélectionne la bonne réponse)",
		'answer1':"A shelter when everything becomes too intense<br>Un refuge quand tout devient trop intense",
		'answer2': "My playground love?<br> Mon “playground love”?",
		'answer3': "A place to learn and explore around sexuality<br>Un endroit où apprendre et explorer",
	}

	

	context = {
		'title' : title,

		'question' : question['question'],
		'answer1' : question['answer1'],
		'answer2' : question['answer2'],
		'answer3' : question['answer3'],


	}

	return render(request, 'mainapp/4q.html', context)


def q5(request):

	if request.method == 'POST' :

		if 'q1a1' in request.POST and not 'q1a2' in request.POST and not 'q1a3' in request.POST :

			return render(request, 'mainapp/res5.html')

	title = 'BEST HUMAN'

	question = {
		'question':"Are you willing to offer and to receive?  (select the correct answer)<br>Es-tu prêt·e à offrir et à recevoir? (sélectionne la bonne réponse)",
		'answer1':"F**K Yeaaaah, this is how I roll<br>F**K Yeaaaah, je vis pour ça",
		'answer2': "I'm used to receiving, give me!<br>J’ai l’habitude de recevoir, donne-moi!",
		'answer3': "Wtf, is it Xmas?<br>Wtf,c’est noel?",
	}

	

	context = {
		'title' : title,

		'question' : question['question'],
		'answer1' : question['answer1'],
		'answer2' : question['answer2'],
		'answer3' : question['answer3'],


	}

	return render(request, 'mainapp/5q.html', context)


def q6(request):

	if request.method == 'POST' :

		if 'q1a1' in request.POST and not 'q1a2' in request.POST and not 'q1a3' in request.POST :

			return render(request, 'mainapp/res6.html')

	title = 'COSTUME'

	question = {
		'question':"Are you willing to get creative?  (select the 2 correct answers)<br>Es-tu prêt·e à laisser parler ta créativité? (sélectionne les bonnes réponses)",
		'answer1':"Oh yeaah, I definitely want to be a part of the magic!<br>Oh yeaah, trop envie de contribuer à la magie!",
		'answer2': "A hat, a cape, should do the trick<br>Un chapeau, une cape, ça devrait le faire",
		'answer3': "Finally a platform where I can express myself<br>Enfin une plateforme où je vais pouvoir m’exprimer",
	}

	

	context = {
		'title' : title,

		'question' : question['question'],
		'answer1' : question['answer1'],
		'answer2' : question['answer2'],
		'answer3' : question['answer3'],


	}

	return render(request, 'mainapp/6q.html', context)

def res(request):

	return render(request, 'mainapp/youdidit.html')