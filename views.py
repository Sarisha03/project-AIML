def dia(request):
    if(request.method=="POST"):
        data=request.POST
       
        radius_mean=data.get('textradius_mean')
        texture_mean=data.get('texttexture_mean')
        perimeter_mean=data.get('textperimeter_mean')
        area_mean=data.get('textarea_mean')
        smoothness_mean=data.get('textsmoothness_mean')
        compactness_mean=data.get('textcompactness_mean')
        concavity_mean=data.get('textconcavity_mean')
        concave_points_mean=data.get('textconcave_points_mean')
        symmetry_mean=data.get('textsymmetry_mean')
        fractal_dimension_mean=data.get('textfractal_dimension_mean')

        radius_se=data.get('textradius_se')
        texture_se=data.get('texttexture_se')
        perimeter_se=data.get('textperimeter_se')
        area_se=data.get('textarea_se')
        smoothness_se=data.get('textsmoothness_se')
        compactness_se=data.get('textcompactness_se')
        concavity_se=data.get('textconcavity_se')
        concave_points_se=data.get('textconcave_points_se')
        symmetry_se=data.get('textsymmetry_se')
        fractal_dimension_se=data.get('textfractal_dimension_se')

        radius_worst=data.get('textradius_worst')
        texture_worst=data.get('texttexture_worst')
        perimeter_worst=data.get('textperimeter_worst')
        area_worst=data.get('textarea_worst')
        smoothness_worst=data.get('textsmoothness_worst')
        compactness_worst=data.get('textcompactness_worst')
        concavity_worst=data.get('textconcavity_worst')
        concave_points_worst=data.get('textconcave_points_worst')
        symmetry_worst=data.get('textsymmetry_worst')
        fractal_dimension_worst=data.get('textfractal_dimension_worst')

        
        if('buttonpredict' in request.POST):
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import LabelEncoder
            import matplotlib.pyplot as plt
            from sklearn.naive_bayes import GaussianNB

            path="C:\\Users\\DELL\\Desktop\\int\\cancertype\\47_cancertype\\bdiag.csv"
            data=pd.read_csv(path)
            #print(data)

            #data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})

            inputs=data.drop(['id','diagnosis'],'columns')
            #prnt(input)

            la_diagnosis=LabelEncoder()
            data["diagnosis_n"]=la_diagnosis.fit_transform(data['diagnosis'])

            output=data['diagnosis']
                    
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            model=GaussianNB()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            #print(y_pred)

            #result=model.predict(([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]]))
            #print(res)

            result=model.predict([[float(radius_mean),float(texture_mean),float(perimeter_mean),float(area_mean),float(smoothness_mean),float(compactness_mean),float(concavity_mean),float(concave_points_mean),float(symmetry_mean),float(fractal_dimension_mean),float(radius_se),float(texture_se),float(perimeter_se),float(area_se),float(smoothness_se),float(compactness_se),float(concavity_se),float(concave_points_se),float(symmetry_se),float(fractal_dimension_se),float(radius_worst),float(texture_worst),float(perimeter_worst),float(area_worst),float(smoothness_worst),float(compactness_worst),float(concavity_worst),float(concave_points_worst),float(symmetry_worst),float(fractal_dimension_worst)]])
            print(result)

            if result==0:
                print("B")
            else:
                print("M")
                    
        return render(request,'dia.html',context={'result':result})
        
    return render(request,'dia.html')