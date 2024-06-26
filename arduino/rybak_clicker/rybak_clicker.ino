#define MAX_BUFF_LEN 255

int space_pin = 18;
int bait_pin = 19;
int space_times;
char c;
char received[MAX_BUFF_LEN];
int idx = 0;
long space_delay;


void click_space(int times){
  for (int i = 0; i < times; i++){
    digitalWrite(space_pin, HIGH);
    space_delay = random(30,50);
    delay(space_delay);
    digitalWrite(space_pin, LOW);
    space_delay = random(100,250);
    delay(space_delay);
  }
}

void click_bait(){
  digitalWrite(bait_pin, HIGH);
  delay(100);
  digitalWrite(bait_pin, LOW);
}

void setup() {
  pinMode(space_pin, OUTPUT);
  pinMode(bait_pin, OUTPUT);
  digitalWrite(space_pin, LOW);
  digitalWrite(bait_pin, LOW);
  Serial.begin(9600);

}

void loop() {
  while(Serial.available() > 0){
    c = Serial.read();
      if(c != '\n'){
        received[idx] = c;
        idx++;
      }
      else{
        received[idx] = '\0';
        idx = 0;
        // Serial.print("ESP:");
        Serial.println(received[0]);
      }
    }

  if(received[0] != 'r' && received[0] != '0'){
    space_times = received[0] - '0';
    click_space(space_times);
    
  }
  else if(received[0] == 'r'){
    click_bait();
  }
  received[0] = '0';
}
