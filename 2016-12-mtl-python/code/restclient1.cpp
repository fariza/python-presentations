#include "restclient-cpp/connection.h"
#include "restclient-cpp/restclient.h"

string BasePSU::get(string url_attr){
  RestClient::Response r = conn->get(url_attr);
  return r.body;
}

string BasePSU::put(string url_attr, string payload){
  RestClient::Response r = conn->put(url_attr, payload);
  return r.body;
}

float BasePSU::get_voltage(){
   string url_attr ("voltage/");
   string r = get(url_attr);
  return atof(r.c_str());
}

void BasePSU::set_voltage(float voltage){
 string url_attr ("voltage/");
 string r = put(url_attr,"{\"voltage\":" + to_string(voltage) + "}");
}
