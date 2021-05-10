from rest_framework import serializers


class DiabetesSerializer(serializers.Serializer):
    preg=serializers.IntegerField()
    glu=serializers.IntegerField()
    bp=serializers.IntegerField()
    skinthickness=serializers.IntegerField()
    insulin=serializers.IntegerField()
    bmi=serializers.FloatField()
    pedigree_func=serializers.FloatField()
    age=serializers.IntegerField()

class LiverSerializer(serializers.Serializer):
    Age  = serializers.IntegerField()  
    Gender = serializers.CharField(max_length=20) 
    Total_Bilirubin = serializers.FloatField()
    Direct_Bilirubin= serializers.FloatField()
    Alkaline_Phosphotase = serializers.IntegerField()  
    Alamine_Aminotransferase = serializers.IntegerField()  
    Aspartate_Aminotransferase = serializers.IntegerField()  
    Total_Protiens = serializers.FloatField()
    Albumin = serializers.FloatField()
    Albumin_and_Globulin_Ratio = serializers.FloatField()


class KidneySerializer(serializers.Serializer):
    # id = serializers.IntegerField()  
    age= serializers.FloatField()
    bp = serializers.FloatField()
    sg = serializers.FloatField()
    al = serializers.FloatField()
    su = serializers.FloatField()
    rbc= serializers.CharField(max_length=30) 
    pc = serializers.CharField(max_length=30) 
    pcc= serializers.CharField(max_length=30) 
    ba = serializers.CharField(max_length=30) 
    bgr= serializers.FloatField()
    bu = serializers.FloatField()
    sc = serializers.FloatField()
    sod= serializers.FloatField()
    pot= serializers.FloatField()
    hemo = serializers.FloatField()
    pcv= serializers.CharField(max_length=30) 
    wc = serializers.CharField(max_length=30) 
    rc = serializers.CharField(max_length=30) 
    htn= serializers.CharField(max_length=30) 
    dm = serializers.CharField(max_length=30) 
    cad = serializers.CharField(max_length=30) 
    appet = serializers.CharField(max_length=30) 
    pe = serializers.CharField(max_length=30) 
    ane= serializers.CharField(max_length=30)


class MalariaSerializer(serializers.Serializer):
    image = serializers.ImageField()

class PneumoniaSerializer(serializers.Serializer):
    image = serializers.ImageField()
    
class SkinSerializer(serializers.Serializer):
    image = serializers.ImageField()

class NearbyHospitalSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=30)
    pincode = serializers.IntegerField()
