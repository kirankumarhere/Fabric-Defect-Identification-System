int error=0;
char c;

void setup() 
{
  Serial.begin(9600);
  Serial.flush();
  pinMode(6,OUTPUT); //to motor
  pinMode(10,OUTPUT); //led..
  pinMode(11,OUTPUT); //buzzer..
  
  //attachInterrupt(digitalPinToInterrupt(interruptPin), count, CHANGE);
}

void run_motor()
{
  
  digitalWrite(6,HIGH); //clock pulse..
  delayMicroseconds(1900); 
  digitalWrite(6,LOW);
  delayMicroseconds(1100);
  
}


void stop_motor()
{
  digitalWrite(6,HIGH); //clock pulse..
  delayMicroseconds(1500); 
  digitalWrite(6,LOW);
  delayMicroseconds(1500);

  if(error==1)
  {
    digitalWrite(10,HIGH);
    digitalWrite(11,HIGH);
  }
  
}


void loop() 
{

if(Serial.available() > 0) 
    c = Serial.read();


if(c == '1')
  {
    if(error==1)
    {
    digitalWrite(10,LOW);
    digitalWrite(11,LOW);
    error=0;
    }
    run_motor();
  
  }
  else if(c == '2')
  stop_motor();
  else if(c == '3')
  {
    error=1; //error occured..
    stop_motor();
  }
  else
  {
  Serial.print("h");
  stop_motor();
  }

//delay(175);
  
}


/*
void count()
{
//Serial.println("Counted...");
if(ct==0)
ct++;
else if(ct==1)
ct++;
else
{
  ct=0;
  l+=10.5;
Serial.print("Length of fabric processed till now: ");
Serial.print(l);
Serial.println("cm...");

Serial.print("Number of complete revolutions of conveyor till now: ");
Serial.println(r);

Serial.println("");
Serial.println("");
if(l%110==0) //10 cycles of start and stop...check it...
r++;
}





}*/
