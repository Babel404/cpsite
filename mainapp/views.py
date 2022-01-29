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
				'question':'<p><b>Why is château perché trying to make you be non judgmental of yourself? (1 answer accepted)</b></p><p><i>Pourquoi est-ce que Château Perché t’invite à être dans le non-jugement envers toi-même? (1 bonne réponse)</i></p>',
				'answer1':"<b>To help you let go, to free yourself and experiment</b> / <i>Afin de t’aider à lâcher prise, te libérer et expérimenter</i>",
				'answer2': "<b>It helps you see clearly</b> / <i>Parce que ça t’aide à y voir plus clair</i>",
				'answer3': "<b>To help you cultivate a peaceful mind</b> / <i>Afin de t’aider à être en paix avec toi-même</i>",
				'answer4':"<b>All of the above</b> / <i>Toutes les réponses ci-dessus</i>",
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
				'question':'<p><b>If you see someone naked on the dancefloor: (select 3 correct answers)</b></p><p><i>Si tu vois quelqu’un nu sur le dancefloor: (sélectionne 3 bonnes réponses)</i></p>',
				'answer1':"<b>I'm happy this person accepts their body</b> / <i>Ahh, enfin quelqu’un qui accepte son corps</i>",
				'answer2': "<b>You stare?</b> / <i>Tu mates?</i>",
				'answer3': "<b>You smile?</b> / <i>Tu souris?</i>",
				'answer4':"<b>Why am I the only one naked on the dancefloor?</b> / <i>Pourquoi suis-je le/la seul·e nu·e sur le dancefloor?</i>",
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
		'question':'<p><b>Why is Château Perché trying to make you be non judgmental of others? (select 3 correct answers)</b></p><p><i>Pourquoi est-ce que Château Perché t’invite à être dans le non-jugement envers les autres? (sélectionne 3 bonnes réponses)</i></p>',
		'answer1':"<b>Cuz you watched it on mainstream media?</b> / <i>Parce que tu as vu ça à la télé?</i>",
		'answer2': "<b>Non-judgment opens you up to more of life’s beauty</b> / <i>Parce que le non-jugement te permet de voir la vie d’une manière encore plus belle</i>",
		'answer3': "<b>To develop an empathic approach to people</b> / <i>Afin de développer de l’empathie envers les autres</i>",
		'answer4': "<b>It helps others to let go</b> / <i>Parce que ça t’aide à lâcher prise</i>",
		'answer5': "<b>Namaste</b>",
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
				'question':'<p><b>Climate change, does that resonate with you? (select 2 correct answers)</b></p><p><i>Le changement climatique, ça te parle? (sélectionne les 2 bonnes réponses)</i></p>',
				'answer1':"<b>It's too late anyway</b> / <i>Foutu pour foutu!</i>",
				'answer2': "<b>I am Pachamama</b> / <i>Je suis Pachamama</i>",
				'answer3': "<b>I do and by doing, I am a part of the solution</b> / <i>Je fais et en faisant, je fais parti de la solution</i>",
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
				'question':"<p><b>We promote a “ I come with Shuttle Bus Only transport mode”, why ? (Select the correct answers)</b></p><p><i>On met en avant le “je viens, mais seulement en navette”, pourquoi? (Sélectionne la bonne réponse)</i></p>",
				'answer1':"<b>It’s way more ecological</b> / <i>C’est indiscutablement plus écologique</i>",
				'answer2': "<b>The budget we would use for parking slots can be reinjected in artistic realisations (the deco budget is the same as for Château Perché 2019 but with half the crowds’ size!!)</b> / <i>Le budget qu’on mettrait dans les places de parking pourrait être réinjecté dans les réalisations artistiques (le budget déco est le même que pour le château Perché 2019 mais avec moitié moins de monde!!)</i>",
				'answer3': "<b>I will benefit from a “Queue- cut at arrival”</b> / <i>Je bénéficierai d’un coupe-queue en arrivant</i>",
				'answer4': "<b>Because buses are faster than cars</b> / <i>Le bus c’est plus rapide</i>",
				'answer5': "<b>All of the above</b> / <i>Toutes les réponses ci-dessus</i>",

			}

			context = {
				'title' : title,

				'question' : question['question'],
				'answer1' : question['answer1'],
				'answer2' : question['answer2'],
				'answer3' : question['answer3'],
				'answer4' : question['answer4'],
				'answer5' : question['answer5'],

			}

			return render(request, 'mainapp/2q3.html', context)

		if not 'q3a1' in request.POST and not 'q3a2' in request.POST and not 'q3a3' in request.POST and not 'q3a4' in request.POST and 'q3a5' in request.POST :
			return render(request, 'mainapp/res2.html')

	

	question = {
		'question':"<p><b>Do you put your cigarettes butts in your grannys' flower pots? (1 correct answer)</b></p><p><i>Est-ce que tu jettes tes cigarettes dans les pots de fleurs de ta mère-grand? (1 bonne réponse)</i></p>",
		'answer1':"<b>Oopsy</b>",
		'answer2': "<b>Naaah, I've got my pocket ashtray</b> / <i>Naan, j’ai mon cendrier de poche of course!</i>",
		'answer3': "<b>It's okay, I'll throw them tomorrow</b> / <i>Ça vaaaa, je les mettrai dans un cendrier demain</i>",
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
				'question':'<p><b>If you come to witness a delicate situation, you: (select 2 correct answers)</b></p><p><i>Si tu es témoin d’une situation délicate, tu: (sélectionne 2 bonnes réponses)</i></p>',
				'answer1':"<b>Look away, you'll forget about it anyway</b> / <i>Fais style que t’as rien vu, t’oublieras vite de toute façon</i>",
				'answer2': "<b>Inform one of the Château Perché crew members</b> / <i>Informes un des membres du crew Château Perché</i>",
				'answer3': "<b>Go and help whoever is experiencing difficulties</b> / <i>Va aider la personne en difficulté</i>",
				'answer4' : "<b>Continue dancing the night/day away</b> / <i>Tu continues à danser comme s’il n’y avait pas de lendemain</i>"
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
		'question':"<p><b>According to you, which situation is NOT respecting consent? [situation which is obviously not welcome at Château Perché] (select 2 correct answers)</b></p><p><i>Selon toi, quelles sont les situations qui ne respectent PAS le consentement?[situations qui ne sont évidemment pas les bienvenues au Château Perché] (sélectionne 2 bonnes réponses)</i></p>",
		'answer1':"<b>Someone you desire is being vulnerable (drugs, alcohol, other...), you take that opportunity to get closer and fulfill this desire</b> / <i>Quelqu’un que tu kiffes se retrouve dans un moment de vulnérabilité (drogues, alcool, autres…), tu saisis cette opportunité pour t’en rapprocher et tenter d’assouvir ton désir</i>",
		'answer2': "<b>Someone you desire is being vulnerable (drugs, alcohol, other...), you try to get closer cuz that’s what you desire, everyone is f****d up anyway</b> / <i>Quelqu’un que tu kiffes se retrouve dans un moment de vulnérabilité (drogues, alcool, autres…), tu saisis cette opportunité pour t’en rapprocher parce que c’est ce que tu désires, et de toute façon, tout le monde est éclaté</i>",
		'answer3': "<b>Someone you desire is being vulnerable (drugs, alcohol, other...), you want to get closer but hey, maybe this person just wants to enjoy and not get involved with your desire</b> / <i>Quelqu’un que tu kiffes se retrouve dans un moment de vulnérabilité (drogues, alcool, autres…), tu aimerai t’en rapprocher, mais attends, peut-être que cette personne est juste en train de kiffer et n’a pas envie de faire parti de ton désir</i>",
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
		'question':"<p><b>What could it be? (select 2 correct answers)</b></p><p><i>Qu’est ce que ça t’évoque? (sélectionne 2 bonnes réponses)</i></p>",
		'answer1':"<b>A shelter when everything becomes too intense</b> / <i>Un refuge quand tout devient trop intense</i>",
		'answer2': "<b>My playground love?</b> /  <i>Mon “playground love”?</i>",
		'answer3': "<b>A place to learn and explore around sexuality</b> / <i>Un endroit où apprendre et explorer</i>",
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
		'question':"<p><b>Are you willing to offer and to receive?  (select the correct answer)</b></p><p><i>Es-tu prêt·e à offrir et à recevoir? (sélectionne la bonne réponse)</i></p>",
		'answer1':"<b>F**K Yeaaaah, this is how I roll</b> / <i>F**K Yeaaaah, je vis pour ça</i>",
		'answer2': "<b>I'm used to receiving, give me!</b> / <i>J’ai l’habitude de recevoir, donne-moi!</i>",
		'answer3': "<b>Wtf, is it Xmas?</b> / <i>Wtf,c’est noel?</i>",
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

		if 'q1a1' in request.POST and not 'q1a2' in request.POST and 'q1a3' in request.POST :

			return render(request, 'mainapp/res6.html')

	title = 'COSTUME'

	question = {
		'question':"<p><b>    Are you willing to get creative and to be RESPECTFUL towards the chosen theme?  (select the correct answers)</b></p><p><i>    Es-tu prêt·e à laisser parler ta créativité et à créer ton costume dans le RESPECT du thème choisi? (sélectionne les bonnes réponses)</i></p>",
		'answer1':"<b>Oh yeaah, I definitely want to be a part of the magic!</b> / <i>Oh yeaah, trop envie de contribuer à la magie!</i>",
		'answer2': "<b>A hat, a cape, should do the trick</b> / <i>Un chapeau, une cape, ça devrait le faire</i>",
		'answer3': "<b>Finally a platform where I can express myself</b> / <i>Enfin une plateforme où je vais pouvoir m’exprimer</i>",
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