/*Arduino Uno Development Board*/
const int RelayPin1 = 2; // Change this to the pin you're using
const int RelayPin2 = 4;
const int RelayPin3 = 7;
const int RelayPin4 = 8;
const int RelayPin5 = 12;
const int RelayPin6 = 13;

void setup() {
    Serial.begin(9600);
    pinMode(RelayPin1, OUTPUT);
    pinMode(RelayPin2, OUTPUT);
    pinMode(RelayPin3, OUTPUT);
    pinMode(RelayPin4, OUTPUT);
    pinMode(RelayPin5, OUTPUT);
    pinMode(RelayPin6, OUTPUT);
    digitalWrite(RelayPin1,LOW);
    digitalWrite(RelayPin2,LOW);
    digitalWrite(RelayPin3,LOW);
    digitalWrite(RelayPin4,LOW);
    digitalWrite(RelayPin5,LOW);
    digitalWrite(RelayPin6,LOW);
}

void loop() {

    if (Serial.available() > 0) {
     String command = Serial.readStringUntil('\n');
        if (command == "11") {
            digitalWrite(RelayPin1, LOW); // Turn ON the relay
            Serial.println("Relay_1 turned ON");
          } 
        else if (command == "10") {
             digitalWrite(RelayPin1, HIGH); // Turn OFF the relay
             Serial.println("Relay_1 turned OFF");
          }
        else if (command == "21") {
             digitalWrite(RelayPin2, LOW); // Turn ON the relay
             Serial.println("Relay_2 turned ON");
          }
        else if (command == "20") {
             digitalWrite(RelayPin2, HIGH); // Turn OFF the relay
             Serial.println("Relay_2 turned OFF");
          }
        else if (command == "31") {
             digitalWrite(RelayPin3, LOW); // Turn ON the relay
             Serial.println("Relay_3 turned ON");
          }
        else if (command == "30") {
             digitalWrite(RelayPin3, HIGH); // Turn OFF the relay
             Serial.println("Relay_3 turned OFF");
          }
        else if (command == "41") {
             digitalWrite(RelayPin4, LOW); // Turn ON the relay
             Serial.println("Relay_4 turned ON");
          }
        else if (command == "40") {
             digitalWrite(RelayPin4, HIGH); // Turn OFF the relay
             Serial.println("Relay_4 turned OFF");
          }
        else if (command == "51") {
             digitalWrite(RelayPin5, LOW); // Turn ON the relay
             Serial.println("Relay_5 turned ON");
          }
        else if (command == "50") {
             digitalWrite(RelayPin5, HIGH); // Turn OFF the relay
             Serial.println("Relay_5 turned OFF");
          }
        else if (command == "61") {
             digitalWrite(RelayPin6, LOW); // Turn ON the relay
             Serial.println("Relay_6 turned ON");
          }
        else if (command == "60") {
             digitalWrite(RelayPin6, HIGH); // Turn OFF the relay
             Serial.println("Relay_6 turned OFF");
          }
    }
}
