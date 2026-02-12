#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

String ssid = "";
String pass = "";

void getWifi() {
  Serial.println("\n--- WiFi Config ---");
  Serial.println("Enter SSID:");
  while (Serial.available() == 0) {}
  ssid = Serial.readStringUntil('\n'); ssid.trim();
  Serial.println("Enter Pass:");
  while (Serial.available() == 0) {}
  pass = Serial.readStringUntil('\n'); pass.trim();
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  getWifi();
  WiFi.begin(ssid.c_str(), pass.c_str());
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
}

void loop() {
  float t = dht.readTemperature();
  int ldr = analogRead(34); // Irradiance proxy

  HTTPClient http;
  http.begin("http://your-solar-app.com/update");
  http.addHeader("Content-Type", "application/json");
  
  String json = "{\"irr\":" + String(ldr) + ",\"temp\":" + String(t) + "}";
  http.POST(json);
  http.end();
  
  delay(5000);
}
