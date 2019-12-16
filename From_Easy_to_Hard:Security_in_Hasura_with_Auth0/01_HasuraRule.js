function (user, context, callback) {
    const namespace = "https://hasura.io/jwt/claims";
    const userId = user.user_id;
  
    context.idToken[namespace] = 
    { 
        'x-hasura-default-role': 'trial',
        'x-hasura-allowed-roles': ['trial', 'user'],
        'x-hasura-user-id': userId,
    };

    callback(null, user, context);
  
}