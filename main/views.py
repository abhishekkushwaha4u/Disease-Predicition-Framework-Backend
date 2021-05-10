from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import (
    DiabetesSerializer,
    LiverSerializer,
    KidneySerializer,
    MalariaSerializer,
    PneumoniaSerializer,
    SkinSerializer,
    NearbyHospitalSerializer
)
import tensorflow as tf
import joblib
from sklearn.preprocessing import LabelEncoder
from chat.chat import (
    CHATBOT_MODEL,
    CHATBOT_ALL_WORDS,
    CHATBOT_TAGS,
    CHATBOT_INTENTS,
    chatbot_output
)

from .utility import image_predicition
from .nearby_hospitals import get_doctors


MALARIA_MODEL = tf.keras.models.load_model('main/ml_models/malaria.h5')
DIABETES_MODEL = joblib.load('main/ml_models/diabetes.joblib')
KIDNEY_MODEL = joblib.load('main/ml_models/kidney.joblib')
SKIN_MODEL = tf.keras.models.load_model('main/ml_models/skin.h5')
PNEUMONIA_MODEL = tf.keras.models.load_model('main/ml_models/pnem.h5')
LIVER_MODEL = joblib.load('main/ml_models/liver.joblib')



class TestRoute(APIView):
    def get(self, request):
        return Response({"status":"Working fine"})


class DiabetesAPIView(APIView):
    def post(self, request):
        serializer = DiabetesSerializer(data=request.data)
        if serializer.is_valid():
            preg=serializer.data.get('preg')
            glu=serializer.data.get('glu')
            bp=serializer.data.get('bp')
            skinthickness=serializer.data.get('skinthickness')
            insulin=serializer.data.get('insulin')
            bmi=serializer.data.get('bmi')
            pedigree_func=serializer.data.get('pedigree_func')
            age=serializer.data.get('age')
        else:
            return Response(serializer.errors, status=400)
        inp=[[preg, glu, bp, skinthickness, insulin, bmi, pedigree_func, age]]
        a=DIABETES_MODEL.predict(inp)
        return Response({"output":bool(a[0])})

class KidneyAPIView(APIView):
    def post(self, request):
        serializer = KidneySerializer(data=request.data)
        if serializer.is_valid():
            id = request.data.get('id')  
            age= request.data.get('age')
            bp = request.data.get('bp')
            sg = request.data.get('sg')
            al = request.data.get('al')
            su = request.data.get('su')
            rbc= request.data.get('rbc') 
            pc = request.data.get('pc') 
            pcc= request.data.get('pcc') 
            ba = request.data.get('ba') 
            bgr= request.data.get('bgr')
            bu = request.data.get('bu')
            sc = request.data.get('sc')
            sod= request.data.get('sod')
            pot= request.data.get('pot')
            hemo = request.data.get('hemo')
            pcv= request.data.get('pcv') 
            wc = request.data.get('wc') 
            rc = request.data.get('rc') 
            htn= request.data.get('htn') 
            dm = request.data.get('dm') 
            cad = request.data.get('cad') 
            appet = request.data.get('appet') 
            pe = request.data.get('pe') 
            ane= request.data.get('ane')
        else:
            return Response(serializer.errors, status=400)
        inp=[[age, bp, sg, al, su, LabelEncoder().fit_transform([rbc]), LabelEncoder().fit_transform([pc]), LabelEncoder().fit_transform([pcc]), LabelEncoder().fit_transform([ba]), bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, LabelEncoder().fit_transform([htn]), LabelEncoder().fit_transform([dm]), LabelEncoder().fit_transform([cad]), LabelEncoder().fit_transform([appet]), LabelEncoder().fit_transform([pe]), LabelEncoder().fit_transform([ane])]]
        a=KIDNEY_MODEL.predict(inp)
        if a[0] == 1:
            return Response({"output":"CKD"})
        else:
            return Response({"output":"Non CKD"})

class LiverAPIView(APIView):
    def post(self, request):
        serializer = LiverSerializer(data=request.data)
        if serializer.is_valid():
            Age  = request.data.get('Age')  
            Gender = request.data.get('Gender') 
            Total_Bilirubin = request.data.get('Total_Bilirubin')
            Direct_Bilirubin= request.data.get('Direct_Bilirubin')
            Alkaline_Phosphotase = request.data.get('Alkaline_Phosphotase')  
            Alamine_Aminotransferase = request.data.get('Alamine_Aminotransferase')  
            Aspartate_Aminotransferase = request.data.get('Aspartate_Aminotransferase')  
            Total_Protiens = request.data.get('Total_Protiens')
            Albumin = request.data.get('Albumin')
            Albumin_and_Globulin_Ratio = request.data.get('Albumin_and_Globulin_Ratio')
        else:
            return Response(serializer.errors, status=400)
        inp=[[Age, LabelEncoder().fit_transform([Gender]), Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]]
        a=LIVER_MODEL.predict(inp)
        if a[0] == 2:
            return Response({"output":"Stage-2"})
        else:
            return Response({"output": "Stage-1"})


class MalariaAPIView(APIView):
    def post(self, request):
        serializer = MalariaSerializer(data=request.data)
        if serializer.is_valid():
            output = image_predicition(request.FILES['image'], MALARIA_MODEL)
            return Response({"response": output})
        else:
            return Response(serializer.errors)

class PneumoniaAPIView(APIView):
    def post(self, request):
        serializer = PneumoniaSerializer(data=request.data)
        if serializer.is_valid():
            output = image_predicition(request.FILES['image'], PNEUMONIA_MODEL)
            return Response({"response": output})
        else:
            return Response(serializer.errors)

class SkinAPIView(APIView):
    def post(self, request):
        serializer = SkinSerializer(data=request.data)
        if serializer.is_valid():
            output = image_predicition(request.FILES['image'], SKIN_MODEL)
            return Response({"response": output})
        else:
            return Response(serializer.errors)

class ChatBotAPIView(APIView):
    def post(self, request):
        user = request.data.get('response')
        if user:
            response = chatbot_output(user, CHATBOT_MODEL, CHATBOT_ALL_WORDS, CHATBOT_TAGS, CHATBOT_INTENTS)
            return Response({"response": response})
        else:
            return Response({"response": "I cannot respond to blank responses!"})


class GetNearbyDoctors(APIView):
    def post(self, request):
        user_info = NearbyHospitalSerializer(data=request.data)
        if user_info.is_valid():
            city = user_info.data.get('city')
            pincode = user_info.data.get('pincode')
            return Response(get_doctors(city, pincode))
        else:
            return Response(user_info.errors)