#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <uri/UriBraces.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <EEPROM.h>
//Adafruit_BMP280 bmp; Sensor Original

#define WIFI_SSID "Wokwi-GUEST" // Na implementacao fisica seria o nome da rede wifi
#define WIFI_PASSWORD ""
#define WIFI_CHANNEL 6
#define RBF_PIN 2
#define EEPROM_SIZE 4*1024 //Tamanho original da memoria da wesmos
WebServer server(80);
Adafruit_MPU6050 mpu;
sensors_event_t a, g, temp;
bool rbf_state = true;
int address = 0;

String getHTML() {
  String response = R"(
    <!DOCTYPE html><html>
      <head>
        <title>Black Box</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
          html { font-family: sans-serif; text-align: center; }
          body { display: inline-flex; flex-direction: column; }
          h1 { margin-bottom: 1.2em; } 
          h2 { margin: 0; }
          div { margin: 10px; }
          .btn { background-color: #EEF5FF; border: none; color: #000; padding: 1em 1em; margin: 0 10px 20px 10px; font-size: 1.5em; text-decoration: none }
          .grid-container {
            display: grid;
            margin: 10px 15% 10px 15%;
            grid-template-columns: auto auto auto auto;
            background-color: #EEF5FF;
            padding: 10px;
          }
          .grid-item {
            background-color: rgba(255, 255, 255, 0.8);
            border: 1px solid rgba(0, 0, 0, 0.8);
            padding: 15px;
            font-size: 25px;
            text-align: center;
          }
        </style>
      </head>
            
      <body>
        <h1>ESP32 Black Box</h1>

        <div>
          <a href="/data" class="btn">Data</a>
          <a href="/max" class="btn">Max</a>
        </div>
        <span></span>
      </body>
    </html>
  )";
  return response;
}

void insertdata(){
  String response = getHTML();
  String elements = "";
  elements += "<span class=\"grid-container\">";
  int i=0;
  float data;
  for(i=0; i<address; i+=4){
    EEPROM.get(i, data);
    elements += "<div class=\"grid-item\">";
    elements +="Tempo: ";
    elements += String(i*0.125*0.5);
    elements +=", Altura: ";
    elements += String(data) + "</div>";
  }
  elements += "</span>";
  response.replace("<span></span>", elements);
  Serial.println(response);
  server.send(200, "text/html", response);
}

void insertmax(){
  String response = getHTML();
  String elements = "";
  elements += "<span class=\"grid-container\">";
  int i=0;
  int maxi = 0;
  float data;
  float max = 0.0;
  for(i=0; i<address; i+=4){
    EEPROM.get(i, data);
    if(data > max){
      maxi = i;
      max = data;
    }
  }
  elements += "<div class=\"grid-item\">";
  elements +="Maximum Height<br/>Tempo: ";
  elements += String(maxi*0.125*0.5);
  elements +=", Altura: ";
  elements += String(max) + "</div>";
  elements += "</span>";
  response.replace("<span></span>", elements);
  Serial.println(response);
  server.send(200, "text/html", response);
}

void setup(void) {
  Serial.begin(115200); // Inicializa a comunicação serial, apenas para efeito de demosntracao no codigo
  pinMode(RBF_PIN, INPUT);
  EEPROM.begin(EEPROM_SIZE);
}

void setup_flight(){
  WiFi.disconnect();
  //bmp.begin(0x76)
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
  address = 0;
  read_flight_data();
}

void read_flight_data(){
  int i=0;
  float values[5];
  float media = 0;
  while(digitalRead(RBF_PIN) == 0){
    while(i<5){
      mpu.getEvent(&a, &g, &temp);
      //bmp.readPressure()/100.0F
      values[i] = temp.temperature;
      i++;
      delay(50);
    }
    for(int j=0; j<5; j++){
      media += values[j];
    }
    media = media/5;
    Serial.printf("Leitura: %f\n", media);
    EEPROM.put(address, media);
    address += 4;
    i = 0;
    media = 0;
    EEPROM.commit();
  }
  if(digitalRead(RBF_PIN) == 1){
    setup_provide_data();
  }
}

void setup_provide_data(){
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD, WIFI_CHANNEL);
  //WiFi.mode(WIFI_AP); Na implementacao fisica teriamos a placa como um acess point
  Serial.println("Connecting to WiFi ");
  Serial.println(WIFI_SSID);
  while (WiFi.status() != WL_CONNECTED && digitalRead(RBF_PIN) == 1) {
    delay(200);
  }
  if(digitalRead(RBF_PIN) == 0){
    setup_flight();
  }else{
    Serial.println("Connected!");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());

    server.on("/", [](){server.send(200, "text/html", getHTML());});
    server.on(UriBraces("/{}"), []() {
      String info = server.pathArg(0);
      if(!strcmp(info.c_str(), "data")){
        insertdata();
      }else if(!strcmp(info.c_str(), "max")){
        insertmax();
      }
    });
    server.onNotFound([](){server.send(404, "text/plain", "404: Not found");});
    server.begin();
    Serial.println("HTTP server started (http://localhost:3000)");
    provide_flight_data();
  }
}

void provide_flight_data(){
  while(digitalRead(RBF_PIN) == 1){
    server.handleClient();
    delay(200);
  }if(digitalRead(RBF_PIN) == 0){
    setup_flight();
  }
}

void loop(void) {
  if(digitalRead(RBF_PIN) == 1){
    setup_provide_data();
  }else{
    setup_flight();
  }
}