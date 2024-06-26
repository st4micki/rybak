

int space = 8;
int f1 = 9;
int space_input = 2;
int f1_input = 4;

void setup(){
pinMode(space, OUTPUT);
pinMode(f1, OUTPUT);
pinMode(space_input, INPUT);
pinMode(f1_input, INPUT);

}

void loop(){
  byte space_state = digitalRead(space_input);
  byte f1_state = digitalRead(f1_input);
  if(space_state == LOW){
    digitalWrite(space, HIGH);
  }
  else{
    digitalWrite(space, LOW);
  }

  if(f1_state == LOW){
    digitalWrite(f1, HIGH);
  }
  else{
    digitalWrite(f1, LOW);
  }

}