int ledPin = LED_BUILTIN;  // Use the built-in LED
int numBlinks = 0;
int randomNum = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  randomSeed(analogRead(0));  // Initialize the random number generator
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming number
    numBlinks = Serial.parseInt();
    
    // Blink the LED numBlinks times
    for (int i = 0; i < numBlinks; i++) {
      digitalWrite(ledPin, HIGH);
      delay(1000);  // Wait for a second
      digitalWrite(ledPin, LOW);
      delay(1000);  // Wait for a second
    }

    // Generate a random number between 1 and 5
    randomNum = random(1, 6);
    
    // Send the random number back to the Python script
    Serial.println(randomNum);
  }
}






