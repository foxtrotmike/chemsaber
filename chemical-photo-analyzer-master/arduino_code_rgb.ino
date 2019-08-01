#define red  5
#define green 6
#define blue 9


void setup() {
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  Serial.begin(9600);
  //color(255,0,0);

}

void loop() {
  if(Serial.available()>0){
    int tred=Serial.parseInt();
    int tgreen=Serial.parseInt();
    int tblue=Serial.parseInt();
    int t=Serial.parseInt();
    
    int tr=tred;
    int tg=tgreen;
    int tb=tblue;
    

    color(tr,tg,tb);
    int  readValue=anaRead();
    int  readValuea=anaRead();
    int  readValueb=anaRead();
    int  readValuec=anaRead();

    

    int  readValue1=anaRead1();
    int  readValue1a=anaRead1();
    int  readValue1b=anaRead1();
    int  readValue1c=anaRead1();


    readValue=anaRead();
    readValuea=anaRead();
    readValueb=anaRead();
    readValuec=anaRead();

    

    readValue1=anaRead1();
    readValue1a=anaRead1();
    readValue1b=anaRead1();
    readValue1c=anaRead1();

    

    readValue=anaRead();
    readValuea=anaRead();
    readValueb=anaRead();
    readValuec=anaRead();

    

    readValue1=anaRead1();
    readValue1a=anaRead1();
    readValue1b=anaRead1();
    readValue1c=anaRead1();

    
    readValue=anaRead();
    readValuea=anaRead();
    readValueb=anaRead();
    readValuec=anaRead();

    

    readValue1=anaRead1();
    readValue1a=anaRead1();
    readValue1b=anaRead1();
    readValue1c=anaRead1();

    
    readValue=anaRead();
    readValuea=anaRead();
    readValueb=anaRead();
    readValuec=anaRead();

    

    readValue1=anaRead1();
    readValue1a=anaRead1();
    readValue1b=anaRead1();
    readValue1c=anaRead1();
    //delay(100);
    Serial.println("red " + (String)tred + " green  " + (String)tgreen + " blue " + (String)tblue+ " Sensor Value 1=  " + (String)readValue + "  "+ (String)readValuea+ "  "+ (String)readValueb+ "  "+ (String)readValuec+ "  "+ " Sensor Value 2=  " + (String)readValue1+ "  "+ (String)readValue1a+ "  "+ (String)readValue1b+ "  "+ (String)readValue1c);
    
  }

 //delay(1000);
}


void color(int cred, int cgreen, int cblue) {
  analogWrite(red, cred);
  analogWrite(green, cgreen);
  analogWrite(blue, cblue);
}

int anaRead(){
  int readValue= analogRead(A0);
  //Serial.println("Sensor Value"+ (String)readValue);
  return readValue;
   
  }

int anaRead1(){
  int readValue1= analogRead(A1);
  //Serial.println("Sensor Value"+ (String)readValue);
  return readValue1;
   
  }
