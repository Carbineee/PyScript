#include <Mouse.h>

byte bf[2];

void setup() {
  Serial.begin(9600);
  Mouse.begin();
}

void loop() {
  if (Serial.available() > 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.readBytes(bf, 2);
    Mouse.move(bf[0], bf[1], 0);
    Serial.print(bf[0]);
  }else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
