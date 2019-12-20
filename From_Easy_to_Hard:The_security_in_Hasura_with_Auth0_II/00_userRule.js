function (user, context, callback) {
    const userId = user.user_id;
    const email = user.email;  
    const mutation = `mutation($userId: String!, $email: String) {
        insert_employee(objects: [{
            auth0_id: $userId,
            email: $email,
          	role_employees:{
              data:[{
                  id_role: 1
                },{
                  id_role: 2
                }]
            }
        }],) {
          affected_rows
        }
    }`;
    
    if (context.stats.loginsCount === 1) {
        request.post({
              headers: {
                "content-type": "application/json",
                "x-hasura-admin-secret": configuration.ACCESS_KEY
            },
            url: "https://<YOUR-HASURA-DOMAIN>.herokuapp.com/v1/graphql",
            body: JSON.stringify({ query: mutation, variables: { userId, email } })
        },
        function(error, response, body) {
          callback(error, user, context);
        });
    }
    else{
      callback(null, user, context);
    }
}