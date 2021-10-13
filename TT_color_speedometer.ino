#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <Adafruit_NeoPixel.h>

/*
  This sketch utilizes code from the examples included in the libraries above.
*/
static const int RXPin = 10, TXPin = 11;
static const uint32_t GPSBaud = 9600;
float mph;

int redval;
int blueval;
int greenval;

//#define PIN 5
//#define NUMPIXELS 8


// The TinyGPS++ object
TinyGPSPlus gps;

// The serial connection to the GPS device
SoftwareSerial ss(RXPin, TXPin);
Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, 5, NEO_GRB + NEO_KHZ800);

void setup()
{
  strip.begin();
  strip.show();
  Serial.begin(115200);
  ss.begin(GPSBaud);

  Serial.println(F("DeviceExample.ino"));
  Serial.println(F("A simple demonstration of TinyGPS++ with an attached GPS module"));
  Serial.print(F("Testing TinyGPS++ library v. ")); Serial.println(TinyGPSPlus::libraryVersion());
  Serial.println(F("by Mikal Hart"));
  Serial.println();
}

void loop()
{
  // This sketch displays information every time a new sentence is correctly encoded.
  while (ss.available() > 0)
    if (gps.encode(ss.read()))
      displayInfo();

  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
    while(true);
  }











}

void displayInfo()
{
  Serial.print(F("Location: ")); 
  if (gps.location.isValid())
  {
    Serial.print(gps.location.lat(), 6);
    Serial.print(F(","));
    Serial.print(gps.location.lng(), 6);
  }
  else
  {
    Serial.print(F("INVALID"));
  }

  Serial.print(F("  Date/Time: "));
  if (gps.date.isValid())
  {
    Serial.print(gps.date.month());
    Serial.print(F("/"));
    Serial.print(gps.date.day());
    Serial.print(F("/"));
    Serial.print(gps.date.year());
  }
  else
  {
    Serial.print(F("INVALID"));
  }

  Serial.print(F(" "));
  if (gps.time.isValid())
  {
    if (gps.time.hour() < 10) Serial.print(F("0"));
    Serial.print(gps.time.hour());
    Serial.print(F(":"));
    if (gps.time.minute() < 10) Serial.print(F("0"));
    Serial.print(gps.time.minute());
    Serial.print(F(":"));
    if (gps.time.second() < 10) Serial.print(F("0"));
    Serial.print(gps.time.second());
    Serial.print(F("."));
    if (gps.time.centisecond() < 10) Serial.print(F("0"));
    Serial.print(gps.time.centisecond());
  }
  else
  {
    Serial.print(F("INVALID"));
  }

  Serial.println();


  mph = gps.speed.mph();

  mph = mph*1.75;
  //mph = mph*10;
  
  Serial.println(mph);

  if(mph > 20 && mph < 26)
  {
    redval = map( mph, 20, 25, 20, 255 );
    greenval = 0;
    blueval = map( mph, 20, 25, 20, 255 );
  }
  else if (mph >= 26 && mph < 30)
  {
    redval = map( mph, 26, 30, 255, 20 );
    greenval = 0;
    blueval = map( mph, 26, 30, 255, 20 );
  }
  else if (mph >= 30 && mph < 36)
  {
    redval = 0;
    greenval = 0;
    blueval = map( mph, 30, 36, 20, 255 );
  }
  else if (mph >= 36 && mph < 40)
  {
    redval = 0;
    greenval = 0;
    blueval = map( mph, 36, 40, 255, 20 );
  }
  else if (mph >= 40 && mph < 46)
  {
    redval = 0;
    greenval = map( mph, 40, 46, 20, 255 );
    blueval = 0;
  }
  else if (mph >= 46 && mph < 50)
  {
    redval = 0;
    greenval = map( mph, 46, 50, 255, 20 );
    blueval = 0;
  }
  else if (mph >= 50 && mph < 56)
  {
    redval = map( mph, 50, 56, 20, 255 );
    greenval = map( mph, 50, 56, 20, 255 );
    blueval = 0;
  }
  else if (mph >= 56 && mph < 60)
  {
    redval = map( mph, 56, 60, 255, 20 );
    greenval = map( mph, 56, 60, 255, 20 );
    blueval = 0;
  }
  else if (mph >= 60 && mph < 66)
  {
    redval = map( mph, 60, 66, 20, 255 );
    greenval = map( mph, 60, 66, 20, 140 );
    blueval = 0;
  }
  else if (mph >= 66 && mph < 70)
  {
    redval = map( mph, 66, 70, 255, 20 );
    greenval = map( mph, 66, 70, 140, 20 );
    blueval = 0;
  }
  else if (mph >= 70 && mph < 76)
  {
    redval = map( mph, 70, 76, 20, 255 );
    greenval = 0;
    blueval = 0;
  }
  else if (mph >= 76 && mph < 80)
  {
    redval = map( mph, 76, 80, 255, 20 );
    greenval = 0;
    blueval = 0;
  }
  else
  {
    Serial.println("stuck in 0's");
    redval = 0;
    greenval = 0;
    blueval = 0;
  }

//delay(20);

 strip.setPixelColor(0, redval,   greenval,   blueval);
  strip.setPixelColor(1, redval,   greenval,   blueval);
  strip.setPixelColor(2,   redval,   greenval,   blueval);
  strip.setPixelColor(3,   redval,   greenval,   blueval);
  strip.setPixelColor(4,   redval,   greenval,   blueval);
 strip.setPixelColor(5, redval,   greenval,   blueval);
  strip.setPixelColor(6, redval,   greenval,   blueval);
  strip.setPixelColor(7,   redval,   greenval,   blueval);
strip.show();



  
}
