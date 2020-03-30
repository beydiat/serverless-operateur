# serverless-operateur

## Install serverless:   

``` bash
$ npm install serverless -g
```

## Deploy

### Deploy ressources (DynamoDb)

``` bash
$ cd ressources/services/database && serverless deploy -stage dev --region us-east-1 
```

### Deploy sevices (API Gateway & Lambda)

``` bash
$ cd services-api/services/operations && serverless deploy -stage dev --region us-east-1
```

At the end of the deployment, you will receive the urls of the 4 deployed endpoints.


Example: 
- Soustraction :

POST Method : https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/soustraction 
body : {"a":300, "b":258}

- Liste : 

GET Method : https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/liste


pensez à remplacer le xxxxxxxxx par l'id du API Gateway retourné

There you go,