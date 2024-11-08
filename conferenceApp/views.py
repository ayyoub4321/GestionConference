from django.contrib.auth import authenticate, logout
from django.contrib.sessions.models import Session
from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from django.urls import reverse


# Create your views here.
def index(request):
    
    return render(request,"index.html",)
def login(request):
    if request.method=="POST":
        email1=request.POST.get('email')
        passw=request.POST.get('password')
        if email1 and passw and email1!='' and passw!='':
            try:
                user=User1.objects.get(email=email1)
                print('USER ',user.email)
                if user.password==passw:
                    request.session['emailUser']=user.email
                    return redirect('conference')
                else:
                    return render(request,"app1/login.html",{"errorpassword":"Invalid password"})
            except:
                print("mochkila")
                x={"errormessage":"email incorrect",}
                return render(request,"app1/login.html",x) 
               
    return render(request,"app1/login.html",)
def registre(request):
    if request.method=="POST":
        nom=request.POST.get('name')
        prenom1=request.POST.get('prenom')
        email1=request.POST.get('email')
        passw=request.POST.get("password")
        role_user, created = Role.objects.get_or_create(role='USER')
        user=User1.objects.create(name=nom,prenom=prenom1,email=email1,password=passw,role=role_user)

    return render(request,'app1/registre.html',)

def conference(request):
    user=login_User(request)
    if user:
        try:
            mots=request.GET.get('searsh')
            if mots:
                conference=Conference.objects.filter(nom__contains=mots)
            else:
                conference=Conference.objects.all()
            x={'conferences':conference,
            'role':user.role.role
            }
            return render(request,'app1/dashbord.html',x)
        except:
            print("mochkila22")
            return  redirect('login')
    return  redirect('login')

def session(request):
    # try:
        user=login_User(request)
        
        if user:
            mots=request.GET.get('searsh')
            if mots:
                print("le mots est ",mots)
                session=Session.objects.filter(titre__contains=mots)
            else:
                session=Session.objects.all()
            x={'sessions':session,
               "role":user.role.role
               }
            return render(request,'app1/dashbord.html',x)
        else:
            print("mochkila1")
            return redirect('login')
    # except:
    #     print("mochkila22")
    #     return  redirect('login')
def ajouterSession(request):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        conferences=Conference.objects.all()
        if request.method=="POST":
            titre=request.POST.get('titre')
            date=request.POST.get('date')
            heureDebut=request.POST.get('heureDebut')
            heureFin=request.POST.get('heureFin')
            description=request.POST.get('description')
            idConference=request.POST.get('idConference')
            if titre and date and heureDebut and heureFin and description and titre !='' and date!='' and heureDebut!='' and heureFin!='' and description!='':
                conference=Conference.objects.get(id=idConference)
                session=Session.objects.create(titre=titre,date=date,heureDebut=heureDebut,heureFin=heureFin,description=description,conference=conference)
        return render(request,'app1/ajouterSession.html',{'conferences':conferences})
    else:
     return redirect('login')   
