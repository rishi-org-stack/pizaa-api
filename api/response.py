errors= {
    401:{
        "status_code":400,
        "error_text":"toppings  are missing",
        "soln":"enter some comma seprated toppings"
    },
    402:{
        "status_code":402,
        "error_text":"size is not present in our database",
        "soln":"/size/"
    },403:{
        "status_code":403,
        "error_text":"size is not entered",
        "soln":"put some values in size box"
    },
    404:{
        "status_code":404,
        "error_text":"no pizza of this size is present to update",
        "soln":"/size/"
    }
}

success ={
    200:{
        "status_code":200,
        "success":"size is successfully added",

    },
    201:{
        "status_code":201,
        "success":"pizza is successfully added",

    },
    202:{
        "status_code":202,
        "success":"pizza is successfully updated",
    },
    203:{
        "status_code":202,
        "success":"pizza is successfully deleted",
    }
}
