char str[2]={'0','1'};
void setup() 
{
  Serial.begin(9600);
  Serial.flush();
}
void loop() 
{
  if(Serial.available() > 0) 
  {
    char data = Serial.read();
    
    str[0] = data;
    str[1] = '\0';
    //Serial.print(str);

//  if(str[0] == '1')
//  Serial.print(str);
//  else if(str[0] == '0')
//  Serial.print(str);
//  else if(str[0] == '2')
//  Serial.print(str);
//  else if(str[0] == '3')
//  Serial.print(str);
//  else
//  Serial.print("h");
  }

  if(str[0] == '1')
  Serial.print(str);
  else if(str[0] == '0')
  Serial.print(str);
  else if(str[0] == '2')
  Serial.print(str);
  else if(str[0] == '3')
  Serial.print(str);
  else
  Serial.print("h");

  delay(125);
  
}
