from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Chargez votre modèle
model = pickle.load(open('model.pkl', 'rb'))



# Fonction pour effectuer une prédiction
def Attendance(model, Hour, Temperature, Humidity, Wind_speed, Visibility, Radiation, Rainfall, Snowfall, Day, Month, Week_day_Friday, Week_day_Monday, Week_day_Saturday, Week_day_Sunday, Week_day_Thursday, Week_day_Tuesday, Week_day_Wednesday, Holiday):
    def seasons(M):
      if M >= 1 & M < 3 :
         Seasons_Autumn = 0
         Seasons_Spring = 0
         Seasons_Summer = 0
         Seasons_Winter = 1
         return Seasons_Autumn, Seasons_Spring, Seasons_Summer, Seasons_Winter
      if M >= 3 & M < 6 :
         Seasons_Autumn = 0
         Seasons_Spring = 1
         Seasons_Summer = 0
         Seasons_Winter = 0
         return Seasons_Autumn, Seasons_Spring, Seasons_Summer, Seasons_Winter
      if M >= 6 & M < 9 :
         Seasons_Autumn = 0
         Seasons_Spring = 0
         Seasons_Summer = 1
         Seasons_Winter = 0
         return Seasons_Autumn, Seasons_Spring, Seasons_Summer, Seasons_Winter
      if M >= 9 & M <= 12 :
         Seasons_Autumn = 1
         Seasons_Spring = 0
         Seasons_Summer = 0
         Seasons_Winter = 0
         return Seasons_Autumn, Seasons_Spring, Seasons_Summer, Seasons_Winter
    
    def moment_day(hour):
        if 0<=hour<6:
          Moment_day_Afternoon = 0
          Moment_day_Evening = 0
          Moment_day_Morning = 0
          Moment_day_Night = 1
          return Moment_day_Afternoon, Moment_day_Evening, Moment_day_Morning, Moment_day_Night
        if 6<=hour<12:
          Moment_day_Afternoon = 0
          Moment_day_Evening = 0
          Moment_day_Morning = 1
          Moment_day_Night = 0
          return Moment_day_Afternoon, Moment_day_Evening, Moment_day_Morning, Moment_day_Night
        if 12<=hour<=18:
          Moment_day_Afternoon = 1
          Moment_day_Evening = 0
          Moment_day_Morning = 0
          Moment_day_Night = 0
          return Moment_day_Afternoon, Moment_day_Evening, Moment_day_Morning, Moment_day_Night
        if 18<hour<=23:
          Moment_day_Afternoon = 0
          Moment_day_Evening = 1
          Moment_day_Morning = 0
          Moment_day_Night = 0
          return Moment_day_Afternoon, Moment_day_Evening, Moment_day_Morning, Moment_day_Night


    Seasons_Autumn, Seasons_Spring, Seasons_Summer,Seasons_Winter = seasons(Month)
    Moment_day_Afternoon, Moment_day_Evening, Moment_day_Morning, Moment_day_Night = moment_day(Hour)

    x = np.array([Hour, Temperature, Humidity, Wind_speed, Visibility, Radiation, Rainfall, Snowfall, Day, Month, Seasons_Autumn, Seasons_Spring, Seasons_Summer,Seasons_Winter, Moment_day_Afternoon, Moment_day_Evening, Moment_day_Morning, Moment_day_Night, Week_day_Friday, Week_day_Monday, Week_day_Saturday, Week_day_Sunday, Week_day_Thursday, Week_day_Tuesday, Week_day_Wednesday, Holiday]).reshape(1, -1)
    prediction = model.predict(x)
    probability = model.predict_proba(x)  
    return prediction, probability

@app.route('/predict', methods=['POST'])
def predict():
    try :
        
        data = request.get_json(force=True)
        prediction, _ = Attendance(
            model,
            data.get('Hour', 0),
            data.get('Temperature', 0),
            data.get('Humidity', 0),
            data.get('Wind_speed', 0),
            data.get('Visibility', 0),
            data.get('Radiation', 0),
            data.get('Rainfall', 0),
            data.get('Snowfall', 0),
            data.get('Day', 0),
            data.get('Month', 0),
            data.get('Week_day_Friday', 0),
            data.get('Week_day_Monday', 0),
            data.get('Week_day_Saturday', 0),
            data.get('Week_day_Sunday', 0),
            data.get('Week_day_Thursday', 0),
            data.get('Week_day_Tuesday', 0),
            data.get('Week_day_Wednesday', 0),
            data.get('Holiday', 0)
        )
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

#Sur un premier terminal, il faut entrer : python app.py