#include <Wire.h>
#include <Servo.h>

struct receiveResult {
  char new_character;
  int speed;
};

void setup(){
  Serial.begin(9600);
  Wire.begin();
}

void loop(){

  if (Serial.available() > 0) {
    
     receiveResult rr = receive();
     Serial.println(rr.new_character + String(rr.speed));
     rr.new_character;
     int integ = rr.speed;
     char charact = rr.new_character;

     Wire.beginTransmission(33);
     Wire.write((uint8_t *)&rr, sizeof(rr));
     Wire.endTransmission();
     delay(1000);
     Serial.print("Getting \t");
       Wire.requestFrom(33, 3);
     while (Wire.available()) {
     
       Serial.print("c:");
       Serial.println(Wire.read());
     }
   }
}

receiveResult receive() {
  char new_character = Serial.read();
  int speed = Serial.parseInt();
  receiveResult rr = {new_character, speed};
  return rr;
}
