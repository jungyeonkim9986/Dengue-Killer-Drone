#include <Servo.h>

char receivedChar;
int angle;
boolean newData = false;

Servo servoSpring

void setup() {
    Serial.begin(9600);
    servoSpring.attach(9);
}

void loop() {
    recvOneChar();
    rotateServo();
}

void recvOneChar() {
    if (Serial.available() > 0) {
        receivedChar = Serial.read();
        newData = true;
    }
}

void rotateServo() {
  angle = receivedChar.toInt();
  servoSpring.write(angle*90);
  newData = false;
}
