{
    "urlogins": [

        {
            "URL": "https://liquidhealthpets.com/products/k9-glucosamine-for-dogs-joint-supplement-1"
        },
        {
            "URL": "https://liquidhealthpets.com/products/k9-complete-8-in-1"
        },
        {
            "URL": "https://liquidhealthpets.com/products/k9-ear-solutions-dog-ear-cleaner-1"
        },
        {
            "URL": "https://liquidhealthpets.com/products/joint-purr-fection-glucosamine-for-cats-1"
        }
    ]
}



JSONParser parse = new JSONParser();
FileReader reader = new FileReader(".\\json\\url.json");
Object obj = parse.parse(reader);
JSONObject xyz = (JSONObject) obj;
JSONArray login = (JSONArray) xyz.get("userlogins");
String arr[] = new String[login.size()];

for (int i=0; i < login.size(); i++)
{
    JSONObject iam = (JSONObject) login.get(i);
String url = (String) iam.get("URL");
arr[i] = url;
}
return arr;