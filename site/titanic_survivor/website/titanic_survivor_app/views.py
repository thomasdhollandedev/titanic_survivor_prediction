from django.shortcuts import render
from titanic_survivor_app.api import getPercentageSurvived


def index(request):
    if request.method == 'GET':
        return render(request, "home.html")
    elif request.method == 'POST':
        
        try:
            form_data = request.POST.dict()
            
            print(form_data)

            bodyFormData = {
                "Age": form_data['age'],
                "Fare": form_data['fare'],
                "FamilySize": form_data['familySize'],
                "Pclass": form_data['class'],
                "Sex_male": form_data['sex'],
                "Embarked_Q": 1 if form_data['embarked'] == "2" else 0,
                "Embarked_S": 1 if form_data['embarked'] == "0" else 0,
            }
            percentage = int(getPercentageSurvived(bodyFormData).get("survival_probability") * 100)
            return render(request, "home.html", {"survival_probability": percentage, "form_data": form_data})
        except:
            return render(request, "home.html", {"error": "Une erreur est survenue. Assurez-vous d'avoir bien rempli tous les champs."})