def modifierSession(request,id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        conferences=Conference.objects.all()
        session=Session.objects.get(id=id)
        if request.method=="POST":
            titre=request.POST.get('titre')
            date=request.POST.get('date')
            heureDebut=request.POST.get('heureDebut')
            heureFin=request.POST.get('heureFin')
            description=request.POST.get('description')
            idConference=request.POST.get('idConference')
            if titre and date and heureDebut and heureFin and description and titre !='' and date!='' and heureDebut!='' and heureFin!='' and description!='':
                conference=Conference.objects.get(id=idConference)
                session.titre=titre
                session.date=datetime.strptime(date,'%Y-%m-%d')
                session.heureDebut=datetime.strptime(heureDebut,'%H:%M:%S')
                session.heureFin=datetime.strptime(heureFin,'%H:%M:%S')
                session.description=description
                session.conference=conference
                session.save()
                return redirect('session')
    return redirect('login')
    
    return render(request,'app1/ajouterSession.html',{'conferences':conferences,'session':session})
def ajouterConference(request):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        if request.method=="POST":
            nom=request.POST.get('nom')
            lieu=request.POST.get('lieu')
            dateDebut=request.POST.get('dateDebut')
            dateFin=request.POST.get('dateFin')
            description=request.POST.get('description')
            print("les information Conferenc hh ",nom,lieu,dateDebut,dateFin,description,sep=" + ")
            if nom and nom!=''and lieu and lieu!=''and dateDebut and dateDebut!=''and dateFin and dateFin!=''and description and description!='':
                conference=Conference.objects.create(nom=nom,lieu=lieu,dateDebut=dateDebut,dateFin=dateFin,them=description)
                print("nom de conference ",conference.nom)
        return  render(request,'app1/ajouterConference.html')
    return redirect('login')

def modifierConference(request,id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        conference=Conference.objects.get(id=id)
        if request.method=="POST":
                nom=request.POST.get('nom')
                lieu=request.POST.get('lieu')
                dateDebut=request.POST.get('dateDebut')
                dateFin=request.POST.get('dateFin')
                description=request.POST.get('description')
                print([nom, lieu, dateDebut, dateFin, description])
                if all([nom, lieu, dateDebut, dateFin, description]):
                    conference.nom = nom
                    conference.lieu = lieu
                    conference.dateDebut = dateDebut
                    conference.dateFin = dateFin
                    conference.description = description
                    conference.save()  # Enregistrer les modifications dans la base de données
                    return redirect('conference')
    
        return  render(request,'app1/ajouterConference.html',{'conference':conference})
    return redirect('login')
def suprimerConference(request,id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        conference=Conference.objects.get(id=id)
        conference.delete()
        return redirect('conference')
    return redirect('login')
def supprimerSession(request,id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        session=Session.objects.get(id=id)
        session.delete()
        return redirect('session')
    return redirect('login')
from django.http import Http404

def intervenant(request, id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        try:
            session = Session.objects.get(id=id)
        except Session.DoesNotExist:
            raise Http404("Session not found")

        session_intervenants = SessionIntervenant.objects.filter(session=session).select_related('intervenant')
        # intervenants=session_intervenants.intervenant
        mots=request.GET.get('searsh')
        if mots:
            session_intervenants = SessionIntervenant.objects.filter(session=session).select_related('intervenant')
            session_intervenants = session_intervenants.filter(
                intervenant__name__icontains=mots
            ) | session_intervenants.filter(
                intervenant__prenom__icontains=mots
            ) | session_intervenants.filter(
                intervenant__email__icontains=mots
            )
        else:
                session_intervenants = SessionIntervenant.objects.filter(session=session).select_related('intervenant')
        x= {'sessionintervenants': session_intervenants,
            'session':session}
        return render(request,'app1/dashbord.html',x)
    return redirect('login')

# Supposons que tu aies un modèle Role
def ajouterIntervenant(request, id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        if request.method == "POST":
            idSession = request.POST.get('idSession')
            session = Session.objects.get(id=id)
            name = request.POST.get('name')
            prenom = request.POST.get('prenom')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if all([name, prenom, email, password]):
                try:
                    intervenant = User1.objects.get(email=email)
                except User1.DoesNotExist:
                    # Récupérer ou créer un rôle
                    role, created = Role.objects.get_or_create(role='USER')  # Get the role instance
                    
                    # Créer l'intervenant avec le rôle
                    try:
                        intervenant = User1.objects.create(
                            name=name,
                            prenom=prenom,
                            email=email,
                            password=password,
                            role=role  # Correctly assign the role instance
                        )
                    except Exception as e:
                        # Log l'erreur ou la traiter
                        print(f"Erreur lors de la création de l'intervenant: {e}")
                        return render(request, 'app1/registre.html', {"session": session, "error": "Erreur lors de la création de l'intervenant."})

                try:
                    # Ajouter l'intervenant à la session
                    SessionIntervenant.objects.create(session=session, intervenant=intervenant)
                except Exception as e:
                    raise Http404(f"Erreur lors de l'ajout de l'intervenant à la session: {e}")
                return redirect(reverse('intervenant',args=[id]))
        session = Session.objects.get(id=id)
        return render(request, 'app1/registre.html', {"session": session})
    return redirect('login')

def modifierIntervenant(request,id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        try:
            session_intervenant = SessionIntervenant.objects.get(id=id)
            x={'session_intervenant':session_intervenant}
            if request.method=="POST":
                name = request.POST.get('name')
                prenom = request.POST.get('prenom')
                email = request.POST.get('email')
                id_intervenant=request.POST.get('id_intervenant')
                id_session=request.POST.get('id_session')
                if all([id_intervenant,email,prenom,name]):
                    intervenant=User1.objects.get(id=id_intervenant)
                    intervenant.name=name
                    intervenant.email=email
                    intervenant.prenom=prenom
                    intervenant.save()
                    return redirect(reverse('intervenant', args=[id_session]))
            return render(request,'app1/registre.html',x)
        except:
            return redirect(login)
    return redirect('login')
def suprimerIntervenant(request, id):
    user=login_User(request)
    if  user and user.role.role == 'GEST':
        try:
            session_intervenants = SessionIntervenant.objects.get(id=id)
            id_session=session_intervenants.session.id
            session_intervenants.delete()
        except:
            return  redirect(login)
        return redirect(reverse('intervenant', args=[id_session]))
    return redirect('login')
def deconnection(request):
    logout(request)
    return redirect('index')
def login_User(req):
    em=req.session.get('emailUser')
    try:
        user=User1.objects.get(email=em)
        return user
    except:
        return None
