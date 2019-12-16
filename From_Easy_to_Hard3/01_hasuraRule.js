function (user, context, callback) {
    const namespace = "https://hasura.io/jwt/claims";
    const userId = user.user_id;
    
    const mutation = `query ($userId: String) {
        employee(where: {auth0_id: {_eq: $userId}}){
          role_employees {
            role {
              text_id
            }
          }
        }
    }`;
    
    request.post({
            headers: {
              "content-type": "application/json",
              "x-hasura-admin-secret": configuration.ACCESS_KEY
            },
            url: "https://<YOUR-HASURA-DOMAIN>.herokuapp.com/v1/graphql",
            body: JSON.stringify({ query: mutation, variables: { userId} })
      }, function(error, response, body){
            if(!error){
                var data = JSON.parse(body);
                let roles_employees = data.data.employee[0].role_employees;
                var roles = [];
                for(let role of roles_employees){
                    roles.push(role.role.text_id);
                }
                context.idToken[namespace] = { 
                    'x-hasura-default-role': roles[0],
                    'x-hasura-allowed-roles': roles,
                    'x-hasura-user-id': userId,
                };
            }  
            callback(error, user, context);
      });
}