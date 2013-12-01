int cups[10];

void setup(){
  //start serial connection
  Serial.begin(9600);
  //configure pin2 as an input and enable the internal pull-up resistor
  pinMode(13, OUTPUT);
  for (int i = 0; i < 10; i++){
    pinMode(i + 2, INPUT_PULLUP);
  }
}

void loop(){
  //read the button value into a variable
 /* int sensorVal = digitalRead(2);
 
  if (sensorVal == HIGH) {
      Serial.println(1);
      digitalWrite(13, HIGH);
  }
  else {
      Serial.println(2);
      digitalWrite(13, LOW);
  }
  delay(500);
  */
  for (int i = 0; i < 10; i++) {
      int sensorVal = digitalRead(i + 2);
      if (sensorVal == HIGH) {
          Serial.println(2*i + 1);      
      }
      else {
          Serial.println(2*i + 2);
      }
      delay(50);
  }
  
  /*for (int i = 0; i < 5; i++){
    int sensorVal = digitalRead(i+2);
    if (sensorVal == HIGH && cups[i] == 0){
        cups[i] = 1;
        Serial.println(2*i+1);
    }
    else if (sensorVal == LOW && cups[i] == 1){
        cups[i] = 0;
        Serial.println(2*i+2);
    }
    delay(100);
  }*/
}



