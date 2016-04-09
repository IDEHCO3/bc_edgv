import  json


obj = u'{"@context": "http://www.w3.org/ns/hydra/context.jsonld",
  "@id": "http://api.example.com/doc/#Comment",
  "@type": "Polygon",
  "title": "Polygon class",
  "description": "A short description of the class.",
  "supportedProperty": [],
  "supportedOperation": []}'


"hydra:operation": [
    "hydra:httpMethod": "POST",
                   "@type": "OrderAction",
                   "hydra:expects": {
                     "@type": "Product",
                     "hydra:supportedProperty": [
                       {
                         "hydra:property": "name",
                         "hydra:required": true,
                         "defaultValue": "shot",
                         "readOnlyValue": true
                       }
                     ]
                   }
]

"supportedOperation": [
    {
      "@type": "CreateResourceOperation",
      "title": "Creates a new comment",
      "method": "POST",
      "expects": "http://api.example.com/doc/#Comment",
      "returns": "http://api.example.com/doc/#Comment",
      "possibleStatus": [
        ... Statuses that should be expected and handled properly ...
      ]
    }
  ]