#include <Servo.h>
#include <Wire.h>

int motor_num;
int min_pulse_rate = 1000;
int max_pulse_rate = 2000;
int i = 37;
int pins[] = {40,42,36,37,38,39};
int num_pins = 2;
Servo motor1;
Servo motor2;
byte echo[3];

struct receiveResult {
  char new_character;
  int speed;
};

int last_speed = 90;

void setup() {
  Wire.onReceive(myHandler);
  Wire.onRequest(myHandler2);
  Wire.begin(33);
  Serial.begin(9600);
  pinMode(36, OUTPUT);
  pinMode(42, OUTPUT);
  motor1.attach(36, min_pulse_rate, max_pulse_rate);
  motor2.attach(42, min_pulse_rate, max_pulse_rate);
  motor1.write(84);
  motor2.write(84);
  /*for(int i = 0; i < num_pins; i++) {
    pinMode(i, OUTPUT);
    motor[i].attach(i, min_pulse_rate, max_pulse_rate);
    motor[i].write(84);
  }*/
  delay(5000);
}

void loop() {
/*  if (Serial.available() > 0) {
    receiveResult rr = receive();
    Serial.println(rr.new_character + String(rr.speed));
    rr.new_character;
    int integ = rr.speed;
    char charact = rr.new_character;
  }*/
  /*if (charact == 'f' || charact == 'F') {
    f(integ);
  }
  if (charact == 'b' || charact == 'B') {
    b(integ);
  }*/
}

/*receiveResult receive() {
  char new_character = Serial.read();
  int speed = Serial.parseInt();
  receiveResult rr = {new_character, speed};
  return rr;
}*/

void f(int desired) {
  for (int j = last_speed; j < desired; j++) {
    motor1.write(j);
    motor2.write(j);
    delay(30);
  }
}

void b(int desired) {
  for (int j = last_speed; j < desired; j++) {
    motor1.write(j * -1);
    motor2.write(j * -1);
    delay(30);
  }
}

void myHandler(int numBytes) {
  for (int i = 0; i < numBytes; i++) {
    char c = Wire.read();
    echo[i] = c;
    Serial.println(c);
  }
}

void myHandler2() {
  Wire.write(echo, 3);
}
