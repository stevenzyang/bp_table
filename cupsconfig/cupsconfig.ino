void setup(){
  //start serial connection
  Serial.begin(9600);
  //configure pin2 as an input and enable the internal pull-up resistor
  pinMode(2, INPUT_PULLUP);
  pinMode(13, OUTPUT); 

}

void loop(){
  //read the button value into a variable
  int sensorVal = digitalRead(2);
  
  if (sensorVal == HIGH) {
    digitalWrite(13, HIGH);
    Serial.println(sensorVal);
  } 
  else {
    digitalWrite(13, LOW);
    Serial.println(2);
  }
  delay(500);
}



